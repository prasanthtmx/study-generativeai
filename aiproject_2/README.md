# AI Project 2

Small Python scripts that send the same kind of prompt to different LLM providers: Google Gemini, OpenAI, Ollama, and Hugging Face.

## Setup

Use the project virtual environment so the packages in `requirements.txt` are the ones that get loaded.

```bash
cd /var/www/html/PythonStudy/aiproject_2
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment variables

Copy the keys you need into a `.env` file in this folder. Do not commit `.env`.

| Variable | Used by |
| --- | --- |
| `GOOGLE_API_KEY` | `gemini_app.py` |
| `GEMINI_API_KEY` | `google_model_avilability.py`, `compare_app,py` |
| `OPENAI_API_KEY` | `opeanai_app.py`, `compare_app,py` |
| `HUGGINGFACE_API_KEY` | `huggingface_app.py` |
| `OLLAMA_API_KEY` | `ollama_app.py` (Ollama usually runs locally and does not need this) |
| `LLM_PROVIDER` | optional; not required by the current scripts |

If Gemini scripts fail with a missing key, set both `GOOGLE_API_KEY` and `GEMINI_API_KEY` to the same Google AI Studio key.

## Scripts

| File | What it does |
| --- | --- |
| `gemini_app.py` | Sends one prompt to Gemini (`gemini-3.8-flash`) using the current `google-genai` SDK |
| `opeanai_app.py` | Sends one prompt to OpenAI (`gpt-4o-mini`) |
| `ollama_app.py` | Sends one prompt to a local Ollama model (`llama3.1:8b`) |
| `huggingface_app.py` | Sends one prompt through Hugging Face Inference Providers (`Qwen/Qwen3-4B-Instruct-2507`) |
| `google_model_avilability.py` | Lists Gemini models that support `generateContent` |
| `compare_app,py` | Runs the same prompt on OpenAI, Gemini, and Ollama, then prints the answers |

Run a script after activating the venv:

```bash
python3 gemini_app.py
python3 opeanai_app.py
python3 ollama_app.py
python3 huggingface_app.py
python3 google_model_avilability.py
python3 "compare_app,py"
```

The compare file is named `compare_app,py` (comma, not a dot). Quotes are required so the shell treats it as one filename.

## Notes

- **Gemini:** `gemini_app.py` uses `from google import genai`. The compare and model-list scripts still use the older `google.generativeai` package.
- **Ollama:** Install [Ollama](https://ollama.com), start it, and pull the model first, for example `ollama pull llama3.1:8b`. The compare script uses `mistral`.
- **Hugging Face:** Inference Providers need account credits. The old host `api-inference.huggingface.co` no longer works.
- **OpenAI and Gemini:** Need valid API keys and network access.

## Requirements

```txt
google-genai
python-dotenv
openai
ollama
huggingface_hub
```
