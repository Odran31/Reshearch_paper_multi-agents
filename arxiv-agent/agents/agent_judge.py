#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                        Judge Agent                       #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#

from utils.llama import llama_generate

def agent_judge(resumes,selected_articles ):

    improved_resumes = []

    for r in resumes:

        articles_text = "\n".join([
            f"{i+1}. {a['title']} ({a.get('source', 'Unknown')}): {a['summary'][:200]}" # 200 for less context yes, but faster processing time (15s less)
            for i, a in enumerate(selected_articles)
        ])

        prompt = f"""
You are a highly experienced scientific review agent.

Original summary for an article:
{r['resume']}

Context from related articles (ArXiv):
{articles_text}

Your task:
- Carefully evaluate the original summary in terms of **accuracy, completeness, clarity, and relevance** to the research topic.
- Identify any missing key points, unclear statements, or gaps in explanation.
- Produce a **fully improved version** of the summary that is more complete, precise, and clear.
- Structure the improved summary in coherent paragraphs, highlighting important points, methodology, and key findings if relevant.
- Enhance readability and ensure it reflects the scientific context accurately.
- Use fluent, formal English suitable for a researcher.
- Respond **only with the improved summary text**. Do **not** include the original summary, comments, or any additional information.
"""


        try:
            improved = llama_generate(prompt)
        except TypeError:
            improved = llama_generate(prompt)

        improved_resumes.append({
            "title": r["title"],
            "improved_resume": improved,
            "authors": r.get("authors", []),
            "date": r.get("date", "Unknown"),
            "url": r.get("url", "")
        })

    return improved_resumes
