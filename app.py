import streamlit as st
from prototype import *
from facade import InsuranceFacade
from state_design import InsuranceContext

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "context" not in st.session_state:
    st.session_state.context = InsuranceContext()

# Main Function
def main():
    st.title("Customized Health Insurance Chatbot")

    # Sidebar for Chat History
    with st.sidebar:
        st.header("Chat History")
        if st.session_state.chat_history:
            for i, message in enumerate(st.session_state.chat_history):
                role = "🧑‍💼 User" if message["role"] == "user" else "🤖 Bot"
                st.write(f"{role}: {message}")
        else:
            st.info("No chat history yet.")

    # Chat Interface
    st.write("Please provide your details to get a customized health insurance plan.")

    with st.form(key="user_details_form"):
        age = st.number_input("Age:", min_value=0, max_value=120, value=30, step=1)
        gender = st.selectbox("Gender:", options=["Male", "Female"])
        height = st.number_input("Height (in cm):", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
        health_history = st.text_input("Health History (e.g., diabetes, hypertension):", value="")
        submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        user_data = {
            "age": age,
            "gender": gender,
            "height": height,
            "health_history": health_history,
        }

        # Add user message to chat history
        user_message = f"Age: {age}, Gender: {gender}, Height: {height} cm, Health History: {health_history}"
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        with st.chat_message("user"):
            st.markdown(user_message)

        # Set user data in context
        st.session_state.context.set_user_data(user_data)

        # Process input and generate response
        st.session_state.context.request()  # This will handle the processing

        # Retrieve the result from context
        if st.session_state.context.result:
            response = str(st.session_state.context.result)
            
            # Format response for Markdown
            formatted_response = response.replace("\\n", "\n")  # Replace escaped newlines with actual newlines
            
            # Add bot message to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": formatted_response})
            
            # Display response with proper formatting using Markdown
            with st.chat_message("assistant"):
                st.markdown(formatted_response)
        else:
            st.error("An error occurred while processing your request. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
