import streamlit as st
from groq import Groq

def generate_first_aid(emergency):

    try:
        # Get API key from Streamlit secrets
        api_key = st.secrets["GROQ_API_KEY"]

        client = Groq(api_key=api_key)

        prompt = f"""
You are a medical first aid assistant.

Provide clear, step-by-step first aid instructions for this situation:

{emergency}

Keep it simple, actionable, and safe.
"""

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192"
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI service error: {str(e)}"