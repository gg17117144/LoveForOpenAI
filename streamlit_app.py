import streamlit as st
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

st.title("告白文生成器")

sender_interests = st.text_input("您的興趣是？")
sender_abilities = st.text_input("您的能力是？")
sender_love_features = st.text_input("您為什麼喜歡對方？")

recipient_interests = st.text_input("對方的興趣是？")
recipient_features = st.text_input("想對對方說的話？")

prompt = (f"我喜歡你！我的興趣是{sender_interests}，我能做到{sender_abilities}，我喜歡你是因為{sender_love_features}我知道你喜歡{recipient_interests}，"
         f"我想對你說{recipient_features}。")

if st.button("生成告白文"):
    love_letter = generate_text(prompt)
    st.write("生成的告白文：", love_letter)

