#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                        Article info                      #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/

def enrich_metadata(selected_articles, all_articles):
    enriched = []

    for sel in selected_articles:
        match = next(
            (a for a in all_articles if a["title"] == sel["title"]),
            None
        )

        if match:
            sel["authors"] = match.get("authors", [])
            sel["date"] = match.get("date", "Unknown")
            sel["url"] = match.get("url", "")

        enriched.append(sel)

    return enriched

