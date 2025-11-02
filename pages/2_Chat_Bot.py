import streamlit as st
import subprocess

# Set page configuration
st.set_page_config(page_title="Dr.Grow Chat", layout="centered")
st.title("🪴Chatbot")

# Model selection
selectoption = st.selectbox(
    'Select a model',
    ('🦙llama', '🤖phi')
)
option = 'llama3.2:1b' if selectoption == '🦙llama' else 'phi'

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)

# Input from user
user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    # Construct the conversation history for context
    context = "\n".join([f"User: {u}\nBot: {b}" for u, b in st.session_state.chat_history])
    full_prompt = f"{context}\nUser: {user_input}\nBot:"

    try:
        with st.spinner("Generating response..."):
            # Run the ollama subprocess
            result = subprocess.run(
                ["ollama", "run", option],
                input=full_prompt,
                capture_output=True,
                text=True,
                check=True,
                encoding="utf-8")
            
            bot_response = result.stdout.strip()

        with st.chat_message("assistant"):
            st.markdown(bot_response)

        # Update session state with new conversation
        st.session_state.chat_history.append((user_input, bot_response))

    except FileNotFoundError:
        st.error("The 'ollama' command was not found. Make sure it is installed and in your system's PATH.")
    except subprocess.CalledProcessError as e:
        st.error(f"Ollama command failed: {e.stderr}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
