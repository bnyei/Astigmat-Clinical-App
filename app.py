import streamlit as st

# 🔷 Import modules
from src.graphical import GraphicalMethod
from src.formula import FormulaMethod
from src.power_vector import PowerVector
from src.visualisation import graphical_plot

# =========================================================
# 🔷 PAGE CONFIG
# =========================================================

st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #f7f9fb;
    }

    /* Section cards */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Headings */
    h1, h2, h3 {
        color: #1f2d3d;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2c7be5;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-weight: 600;
    }

    /* Input fields */
    input {
        border-radius: 6px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#################################################################

st.title("👁️ Astigmatism Prescription Clinical Tool")
st.caption("Graphical • Formula • Power Vector")

st.warning(
    "This tool is designed for combining two cylindrical or sphero-cylindrical lenses "
    "whose axes are either obliquely crossed (i.e., not 90° apart) or orthogonally crossed (i.e., 90° apart).\n\n"
    
    "Obliquely crossed lenses are considerably more complex to compute manually in clinical practice "
    "compared to orthogonal lens combinations.\n\n"
    
    "To facilitate efficient and accurate computation, this platform implements two established approaches: "
    "the Graphical Method and the Formula Method.\n\n"
    
    "👉 Due the Formula Method, it is recommended to input the lens with the smaller axis first.\n\n"
    "👉 Both must be written as plus cylinders or both written as minus cylinders.\n\n"
    
    "⚠️ This tool is intended to support, not replace, clinical judgment."
)

st.subheader("🔹 Input Prescription")
    
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Prescription 1**")
    sph_1 = st.number_input("Sphere 1", value=0.0, step=0.25)
    cyl_1 = st.number_input("Cylinder 1", value=0.0, step=0.25)
    axis_1 = st.slider("Axis 1", 0, 180, 0)

with col2:
    st.markdown("**Prescription 2**")
    sph_2 = st.number_input("Sphere 2", value=0.0, step=0.25)
    cyl_2 = st.number_input("Cylinder 2", value=0.0, step=0.25)
    axis_2 = st.slider("Axis 2", 0, 180, 0)

if st.button("🔍 Compute", use_container_width=True):

    gm = GraphicalMethod(sph_1, cyl_1, axis_1, sph_2, cyl_2, axis_2)
    fm = FormulaMethod(sph_1, cyl_1, axis_1, sph_2, cyl_2, axis_2)
    pv = PowerVector(sph_1, cyl_1, axis_1, sph_2, cyl_2, axis_2)

    gm.compute()
    fm.compute()
    pv.compute()

    table, g_summary = gm.results()
    f_summary = fm.results()
    pv_table = pv.results()
    fig = graphical_plot(gm)

    st.markdown("## 📊 Results")

    st.success(f"**Graphical:** {g_summary}")
    st.info(f"**Formula:** {f_summary}")

    st.markdown("### Graphical Method Table")
    st.dataframe(table, use_container_width=True)

    st.markdown("### Power Vector (M, J0, J45)")
    st.dataframe(pv_table, use_container_width=True)
        
    st.markdown("### Graphical Plot")
    st.pyplot(fig)

# =========================================================
# 🔷 PAGE FOOTER
# =========================================================        

st.markdown("---")
st.caption(
    "Developed by Ntiamoah Baffour Kyei | Optometrist & Scientist (Health Technology)\n"
    " | Clinical Tool for Astigmatism Analysis\n"
    "© 2026"
)