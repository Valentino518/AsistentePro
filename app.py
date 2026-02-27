
import streamlit as st

# Configuración básica
st.set_page_config(page_title="Business Boss AI", page_icon="💼")

st.title("💼 Business Boss AI")
st.subheader("Tu Consultor de Estrategia y Ventas 24/7")

# Botones de acción rápida
st.markdown("### 🚀 Herramientas Rápidas")
opcion = st.radio("Selecciona una tarea:", 
                 ["Elegir...", "Guion de WhatsApp", "7 Días de Redes Sociales", "Email de Ventas"])

if opcion == "Guion de WhatsApp":
    st.write("👉 **Copia esto:** 'Hola, vi tu interés en nuestro producto. Solo por hoy tenemos un bono especial. ¿Te gustaría agendar una llamada?'")

if opcion == "7 Días de Redes Sociales":
    st.write("👉 **Idea Día 1:** Muestra el detrás de cámara de tu negocio.")

# Chat
st.markdown("---")
user_input = st.text_input("Hazle una pregunta a tu consultor:")
if user_input:
    st.write(f"Analizando: '{user_input}'... (Aquí conectaremos tu Inteligencia pronto)")

st.sidebar.title("💎 Versión Premium")
st.sidebar.write("Desbloquea análisis financiero avanzado.")
