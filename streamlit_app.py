import openai
import streamlit as st

# Prompt the user for their OpenAI API key
api_key = st.text_input("Enter your OpenAI API key:")

# Validate the API key
def validate_api_key(api_key):
    try:
        openai.api_key = api_key
        openai.Engine.list()
        return True
    except openai.exceptions.OpenAIError as e:
        return False

if not validate_api_key(api_key):
    st.error("Invalid API key. Please enter a valid key.")
else:
    # Create variables for the number of tokens and temperature
    st.sidebar.title("Settings")
    temperature = st.sidebar.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.5)

    def generate_text(prompt):
        max_tokens = st.sidebar.number_input("Number of tokens:", min_value=1, max_value=4024, value=1024)
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
