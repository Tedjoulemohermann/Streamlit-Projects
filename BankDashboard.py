# Import librairies
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Tableau de Bord d'une Banque",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

sns.set(style='dark', context='notebook',
        palette=['#ff5252', '#1de9b6'])

data = pd.read_excel("banque.xlsx")

# Add a Sidebar
with st.sidebar:
    st.title('BANQUE DE FRANCE')
    sex_options=["Male", "Female"]
    sex_plot = st.sidebar.selectbox("Sex",sex_options)
    sitmat_options = ["Marié", "Célibataire"]
    sex_plot = st.sidebar.selectbox("Situation matrimoniale", sitmat_options)
    selected_year = st.sidebar.selectbox("Année", [2022, 2023, 2024])

st.title('📊 Tableau de bord Suivi de la Performance d\'une banque ')

# --- KPIs ---
n_clients = data["Client ID"].count()
n_comptes= data["Compte ID"].count()
n_transactions= data["Transaction ID"].count()
solde = data["Solde après Transaction"].sum()
taux = data["Statut"].value_counts(normalize=True)[0]

col1, col2, col3, col4,col5 = st.columns(5)
col1.metric("Nombre de clients", f"{n_clients:,} ")
col2.metric("Nombre de Comptes", f"{n_comptes:,} ")
col3.metric("Nombre de Transactions", f"{n_transactions:,}")
col4.metric("Solde Total des comptes", f"{solde:,} €")
col5.metric("% actifs", f"{np.round(taux*100,0):,} %")

st.markdown("---")

# --- GRAPHIQUES : Ligne 1 (2 colonnes) ---
st.subheader("📈 Transactions")

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    agence_group = data.groupby("Agence ID")["Transaction ID"].count()
    ax1.bar(agence_group.index, agence_group.values, color="skyblue")
    ax1.set_title("Nombre de transactions par Agence")
    ax1.set_ylabel("Nombre")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    t_c_group = data.groupby("Type de Client")["Transaction ID"].count()
    ax2.bar(t_c_group.index, t_c_group.values, color="skyblue")
    ax2.set_title("Nombre de transactions par type de client")
    ax2.set_ylabel("Nombre")
    st.pyplot(fig2)
# --- GRAPHIQUES : Ligne 2 (3 colonnes) ---
st.subheader("📊 Clients")

col3, col4, col5 = st.columns(3)

with col3:
    fig3, ax3 = plt.subplots()
    ax3.hist(data["Âge"], bins=10, color="skyblue", edgecolor="black")
    ax3.set_title("Distribution des clients par Age")
    st.pyplot(fig3)

with col4:
    fig4, ax4 = plt.subplots()
    client_actif = data.groupby("Statut")["Statut"].count()
    ax4.bar(client_actif.index, client_actif.values, color="skyblue")
    ax4.set_xlabel("Statut des clients")
    ax4.set_ylabel("Nombre")
    ax4.set_title("Nombre de Clients Actif et Inactif")
    st.pyplot(fig4)

with col5:
    fig5, ax5 = plt.subplots()
    profit_by_year = data.groupby("Agence ID")["Client ID"].count()
    ax5.bar(profit_by_year.index, profit_by_year.values, color="skyblue")
    ax5.set_title("Nombre de Client par Agence")
    st.pyplot(fig5)

# --- GRAPHIQUES : Ligne 3 (1 colonne) ---
st.subheader("📊 Tendance")

col6, col7= st.columns(2)

with col6 :
    fig6, ax6 = plt.subplots()
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    tendance = data.groupby("Date")["Transaction ID"].count()
    ax6.plot(tendance.index, tendance.values, color="red", alpha=0.6)
    ax6.set_title("Evolution des transactions")
    ax6.set_xlabel("Date")
    ax6.set_ylabel("Nombre")
    st.pyplot(fig6)