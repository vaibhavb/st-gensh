import streamlit as st
import gensh

def main():
    st.info("Hello from st-gensh!")
    st.info(f"Gensh {gensh.__version__}")

if __name__ == "__main__":
    st.set_page_config(page_title="Gensh Streamlit App")
    st.title('Gensh Streamlit App')
    main()
