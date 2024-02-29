import streamlit as st
import os
import logging

# Function to configure logging
def configure_logging(file_path, level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)

    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

# Function to handle user input and generate response
def generate_response(question):
    logging.info(f"Received question: {question}")
    # Your chatbot logic here
    answer = "This is the answer to the question."
    logging.info(f"Generated answer: {answer}")
    return answer

# Main function
if __name__ == '__main__':
    # Configure logging
    log_file = os.path.join(os.getcwd(), 'chatbot.log')
    logger = configure_logging(log_file)

    # Streamlit UI
    st.title("Simple Chatbot")
    
    # Text input for user question
    question = st.text_input("Ask a question:")
    
    # Button to trigger chatbot response
    if st.button("Get Answer"):
        # Generate and display response
        answer = generate_response(question)
        st.write("Answer:", answer)
