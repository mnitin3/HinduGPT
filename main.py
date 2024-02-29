import streamlit as st

# Define a function to provide responses based on user input
def get_response(user_input):
    # Simple chatbot responses
    responses = {
        "hello": "Pranam! How can I assist you today?",
        "how are you": "I'm just a program, but I'm here to help!",
        "thank you": "You're welcome!",
        # Add more responses as needed
    }
    
    # Check if the user input matches any predefined responses
    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "I'm sorry, I don't understand that question."

# Streamlit UI components
st.title("HinduGPT Bot")
header_container = st.container()
header_container.image("images/swastiklogo.png", width=50, height=50)  # Replace "your_logo.png" with the path to your logo image
header_container.write("Welcome to Hindu History Chatbot")

st.sidebar.title("Navigation")

# Website navigation links
page = st.sidebar.radio("Go to", ["Home", "Explore"])

if page == "Home":
    st.header("Welcome to HinduGPT bot.")
    user_question = st.text_input("Ask me anything:")
    if user_question:
        bot_response = get_response(user_question)
        st.text_area("Bot's response:", value=bot_response, height=100)

elif page == "About":
    st.header("About")
    st.write("This chatbot provides answers to questions related to Hindu history and epics.")

# Footer with GitHub link
st.sidebar.markdown("---")
st.sidebar.markdown("[GitHub](https://github.com/yourusername/yourrepository)")
