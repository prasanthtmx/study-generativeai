"""
LLM client wrapper for the CLI chatbot.

Builds an OpenAI or Gemini client from config.json, then sends
one user message and returns the model's text reply.
Load .env with python-dotenv before creating LLMProvider.
"""

import os
import google.generativeai as genai
from openai import OpenAI


class LLMProvider:
    """Talk to one LLM provider using settings from a config dict."""

    def __init__(self, config: dict):
        """
        Create the client for the provider named in config.

        Expected config shape:
            {
                "provider": "gemini",
                "models": {
                    "openai": "gpt-4o-mini",
                    "gemini": "gemini-2.5-flash"
                }
            }
        """
        # Which API to use, and which model name that API should call.
        self.provider = config["provider"]
        self.model = config["models"][self.provider]

        if self.provider == "openai":
            # OpenAI reads OPENAI_API_KEY from the environment.
            key = os.getenv("OPENAI_API_KEY")
            if not key:
                raise ValueError("OPENAI_API_KEY env variable was not set.")
            self.client = OpenAI(api_key=key)
        elif self.provider == "gemini":
            # Gemini SDK is configured once, then a model object is created.
            # Accept either name so .env can use GEMINI_API_KEY or GOOGLE_API_KEY.
            key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
            if not key:
                raise ValueError("GEMINI_API_KEY or GOOGLE_API_KEY env variable was not set.")
            genai.configure(api_key=key)
            self.client = genai.GenerativeModel(self.model)
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")
        print(f"{self.provider.title()} client initiated successfully.✅")

    def chat(self, user_message: str) -> str:
        """Send one user message and return the model's text reply."""
        try:
            if self.provider == "openai":
                # Chat Completions API: a list of role/content messages.
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": user_message}]
                )
                return response.choices[0].message.content
            elif self.provider == "gemini":
                # Gemini generate_content takes the prompt string directly.
                response = self.client.generate_content(user_message)
                return response.text

        except Exception as e:
            raise Exception(f"Error in {self.provider} chat: {str(e)}")
