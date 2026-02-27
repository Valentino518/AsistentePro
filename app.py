import streamlit as st
import google.generativeai as genai

# Configuración de la IA con tu llave secreta
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Falta la clave API en los Secrets de Streamlit")

st.set_page_config(page_title="Business Boss AI", page_icon="💼")

st.title("💼 Business Boss AI")
st.subheader("Tu Consultor de Estrategia y Ventas 24/7")

# --- BOTONES DE PAGO ---
st.sidebar.title("💎 Versión Pro")
st.sidebar.markdown(
    f'<a href="TU_LINK_PAYPAL" target="_blank"><button style="width:100%; background-color:#0070ba; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Pagar con PayPal (USD)</button></a>',
    unsafe_allow_html=True
)
st.sidebar.write("")
st.sidebar.markdown(
    f'<a href="TU_LINK_MERCADOPAGO" target="_blank"><button style="width:100%; background-color:#009ee3; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Pagar con Mercado Pago</button></a>',
    unsafe_allow_html=True
)

# --- LÓGICA DE CHAT ---
user_input = st.text_input("Hazle una pregunta a tu consultor de negocios:")
if user_input:
    try:
        response = model.generate_content(f"Actúa como un experto en negocios y ventas. Responde de forma breve y práctica a: {user_input}")
        st.write(response.text)
    except Exception as e:
        st.error("Dile al administrador que verifique la configuración de la IA.")

# Recuerda cambiar TU_LINK_PAYPAL y TU_LINK_MERCADOPAGO por tus links reales.
