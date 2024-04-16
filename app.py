import streamlit as st
import openai
from openai import OpenAI

# Set API Key
with open("C:/Users/rjsek/OneDrive/Documents/Work and Professional documents/Innomatics Research Labs/Data Science Internship Jan 2024/Gen AI App/.Gen AI Key.txt") as f:
    OPENAI_API_KEY = f.read()
client = OpenAI(api_key=OPENAI_API_KEY)

def main():
    st.title("🤖Gen AI App - AI Code Reviewer🚀")
    st.markdown("---")
    st.subheader("Code Reviewer")
    prompt = st.text_area("Enter your python code here:")

    if st.button("Find Bugs"):
        st.markdown("🔍 **Analyzing your code...**")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "🤖 **You are a helpful AI Assistant and Code reviewer**\nFind the Bugs and error in the program."},
                {"role": "user", "content": prompt}
            ]
        )

        st.markdown("---")
        st.write("🔍 **Code Review Result:**")
        try:
            st.write(response.choices[0].message.content)
        except IndexError:
            st.error("No response received. Please check your input and try again.")

if __name__ == "__main__":
    main()