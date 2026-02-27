import streamlit as st
import google.generativeai as genai

# Configuración de la IA con tu llave secreta
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Business Boss AI", page_icon="💼")

st.title("💼 Business Boss AI")
st.subheader("Tu Consultor de Estrategia y Ventas 24/7")

# ... (el resto del código de los botones) ...

# Lógica para que la IA responda de verdad
user_input = st.text_input("Hazle una pregunta a tu consultor:")
if user_input:
    response = model.generate_content(f"Actúa como un experto en negocios. Responde a: {user_input}")
    st.write(response.text)

