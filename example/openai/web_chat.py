import os

import openai 
import streamlit as st

from streamlit_chat import message
from dotenv import load_dotenv

load_dotenv()    

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt1, prompt2, p_type):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt2,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

def get_text():
    input_text1 = st.text_input("Write message : ", key='input_text1')
    input_text2 = st.text_input("Write message222 : ", key='input_text2')
    return input_text1, input_text2

st.title("chatBot : Streamlit + openAI")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input1, user_input2 = get_text()
p_type = st.radio(label = 'type_btn', options = ['단답형', 'O/X'], horizontal=True)

if (user_input1) and (user_input2):
    output = generate_response(user_input1, user_input2, p_type)
    # store the output 
    st.session_state.past.append(user_input2)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')