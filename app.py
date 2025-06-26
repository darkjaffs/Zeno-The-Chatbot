import streamlit as st
from transformers import pipeline, set_seed

st.title("Zeno: Your Sarcastic AI Assistant")


@st.cache_resource
def load_generator():
    generator = pipeline("text-generation", model="gpt2")
    return generator

generator = load_generator()
set_seed(42)


user_input = st.text_input("You:", "")

persona = "You are Zeno, a sarcastic but helpful assistant. Always reply with a hint of wit."

if user_input:
    prompt = f"{persona}]\nHuman: {user_input}\nZeno"
    result = generator(prompt, max_length=150, num_return_sequences=1, truncation=True)
    bot_response = result[0]["generated_text"].split("Zeno")[-1].strip()
    
    st.markdown(f"**Zeno:** {bot_response}")


