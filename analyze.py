import os
from dotenv import load_dotenv
import openai

# Load your API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_failure(log_snippet: str) -> str:
    """
    Analyze test failure logs using GPT-4o-mini
    Returns a string with:
    - Root Cause
    - Reason
    - Suggested Fix
    """
    prompt = f"""
    You are a test failure expert. Analyze this test log and provide:
    - Root Cause (Assertion failure / Element not found / Timeout / API error)
    - Reason (short explanation)
    - Suggested fix

    Test Log:
    {log_snippet}
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content