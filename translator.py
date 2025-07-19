# 📚 Import Libraries
import streamlit as st
import google.generativeai as genai

# 🔑 Gemini API Key Setup (Replace YOUR_API_KEY_HERE)
genai.configure(api_key="AIzaSyDI5Hr2zxpxm3ZyfCGgO5iTWeAp_eprUaA")

# 🎯 Load Gemini Model
model = genai.GenerativeModel('gemini-2.5-pro')

# 🏠 Streamlit App Setup
st.set_page_config(page_title="AI Text Translator", page_icon="🌐")
st.title("🌐 AI Text Translator for Kids (Powered by Gemini)")
st.write("Pick languages, type text, and get instant translation!")

# 📋 Language Options
languages = ["English", "French", "Spanish", "German", "Hindi", "Chinese", "Japanese", "Korean", "Italian"]

# 🎌 Language Pickers
source_lang = st.selectbox("Pick your Source Language:", languages)
target_lang = st.selectbox("Pick your Target Language:", languages)

# 📝 Text Input
user_text = st.text_area("✏️ Type your text to translate:")

# 🚀 Translate Button
if st.button("🔄 Translate"):
    if user_text.strip() != "":
        with st.spinner("Translating your text..."):
            # Prepare Prompt for Gemini
            prompt = f"Translate this text from {source_lang} to {target_lang}:\n\n{user_text}"
            
            # AI Translation
            response = model.generate_content(prompt)
            translation = response.text

            # Show Result
            st.success(f"Translation in {target_lang}:")
            st.write(translation)
    else:
        st.warning("Please type something to translate!")

# 📎 Footer
st.caption("Made with ❤️ using Streamlit & Gemini AI")
