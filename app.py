import streamlit as st

# CONFIGURAÇÃO DA PÁGINA (Define o título da aba do navegador)
st.set_page_config(
    page_title="EduTrack AI",
    page_icon="🎓"
)


# TÍTULO PRINCIPAL
st.title("🎓 EduTrack AI")


# SIDEBAR (MENU LATERAL)
st.sidebar.header("Menu")

menu_option = st.sidebar.radio(
    "Navegar",
    ["Dashboard", "Disciplinas", "Tarefas"]
)

# CONTEÚDO DINÂMICO

if menu_option == "Dashboard":
    st.write("Bem-vindo ao seu assistente acadêmico!")
    
    st.info("Conecte ao Xano para ver seus dados reais.")
    
    # Exemplo de Métrica Visual
    col1, col2 = st.columns(2)
    
    col1.metric("Disciplinas Ativas", "0")
    col2.metric("Tarefas Pendentes", "0")


elif menu_option == "Disciplinas":
    st.subheader("Minhas Disciplinas")
    
    st.write("Aqui listaremos as matérias cadastradas no backend.")


elif menu_option == "Tarefas":
    st.subheader("Gerenciamento de Tarefas")
    
    tarefa = st.checkbox("Estudar Streamlit")
    