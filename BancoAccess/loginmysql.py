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
    cursor.execute("SELECT hash FROM Usuarios WHERE nome = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result and bcrypt.checkpw(password.encode(), result[0].encode()):
        return True
    return False

# Função de verificação de logindef is_logged_in():
def is_logged_in():
    return st.session_state.get("logged_in", False)

def Login():
    st.title("Login")
    username = st.text_input("Nome")
    password = st.text_input("Senha", type="password")

    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Login bem-sucedido!")
            st.rerun()  # Força atualização da tela
        else:
            st.error("Usuário ou senha inválidos")
