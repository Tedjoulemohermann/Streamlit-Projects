# Import librairies
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Blood Donation Campaign Dashboard",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded")

sns.set(style='dark', context='notebook',
        palette=['#ff5252', '#1de9b6'])

data = pd.read_excel("Updated Challenge dataset.xlsx")

# Add a Sidebar
with st.sidebar:
    st.title('Blood Donation Campaign Dashboard')
    sex_options=["Male", "Female"]
    sex_plot = st.sidebar.selectbox("Sex",sex_options)
    sitmat_options = ["Marié", "Célibataire"]
    sex_plot = st.sidebar.selectbox("Situation matrimoniale", sitmat_options)

st.title('Blood Donation Campaign Dashboard')


fig, ax =plt.subplots(3,1)
sns.countplot(data=data,x="Genre", ax=ax[0])
sns.countplot(data=data,x="ÉLIGIBILITÉ AU DON.",ax=ax[1])
sns.histplot(data=data,x="Poids",ax=ax[2])
st.pyplot(fig)