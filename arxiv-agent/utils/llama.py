#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/
#                 llama usage function                    #
#/#/#/#/#/#/#/#/#/#/#/#/#//#/#/#/#/#/#//#/#//#/#/#/#/#/#/#/#/

from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path

#load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

env_path = Path(__file__).resolve().parent.parent / ".env"
print(f"Chemin .env : {env_path}")
print(f"Fichier existe : {env_path.exists()}")
load_dotenv(dotenv_path=env_path)
print(f"Clé lue : {os.getenv('GROQ_API_KEY')}")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def llama_generate(prompt, max_tokens=1500):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Tu es un assistant scientifique expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,  # 0.3 for Similar summary for articles 1 and 2
        max_tokens=max_tokens
    )
    return response.choices[0].message.content