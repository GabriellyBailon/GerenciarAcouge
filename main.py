import streamlit as st
import calculadora_acougue
import BancoAccess.loginmysql as ms

st.set_page_config(
    page_title="Meu Açougue Online",
    page_icon="👋",
)

st.title("Bem vindo ao Meu Açougue Online! 👋")

escolha = st.sidebar.radio("Menu", ["Calculadora"])

if escolha == "Calculadora":
    calculadora_acougue.CalcularMargem()
