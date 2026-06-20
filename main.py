import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Setup
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")
if api_key:
    genai.configure(api_key=api_key)

st.title("🔲 BlackBox Math Engine")
uploaded_file = st.file_uploader("Upload math image...", type=["jpg", "png", "jpeg"])

# 2. Logic
if uploaded_file and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="Current Working Out", use_container_width=True)
    
    system_prompt = "You are an elite math tutor. Audit the user's work for heuristic shortcuts."
    model = genai.GenerativeModel('gemini-1.5-flash')

    if st.button("RUN ADVERSARIAL AUDIT"):
        with st.spinner("Engine auditing..."):
            response = model.generate_content([system_prompt, image])
            st.subheader("Audit Results")
            st.write(response.text)



