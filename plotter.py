import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and layout
st.title('Easy Plots')
st.write('Upload your data, select the type of plot you want to create, optionally add reference lines, choose a plot color, and select a column for dynamic coloring.')

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

# Function to load data
@st.cache_data
def load_data(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    return df

# Plotting function with dynamic coloring option
def plot_data(plot_type, data):
    # st.markdown(f"<h3 style='color: white;'>Number of data points: {len(data)}</h3>", unsafe_allow_html=True)
    
    # Allow user to select a column for coloring the plot
    color_column = st.selectbox('Choose a column to color by (optional):', ['None'] + list(data.columns))
    color_column = None if color_column == 'None' else color_column

    if plot_type == 'Histogram':
        col = st.selectbox('Select column for histogram', data.columns)
        fig = px.histogram(data, x=col, color=color_column)
    elif plot_type == 'Boxplot':
        col = st.selectbox('Select column for boxplot', data.columns)
        fig = px.box(data, y=col, color=color_column)
    elif plot_type == 'Scatter Plot':
        x_col = st.selectbox('Select X axis', data.columns, index=0)
        y_col = st.selectbox('Select Y axis', data.columns, index=1)
        fig = px.scatter(data, x=x_col, y=y_col, color=color_column)
    else:
        st.write("Select a plot type.")
        return
    
    # Add reference lines if necessary, as per previous enhancements
    # Your code for reference lines goes here
    st.markdown(f"Number of data points: {len(data)}")
    st.write(fig)

if uploaded_file is not None:
    df = load_data(uploaded_file)
    plot_type = st.radio("Select Plot Type", ('Histogram', 'Boxplot', 'Scatter Plot'))
    plot_data(plot_type, df)
else:
    st.write("Please upload a file to begin.")
