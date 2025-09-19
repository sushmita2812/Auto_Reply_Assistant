import os
from openai import OpenAI

# Try to get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "❌ OPENAI_API_KEY is not set. Please set it as an environment variable:\n"
        "   PowerShell: setx OPENAI_API_KEY \"your_api_key_here\"\n"
        "   Then restart VS Code and run again."
    )

# Initialize client
client = OpenAI(api_key=api_key)

def generate_responses(user_message: str):
    """Generate 3 short, polite professional auto-replies for a given message."""
    prompt = f"""
You are an AI assistant. 
Generate 3 **short, polite, professional auto-replies** for the following message. 
Do NOT repeat the sender's message. 
Number the replies 1, 2, 3. 
Each reply should be 1–2 sentences only. 

Message: "{user_message}"

Output format:
1. Reply 1
2. Reply 2
3. Reply 3
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200
    )

    # Correct dot notation
    raw_output = response.choices[0].message.content

    # Parse numbered replies cleanly
    replies = []
    for line in raw_output.split("\n"):
        line = line.strip()
        if line and (line[0].isdigit() and line[1] in [".", ")"]):
            # remove "1. ", "2. ", etc.
            replies.append(line[2:].strip())
    return replies[:3]
