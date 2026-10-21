# Call Transcript Analyzer

Read customer-support call transcripts, classify the call type, score the agent, then write a summary and coaching tips.

This is a study project. The working notebook is `experiment_one.ipynb`. `project_document.py` is the study plan.

## What it does

1. Load API keys from `.env` and settings from `config/config.json`.
2. Read transcripts from `data/transcripts.csv`.
3. Classify each call as `billing`, `claims`, `complaint`, or `general_query`.
4. Choose evaluation criteria from the predicted call type.
5. Score the agent from 1 to 5 and explain the score.
6. Later: save results to `data/output.xlsx` and wrap this in FastAPI.

## Evaluation plan

Not every call uses every criterion.

| Call type | Criteria |
|---|---|
| billing | knowledge_accuracy, resolution_quality |
| claims | knowledge_accuracy, resolution_quality |
| complaint | tone_empathy, resolution_quality |
| general_query | knowledge_accuracy |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy the env template and add your keys:

```bash
cp .env.example .env
```

Set these in `.env`:

```
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
LLM_PROVIDER=openai
```

`LLM_PROVIDER` can be `openai` or `gemini`. Do not commit `.env`.

## Run

Study plan:

```bash
python project_document.py
```

Main experiment:

```bash
jupyter notebook experiment_one.ipynb
```

The notebook:

1. Loads config and transcript data
2. Initializes OpenAI or Gemini through LangChain
3. Classifies all sample calls
4. Routes each call to the right evaluation criteria
5. Builds tone, resolution, and knowledge scoring chains

## Project folders

```
.gitignore              ignore .env, .venv, and local cache
.env / .env.example     secrets template and local keys
config/config.json      models, labels, score range
data/                   input transcripts and output Excel
experiment_one.ipynb    classify + evaluate transcripts
experiment.ipynb        first load of config and data
project_document.py     study plan
requirements.txt        packages for .venv
```

## Data

Each transcript row has:

- `call_id`
- `agent_name`
- `transcript`
- `expected_call_type`

Sample files:

- `data/transcripts.csv` — sample calls used in the notebook
- `data/transcripts.xlsx` — same shape, different agent names
- `data/output.xlsx` — later results after the model runs

## Config

`config/config.json` stores settings, not secrets.

- Models: `gpt-4o-mini` / `gemini-1.5-flash`
- Temperature: `0.3` (low = more consistent answers)
- Labels: billing, claims, complaint, general_query
- Scores: 1 to 5

## Ideas used

- Dictionary / JSON — config and each transcript row
- List — many calls, labels, recommendations
- pandas — load CSV / Excel and save output
- python-dotenv — read API keys from `.env`
- LangChain — talk to OpenAI or Gemini
- Pydantic — force the model answer into a fixed shape
- FastAPI — later, a small web API for uploads

## Goal

Help a support team review calls quickly:

- know what the call was about
- know how the agent performed
- get clear coaching next steps
