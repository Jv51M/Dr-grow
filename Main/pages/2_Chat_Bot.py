import streamlit as st
import ollama

st.set_page_config(page_title="Dr.Grow Chat", layout="centered")
st.title("🪴Chatbot")

selectoption=st.selectbox(
    'Select a model',
    ('🦙llama', '🤖phi')
)
if selectoption=='llama':
    option='llama3.2:1b'
else :
    option='phi'
# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat-like display
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)
# User input box
user_input = st.chat_input("Type your message...")

# When the user submits a message
if user_input:
    # Display user's message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build prompt using previous messages
    context = "\n".join([f"User: {u}\nBot: {b}" for u, b in st.session_state.chat_history])
    full_prompt = context + f"\nUser: {user_input}\nBot:"

    try:
        # Call the model
        with st.spinner("Generating response..."):
            command = ["ollama", "run", option, full_prompt]
            response = ollama.generate(model=option, prompt=full_prompt)
        bot_response = response['response'].strip()

        # Display bot's message
        with st.chat_message("assistant"):
            st.markdown(bot_response)

        # Save conversation to session state
        st.session_state.chat_history.append((user_input, bot_response))

    except FileNotFoundError:
        st.error("The 'ollama' command was not found.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
