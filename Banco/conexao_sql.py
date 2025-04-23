import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",     # ou IP da sua máquina
        user="root",          # ou outro usuário
        password="sua_senha",
        database="streamlit_app"
    )
