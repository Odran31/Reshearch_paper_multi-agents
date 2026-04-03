#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                      Selection Agent                     #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#

from utils.llama import llama_generate

def agent_selection(all_articles, task):

    articles_text = "\n".join([
      f"""{i+1}. {a['title']}
      Authors: {', '.join(a.get('authors', []))}
      Date: {a.get('date', 'Unknown')}
      Summary: {a['summary'][:200]}
      URL: {a['url']}
      """
    for i, a in enumerate(all_articles)
    ])

    prompt = f"""
You are a scientific research expert.

Here are the results from a search on: "{task}".

Articles found:
{articles_text}

Your task:
Select the **two most relevant and important articles** for the given research topic.

Requirements:
- The two articles must be **different**.
- Consider the **title, summary, and source** when determining relevance.
- Focus on **importance, clarity, and relevance** to the topic.
- Respond strictly in the following **JSON format**:

[
  {{
    "title": "Article title",
    "summary": "Concise summary",
    "authors": ["Author 1", "Author 2"],
    "date": "YYYY-MM-DD",
    "source": "arXiv",
    "url": "Link"
  }},
  {{
    "title": "...",
    "summary": "...",
    "authors": [...],
    "date": "...",
    "source": "...",
    "url": "..."
  }}
]

- Select only **two articles**.
- Respond **only with valid JSON**. Do **not** include explanations, notes, or any extra text.
"""


    try:
        selection = llama_generate(prompt)
    except TypeError:

        selection = llama_generate(prompt)
    return selection