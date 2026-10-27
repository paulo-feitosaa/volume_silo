import streamlit as st
import math

st.set_page_config(
    layout="centered",
    page_title='Volume do Silo',
)

# Título do aplicativo
st.title("Volume do Silo")

h = st.number_input("Digite a leitura do sensor em mm", min_value=0.0, step=1.0,  value=None, placeholder='Digite o valor de h em mm') 

D = st.number_input("Digite o Diâmetro do silo (**D**) em mm", min_value=0.0, step=1.0,  value=3750.0)  # Campo de entrada do raio

H_silo = st.number_input("Digite a Altura do silo (**H_silo**) em mm", min_value=0.0, step=1.0,  value=3000.0) 

H2 = st.number_input("Digite a Altura do cone (**H_cone**) em mm", min_value=0.0, step=1.0,  value=2500.0) 

d = st.number_input("Digite o Diâmetro da base menor do cone (**d**) em mm", min_value=0.0, step=1.0,  value=200.0) 

#hs = st.number_input("Digite o valor da altura do cilindro em mm", min_value=0.0, step=1.0,  value=3000.0) 

density = st.number_input("Digite o valor da densidade em t/m³", min_value=0.0, step=1.0,  value=1.0) 
# Função para calcular o volume da esfera
def calcular_volume(h):
    H1 = H_silo - H2

    if h <= H1:
        vol_cilin = (math.pi / 4) * D * D * (H1 - h)
        vol_cone = (math.pi / 12) * H2 * (D*D + d*d + D*d)
        vol = vol_cilin + vol_cone
    else:
        H3 = H_silo - h
        D2 = d + (D - d) * (H3 / H2)
        vol = (H3 * math.pi / 12) * (D2*D2 + d*d + D2*d)      
    return vol
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

st.image('silo_geral.jpg')