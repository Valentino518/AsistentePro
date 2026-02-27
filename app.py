import streamlit as st
import google.generativeai as genai

# DIRECT CONFIGURATION (Hardcoded Key)
# Reemplaza AIza... por tu llave real dentro de las comillas
genai.configure(api_key="AIzaSyC7yRHpl1NAFIWeJYlsi0s-R1-tNZ5tEBE")
model = genai.GenerativeModel('gemini-1.5-flash')

# PAGE SETUP
st.set_page_config(page_title="Business Boss AI", page_icon="💼")

st.title("💼 Business Boss AI")
st.subheader("Your 24/7 Strategy & Sales Consultant")

# SIDEBAR & PAYMENTS
st.sidebar.title("💎 Pro Version")
st.sidebar.markdown(
    f'<a href="YOUR_PAYPAL_LINK" target="_blank"><button style="width:100%; background-color:#0070ba; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Pay with PayPal (USD)</button></a>',
    unsafe_allow_html=True
)

st.sidebar.write("")

st.sidebar.markdown(
    f'<a href="YOUR_MERCADOPAGO_LINK" target="_blank"><button style="width:100%; background-color:#009ee3; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Pay with Mercado Pago</button></a>',
    unsafe_allow_html=True
)

# CHAT INTERFACE
user_input = st.text_input("Ask your business consultant a question:")

if user_input:
    try:
        response = model.generate_content(f"Act as a professional business expert. Answer: {user_input}")
        st.write("💡 **Response:**")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
