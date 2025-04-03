import pandas as pd
from collections import defaultdict

# Load the Excel file
df = pd.read_excel("publications.xlsx")

# Group by year in descending order
df["Year"] = df["Year"].astype(str)
grouped = df.groupby("Year", sort=False)

# Sort years descending
sorted_years = sorted(grouped.groups.keys(), reverse=True)

# Start generating the Markdown
with open("publications.md", "w", encoding="utf-8") as f:
    f.write("---\nlayout: page\ntitle: Publications\npermalink: /publications/\n---\n\n")
    f.write("# 📚 Recent Publications\n\n")
    f.write("Below is a list of selected publications. Click each title to expand details.\n\n")

    for year in sorted_years:
        f.write(f"## 🔸 {year}\n\n")
        year_df = grouped.get_group(year)
        for _, row in year_df.iterrows():
            title = row.get("Title", "No Title")
            authors = row.get("Authors", "Unknown")
            venue = row.get("Venue", "")
            doi = row.get("DOI", "")
            url = row.get("URL", "")
            abstract = row.get("Abstract", "")

            f.write("<details>\n")
            f.write(f"<summary><strong>{title}</strong></summary>\n\n")
            f.write(f"- **Authors:** {authors}\n")
            if venue:
                f.write(f"- **Venue:** *{venue}*, {year}\n")
            if doi:
                f.write(f"- **Links:** [DOI](https://doi.org/{doi})")
                if url:
                    f.write(f" · [PDF]({url})\n")
                else:
                    f.write("\n")
            elif url:
                f.write(f"- **Links:** [PDF]({url})\n")
            if abstract:
                f.write(f"- **Abstract:** {abstract}\n")
            f.write("\n</details>\n\n")