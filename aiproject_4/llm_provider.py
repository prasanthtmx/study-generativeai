"""
LLM router: sends chat history to OpenAI or Gemini based on config.json.

API keys stay in the local .env file. This module is imported by app.py.
"""

import json
import os
import warnings

import google.generativeai as genai
from dotenv import load_dotenv
from openai import OpenAI

warnings.filterwarnings("ignore")

# Resolve files from this script so Streamlit works from any working directory.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

with open(os.path.join(BASE_DIR, "config.json"), "r", encoding="utf-8") as f:
    CONFIG = json.load(f)


def run_openai(messages):
    """Send the full chat history to OpenAI and return the assistant text."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "[Error] OPENAI_API_KEY is missing in the .env file."

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=CONFIG["openai"]["model"],
        messages=messages,
        max_tokens=CONFIG["openai"].get("max_tokens", 200),
        temperature=CONFIG["openai"].get("temperature", 0.7),
        top_p=CONFIG["openai"].get("top_p", 0.9),
    )
    content = response.choices[0].message.content
    return content.strip() if content else "[Error] OpenAI returned an empty reply."


def run_gemini(prompt: str):
    """Send a flattened conversation string to Gemini and return the text."""
    # Accept either key name so a typical Google .env still works.
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "[Error] GEMINI_API_KEY or GOOGLE_API_KEY is missing in the .env file."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(CONFIG["gemini"]["model"])

    # config.json uses max_tokens; Gemini's SDK expects max_output_tokens.
    max_output = CONFIG["gemini"].get("max_output_tokens") or CONFIG["gemini"].get(
        "max_tokens", 200
    )

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": CONFIG["gemini"].get("temperature", 0.7),
            "top_p": CONFIG["gemini"].get("top_p", 0.9),
            "max_output_tokens": max_output,
        },
    )

    # response.text can be empty or raise if Gemini blocked the reply.
    try:
        text = response.text
    except Exception:
        return "[Error] Gemini returned an empty or blocked response."

    return text.strip() if text else "[Error] Gemini returned an empty or blocked response."


def run_llm(history):
    """Route the conversation to the provider named in config.json (or .env)."""
    # .env LLM_PROVIDER can override config.json without editing the JSON file.
    provider = os.getenv("LLM_PROVIDER", CONFIG.get("provider", "")).strip().lower()

    if provider == "openai":
        return run_openai(history)

    if provider == "gemini":
        conversation_text = "\n".join(
            f"{m['role']}: {m['content']}" for m in history
        )
        return run_gemini(conversation_text)

    return "[Error] Invalid provider. Use 'openai' or 'gemini' in config.json or .env."
