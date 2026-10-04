import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖",
    layout="centered",
)


# -----------------------------
# Model
# -----------------------------
model = ChatOpenRouter(
    model="qwen/qwen3.8-27b:free",
)


# -----------------------------
# Agent Modes
# -----------------------------
AGENT_MODES = {
    "Angry Agent": (
        "You are an Angry AI agent. "
        "You respond aggressively and impatiently."
    ),
    "Sad Agent": (
        "You are a very sad AI agent. "
        "You respond in a depressed and emotional tone."
    ),
    "Funny Agent": (
        "You are a very Funny AI agent. "
        "You respond with humor and jokes."
    ),
}


# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = None


# -----------------------------
# Header
# -----------------------------
st.title("🤖 Choose Your Agent Wisely!")
st.write("Select an agent and start chatting.")


# -----------------------------
# Agent Selection
# -----------------------------
choice = st.radio(
    "Choose your agent:",
    options=list(AGENT_MODES.keys()),
    horizontal=True,
)


# Reset conversation when agent changes
if st.session_state.mode != choice:
    st.session_state.mode = choice
    st.session_state.messages = [
        SystemMessage(content=AGENT_MODES[choice])
    ]


# -----------------------------
# Clear Chat
# -----------------------------
if st.button("Clear Chat"):
    st.session_state.messages = [
        SystemMessage(content=AGENT_MODES[choice])
    ]
    st.rerun()


# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)


# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Type your message...")


if prompt:

    # Exit functionality
    if prompt == "0":
        st.write("Application exited.")
        st.stop()

    # Add user message
    human_message = HumanMessage(content=prompt)
    st.session_state.messages.append(human_message)

    # Display user message immediately
    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    response = model.invoke(st.session_state.messages)

    # Add AI message
    ai_message = AIMessage(content=response.text)
    st.session_state.messages.append(ai_message)

    # Display AI response
    with st.chat_message("assistant"):
        st.write(response.text)