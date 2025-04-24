import streamlit as st

def CalcularMargem():
    nome = st.text_input("Digite o nome da peça de carne: ")

    peso : float = st.number_input(label= "Digite o peso da peça de carne em quilos: ", min_value=0., max_value=1000000000., step=1.)

    preco : float = st.number_input(label= "Digite o preco que você pagou pelo quilo: ", min_value=0., max_value=1000000000., step=1.)

    porcentagemQuebra : float = st.number_input(label= "Digite a porcentagem de quebra: ", min_value=0., max_value=100., step=1.)

    porcentagemLucro : float = st.number_input(label= "Digite a porcentagem desejada de lucro: ", min_value=0., max_value=100., step=1.)

    if st.button("Calcular"):
        valorPago : float = peso * preco
        quebra = peso * (porcentagemQuebra / 100)
        pesoVendavel = peso - quebra
        margemLucro = valorPago * (porcentagemLucro / 100)
        valorASerAtingido = valorPago + margemLucro

        total = valorASerAtingido / pesoVendavel

        st.success(f"O peso final sem a quebra é de {pesoVendavel:.2f} quilos.")
        st.success(f"Valor ideal para o quilo da {nome} é de R${total:.2f}")