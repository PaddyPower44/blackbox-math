import os
import json
import streamlit as st
from PIL import Image
from google import genai
from google.genai import types

# -------------------------------------------------------------------------
# 1. APPLICATION & PAGE CONFIGURATION (Premium Dark-Mode Aesthetic)
# -------------------------------------------------------------------------
st.set_page_config(
    page_title="BlackBox // The Nonpareil Bridging Engine",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS injection to force an elite, high-contrast dark interface
st.markdown("""
    <style>
        .reportview-container { background: #0E1117; }
        .stAlert { border-radius: 8px; border: 1px solid #FF4B4B; }
        .scaffold-lock {
            background-color: #1A1C23;
            padding: 25px;
            border-radius: 12px;
            border: 2px dashed #FF4B4B;
            margin-bottom: 20px;
        }
        .metric-card {
            background: #1F2937;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #374151;
            text-align: center;
        }
        .audit-line-correct {
            padding: 10px; margin: 5px 0; border-left: 4px solid #10B981; background: #064E3B; color: #E5E7EB; border-radius: 4px;
        }
        .audit-line-error {
            padding: 10px; margin: 5px 0; border-left: 4px solid #EF4444; background: #7F1D1D; color: #FCA5A5; border-radius: 4px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# 2. SESSION STATE INITIALIZATION (The Persistent Engine Memory)
# -------------------------------------------------------------------------
if "app_locked" not in st.session_state:
    st.session_state.app_locked = False
if "scaffold_data" not in st.session_state:
    st.session_state.scaffold_data = None
if "current_analysis" not in st.session_state:
    st.session_state.current_analysis = None

# -------------------------------------------------------------------------
# 3. SIDEBAR CONTROLS & API INITIALIZATION
# -------------------------------------------------------------------------
st.sidebar.title("⬛ BLACKBOX CORE")
st.sidebar.markdown("---")

# Secure API Key Entry Path
api_key_input = st.sidebar.text_input("Enter Gemini API Key:", type="password", help="Your key remains secure and is never stored externally.")
api_key = api_key_input or os.environ.get("GEMINI_API_KEY")

# Target Syllabus Trajectory Nodes
target_node = st.sidebar.selectbox(
    "Select Target Math Node:",
    [
        "A-Level Core: Differentiation by First Principles",
        "A-Level Core: Integration by Substitution",
        "A-Level Core: Parametric Equations & Coordinate Geometry",
        "Further Maths: Matrix Transformations & Inverses",
        "TMUA Elite: Formal Symbolic Logic & Contrapositive Proofs"
    ]
)

syllabus_context = "Transitioning from GCSE Grade 5 foundation to elite algebraic accuracy for Warwick MORSE admission."

st.sidebar.markdown("---")
st.sidebar.info("Status: Active Logic Monitor")

# -------------------------------------------------------------------------
# 4. CORE REASONING ENGINE (Gemini 3.1 Pro Integration)
# -------------------------------------------------------------------------
def run_diagnostic_analysis(uploaded_image, node_title, context_text):
    """Orchestrates image parsing, line-by-line auditing, and scaffolding routing."""
    if not api_key:
        st.error("Missing API Key! Please enter your Gemini API Key in the sidebar.")
        return None
        
    try:
        # Initialize client with current authenticated credentials
        client = genai.Client(api_key=api_key)
        pil_image = Image.open(uploaded_image)
        
        system_prompt = (
            "You are the central core of BlackBox, the absolute world-class mathematical bridging engine.\n"
            "Your target user is a student moving from a GCSE Grade 5 foundation to an A* at A-Level Maths "
            "and a 5.0+ in the TMUA to secure a place at Warwick MORSE.\n\n"
            "CRITICAL PROTOCOLS:\n"
            "1. Inspect handwritten mathematical steps line-by-line via the provided image.\n"
            "2. Identify the EXACT line where the user commits a logical, arithmetic, or algebraic error.\n"
            "3. Determine the 'failure_tier':\n"
            "   - 'Tier 1 (GCSE Foundational)': Dropping marks on core fractions, standard indices, linear transposition.\n"
            "   - 'Tier 2 (Advanced GCSE Bridge)': Dropping marks on completing the square, indices laws, simultaneous expansions.\n"
            "   - 'Tier 3 (A-Level Core)': Failure to understand differentiation rules, radian geometry, parametric forms.\n"
            "   - 'Tier 4 (TMUA Elite)': Deficiencies in formal symbolic logic, necessity vs. sufficiency, structural proofs.\n"
            "4. If the failure is Tier 1 or Tier 2, you MUST set scaffolding_required to true and generate a progressive, "
            "custom 3-step 'scaffolding_ladder' to fix their foundation.\n"
            "5. Respond exclusively in clean, valid JSON matching the exact schema requested."
        )

        prompt_instructions = f"""
        Analyze the attached student work for the following Target Topic Node:
        [TOPIC]: {node_title}
        [CONTEXT]: {context_text}

        Evaluate their work line-by-line and return a JSON object matching this exact schema structure:
        {{
            "is_solution_correct": false,
            "overall_score_awarded": "3/7",
            "exact_error_line_index": 2,
            "line_by_line_audit": [
                "Line 0: Correct initialization of the curve equation.",
                "Line 1: Correct application of the chain rule derivative.",
                "Line 2: CRITICAL FAILURE - Student expanded (3x)^-1 as 3x^-1 instead of 1/(3x). Denominator rule violated."
            ],
            "cognitive_misconception_analysis": "The student fails to apply negative index distribution to scalar coefficients within a bracket.",
            "failure_tier": "Tier 2 (Advanced GCSE Bridge)",
            "scaffolding_required": true,
            "scaffolding_ladder": [
                {{
                    "step_number": 1,
                    "focus": "Base Tier 1 Index Laws",
                    "bridging_question": "Simplify the expression (2x)^3 completely.",
                    "worked_solution_proof": "Step 1: Distribute the power of 3 to both components: 2^3 * x^3. Step 2: Evaluate 2^3 = 8. Answer: 8x^3."
                }}
            ]
        }}
        """
        
        with st.spinner("BlackBox Engine executing deep line-by-line mathematical parsing..."):
            response = client.models.generate_content(
                model='gemini-3.1-pro',
                contents=[pil_image, prompt_instructions],
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    response_mime_type="application/json",
                    temperature=0.0
                )
            )
            return json.loads(response.text)
            
    except Exception as e:
        st.error(f"Engine Core Interrupted: {str(e)}")
        return None

# -------------------------------------------------------------------------
# 5. INTERLOCKING STATE CONTROLLER (The Screen Takeover System)
# -------------------------------------------------------------------------
if st.session_state.app_locked:
    st.markdown("<div class='scaffold-lock'>", unsafe_allow_html=True)
    st.error("🚨 SYSTEM INTERLOCK ACTIVE: FOUNDATIONAL COGNITIVE BLIND SPOT DETECTED")
    st.markdown(f"**Reason:** {st.session_state.current_analysis.get('cognitive_misconception_analysis')}")
    st.markdown("Your access to A-Level modules is frozen. Complete the adaptive GCSE skill ladder below to unlock your workspace.")
    st.markdown("---")
    
    ladder = st.session_state.scaffold_data
    all_cleared = True
    
    for idx, step in enumerate(ladder):
        st.subheader(f"Step {step['step_number']}: {step['focus']}")
        st.info(step['bridging_question'])
        
        user_ans = st.text_input(f"Enter your final calculation for Step {step['step_number']}:", key=f"user_step_{idx}")
        
        show_proof = st.checkbox(f"Reveal Worked Proof & Verify Step {step['step_number']}", key=f"proof_step_{idx}")
        if show_proof:
            st.success(f"**System Verification Model:** {step['worked_solution_proof']}")
            confirmation = st.radio(f"Did your working steps logically match?", ("No", "Yes"), key=f"confirm_step_{idx}")
            if confirmation == "No":
                all_cleared = False
        else:
            all_cleared = False
        st.markdown("---")
        
    if st.button("Submit Completed Ladder & Request Unlock"):
        if all_cleared:
            st.session_state.app_locked = False
            st.session_state.scaffold_data = None
            st.session_state.current_analysis = None
            st.success("Foundation Verified. Workspace Unlocked! Reloading...")
            st.rerun()
        else:
            st.warning("System Interlock Refused. You must verify and successfully resolve all sub-nodes to unlock.")
            
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# -------------------------------------------------------------------------
# 6. MASTER WORKING SUITE (The Primary Workspace View)
# -------------------------------------------------------------------------
st.title("⬛ BlackBox // The Nonpareil Bridging Engine")
st.markdown(f"**Active Workspace Target:** `{target_node}`")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("1. Submit Solution Data")
    uploaded_file = st.file_uploader("Upload an image of your handwritten working out:", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Captured Mathematical Submission Payload", use_container_width=True)
        
        if st.button("RUN ADVERSARIAL AUDIT", use_container_width=True):
            result = run_diagnostic_analysis(uploaded_file, target_node, syllabus_context)
            
            if result:
                st.session_state.current_analysis = result
                if result.get("scaffolding_required", False):
                    st.session_state.app_locked = True
                    st.session_state.scaffold_data = result.get("scaffolding_ladder")
                    st.rerun()

with col2:
    st.header("2. Real-Time Diagnostic Feed")
    
    if st.session_state.current_analysis:
        res = st.session_state.current_analysis
        
        # Display high-level metric cards
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            status_text = "🟢 CLEARED" if res.get("is_solution_correct") else "🔴 FAILED"
            st.markdown(f"<div class='metric-card'><b>Verdict</b><br><span style='font-size:20px;'>{status_text}</span></div>", unsafe_allow_html=True)
        with m_col2:
            st.markdown(f"<div class='metric-card'><b>Marks Awarded</b><br><span style='font-size:20px;'>{res.get('overall_score_awarded')}</span></div>", unsafe_allow_html=True)
        with m_col3:
            st.markdown(f"<div class='metric-card'><b>Deficiency Tier</b><br><span style='font-size:16px; color:#FF4B4B;'>{res.get('failure_tier')}</span></div>", unsafe_allow_html=True)
            
        st.markdown("---")
        st.subheader("Line-by-Line Examiner Audit View")
        
        err_idx = res.get("exact_error_line_index")
        for i, line in enumerate(res.get("line_by_line_audit", [])):
            if err_idx is not None and i == err_idx:
                st.markdown(f"<div class='audit-line-error'>{line}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='audit-line-correct'>{line}</div>", unsafe_allow_html=True)
                
        st.markdown("---")
        st.subheader("Structural Cognitive Analysis")
        st.write(res.get("cognitive_misconception_analysis"))
        
    else:
        st.info("Awaiting structural input math payload. Upload your working out and trigger the Adversarial Audit to engage the engine tracking.")
