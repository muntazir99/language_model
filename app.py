from langchain.llms import OpenAI
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

#function to load openai model and get response
def get_openai_response(question):
        # Load the API key from the environment
    api_key = os.environ["OPENAI_API_KEY"]

    # Create an OpenAI object
    llm = OpenAI(api_key=api_key)
    client=OpenAI()

    # Generate a text completion using the GPT-3.5 Turbo model
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  
        prompt=question,
        max_tokens=100,
        temperature=0.6,
    )

    return response.choices[0].text

#int streamlit app
st.set_page_config(page_title="Q&A demo")

st.header("Langchain application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)
submit=st.button("ask the Question")


if submit:
    st.subheader("The Response is: ")
    st.write(response)


