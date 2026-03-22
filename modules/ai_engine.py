import os
from groq import Groq
import streamlit as st

api_key = st.secrets["GROQ_API_KEY"]

# read the key
api_key = os.getenv("GROQ_API_KEY")

print("DEBUG KEY:", api_key)  # temporary debug

client = Groq(api_key=api_key)

def generate_first_aid(emergency):

    prompt = f"""
You are a professional first aid assistant.

Emergency situation: {emergency}

Provide:

1. Immediate actions
2. What NOT to do
3. Warning signs
4. When to seek medical help
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI request failed: {e}"