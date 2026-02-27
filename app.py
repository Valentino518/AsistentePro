import streamlit as st

# 1. Configuración de Estilo y Pantalla
st.set_page_config(page_title="Business Boss AI", page_icon="💼", layout="centered")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007BFF; color: white; }
    .main { background-color: #f5f7f9; }
    </style>
    """, unsafe_allow_stdio=True)

# 2. Título y Bienvenida
st.title("💼 Business Boss AI")
st.subheader("Tu Consultor de Estrategia y Ventas 24/7")
st.info("Selecciona una herramienta rápida o chatea con tu consultor abajo.")

# 3. Herramientas de Ventas Rápidas (Lo que genera dinero)
col1, col2 = st.columns(2)

with col1:
    if st.button("📈 Guion de Ventas (WhatsApp)"):
        st.session_state.prompt_rapido = "Redacta un mensaje de WhatsApp persuasivo para cerrar una venta hoy mismo. Usa escasez y un llamado a la acción claro."

    if st.button("📱 7 Días de Contenido (Redes)"):
        st.session_state.prompt_rapido = "Crea un calendario de 7 días para Instagram que atraiga clientes nuevos, alternando entre valor y venta directa."

with col2:
    if st.button("📧 Email de Re-contacto"):
        st.session_state.prompt_rapido = "Escribe un correo para un cliente que pidió presupuesto pero no respondió. Sé amable pero profesional."

    if st.button("💸 Estrategia de Precios"):
        st.session_state.prompt_rapido = "Ayúdame a calcular cuánto debo cobrar para tener un margen del 40% después de impuestos y gastos."

# 4. Lógica del Chat
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Mensaje inicial de la IA
    st.session_state.messages.append({"role": "assistant", "content": "Hola Jefe, ¿en qué área de su negocio vamos a trabajar hoy? Ventas, Marketing o Finanzas?"})

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Manejo de entrada de usuario o botones rápidos
input_usuario = st.chat_input("Escribe tu duda de negocio aquí...")
if "prompt_rapido" in st.session_state:
    input_usuario = st.session_state.pop("prompt_rapido")

if input_usuario:
    st.session_state.messages.append({"role": "user", "content": input_usuario})
    with st.chat_message("user"):
        st.markdown(input_usuario)

    # AQUÍ SE CONECTA CON GEMINI (Simulación de respuesta profesional)
    with st.chat_message("assistant"):
        # NOTA: Aquí insertarías la llamada a la API de Gemini
        respuesta_pro = f"Como tu consultor, aquí tienes la estrategia para: '{input_usuario}'. \n\n1. Enfócate en el beneficio, no en el precio. \n2. Reduce la fricción del cliente. \n3. Haz un seguimiento en 24 horas. \n\n¿Quieres que profundicemos en algún punto?"
        st.markdown(respuesta_pro)
        st.session_state.messages.append({"role": "assistant", "content": respuesta_pro})

# 5. Pie de página con botón de "Upgrade"
st.sidebar.title("💎 Cuenta Premium")
st.sidebar.write("Obtén acceso a análisis de documentos PDF y conexión con WhatsApp.")
if st.sidebar.button("Activar Versión Pro"):
    st.sidebar.success("Redirigiendo a pasarela de pago (Stripe/PayPal)...")
