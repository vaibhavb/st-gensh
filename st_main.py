import streamlit as st
import gensh

def main():
    st.info("Hello from st-gensh!")
    st.info(f"Gensh {gensh.__version__}")
    with st.form('my_form'):
        text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
        submitted = st.form_submit_button('Submit')

def make_sidebar():
    openai_api_key = st.sidebar.text_input('OpenAI API Key')

if __name__ == "__main__":
    st.set_page_config(page_title="Gensh Streamlit App")
    st.title('Gensh Streamlit App')
    make_sidebar()
    main()

