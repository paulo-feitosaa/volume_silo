import streamlit as st
import math

st.set_page_config(
    layout="centered",
    page_title='Volume do Silo',
)

# Título do aplicativo
st.title("Volume do Silo")
st.image('cone45.jpg')
h = st.number_input("Digite a leitura do sensor em mm", min_value=0.0, step=1.0,  value=None, placeholder='Digite o valor de h em mm') 

D = st.number_input("Digite o valor de D em mm", min_value=0.0, step=1.0,  value=3750.0)  # Campo de entrada do raio

# H = st.number_input("Digite o valor de H em mm", min_value=0.0, step=1.0,  value=3000.0) 

d = st.number_input("Digite o valor de d em mm", min_value=0.0, step=1.0,  value=200.0) 

density = st.number_input("Digite o valor da densidade em t/m³", min_value=0.0, step=1.0,  value=1.0) 
# Função para calcular o volume da esfera
def calcular_volume(h):
    # c = d + (H - h) * (D - d) / H
    return (h * math.pi / 36) * (9*d*d + 6 * d * h * math.sqrt(3) + 4 * h * h)

# Botão para cálculo e exibição do resultado
if st.button("Calcular Volume"):
    if h != None:
        if h >= 0:
            volume = calcular_volume(h) * 1e-9
            mass = volume * density
            st.success(f"O volume do silo é: {volume:.2f} m³")
            st.success(f"A massa total é: {mass:.2f} toneladas")
    else:
        st.warning("Por favor, insira um valor válido para a altura.")

