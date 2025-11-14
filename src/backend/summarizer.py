from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str) -> str:
    prompt = ("Summarize the following text into academic, clean and understandable bullet points!"
              "Focus on the key concepts and give a short explanation of them.\n\n"
              f"{text}\n\nSummary:")

    response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content