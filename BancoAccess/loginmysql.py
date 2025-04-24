import streamlit as st
import mysql.connector
import bcrypt

# Função para conectar ao banco
def get_connection():
    return mysql.connector.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        database=st.secrets["DB_NAME"]
    )

# Criar usuário
def create_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Usuarios(nome, hash) VALUES (%s, %s)", (username, hashed))
        conn.commit()
    except mysql.connector.IntegrityError:
        st.error("Usuário já existe!")
    finally:
        cursor.close()
        conn.close()

# Verificar login
def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result and bcrypt.checkpw(password.encode(), result[0].encode()):
        return True
    return False

def Login():
    # Interface Streamlit
    st.title("Login Seguro com Streamlit + MySQL")

    menu = st.sidebar.selectbox("Menu", ["Login", "Cadastro"])

    if menu == "Cadastro":
        st.subheader("Criar Conta")
        user = st.text_input("Usuário")
        pwd = st.text_input("Senha", type="password")
        if st.button("Cadastrar"):
            create_user(user, pwd)
            st.success("Usuário criado com sucesso!")

    elif menu == "Login":
        st.subheader("Login")
        user = st.text_input("Usuário")
        pwd = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if login_user(user, pwd):
                st.success(f"Bem-vindo, {user}!")
            else:
                st.error("Usuário ou senha inválidos.")
