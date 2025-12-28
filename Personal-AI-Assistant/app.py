import streamlit as st
import google.generativeai as genai
import json

from config.settings import Settings

from jarvis.assistant import JarvisAssistant
from jarvis.gemini_engine import GeminiEngine
from jarvis.prompt_controller import PromptController
from jarvis.memory import Memory
from jarvis.command_handler import CommandHandler


# Streaming Response Function
def stream_response(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt, stream=True)
    output = ""
    placeholder = st.empty()
    for chunk in response:
        if chunk.text:
            output += chunk.text
            placeholder.markdown(output)
    return output 

# Page Config (Tab)
st.set_page_config(page_title="Personal-AI-Assistant",page_icon="🔮")
st.markdown(
    """
    <style>
    /* Main screen background only */
   .stApp, .main {
    background-color: #f8f8f8;  
    color: #000000;             
}
    /* Chat messages & text readability */
    .stMarkdown, .stText, .stExpanderContent, .stChatMessage {
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Greeting & Title
st.title("Jarvis – AI Assistant")
st.write("👋 Hello! I’m Jarvis, ready to help you learn, code, or plan your career!")

# Sidebar Controls
st.sidebar.header("📂 Controls")
role = st.sidebar.selectbox("Choose Jarvis Role", ["General", "Command", "Tutor", "Coder", "Mentor"])

if st.sidebar.button("Clear History"):
    open("conversation.json", "w").write("[]")
    st.sidebar.success("Erase Memory!")

# Chat Input
user_input = st.chat_input("Ask Jarvis anything.....")

# Core Initialization
settings = Settings()
engine = GeminiEngine(settings.load_api_key())
memory = Memory()
prompt_controller = PromptController(role=role)
jarvis = JarvisAssistant(engine, prompt_controller, memory)
command_handler = CommandHandler()


# Session Greeting
if not memory.get_history():
    st.chat_message("assistant").write("👋 Hi, I’m Jarvis. How can I help you?")

# Display Previous Chat History
for msg in memory.get_history():
    st.chat_message(msg["role"]).write(msg["message"])



# Chat Input and Response
if user_input:
    st.chat_message("user").write(user_input)

    if role == "Command":
        # Handle command mode
        command_response = command_handler.handle(user_input)
        if command_response:
            st.chat_message("assistant").write(command_response)
        else:
            st.chat_message("assistant").write("Unknown command.")
    else:
        # Assistant mode
        prompt = prompt_controller.build_prompt(user_input, memory)
        response = stream_response(prompt)

        # Save to memory
        memory.add("user", user_input)
        memory.add("assistant", response)

        # Role-based styling
        if role == "Tutor":
            st.chat_message("assistant").write(f"{response}")
        elif role == "Coder":
            st.chat_message("assistant").code(response)
        elif role == "Mentor":
            st.chat_message("assistant").write(f"{response}")
        else:
            st.chat_message("assistant").write(response)