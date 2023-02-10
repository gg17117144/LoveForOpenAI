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
sender_features = st.text_input("您的特點是？")
sender_love_reason = st.text_input("您為什麼喜歡對方？")

recipient_name = st.text_input("對方的名字是？")

prompt = (f"親愛的{recipient_name}，我是{sender_interests}愛好者，在我的生活中，我有{sender_features}的特點。"
        f"但是，最重要的是，我喜歡你，因為{sender_love_reason}。我希望能和你交往。")

        
if st.button("生成告白"):
    love_letter = generate_text(prompt)
    st.write("生成的告白：", love_letter)

