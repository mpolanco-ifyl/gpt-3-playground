import openai
import streamlit as st

# Prompt the user for their OpenAI API key
api_key = st.text_input("Enter your OpenAI API key:")

# Use the user's API key to set the openai API key
openai.api_key = api_key

# Create variables for the number of tokens and temperature
max_tokens = st.slider("Number of tokens:", min_value=10, max_value=4000, value=512)
temperature = st.slider("Temperature:", min_value=0.1, max_value=1.0, value=0.5, step=0.1)

# Create a function to generate GPT-3 text
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    return response["choices"][0]["text"]

# Create a Streamlit UI for the GPT-3 playground
st.title("GPT-3 Playground")
prompt = st.text_input("Enter your prompt:")
st.write("Generated text:")
st.write(generate_text(prompt))
