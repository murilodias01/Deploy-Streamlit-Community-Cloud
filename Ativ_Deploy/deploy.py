import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Minha Aplicação Streamlit", layout="wide")

st.title("Minha Primeira Aplicação no Streamlit")
st.write("Seu aplicativo está rodando localmente com sucesso!")

st.subheader("Exemplo de Tabela de Dados")
dados = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['Coluna A', 'Coluna B', 'Coluna C']
)
st.dataframe(dados)