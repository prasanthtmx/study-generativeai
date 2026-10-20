"""
Streamlit chat UI for a simple AI assistant.

Conversation history lives in session state and is sent to the LLM
provider selected in config.json (OpenAI or Gemini).
"""

import warnings

warnings.filterwarnings("ignore")

import streamlit as st
from llm_provider import run_llm  # filename is llm_provider.py (singular)

# Browser tab title and page heading
st.set_page_config(page_title="My First AI Chat Assistant", page_icon="🤖")
st.title("🤖 My First AI Chat Assistant")

# Create conversation memory the first time the page loads
if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

# Replay previous messages so the chat stays visible after each Streamlit rerun
for msg in st.session_state["history"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Wait for the user to type a message
if prompt := st.chat_input("Type your message..."):
    # Store and show the user message immediately
    st.session_state["history"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Call the configured provider with the full conversation
    try:
        reply = run_llm(st.session_state["history"])
    except Exception as exc:
        reply = f"[Error] Could not get a reply: {exc}"

    # Store and show the assistant reply
    st.session_state["history"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)

# Clear history without refreshing the browser
if st.button("🔄 Reset Conversation"):
    st.session_state["history"] = [
        {"role": "assistant", "content": "Conversation reset. How can I assist you?"}
    ]
    st.rerun()
