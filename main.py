import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure Gemini
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")
if api_key:
    genai.configure(api_key=api_key)

st.set_page_config(page_title="BlackBox Math Engine", layout="wide")
st.title("🔲 BlackBox Math Engine")

st.markdown("""
### Adversarial Audit Ready
Upload your working out below. The engine will perform a structural 
integrity check and identify any heuristic shortcuts for your Edexcel A-Level/TMUA prep.
""")

uploaded_file = st.file_uploader("Upload math image...", type=["jpg", "png", "jpeg"])

if uploaded_file and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="Current Working Out", use_container_width=True)
    
    if st.button("RUN ADVERSARIAL AUDIT"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        system_prompt = (
            "You are the central core of BlackBox, the elite mathematical bridging engine.\n"
            "Your objective is to find the MOST SIMPLE, EFFICIENT, AND INTUITIVE method possible for every problem.\n\n"
            "CRITICAL PROTOCOLS FOR SIMPLIFICATION:\n"
            "1. ALWAYS prioritize 'shortcut' or 'heuristic' methods (e.g., Grid Method for division, "
            "Box Method for expansions, recognition of standard patterns over long-form algorithms).\n"
            "2. If a user uses a laborious, standard method (like Polynomial Long Division) when a simpler "
            "alternative exists (like the Grid/Area Method), you MUST flag this as a 'Heuristic Opportunity'.\n"
            "3. Audit the user's work. If they get the right answer but use a complex, high-friction method, "
            "gently guide them toward the simpler, faster, nonpareil alternative.\n"
            "4. Your scaffolding ladder must teach the 'Simple Method' first, not the textbook algorithm.\n"
            "5. Respond in JSON. Match the schema: include a field 'heuristic_shortcut_suggestion' "
            "that explicitly names the simpler method."
        )
        
        response = model.generate_content([system_prompt, image])
        st.subheader("Audit Results")
        st.json(response.text)


