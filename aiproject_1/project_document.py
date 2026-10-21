"""
Python Study — AI Project 1 document
Call Transcript Classifier and Evaluator

This file is the study plan only.
It explains what we will build and which ideas we need.
The actual LangChain / FastAPI program comes next.
"""

print("=" * 60)
print("AI PROJECT 1: CALL TRANSCRIPT ANALYZER")
print("=" * 60)
print("Read customer-support call transcripts, classify the call")
print("type, score the agent, then write a summary and tips.")
print()

# ------------------------------------------------------------------
# 1. DATA STORED
# ------------------------------------------------------------------
print("1. DATA STORED")
print("-" * 60)

transcripts = [
    {
        "call_id": 1,
        "agent_name": "Alice",
        "transcript": "Customer: I was charged twice... Agent: Let me check...",
        "expected_call_type": "billing",
    },
    {
        "call_id": 2,
        "agent_name": "Bob",
        "transcript": "Customer: My claim has been pending... Agent: I understand...",
        "expected_call_type": "claims",
    },
    {
        "call_id": 3,
        "agent_name": "Charlie",
        "transcript": "Customer: This is the third time I'm calling! Agent: I apologize...",
        "expected_call_type": "complaint",
    },
    {
        "call_id": 4,
        "agent_name": "Diana",
        "transcript": "Customer: Can you explain my coverage... Agent: Sure, let me walk you through...",
        "expected_call_type": "general_query",
    },
]

print("Transcripts (list of dictionaries): one row per call")
print("  Columns: call_id, agent_name, transcript, expected_call_type")
print()
for row in transcripts:
    print(f"  Call {row['call_id']} | {row['agent_name']:8} | {row['expected_call_type']}")
print()
print("Files:")
print("  data/transcripts.csv   -> sample calls used in the notebook")
print("  data/transcripts.xlsx  -> same shape, different agent names")
print("  data/output.xlsx       -> later results after the model runs")
print()

# ------------------------------------------------------------------
# 2. CONFIG AND SECRETS
# ------------------------------------------------------------------
print("2. CONFIG AND SECRETS")
print("-" * 60)

config = {
    "llm": {
        "openai_model": "gpt-4o-mini",
        "gemini_model": "gemini-1.5-flash",
        "temperature": 0.3,
    },
    "evaluation": {
        "criteria": ["tone_empathy", "knowledge_accuracy", "resolution_quality"],
        "score_range": [1, 5],
    },
    "classification": {
        "labels": ["billing", "claims", "complaint", "general_query"],
    },
}

print("config/config.json stores settings, not secrets.")
print(f"  Models: {config['llm']['openai_model']} / {config['llm']['gemini_model']}")
print(f"  Temperature: {config['llm']['temperature']}  (low = more consistent answers)")
print(f"  Labels: {', '.join(config['classification']['labels'])}")
print(f"  Scores: {config['evaluation']['score_range'][0]} to {config['evaluation']['score_range'][1]}")
print()
print(".env stores secret keys. Copy from .env.example and fill in:")
print("  OPENAI_API_KEY")
print("  GOOGLE_API_KEY")
print("  LLM_PROVIDER   (openai or gemini)")
print("Never print or commit the real keys.")
print()

# ------------------------------------------------------------------
# 3. PROGRAM FLOW
# ------------------------------------------------------------------
print("3. PROGRAM FLOW")
print("-" * 60)
print("  1. Load .env keys with python-dotenv")
print("  2. Load config/config.json")
print("  3. Read transcripts from CSV or Excel with pandas")
print("  4. For each call, send the transcript to the LLM")
print("  5. Classify the call type")
print("  6. Score the agent on the right criteria")
print("  7. Write a short summary and recommendations")
print("  8. Save results to data/output.xlsx")
print("  9. Later: wrap this in FastAPI so others can upload calls")
print()

# ------------------------------------------------------------------
# 4. ACTIONS
# ------------------------------------------------------------------
print("4. ACTIONS (WHAT THE MODEL DOES)")
print("-" * 60)

print("  Classify")
print("    Read the transcript.")
print("    Pick one label: billing / claims / complaint / general_query.")
print("    Also return a confidence score (0 to 1).")
print()

print("  Choose evaluation plan")
print("    Not every call uses every criterion.")
print("    billing / claims  -> knowledge_accuracy + resolution_quality")
print("    complaint         -> tone_empathy + resolution_quality")
print("    general_query     -> knowledge_accuracy")
print()

print("  Evaluate")
print("    Score each chosen criterion from 1 to 5.")
print("    Add a short reason for the score.")
print()

print("  Summarize")
print("    One paragraph: what the agent did well and what was missing.")
print()

print("  Recommend")
print("    A short list of coaching tips for the agent.")
print()

# Mini study: pick criteria from the call type
sample_type = "complaint"
plan = {
    "billing": ["knowledge_accuracy", "resolution_quality"],
    "claims": ["knowledge_accuracy", "resolution_quality"],
    "complaint": ["tone_empathy", "resolution_quality"],
    "general_query": ["knowledge_accuracy"],
}

print("Study example: choose the evaluation plan")
print(f"  call type = {sample_type}")
print(f"  plan      = {plan[sample_type]}")
print()

# Mini study: compare predicted vs expected
predicted = "billing"
expected = transcripts[0]["expected_call_type"]
print("Study example: check classification")
print(f"  expected  = {expected}")
print(f"  predicted = {predicted}")
print(f"  match     = {predicted == expected}")
print()

# ------------------------------------------------------------------
# 5. IDEAS USED IN THIS PROJECT
# ------------------------------------------------------------------
print("5. IDEAS USED")
print("-" * 60)
print("  Dictionary / JSON  -> config and each transcript row")
print("  List               -> many calls, labels, recommendations")
print("  pandas             -> load CSV / Excel and save output")
print("  python-dotenv      -> read API keys from .env")
print("  LangChain          -> talk to OpenAI or Gemini")
print("  Pydantic           -> force the model answer into a fixed shape")
print("  FastAPI            -> later, a small web API for uploads")
print()

# ------------------------------------------------------------------
# 6. PROJECT FOLDERS
# ------------------------------------------------------------------
print("6. PROJECT FOLDERS")
print("-" * 60)
print("  .env / .env.example   secrets template and local keys")
print("  config/config.json    models, labels, score range")
print("  data/                 input transcripts and output Excel")
print("  experiment.ipynb      first experiments: load config + data")
print("  requirements.txt      packages to install in .venv")
print("  project_document.py   this study plan")
print()

# ------------------------------------------------------------------
# 7. GOAL
# ------------------------------------------------------------------
print("7. GOAL")
print("-" * 60)
print("Help a support team review calls quickly:")
print("  know what the call was about,")
print("  know how the agent performed,")
print("  and get clear coaching next steps.")
print()
print("Next step: wire LangChain to classify one transcript")
print("and return a structured evaluation.")
print("=" * 60)
