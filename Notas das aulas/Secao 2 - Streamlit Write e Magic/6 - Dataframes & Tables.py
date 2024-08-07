import streamlit as st
import pandas as pd
import numpy as np


# Gerando Dataframe
st.header('Aula de Dataframe')
df = pd.DataFrame(
    np.random.randn(5,5),
    columns=('col %d' %i for i in range(5))
)
st.dataframe(df)


# Alterando dimensões
st.subheader('Exemplo 2 - Alterando dimensões')
st.dataframe(df, 300, 200)


# Dando destaque nos maiores valores
st.subheader('Exemplo 3 - Dando um destaque nos maiores valores')
st.dataframe(df.style.highlight_max(axis=0)) # axis=0 considera a coluna, axis=1 considera a linha


# Usando TABLE, que é similar ao DataFrame
st.subheader('TABLE - Exemplo similar ao Dataframe')
st.table(df)
