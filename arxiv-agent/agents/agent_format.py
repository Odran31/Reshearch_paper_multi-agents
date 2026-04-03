#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                      Format Agent                     #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#


def agent_format(arxiv_articles,improved_resumes):

    formatted = ""
      # Format of all article find
    formatted += "# All Articles Found (arXiv)\n\n"
    for i, a in enumerate(arxiv_articles, start=1):
        authors = ", ".join(a.get("authors", ["Unknown"]))
        date = a.get("date", "Unknown")
        url = a.get("url", "#")
        formatted += f"{i}. **{a['title']}**\n"
        formatted += f"   - Authors: {authors}\n"
        formatted += f"   - Date: {date}\n"
        formatted += f"   - Link: [{url}]({url})\n\n"

    formatted += "# Selected Research Articles\n\n"
        # info retrival
    for i, r in enumerate(improved_resumes, start=1):
        title = r.get("title", "N/A")
        authors = ", ".join(r.get("authors", ["Unknown"]))
        date = r.get("date", "Unknown")
        url = r.get("url", "#")
        summary = r.get("improved_resume", "")

        formatted += f"## {i}. {title}\n\n"

        # Format Métadonnées
        formatted += f"- **Authors:** {authors}\n"
        formatted += f"- **Publication Date:** {date}\n"
        formatted += f"- **Link:** [{url}]({url})\n\n"

        # format summary
        formatted += f"### Summary\n\n{summary}\n\n"

        formatted += "---\n\n"

    return formatted