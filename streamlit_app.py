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

st.title("告白生成器")

sender_interests = st.text_input("您的興趣是？")
sender_abilities = st.text_input("您的能力是？")
sender_love_features = st.text_input("您為什麼喜歡對方？")

recipient_interests = st.text_input("對方的興趣是？")
recipient_features = st.text_input("想對對方說的話？")

prompt = (f"告白。我的興趣是{sender_interests}，我的能力是{sender_abilities}，"
         f"我喜歡對方是因為{sender_love_features}。對方的興趣是{recipient_interests}，"
         f"我想對你說{recipient_features}！我喜歡你！請你和我交往！")

if st.button("生成告白"):
    love_letter = generate_text(prompt)
    st.write("生成的告白：", love_letter)

