#streamlit run streamlit_app.py
import streamlit as st
import json
import openai

api_key = st.secrets["openai"]["api_key"]
openai.api_key = api_key

start_message = """
##### Welcome to the translator app. Please select your input language.
1. Spanish
2. English
3. Japanese
"""

st.write(start_message)

selection = st.text_input("Enter number below.")
input_language = ""

while selection != "1" and selection != "2" and selection != "3":
    selection = input(start_message)

if selection == "1":
    input_language = "Spanish"
elif selection == "2":
    input_language = "English"
elif selection == "3":
    input_language = "Japanese"

request_output = """
##### Please select a language to translate to.
1. French
2. Mandarin
3. German
"""

input_text = st.text_input("Please enter your text in " + input_language + ": ")

st.write(request_output)

selection = st.text_input("Enter number below. ")
output_language = ""

while selection != "1" and selection != "2" and selection != "3":
    selection = input(request_output)

if selection == "1":
    output_language = "French"
elif selection == "2":
    output_language = "Mandarin"
elif selection == "3":
    output_language = "German"

system_prompt = """
You are a language translator. A user will give you an input language and a message they want translated. Output ONLY their translated message.
"""
user_prompt = f"{input_language} -> {output_language}, my message is: {input_text}"

response = openai.chat.completions.create (
    model = "gpt-3.5-turbo-0125",
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)
st.write(f"Here is the translation: " + response.choices[0].message.content)