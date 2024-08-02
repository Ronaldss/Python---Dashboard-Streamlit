import pandas as pd
import streamlit as st
import numpy as np
import altair  as alt

# Criando tabela simples com Streamlit
df = pd.DataFrame({'col1': [1,2,3]})
df

st.write(pd.DataFrame({
    'Coluna A': [1, 2, 3, 4, 5],
    'Coluna B': ["Cachorro", "Gato", "Cavalo", "zebra", "Pássaro"],
}))

'''
TEXTOS

Com o *Magic* é possível escrever diretamente o texto!
'''

'''
### VARIÁVEIS ###
'''
x = "Olá, mundo! :sunglasses:"
st.write("String:  " +x)

z = 10
y =  3
st.write("Z = 10")
st.write("Y =  3")

st.write("Z + Y =   ", z+y)
st.write("Z * Y =   ", z*y)

st.write("Este é um outro texto com o write do streamlit.")



'''
### ARRAY ###
'''
array = [1, 2, "abc", "Ronald", True]
st.write('Aqui temos uma array:  ', array)



'''
TRABALHANDO COM GRÁFICOS (NUMPY, ALTAIR)
'''

df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
        
st.write(c)
