import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="¡Feliz Cumpleaños!", page_icon="🎂", layout="centered")

# Estilos personalizados
st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
    }
    .sub-font {
        font-size:25px !important;
        color: #FF69B4;
        text-align: center;
    }
    .text-font {
        font-size:20px !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.markdown('<p class="big-font">¡Feliz Cumpleaños, mi amor! 🎉</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-font">Para la chica más increíble, Lubaloo ❤️</p>', unsafe_allow_html=True)

st.write("---")

# Espacio para una imagen o GIF romántico
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Puedes cambiar este enlace por una foto de ustedes usando st.image("ruta_a_tu_foto.jpg")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDdvbHkwbnpqYThsMnZsM281N2F0cWZ1bHZ0bmZ0YnlxZnF6bGhvOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/M90mJvfWfd5mbUuULX/giphy.gif", use_container_width=True)

st.write("---")

# Mensaje romántico
st.markdown('<p class="text-font">Hoy celebramos un año más de tu hermosa vida. Me siento el chico más afortunado del mundo por poder compartir este día contigo. Eres mi inspiración, mi alegría y mi persona favorita en todo el universo.</p>', unsafe_allow_html=True)

st.write("")
st.write("")

# Botón interactivo
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Toca aquí para una sorpresa 🎁", use_container_width=True):
        st.balloons()
        time.sleep(1)
        st.success("¡Te amo muchísimo! Que este nuevo año de vida te traiga tantas sonrisas como las que tú me das a mí. Con todo mi amor, Justin. 💕")
