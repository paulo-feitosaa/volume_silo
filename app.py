import streamlit as st
import math

st.set_page_config(
    layout="centered",
    page_title='Volume do Silo',
)

# Título do aplicativo
st.title("Volume do Silo")

altura = st.number_input("", min_value=0.0, step=0.1, max_value=3.247, value=None, placeholder='Digite o valor de H em m')  # Campo de entrada do raio

st.image('triangulo45.jpg')

# Função para calcular o volume da esfera
def calcular_volume(altura):
    return (math.pi / 72) * (math.sqrt(3) * 3.75 - 2 * altura)**3 

# Botão para cálculo e exibição do resultado
if st.button("Calcular Volume"):
    if altura != None:
        if altura >= 0 and altura < 3.247:
            volume = calcular_volume(altura)
            st.success(f"O volume do silo é: {volume:.2f} m³")
    else:
        st.warning("Por favor, insira um valor válido para a altura.")

