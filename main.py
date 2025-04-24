import streamlit as st

import calculadora_acougue

st.set_page_config(
    page_title="Meu Açougue Online",
    page_icon="👋",
)

st.title("Bem vindo ao Meu Açougue Online! 👋")

calculadora_acougue.CalcularMargem()
