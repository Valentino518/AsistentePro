import streamlit as st
import google.generativeai as genai

# --- AI CONFIGURATION ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Missing GOOGLE_API_KEY in Streamlit Secrets")

# --- PAGE SETUP ---
st.set_page_config(page_title="Business Boss AI", page_icon="💼")

st.title("💼 Business Boss AI")
st.subheader("Your 24/7 Strategy & Sales Consultant")

# --- SIDEBAR & PAYMENTS ---
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

# --- CHAT INTERFACE ---
user_input = st.text_input("Ask your business consultant a question:")

if user_input:
    try:
        # Prompt telling the AI how to behave
        full_prompt = f"Act as an expert business consultant. Give practical and professional advice about: {user_input}"
        response = model.generate_content(full_prompt)
        st.write("💡 **Response:**")
        st.write(response.text)
    except Exception as e:
        st.error("AI Error. Please check your API Key in Secrets.")
