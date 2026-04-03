#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                        Editor Agent                      #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#

from utils.llama import llama_generate

def agent_redacteur_par_article(selected_articles):
    all_resumes = []

    for i, article in enumerate(selected_articles, start=1):
        prompt = f"""
You are a highly skilled scientific writing assistant.

Your task:
Create a **very detailed, structured, and comprehensive summary** of the following scientific article.
The summary should be precise, understandable, and suitable for a researcher familiar with the field. Include the main ideas, key findings, methodology if relevant, and any important context.

Article information:
- Title: {article['title']}
- Source: {article['source']}
- Original Abstract: {article['summary']}
- URL: {article['url']}

Instructions:
- Expand the summary significantly beyond the original abstract.
- Explain ALL important concepts in detail
- Make it informative and coherent, suitable for someone doing scientific research.
- Do not omit important information from the original abstract.
- Write in fluent English.
- Include context, background, and explanations
- Make the summary understandable but deep

STRICT FORMAT (MUST FOLLOW EXACTLY):

### 1. Overview
Brief explanation of the article and its purpose.

### 2. Methodology
Describe the methods, models, or approach used.

### 3. Key Findings
List the main results and contributions.

### 4. Implications
Explain why this work is important.

Rules:
- Use ALL sections (even if brief)
- Use the EXACT section titles
- No extra sections
- No introduction text before sections
- No conclusion outside sections
- Write in clear academic English

"""
        resume = llama_generate(prompt)

        all_resumes.append({
              "title": article['title'],
              "resume": resume,
              "url": article['url'],
              "source": article['source'],
              "authors": article.get("authors", []),
              "date": article.get("date", "Unknown")
        })

    return all_resumes