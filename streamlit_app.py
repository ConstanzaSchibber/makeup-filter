import streamlit as st
from st_clickable_images import clickable_images
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters
from PIL import Image
import base64


# Set page config
st.set_page_config(
    page_title="Discover Your Perfect Makeup Shade!",
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
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    "## Filter More Options!"
# Title and Introduction
st.title("Discover Your Perfect Makeup Shade! 💄")
st.markdown("""
This tool allows you to filter a makeup by color shade 🎨, product category, and brand. 
""")

# Instructions
st.header("Instructions")
st.markdown("""
1. **Color Palette 🎨:** Click the color palette below to filter products by shade.
2. **Sidebar:** Use the sidebar to narrow down options by product (e.g. blush, lipstick) or brand.
""")

df = pd.read_csv('./data/df_newcolors_for_streamlit.csv') 
df = df[df.ground_truth == 1]
df = df[['category', 'brand', 'new_median_hex_circle', 'Circle', 'img_url']]

df = df.rename(columns={
    'category': 'Makeup Category',
    'brand': 'Brand',
    'new_median_hex_circle': 'Shade Group',
    'Circle': 'Product (Predicted) Color',
    'img_url': 'Product'
})

# Filter Sidebar

dynamic_filters = DynamicFilters(df=df, filters=['Makeup Category', 'Brand'])
#dynamic_filters.display_filters(location='sidebar')

# save filtered df as new variable
new_df = dynamic_filters.filter_df()

# Color pick

list_images = ['59332f.png',
 '5e1920.png',
 '7f2538.png',
 '82232b.png',
 '93092b.png',
 'a13c3e.png',
 'a62b32.png',
 'ac221c.png',
 'b83c3e.png',
 'b95737.png',
 'c14441.png',
 'c93713.png',
 'd76878.png',
 'd85d78.png',
 'da7670.png',
 'de9592.png',
 'df535b.png',
 'e34d38.png',
 'e5817c.png',
 'eba7a7.png',
 'ed9288.png',
 'f3a89b.png',
 'f6afa8.png',
 'f6e7e7.png',
 'f9c2b5.png',
 'ffd9d5.png']

images = []
for file in list_images:
    file_path = './data/' + str(file)
    with open(file_path, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        images.append(f"data:image/jpeg;base64,{encoded}")

### Create color bar
clicked = clickable_images(
    images,
    titles=[f"Image #{str(i)}" for i in range(10)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "50px"},
)

## Filter by color
if clicked == 0:
  cat = df['Shade Group'].unique()[0]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 1:
  cat = df['Shade Group'].unique()[1]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 2:
  cat = df['Shade Group'].unique()[2]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 3:
  cat = df['Shade Group'].unique()[3]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 4:
  cat = df['Shade Group'].unique()[4]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 5:
  cat = df['Shade Group'].unique()[5]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 6:
  cat = df['Shade Group'].unique()[6]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 7:
  cat = df['Shade Group'].unique()[7]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 8:
  cat = df['Shade Group'].unique()[8]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 9:
  cat = df['Shade Group'].unique()[9]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 10:
  cat = df['Shade Group'].unique()[10]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 11:
  cat = df['Shade Group'].unique()[11]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 12:
  cat = df['Shade Group'].unique()[12]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 13:
  cat = df['Shade Group'].unique()[13]
  new_df = new_df[new_df['Shade Group']== cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 14:
  cat = df['Shade Group'].unique()[14]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 15:
  cat = df['Shade Group'].unique()[15]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 16:
  cat = df['Shade Group'].unique()[16]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 17:
  cat = df['Shade Group'].unique()[17]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 18:
  cat = df['Shade Group'].unique()[18]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 19:
  cat = df['Shade Group'].unique()[19]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 20:
  cat = df['Shade Group'].unique()[20]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 21:
  cat = df['Shade Group'].unique()[21]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 22:
  cat = df['Shade Group'].unique()[22]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 23:
  cat = df['Shade Group'].unique()[23]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 24:
  cat = df['Shade Group'].unique()[24]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])

elif clicked == 25:
  cat = df['Shade Group'].unique()[25]
  new_df = new_df[new_df['Shade Group'] == cat]
  dynamic_filters = DynamicFilters(df=new_df, filters=['Makeup Category', 'Brand'])


dynamic_filters.display_filters(location='sidebar')

# Converting links to html tags
def path_to_image_html(path):
    return '<img src="' + path + '" height="60" >'


if len(new_df) < len(df):
    # Apply the color_square function to the 'District' column
    #new_df['District'] = new_df['District'].apply(color_square)
    new_df = new_df.sort_values(by = ['Makeup Category','Brand'])
    # Display the dataframe with HTML
    #st.write(new_df.to_html(escape=False, index=False), formatters=dict(img_url=path_to_image_html), unsafe_allow_html=True)

    def convert_df(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, index=False, formatters=dict(Product=path_to_image_html))

    html = convert_df(new_df)

    st.markdown(
    html,
    unsafe_allow_html=True
    )

else:
    st.write("Please select at least one filter to display the data.")
