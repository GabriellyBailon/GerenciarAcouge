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

# Função para verificar permissões do usuário (apenas admin pode cadastrar)
def is_admin(username):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT idpermissoes FROM Usuarios WHERE nome = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    # Se o idpermissoes for 1, é admin
    print(result)
    return result and int(result[0]) == 1

# Função para cadastrar um novo usuário (só admin pode)
def register_user():
    if is_admin(st.session_state['user']):
        st.title("Cadastro de Usuário")
        username = st.text_input("Nome de usuário")
        password = st.text_input("Senha", type="password")
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        if st.button("Cadastrar"):
            connection = get_connection()
            cursor = connection.cursor()

            # Inserir novo usuário no banco
            query = "INSERT INTO Usuarios (nome, hash, idpermissoes) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, password_hash, 2))  # 2 é um nível de permissão normal
            connection.commit()

            cursor.close()
            connection.close()

            st.success(f"Usuário {username} cadastrado com sucesso!")
    else:
        st.error("Apenas administradores podem cadastrar novos usuários.")
