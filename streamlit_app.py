import streamlit as st
#from st_clickable_images import clickable_images
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters
from PIL import Image
import base64


# Set page config
st.set_page_config(
    page_title="Makeup Filter App",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>

    /* Change background color */
    .main {
        background-color: #f5f5f5; /* Light grey background */
    }

    /* Change font color and style */
    h1, h2, h3, h4, h5, h6, p, li {
        color: #333333; /* Dark grey font color */
        font-family: 'Arial', sans-serif;
    }

    /* Target the entire sidebar */
    [data-testid="stSidebar"] {
        background-color: #210340;
    }

    /* Target all text elements within the sidebar */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Specific selectors for different text elements */
    [data-testid="stSidebar"] .stMarkdown p {
        color: white !important;
    }

    [data-testid="stSidebar"] .stSelectbox label {
        color: white !important;
    }

    [data-testid="stSidebar"] .stMultiSelect label {
        color: white !important;
    }

    /* Style for sidebar header */
    [data-testid="stSidebarNav"] {
        color: white !important;
    }

    /* Style for dropdown menus in sidebar */
    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div,
    [data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] > div {
    background-color: #87034e !important;
      }

    /* Style for dropdown options */
    [data-testid="stSidebar"] ul[data-baseweb="menu"] {
    background-color: white !important;
    }

    /* Style for dropdown text */
    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] span,
    [data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] span,
    [data-testid="stSidebar"] ul[data-baseweb="menu"] li {
    color: #87034e !important;
    }

    /* Table styles */
    .dataframe {
        color: #333333 !important;
    }
    .dataframe th {
        background-color: #210340;
        color: white !important;
    }
    .dataframe td {
        background-color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    "## Filter Makeup Options!"
# Title and Introduction
st.title("Makeup Filter App 💄")
st.markdown("""
Welcome to the Makeup Filter App! This tool allows you to filter a makeup by color shade, product category, and brand. Use the filters in the sidebar to narrow down the table and explore the data.
""")

# Instructions
st.header("Instructions")
st.markdown("""
1. **Color Palette and Sidebar Filters:** Pick a shade in the color pallete below and apply the filters in the sidebar for makeup product and brand.
2. **View the Table:** The filtered table will be displayed below the filters.
3. **Explore:** You can experiment with different combinations of filters to explore the dataset.

This app is designed to help you easily navigate through the makeup options by providing dynamic filtering options.
""")
