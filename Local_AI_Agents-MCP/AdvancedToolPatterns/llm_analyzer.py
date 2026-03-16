import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def llm_project_analysis(report):

    prompt = f"""
    Aşağıdaki proje analizini yorumla:

    {report}

    Bu proje hangi tür bir proje olabilir?
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content