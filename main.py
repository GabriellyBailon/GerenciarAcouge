import streamlit as st
import calculadora_acougue
import BancoAccess.loginmysql as ms

st.set_page_config(
    page_title="Meu Açougue Online",
    page_icon="👋",
)

st.title("Bem vindo ao Meu Açougue Online! 👋")

if not ms.is_logged_in():
        ms.Login()  # Exibe a tela de login
else:
    st.sidebar.success(f"Logado como: {st.session_state['user']}")
    calculadora_acougue.CalcularMargem()
