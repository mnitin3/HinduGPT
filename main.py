import streamlit as st

# Define a function to provide responses based on user input
def get_response(user_input):
    # Simple chatbot responses
    responses = {
        "hello": "Hello! How can I assist you today?",
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
st.title("Chatbot Application")
user_question = st.text_input("Ask me anything:")

# Check if the user has asked a question
if user_question:
    # Get the response from the chatbot function
    bot_response = get_response(user_question)
    # Display the response
    st.text_area("Bot's response:", value=bot_response, height=100)
