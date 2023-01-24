import openai
import streamlit as st

st.subheader("API Key")
# Prompt the user for their OpenAI API key
api_key = st.text_input("Enter your OpenAI API key:")






# Validate the API key
def validate_api_key(api_key):
    openai.api_key = api_key
    response = openai.Engine.list()
    if response.status_code != 200:
        return False
    return True
    except openai.exceptions.OpenAIError as e:
        return False

if not validate_api_key(api_key):
    st.error("Invalid API key. Please enter a valid key.")
else:
    # Create variables for the number of tokens and temperature
    st.sidebar.title("Settings")
    max_tokens = st.sidebar.number_input("Number of tokens:", min_value=1, max_value=2048, value=1024)
    temperature = st.sidebar.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.5)

    def generate_text(prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
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
