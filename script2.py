"""
Citizen Golden Record Simulator - Script 2
A Streamlit application for simulating identity confidence scoring.
"""

import streamlit as st
import pandas as pd
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="GRCS Simulator",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
<style>
    html, body {
        margin: 0 !important;
        padding: 0 !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }
    [data-testid="stToolbar"] {
        display: block !important;
        visibility: visible !important;
    }
    [data-testid="stDecoration"] {display: none !important;}
    #MainMenu {display: none !important;}
    .stDeployButton {display: none !important;}
    footer {display: none !important;}

    [data-testid="stAppViewContainer"] {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    [data-testid="stAppViewContainer"] > .main {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    .stApp {
        background: linear-gradient(180deg, #e3f2fd 0%, #bbdefb 100%);
    }

    .main {
        padding-top: 0rem !important;
        background: transparent;
    }

    .block-container {
        padding-top: 5.2rem !important;
        background: transparent;
    }

    h1 {font-size: 32px !important; font-weight: 700 !important; color: #0d47a1; margin-bottom: 1rem;}
    h2 {font-size: 22px !important; font-weight: 600 !important; color: #1565c0; margin-top: 1.2rem; margin-bottom: 0.8rem;}
    h3 {font-size: 16px !important; font-weight: 600 !important; color: #1976d2; margin-top: 1rem; margin-bottom: 0.5rem;}
    p, label {font-size: 15px !important; color: #263238; font-weight: 500;}

    /* Dataframe: centered content + readable text */
    [data-testid="stDataFrame"] [role="columnheader"],
    [data-testid="stDataFrame"] [role="gridcell"],
    [data-testid="stTable"] th,
    [data-testid="stTable"] td {
        text-align: center !important;
    }

    [data-testid="stDataFrame"] [role="columnheader"],
    [data-testid="stTable"] th {
        font-weight: 700 !important;
    }

    /* Make dataframe popup/context menu readable */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] * {
        color: #10243a !important;
        opacity: 1 !important;
    }

    div[data-baseweb="popover"] [role="menu"],
    div[data-baseweb="popover"] [role="menuitem"],
    div[data-baseweb="popover"] [role="option"],
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] li {
        background: #ffffff !important;
        color: #10243a !important;
    }

    div[data-baseweb="popover"] [role="menuitem"]:hover,
    div[data-baseweb="popover"] [role="option"]:hover,
    div[data-baseweb="popover"] li:hover {
        background: #e3f2fd !important;
        color: #0d47a1 !important;
    }

    .top-navbar {
        background: linear-gradient(135deg, #bbdefb 0%, #90caf9 100%);
        padding: 1rem 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100vw;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border-radius: 0;
    }

    .navbar-logo {
        height: 50px;
        width: auto;
        background: white;
        padding: 8px;
        border-radius: 8px;
    }

    .navbar-title {
        color: #0d47a1;
        font-size: 24px;
        font-weight: 700;
        margin: 0 2rem;
        flex-grow: 1;
        text-align: center;
    }

    .page-header {
        text-align: center;
        padding: 1.5rem 1.5rem;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(13, 71, 161, 0.12);
        margin: 0.2rem auto 1.5rem auto;
        max-width: 900px;
        border: 2px solid #2196f3;
    }

    .page-header h1 {
        font-size: 28px !important;
        color: #0d47a1 !important;
        margin-bottom: 0.5rem !important;
        font-weight: 800 !important;
    }

    .page-header p {
        font-size: 13px !important;
        color: #37474f !important;
        margin: 0 !important;
        font-weight: 400 !important;
        text-align: center !important;
    }

    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.78);
        border-right: 1px solid #90caf9;
    }

    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        position: fixed !important;
        top: 5.6rem !important;
        left: 0.5rem !important;
        z-index: 1200 !important;
    }

    [data-testid="collapsedControl"] button,
    [data-testid="stSidebarCollapsedControl"] button,
    button[aria-label="Open sidebar"],
    button[aria-label="Close sidebar"] {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 42px !important;
        height: 42px !important;
        background: #0d47a1 !important;
        border: 2px solid #bbdefb !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(13, 71, 161, 0.45) !important;
        visibility: visible !important;
        opacity: 1 !important;
        color: #ffffff !important;
        transition: all 0.2s ease-in-out !important;
    }

    [data-testid="collapsedControl"] button:hover,
    [data-testid="stSidebarCollapsedControl"] button:hover,
    button[aria-label="Open sidebar"]:hover,
    button[aria-label="Close sidebar"]:hover {
        background: #1565c0 !important;
        border-color: #e3f2fd !important;
        box-shadow: 0 6px 16px rgba(13, 71, 161, 0.55) !important;
        transform: translateY(-1px) !important;
    }

    [data-testid="collapsedControl"] button:focus-visible,
    [data-testid="stSidebarCollapsedControl"] button:focus-visible,
    button[aria-label="Open sidebar"]:focus-visible,
    button[aria-label="Close sidebar"]:focus-visible {
        outline: 2px solid #ffffff !important;
        outline-offset: 2px !important;
    }

    [data-testid="collapsedControl"] button svg,
    [data-testid="stSidebarCollapsedControl"] button svg,
    button[aria-label="Open sidebar"] svg,
    button[aria-label="Close sidebar"] svg {
        color: #ffffff !important;
        fill: #ffffff !important;
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #0d47a1 !important;
    }

    /* Improve readability for remaining UI elements */
    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] span {
        color: #1b2a3a !important;
        opacity: 1 !important;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] *,
    [data-testid="stMetricValue"],
    [data-testid="stMetricValue"] * {
        color: #0d47a1 !important;
        opacity: 1 !important;
        font-weight: 700 !important;
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {
        color: #12304c !important;
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="slider"] * {
        color: #12304c !important;
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="slider"] [role="slider"] {
        background: #1565c0 !important;
        border-color: #0d47a1 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: #ffffff !important;
        color: #10243a !important;
        border: 1px solid #90caf9 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] input,
    [data-testid="stSidebar"] [data-baseweb="select"] span,
    [data-testid="stSidebar"] [data-baseweb="select"] div {
        color: #10243a !important;
        opacity: 1 !important;
    }

    /* Keep chart labels readable on light background */
    [data-testid="stVegaLiteChart"] text,
    [data-testid="stVegaLiteChart"] span,
    [data-testid="stVegaLiteChart"] div {
        color: #12304c !important;
        fill: #12304c !important;
        opacity: 1 !important;
    }

    /* Fix bar chart readability - WHITE BACKGROUND */
    [data-testid="stVegaLiteChart"],
    [data-testid="stVegaLiteChart"] canvas,
    [data-testid="stVegaLiteChart"] svg,
    [data-testid="stVegaLiteChart"] > div,
    [data-testid="stVegaLiteChart"] .vega-embed,
    [data-testid="stVegaLiteChart"] .chart-wrapper,
    [data-testid="stArrowVegaLiteChart"],
    [data-testid="stArrowVegaLiteChart"] > div,
    .stVegaLiteChart,
    div[data-testid="stVegaLiteChart"] * {
        background: #ffffff !important;
        background-color: #ffffff !important;
    }

    /* Chart axis labels and text */
    [data-testid="stVegaLiteChart"] text {
        fill: #0d47a1 !important;
        color: #0d47a1 !important;
        font-weight: 600 !important;
        opacity: 1 !important;
    }

    /* Chart container styling */
    [data-testid="stArrowVegaLiteChart"] {
        padding: 1rem !important;
        border-radius: 8px !important;
        background: #ffffff !important;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Load logos with error handling for deployment
def load_logo_base64(logo_path):
    """Load and encode logo file to base64 string."""
    try:
        if logo_path.exists():
            return base64.b64encode(logo_path.read_bytes()).decode()
    except Exception:
        st.warning(
            f"Logo not found: {logo_path.name}. "
            "App will work without logos."
        )
    return None


try:
    script_dir = Path(__file__).parent
    logo_bihar_path = script_dir / "assets" / "bihargovt-logo.png"
    logo_cipl_path = script_dir / "assets" / "cipl-logo.png"

    logo_bihar_b64 = load_logo_base64(logo_bihar_path)
    logo_cipl_b64 = load_logo_base64(logo_cipl_path)

    # Render navbar with or without logos
    if logo_bihar_b64 and logo_cipl_b64:
        st.markdown(
            f"""
        <div class="top-navbar">
            <img src="data:image/png;base64,{logo_cipl_b64}"
                 class="navbar-logo" alt="CIPL Logo">
            <h2 class="navbar-title">
                Golden Record Confidence Score (GRCS)
            </h2>
            <img src="data:image/png;base64,{logo_bihar_b64}"
                 class="navbar-logo" alt="Bihar Government Logo">
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        # Fallback navbar without logos
        st.markdown(
            """
        <div class="top-navbar">
            <h2 class="navbar-title" style="text-align: center; width: 100%;">
                Golden Record Confidence Score (GRCS)
            </h2>
        </div>
        """,
            unsafe_allow_html=True,
        )
except Exception as e:
    st.error(f"Error loading navbar: {e}")
    # Continue anyway with minimal header
    st.title("Golden Record Confidence Score (GRCS)")

st.markdown(
    """
<div class="page-header">
    <h1>Citizen Golden Record Simulator</h1>
    <p>Adjust identity attributes to see how the system classifies a citizen record.</p>
</div>
""",
    unsafe_allow_html=True,
)

# ==========================================
# Application Configuration
# ==========================================

# Attribute weights (simplified demo)
weights = {
    "Aadhaar": 0.18,
    "Name": 0.09,
    "DOB": 0.09,
    "Address": 0.07,
    "PAN": 0.05,
    "Passport": 0.03,
    "EPIC": 0.03,
    "Ration Card": 0.05,
    "Father Name": 0.04,
    "Mobile": 0.04
}

authority_scores = {
    "Aadhaar": 85,
    "Name": 80,
    "DOB": 80,
    "Address": 70,
    "PAN": 78,
    "Passport": 78,
    "EPIC": 75,
    "Ration Card": 70,
    "Father Name": 70,
    "Mobile": 70
}

# ==========================================
# Main Application Logic
# ==========================================

results = []

st.sidebar.header("Scenario Inputs")

# Process each attribute
for attribute, weight in weights.items():
    
    mi = st.sidebar.slider(
        f"{attribute} Match Strength (Mi)",
        0.0,
        1.0,
        1.0
    )
    
    si = authority_scores[attribute] / 100
    
    contribution = weight * mi * si
    
    results.append({
        "Attribute": attribute,
        "Weight": weight,
        "Mi": mi,
        "Si": si,
        "Contribution": contribution
    })

# Create results dataframe
df = pd.DataFrame(results)

# Calculate Identity Confidence Score
ICS = df["Contribution"].sum()

# Display results
st.subheader("Attribute Contribution")
st.dataframe(df, use_container_width=True)

st.subheader("Identity Confidence Score")
st.metric("ICS", f"{round(ICS * 100, 2)}%")

# ==========================================
# Classification Logic
# ==========================================
if ICS >= 0.92:
    status = "Golden"
    color = "green"
elif ICS >= 0.75:
    status = "Silver"
    color = "orange"
else:
    status = "Grey"
    color = "red"

st.markdown(f"## Record Classification: :{color}[{status}]")

# Visualize contributions
st.subheader("Contribution by Attribute")
st.bar_chart(df.set_index("Attribute")["Contribution"])

# Footer for deployment info
st.markdown("---")
st.caption(
    "Golden Record Confidence Score (GRCS) Simulator | "
    "Citizen Golden Record System"
)
