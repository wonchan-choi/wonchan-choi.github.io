import os
import pdfplumber
import re
import pandas as pd

# --- Step 1. Extract the relevant text from the CV PDF ---

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.realpath(__file__))
# Construct the absolute path to the PDF file located in assets/files folder of your repository
pdf_file = os.path.join(script_dir, "..", "assets", "files", "Choi-CV.pdf")
print("Using PDF file:", pdf_file)

all_text = ""

# Open and read all pages from the CV
with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            all_text += text + "\n"

# Extract the "RESEARCH, SCHOLARSHIP, & PROFESSIONAL ACTIVITIES" section.
# We assume this section begins at its header and ends at the next major section (e.g., "Presentations at Academic")
research_match = re.search(
    r'RESEARCH, SCHOLARSHIP, & PROFESSIONAL ACTIVITIES(.*?)Presentations at Academic',
    all_text,
    re.DOTALL
)
research_text = research_match.group(1) if research_match else all_text

# --- Step 2. Isolate publication entries for journals and conferences ---

# Locate the "Articles in Peer-Reviewed Journals" subsection
journals_match = re.search(
    r'Articles in Peer-Reviewed Journals(.*?)Articles in Peer-Reviewed Conference Proceedings',
    research_text,
    re.DOTALL
)
journals_text = journals_match.group(1).strip() if journals_match else ""

# Locate the "Articles in Peer-Reviewed Conference Proceedings" subsection.
# We assume this section continues until the next major header (or end of text).
conferences_match = re.search(
    r'Articles in Peer-Reviewed Conference Proceedings(.*?)(?:Presentations at Academic|$)',
    research_text,
    re.DOTALL
)
conferences_text = conferences_match.group(1).strip() if conferences_match else ""

# Split the text into individual publication entries.
# This assumes that entries are separated by at least one blank line.
journals_entries = [entry.strip() for entry in re.split(r'\n\s*\n', journals_text) if entry.strip()]
conferences_entries = [entry.strip() for entry in re.split(r'\n\s*\n', conferences_text) if entry.strip()]

def parse_entry(entry):
    """
    Extracts the publication year (if found) and returns a tuple of (year, full entry).
    Looks for a four-digit year inside parentheses.
    """
    year_match = re.search(r'\((\d{4})\)', entry)
    year = int(year_match.group(1)) if year_match else None
    return year, entry

# Build a list of dictionaries for all entries
data = []
for entry in journals_entries:
    year, info = parse_entry(entry)
    data.append({'Year': year, 'Entry': info, 'Type': 'Paper'})
for entry in conferences_entries:
    year, info = parse_entry(entry)
    data.append({'Year': year, 'Entry': info, 'Type': 'Conference Proceedings'})

# Create a DataFrame and remove entries without a detected year
df = pd.DataFrame(data)
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)

# Separate DataFrames for Papers and Conference Proceedings
papers_df = df[df['Type'] == 'Paper']
proceedings_df = df[df['Type'] == 'Conference Proceedings']

# --- Step 3. Generate Markdown output ---

def generate_markdown_for_df(df, header):
    """
    Generates markdown text for a given DataFrame grouped by year,
    using the provided header as the subsection title.
    """
    markdown = f"## {header}\n\n"
    sorted_years = sorted(df['Year'].unique(), reverse=True)
    for year in sorted_years:
        markdown += f"### {year}\n\n"
        year_df = df[df['Year'] == year]
        for _, row in year_df.iterrows():
            entry = row['Entry']
            # Use the text before the first period as a summary title (if available)
            title = entry.split('.')[0]
            markdown += "<details>\n"
            markdown += f"<summary><strong>{title}</strong></summary>\n\n"
            markdown += entry + "\n\n"
            markdown += "</details>\n\n"
    return markdown

# Generate the full publications page with two subsections
with open(os.path.join(script_dir, "publications.md"), "w", encoding="utf-8") as f:
    f.write("---\nlayout: page\ntitle: Publications\npermalink: /publications/\n---\n\n")
    f.write("# 📚 Publications\n\n")
    f.write("Below is a list of publications extracted from the CV.\n\n")
    f.write(generate_markdown_for_df(papers_df, "Papers"))
    f.write(generate_markdown_for_df(proceedings_df, "Conference Proceedings"))

# Generate the home page markdown that shows the 5 most recent papers (from journals)
recent_papers = papers_df.sort_values("Year", ascending=False).head(5)
recent_markdown = "# 📚 Recent Papers\n\n"
for _, row in recent_papers.iterrows():
    entry = row['Entry']
    title = entry.split('.')[0]
    recent_markdown += "<details>\n"
    recent_markdown += f"<summary><strong>{title}</strong></summary>\n\n"
    recent_markdown += entry + "\n\n"
    recent_markdown += "</details>\n\n"

with open(os.path.join(script_dir, "recent_papers.md"), "w", encoding="utf-8") as f:
    f.write("---\nlayout: home\n---\n\n")
    f.write(recent_markdown)

print("Markdown files generated successfully!")