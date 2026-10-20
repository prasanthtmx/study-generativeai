"""
CLI entry point for the chatbot.

Loads .env keys, reads config.json, builds LLMProvider,
then loops on terminal input until the user types exit or quit.
"""

import os
import json
from dotenv import load_dotenv
from llm_provider import LLMProvider


def load_config(config_path: str = "config.json") -> dict:
    """Read provider and model names from a JSON config file."""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {config_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON in the config file: {config_path}")


def run_chat():
    """Start the chatbot: load config, create the client, then chat in a loop."""
    print(">>>>> Simple CLI Chatbot(type 'exit' to quit)")

    # Fail early if config or API keys are missing, so the loop never starts.
    try:
        config = load_config()
        print(f"Loaded configuration: {config['provider']} with model {config['models'][config['provider']]}")

        bot = LLMProvider(config)
    except Exception as e:
        print(f"Initialization error: {e}")
        return

    while True:
        user_input = input("You: ")
        # Allow either "exit" or "quit", ignoring letter case.
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye...")
            break
        # Skip blank lines so we do not send empty prompts to the API.
        if not user_input.strip():
            print("Please enter a valid question or message for the bot..")
            continue
        try:
            reply = bot.chat(user_message=user_input)
            print(f"Bot: {reply}\n")
        except Exception as e:
            print(f"Error while chat: {str(e)}")


if __name__ == "__main__":
    # Load API keys from .env before LLMProvider reads os.getenv.
    load_dotenv()
    run_chat()
