import streamlit as st
from state_design import InsuranceContext

def main():
    context = InsuranceContext()
    print("Starting The Program")
    st.title("Health Insurance Chatbot")
    st.write("Welcome to the Health Insurance Chatbot! Please provide your details to get a personalized health insurance plan.")

    if 'state' not in st.session_state:
        st.session_state['state'] = context
    
    with st.form(key = "user_input_form"):
        age = st.number_input("Age:", min_value = 1, step = 1, format= "%d")
        gender = st.selectbox("Gender:", options = ["Male", "Female"])
        height = st.number_input("Height (in cm):", min_value=1.0, step=0.1, format="%.1f")
        health_history = st.text_input("Health History (e.g., diabetes, hypertension):")
        submit = st.form_submit_button("Submit")
    
    if submit:
        user_data = {
            "age": age,
            "gender": gender,
            "height": height,
            "health_history": health_history,
        }

        st.session_state["state"].set_user_data(user_data)
        st.session_state["state"].request() #process state
        st.session_state["state"].request() #completed state

        if st.session_state["state"].result:
            st.subheader("Your Customized Insurance Plan:")
            st.text(str(st.session_state["state"].result))

if __name__ == "__main__":
    main()
