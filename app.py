import streamlit as st
from prototype import *
from facade import DentalCareFacade
from state_design import DentalContext

# Initialize session state
if "context" not in st.session_state:
    st.session_state.context = DentalContext()

# Main Function
def main():
    st.title("Customized Dental Care Chatbot")

    # Chat Interface
    st.write("Please provide your details to get a customized Dental Care plan.")

    with st.form(key="user_details_form"):
        age = st.number_input("Age:", min_value=0, max_value=120, value=30, step=1)
        gender = st.selectbox("Gender:", options=["Male", "Female"])
        height = st.number_input("Height (in cm):", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
        health_history = st.text_input("Dental Health History (e.g., cavity, diabetes, hypertension):", value="")
        submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        # Clear previous recommendations
        st.session_state.context.result = None

        # Collect user data
        user_data = {
            "age": age,
            "gender": gender,
            "height": height,
            "health_history": health_history,
        }

        # Set user data in context
        st.session_state.context.set_user_data(user_data)

        # Process input and generate response
        st.session_state.context.request()  # This will handle the processing

        # Retrieve the result from context
        if st.session_state.context.result:
            response = str(st.session_state.context.result)
            
            # Format response for Markdown
            formatted_response = response.replace("\\n", "\n")  # Replace escaped newlines with actual newlines
            
            # Display response with proper formatting using Markdown
            st.markdown(f"### Your Customized Dental Care Plan:\n\n{formatted_response}")
        else:
            st.error("An error occurred while processing your request. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
