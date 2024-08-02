import streamlit as st
# title
st.title('Este é o título')

# header
st.header("Header do ST")

# subheader
st.subheader("Subheader do ST")

# caption
st.caption("Este é um Caption")


# Code
code = '''if(fome > 0):
    return "ir para geladeira"
else:
    retun "estudar Streamlit"'''
st.code(code, language='python')

# text
st.text('Este é um texto usando st.text')

# Latex https://katex.org/docs/supported.html
st.latex('\int x²+y²+32ab \isin x²+y²+z²')


# markdown
st.text('MARKDOWN') 

st.markdown("A nota dos alunos foi em **media**, maior que o *semestre* passado")

st.markdown('Teste de markdown com **textos em negrito**.')

st.markdown('Teste de markdown e *textos em itálico*.')

st.markdown('Teste de markdown e ~~textos tachados~~.')

st.markdown('Teste de markdown e `textos de códigos`.')

st.markdown('Teste de markdown e [Link Google](http://www.google.com.br).')

st.markdown(':fireworks:')
