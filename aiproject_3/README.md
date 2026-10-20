# AI Project 3 — CLI Chatbot

A terminal chatbot that sends one message at a time to OpenAI or Google Gemini. Switch the provider in `config.json`. Type `exit` or `quit` to stop.

## Project files

| File | What it does |
| --- | --- |
| `main.py` | Loads `.env` and `config.json`, then runs the chat loop |
| `llm_provider.py` | Builds an OpenAI or Gemini client and sends one user message |
| `config.json` | Active provider and model names |
| `.env` | API keys (do not commit this file) |
| `requirments.txt` | Packages to install (filename is missing an `e`) |

## Setup

Use this project's virtual environment so `python3` loads the packages installed here.

```bash
cd /var/www/html/PythonStudy/aiproject_3
source .venv/bin/activate
pip install -r requirments.txt
```

Put your keys in a `.env` file in this folder:

```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

| Variable | Used by |
| --- | --- |
| `OPENAI_API_KEY` | `llm_provider.py` when `provider` is `openai` |
| `GOOGLE_API_KEY` | `llm_provider.py` when `provider` is `gemini` |
| `GEMINI_API_KEY` | optional alias for Gemini; used if `GOOGLE_API_KEY` is not set |

`main.py` calls `load_dotenv()` first. Gemini reads `GEMINI_API_KEY`, then falls back to `GOOGLE_API_KEY`.

`LLM_PROVIDER` in `.env` is not used. The provider comes from `config.json`.

## Config

`config.json` chooses which API and model to use:

```json
{
    "provider": "gemini",
    "models": {
        "openai": "gpt-4o-mini",
        "gemini": "gemini-2.5-flash"
    }
}
```

- `"provider": "gemini"` uses `gemini-2.5-flash` and `GEMINI_API_KEY` or `GOOGLE_API_KEY`
- `"provider": "openai"` uses `gpt-4o-mini` and `OPENAI_API_KEY`

## How to run

From this folder, with the venv active:

```bash
source .venv/bin/activate
python3 main.py
```

If you skip `source .venv/bin/activate`, `python3` may use `~/.local` packages instead of this project's venv.

Commands inside the chat:

| You type | What happens |
| --- | --- |
| any question | sent to the model; the reply is printed |
| empty line | skipped; you are asked to type a message |
| `exit` or `quit` | prints `Goodbye...` and stops |

Letter case does not matter for `exit` / `quit`.

## Input and output

Startup (Gemini, as in the current config):

```text
>>>>> Simple CLI Chatbot(type 'exit' to quit)
Loaded configuration: gemini with model gemini-2.5-flash
Gemini client initiated successfully.✅
You:
```

One turn:

```text
You: What is a list in Python?
Bot: A list is an ordered, mutable collection of items, written with square brackets.

You: exit
Goodbye...
```

Blank input:

```text
You:
Please enter a valid question or message for the bot..
You:
```

If `config.json` is missing or neither Gemini key is set, the program prints an initialization error and exits before the loop starts:

```text
>>>>> Simple CLI Chatbot(type 'exit' to quit)
Loaded configuration: gemini with model gemini-2.5-flash
Initialization error: GEMINI_API_KEY or GOOGLE_API_KEY env variable was not set.
```

If a request fails after the loop has started:

```text
You: Hello
Error while chat: Error in gemini chat: ...
```

Each `chat()` call is a new request. The bot does not keep earlier messages as conversation history.

## How the code fits together

1. `main.py` loads `.env`, then `load_config()` reads `config.json`.
2. `LLMProvider(config)` creates either `OpenAI(...)` or `genai.GenerativeModel(...)`.
3. For Gemini, the key is `os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")`.
4. The `while True` loop reads `You: ` from the terminal.
5. `bot.chat(user_message=...)` sends that one string to the API.
6. OpenAI uses `chat.completions.create` and returns `choices[0].message.content`.
7. Gemini uses `generate_content` and returns `response.text`.
8. The reply is printed as `Bot: ...`.

## Troubleshooting

| What you see | Cause | Fix |
| --- | --- | --- |
| `GEMINI_API_KEY or GOOGLE_API_KEY env variable was not set` | Gemini is selected, but `.env` has neither key | Add `GOOGLE_API_KEY` (or `GEMINI_API_KEY`) to `.env` |
| `OPENAI_API_KEY env variable was not set` | OpenAI is selected, but the key is missing | Add `OPENAI_API_KEY` to `.env` |
| `FutureWarning` from `~/.local/lib/python3.10/...` | Ran `python3` without this project's venv | `source .venv/bin/activate` then `python3 main.py` |
| Unsupported provider | `config.json` `provider` is not `openai` or `gemini` | Set `"provider"` to `openai` or `gemini` |

## Requirements

```txt
openai
anthropic
google-generativeai
transformers
huggingface_hub
ollama
python-dotenv
```

The chatbot code uses `openai`, `google-generativeai`, and `python-dotenv`. The other packages are listed for later provider work.
