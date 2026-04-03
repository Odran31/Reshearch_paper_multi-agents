#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                        Search Agent                      #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#
from datetime import datetime
from utils.arxiv import arxiv_search

def agent_recherche(task, arxiv_count=5):
    print(f"\n=== Agent Recherche : {task} ===\nDate : {datetime.now().strftime('%Y-%m-%d')}\n")

    # Tool using
    arxiv_results = arxiv_search(task, max_results=arxiv_count)
    for a in arxiv_results:
        a["source"] = "arXiv"

    return arxiv_results
