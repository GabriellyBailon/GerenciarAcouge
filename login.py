import streamlit as st

st.title("Login")

aba = st.radio("Escolha uma opção", ["Login", "Cadastro"])

if aba == "Login":
    username = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        autenticado, nome = autenticar_usuario(username, senha)
        if autenticado:
            st.success(f"Bem-vindo, {nome}!")
            # aqui pode ir para próxima página ou liberar o menu
        else:
            st.error("Usuário ou senha inválidos.")

else:
    nome = st.text_input("Nome completo")
    username = st.text_input("Nome de usuário")
    senha = st.text_input("Senha", type="password")
    senha2 = st.text_input("Confirme a senha", type="password")

    if st.button("Cadastrar"):
        if senha != senha2:
            st.warning("As senhas não coincidem.")
        else:
            sucesso, msg = cadastrar_usuario(username, nome, senha)
            if sucesso:
                st.success(msg)
            else:
                st.error(msg)