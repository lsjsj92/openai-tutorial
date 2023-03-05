import streamlit as st
import requests
headers = {
    "Content-type": "application/json",
    "accept": "application/json"
}
model_url = "http://localhost:8088/gpt3/predict"
save_url = "http://localhost:8088/save_qa"


body = st.text_area('본문을 입력해주세요')

Q = st.text_input("질문을 입력해주세요")

btn_clicked = st.button("전송", key='confirm_btn')

if btn_clicked:
    
    params = {
        "model": "gpt3",
        "temperature": 0,
        "max_tokens": 512,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "body_text": f"{body}",
        "q_text": f"{Q}"
    }
    
    res = requests.post(model_url, json=params, headers=headers)
    st.title("정답은 아래와 같습니다.")
    st.text_input("", f"{res.json()['response']['choices'][0]['text']}", disabled=True, key="answer")
    
save_btn = st.button("저장")

if (save_btn) and ('answer' in st.session_state):
    params = {
        "body_text": body,
        "q_text": Q,
        "a_text": st.session_state.answer
    }
    res = requests.post(save_url, json=params, headers=headers)
    st.text_input("", f"{res.json()['response']}", disabled=True, key="final")
    