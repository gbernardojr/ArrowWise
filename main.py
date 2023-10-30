import streamlit as st



st.title("Sistema de Gestão de Pedido")

st.sidebar.markdown("## Menu")

vSelectCadastros = st.sidebar.selectbox("Cadastros",["Cadastro da Empresa","Cadastro de Clientes","Cadastro de produtos"])
vSelectOperacionais = st.sidebar.selectbox("Operacional",["Emissão de Orçamentos"])