#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                          Pipeline                        #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#
import json
from utils.article_info import enrich_metadata
from agents.agent_recherche import agent_recherche
from agents.agent_selection import agent_selection
from agents.agent_editor import agent_redacteur_par_article
from agents.agent_judge import agent_judge
from agents.agent_format import agent_format
import gradio as gr

import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError(" Missing GROQ_API_KEY in .env")


def research_pipeline(task, output_format="markdown"):


    #   Call Research agent
    arxiv_articles = agent_recherche(task, arxiv_count=10)

    # Call selection agent
    selection_json = agent_selection(arxiv_articles, task)

    #  convertion llama slection output (JSON) to python list

    try:
        selected_articles = json.loads(selection_json)
    except:
        print(" Error parsing JSON → fallback arXiv")
        selected_articles = [
            {
                "title": a["title"],
                "summary": a["summary"],
                "source": "arXiv",
                "url": a["url"],
                "authors": a.get("authors", ["Unknown"]),
                "date": a.get("date", "Unknown")
            }
            for a in arxiv_articles[:2]
        ]

    selected_articles = enrich_metadata(selected_articles, arxiv_articles)
    
    if len(selected_articles) < 2:
        raise ValueError("Not enough articles selected (need at least 2)")

    # article storage
    article1 = selected_articles[0]
    article2 = selected_articles[1]

    # Call editor agent
    resumes = agent_redacteur_par_article([article1, article2])

    # Call judge agent
    improved_resumes = agent_judge(resumes, arxiv_articles)

    # Call format agent
    formatted_output = agent_format(arxiv_articles,improved_resumes)

    status = ""

    return formatted_output, status



#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                          Gradio UI                       #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#

with gr.Blocks(css="""
.title-box {
    background-color: black;
    border: 3px solid orange;
    color: white;
    text-align: center;
    padding: 15px;
    border-radius: 10px;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 20px;
}

.subtitle {
    text-align: center;
    color: white;
    font-size: 16px;
    margin-bottom: 10px;
}

.warning {
    text-align: center;
    color: orange;
    font-size: 15px;
    margin-bottom: 20px;
    font-weight: bold;
}

/* bouton orange */
button {
    background-color: orange !important;
    color: white !important;
    font-weight: bold;
}

/* status box styling */
.status-box {
    text-align: center;
    color: orange;
    font-weight: bold;
    font-size: 14px;
}
""") as UI:

    # Title
    gr.Markdown('Scientific Paper Research Agent on ArXiv')

    # sentance
    gr.Markdown("""

This AI agent searches scientific paper on ArXiv, selects the most relevant articles,
and generates a clear and improved summary using multiple intelligent agents.

""")

    # time warning
    gr.Markdown("""

⚠️ The research process may take around 40 seconds. Please be patient.

""")

    # raw organisation
    with gr.Row():
        query = gr.Textbox(
            label="Research Topic",
            placeholder="Enter a research topic here...",
            elem_id="query-box",
            scale=4
        )
        status_box = gr.Label(
            value="",
            elem_classes="status-box",
            scale=1
        )

    #  Markdown output
    output_box = gr.Markdown(label="Research Results")

    # Bouton
    run_btn = gr.Button("Run Research")

    # parameters bouton
    run_btn.click(
        fn=research_pipeline,
        inputs=query,
        outputs=[output_box, status_box]
    )
    # enter to start like bouton
    query.submit(
        fn=research_pipeline,
        inputs=query,
        outputs=[output_box, status_box]
    )

UI.launch(share=True)