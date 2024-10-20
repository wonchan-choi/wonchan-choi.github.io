import os
import pandas as pd
from docx import Document

# Function to extract specific section (Section 3) from the Word document
def extract_section_3(file_path):
    doc = Document(file_path)
    section_found = False
    data = []
    section_data = []

    # Loop through each paragraph in the document
    for para in doc.paragraphs:
        text = para.text.strip()
        
        # Check if we are in Section 3
        if text.startswith("3."):
            section_found = True
        
        # Stop extracting when a new main section is encountered (Section 4 or higher)
        if section_found and (text.startswith("4.") or text.startswith("5.")):
            break
        
        # Extract data within Section 3
        if section_found:
            section_data.append(text)

    return section_data

# Helper function to process the extracted data into a DataFrame format
def process_section_data(section_data):
    publications = []
    for line in section_data:
        if line.startswith("3.1"):  # Published papers section
            # Example parsing logic based on known patterns in your file
            # You may need to adjust this for different formatting
            parts = line.split(". ", 1)
            if len(parts) > 1:
                citation = parts[1]
                publications.append({
                    'pub_date': "unknown",  # Placeholder (consider improving with date extraction logic)
                    'title': citation.split(". ")[0],  # Assume title is before the first period
                    'venue': citation.split(". ")[1] if len(citation.split(". ")) > 1 else "unknown",  # Example of venue extraction
                    'citation': citation
                })
    return pd.DataFrame(publications)

# Read the Word file and extract Section 3
section_data = extract_section_3("/mnt/data/Choi-CV-2024-01-17.docx")
publications_df = process_section_data(section_data)

# Escape special characters for YAML
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)

# Create markdown files from extracted data
for _, item in publications_df.iterrows():
    md_filename = "unknown-" + item['title'].replace(" ", "-") + ".md"
    html_filename = "unknown-" + item['title'].replace(" ", "-")

    # YAML variables
    md = "---\ntitle: \"" + item['title'] + '"\n'
    md += "collection: publications"
    md += "\npermalink: /publication/" + html_filename

    md += "\ndate: " + str(item['pub_date'])
    md += "\nvenue: '" + html_escape(item['venue']) + "'"
    md += "\ncitation: '" + html_escape(item['citation']) + "'"
    md += "\n---"

    # Save markdown file
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)

print("Markdown files generated.")