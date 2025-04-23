import streamlit as st

import calculadora_acougue

st.set_page_config(
    page_title="Açougue Digital",
    page_icon="👋",
)

st.title("Bem vindo ao Açougue Digital! 👋")

calculadora_acougue.CalcularMargem()
