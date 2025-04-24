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

    admin = ms.is_admin(st.session_state['user'])

    if admin:
        escolha = st.sidebar.radio("Menu", ["Calculadora", "Cadastrar Usuário", "Sair"])
    else:
        escolha = st.sidebar.radio("Menu", ["Calculadora", "Sair"])

    if escolha == "Calculadora":
        calculadora_acougue.CalcularMargem()

    elif escolha == "Cadastrar Usuário" and admin:
        ms.register_user()

    elif escolha == "Sair":
        st.session_state.clear()
        st.success("Você saiu com sucesso.")
        st.rerun()
