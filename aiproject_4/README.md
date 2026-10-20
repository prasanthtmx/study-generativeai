# AI Project 4 — Streamlit Chat Assistant

A browser chat app that sends the full conversation to **OpenAI** or **Google Gemini**. The UI is built with **Streamlit**. Switch the provider in `config.json` or with `LLM_PROVIDER` in `.env`.

This is different from `aiproject_3`, which is a terminal chatbot (`python3 main.py`). This project is a web UI:

```bash
streamlit run app.py
```

Then open [http://127.0.0.1:8501](http://127.0.0.1:8501) in your browser.

## What Streamlit is

[Streamlit](https://streamlit.io) is a Python library that turns a script into a web app. You write normal Python (`st.title`, `st.chat_input`, `st.button`). Streamlit starts a local web server, opens a page in the browser, and **re-runs the whole script** every time the user types, clicks, or submits.

That rerun model is why this app stores messages in `st.session_state["history"]`. Without session state, the chat would disappear after every message.

| Streamlit piece | Used in this project | What it does |
| --- | --- | --- |
| `streamlit run app.py` | how you start the app | Starts a local server (default port **8501**) |
| `st.set_page_config` | `app.py` | Sets the browser tab title and icon |
| `st.title` | `app.py` | Page heading: My First AI Chat Assistant |
| `st.session_state` | `app.py` | Keeps the conversation across reruns |
| `st.chat_message` | `app.py` | Draws a user or assistant bubble |
| `st.chat_input` | `app.py` | The box at the bottom: "Type your message..." |
| `st.button` | `app.py` | Reset Conversation |
| `st.rerun` | `app.py` | Reloads the page after a reset |
| `st.markdown` | `app.py` | Renders message text |

### How a Streamlit rerun works here

1. The page loads. `app.py` runs from top to bottom.
2. If `history` is missing, it is created with a greeting.
3. Every stored message is drawn again.
4. If you type and send, Streamlit reruns `app.py`, the new user message is appended, `run_llm()` is called, and the reply is stored.
5. If you click **Reset Conversation**, history is replaced with a reset greeting and `st.rerun()` refreshes the page.

You do **not** run this file with `python app.py`. Streamlit must launch it so the web server and widgets exist.

## Project files

| File | What it does |
| --- | --- |
| `app.py` | Streamlit UI: chat history, input box, reset button |
| `llm_provider.py` | Loads `.env` and `config.json`, then calls OpenAI or Gemini |
| `config.json` | Active provider plus model and generation settings |
| `.env` | API keys (do not commit this file) |
| `requirements.txt` | Packages to install, including **streamlit** |
| `requirments.txt` | Same package list (older misspelled filename) |

## Setup

Use **this** project's virtual environment. A venv from another folder (for example `aiproject_3`) will not have Streamlit on `PATH`, and you will see `streamlit: command not found`.

```bash
cd /var/www/html/PythonStudy/aiproject_4
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Confirm Streamlit is installed in the active venv:

```bash
which streamlit
streamlit --version
```

`which streamlit` should point at `/var/www/html/PythonStudy/aiproject_4/.venv/bin/streamlit`.

If you already have `.venv`, skip `python3 -m venv .venv` and only activate + install.

### If you see `streamlit: command not found`

1. Check the folder. You must be in `aiproject_4`, not `aiproject_3`.
2. Activate this project's venv: `source .venv/bin/activate`
3. Install packages: `pip install -r requirements.txt`
4. Run again: `streamlit run app.py`

You can also call Streamlit through the venv Python if the command is still missing:

```bash
.venv/bin/python -m streamlit run app.py
```

## Environment variables (`.env`)

Create a `.env` file in this folder. Do not commit real keys.

```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
LLM_PROVIDER=openai
```

| Variable | Used by |
| --- | --- |
| `OPENAI_API_KEY` | OpenAI when the provider is `openai` |
| `GOOGLE_API_KEY` | Gemini when the provider is `gemini` |
| `GEMINI_API_KEY` | Optional alias for Gemini if `GOOGLE_API_KEY` is not set |
| `LLM_PROVIDER` | Optional override: `openai` or `gemini`. If set, it wins over `config.json` |

`llm_provider.py` calls `load_dotenv()` using the folder that contains the script, so keys load even if you start Streamlit from another directory.

## Config

`config.json` chooses the default provider and the generation settings:

```json
{
    "provider": "openai",
    "openai": {
        "model": "gpt-4o-mini",
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 200
    },
    "gemini": {
        "model": "gemini-2.5-flash",
        "temperature": 0.6,
        "top_p": 0.8,
        "max_tokens": 300
    }
}
```

| Field | Meaning |
| --- | --- |
| `provider` | `"openai"` or `"gemini"` (ignored if `LLM_PROVIDER` is set in `.env`) |
| `model` | Which model that provider should call |
| `temperature` | Higher = more varied answers |
| `top_p` | Nucleus sampling |
| `max_tokens` | Max length of the reply. For Gemini this is sent as `max_output_tokens` |

To use Gemini, either set `"provider": "gemini"` in `config.json` or set `LLM_PROVIDER=gemini` in `.env`. Restart Streamlit (or let it auto-reload) after changing these files.

## How to run

From this folder, with the venv active:

```bash
cd /var/www/html/PythonStudy/aiproject_4
source .venv/bin/activate
streamlit run app.py
```

Streamlit prints a local URL, usually:

```text
URL: http://127.0.0.1:8501
```

Open that URL in your browser.

| In the UI | What happens |
| --- | --- |
| Type a message and press Enter / Send | Message is stored, sent to the LLM, reply is shown |
| Reset Conversation | History is cleared and a new greeting is shown |

Stop the server with `Ctrl+C` in the terminal.

If port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

## How the code flows

```text
Browser (Streamlit page)
        |
        v
     app.py
        |  keeps messages in st.session_state["history"]
        v
  llm_provider.run_llm(history)
        |  reads CONFIG["provider"] or LLM_PROVIDER
        +-- openai  --> OpenAI chat.completions
        +-- gemini  --> Gemini generate_content
```

1. `app.py` builds or updates `history`: a list of `{ "role": "user"|"assistant", "content": "..." }`.
2. `run_llm(history)` picks the provider.
3. OpenAI receives the list as chat messages.
4. Gemini receives the same history flattened into one text block (`role: content` on each line).
5. The reply string is appended to `history` and drawn as an assistant bubble.

If a key is missing or the API fails, the error is shown in the chat instead of crashing the page.

## Packages

`requirements.txt` (and `requirments.txt`) lists:

| Package | Why it is needed |
| --- | --- |
| `streamlit` | Web UI and `streamlit run` command |
| `openai` | Official OpenAI client |
| `google-generativeai` | Gemini client |
| `python-dotenv` | Loads `.env` into environment variables |

## Troubleshooting

| Problem | Likely cause | Fix |
| --- | --- | --- |
| `streamlit: command not found` | Wrong folder or venv not active | `cd aiproject_4`, `source .venv/bin/activate`, `pip install -r requirements.txt` |
| `ModuleNotFoundError: llm_providers` | Old import (plural) | Current `app.py` imports `llm_provider` (singular) |
| `[Error] OPENAI_API_KEY is missing` | No key in `.env` | Add `OPENAI_API_KEY=...` in this project's `.env` |
| `[Error] GEMINI_API_KEY or GOOGLE_API_KEY is missing` | No Google key | Add `GOOGLE_API_KEY=...` or `GEMINI_API_KEY=...` |
| `[Error] Invalid provider` | Typo in provider name | Use `openai` or `gemini` in `config.json` or `LLM_PROVIDER` |
| Page opens but chat does nothing | Streamlit not serving this `app.py` | Run `streamlit run app.py` from `aiproject_4` |
| You are in `aiproject_3` | That project is a CLI app | Use `python3 main.py` there, or `cd` here for Streamlit |

## Quick start (copy/paste)

```bash
cd /var/www/html/PythonStudy/aiproject_4
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then chat at [http://127.0.0.1:8501](http://127.0.0.1:8501).
