import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage, AIMessage
import uuid

# =========================================
# Utility Functions
# =========================================

def generate_thread_id():
    return str(uuid.uuid4())


def generate_chat_title(user_message):
    """
    Creates a ChatGPT-style title from first message.
    """
    title = user_message.strip()

    if len(title) > 35:
        title = title[:35] + "..."

    return title


def add_thread(thread_id, title="New Chat"):

    if thread_id not in st.session_state["chat_titles"]:

        st.session_state["chat_titles"][thread_id] = title

        if thread_id not in st.session_state["chat_threads"]:
            st.session_state["chat_threads"].append(thread_id)


def reset_chat():

    new_thread = generate_thread_id()

    st.session_state["thread_id"] = new_thread

    add_thread(new_thread)

    st.session_state["message_history"] = []


def load_conversation(thread_id):

    state = chatbot.get_state(
        config={"configurable": {"thread_id": thread_id}}
    )

    return state.values.get("messages", [])


# =========================================
# Session Setup
# =========================================

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = []

if "chat_titles" not in st.session_state:
    st.session_state["chat_titles"] = {}

add_thread(st.session_state["thread_id"])

# =========================================
# Sidebar
# =========================================

st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("➕ New Chat"):
    reset_chat()
    st.rerun()

st.sidebar.markdown("### My Conversations")

for thread_id in reversed(st.session_state["chat_threads"]):

    title = st.session_state["chat_titles"].get(
        thread_id,
        "Untitled Chat"
    )

    if st.sidebar.button(title, key=thread_id):

        st.session_state["thread_id"] = thread_id

        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:

            if isinstance(msg, HumanMessage):
                role = "user"
            else:
                role = "assistant"

            temp_messages.append(
                {
                    "role": role,
                    "content": msg.content
                }
            )

        st.session_state["message_history"] = temp_messages

        st.rerun()

# =========================================
# Main Chat Area
# =========================================

for message in st.session_state["message_history"]:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type here")

# =========================================
# User Sends Message
# =========================================

if user_input:

    current_thread = st.session_state["thread_id"]

    # If this is the first message, create title
    if len(st.session_state["message_history"]) == 0:

        title = generate_chat_title(user_input)

        st.session_state["chat_titles"][current_thread] = title

    # Display user message
    st.session_state["message_history"].append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    CONFIG = {
        "configurable": {
            "thread_id": current_thread
        }
    }

    with st.chat_message("assistant"):

        def ai_only_stream():

            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            ):

                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

    st.session_state["message_history"].append(
        {
            "role": "assistant",
            "content": ai_message
        }
    )