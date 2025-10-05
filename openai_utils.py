import os
import openai
from dotenv import load_dotenv

# Load environment variables and configure the API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def summarize_text(pdf_context, summary_type):
    """
    Generates a summary for the given text using OpenAI's GPT-3.5-turbo model.
    """
    prompt_map = {
        "Concise": "Generate a concise, easy-to-read summary of the following document, focusing on the main purpose and key findings. Keep it under 150 words.",
        "Detailed": "Provide a detailed, section-by-section summary of the following document. Use markdown headings for each section.",
        "Bullet Points": "Extract the most important findings, conclusions, and action items from the following document as a clear, concise bulleted list.",
    }

    prompt = f"{prompt_map[summary_type]}\n\nDOCUMENT TEXT:\n{pdf_context}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes documents accurately and concisely.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred during summarization: {e}"


def ask_question(pdf_context, user_question):
    """
    Answers a user's question based on the provided PDF text.
    """
    prompt = f"""
    Based *only* on the document context provided below, answer the user's question.
    If the answer is not found in the document, say "The answer is not available in the provided document."

    DOCUMENT CONTEXT:
    {pdf_context}

    QUESTION: {user_question}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions based only on the provided document context.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while answering the question: {e}"
