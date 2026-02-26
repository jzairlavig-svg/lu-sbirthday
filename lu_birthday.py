import streamlit as st
import time
import os
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="¡Feliz Cumpleaños Mi Amor!",
    page_icon="💖",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- FUNCIÓN PARA CARGAR IMÁGENES LOCALES ---
def cargar_imagen_local(ruta):
    if os.path.exists(ruta):
        try:
            with open(ruta, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            ext = ruta.split('.')[-1].lower()
            mime_type = "image/png" if ext == "png" else "image/jpeg"
            return f"data:{mime_type};base64,{encoded_string}"
        except Exception:
            return "https://via.placeholder.com/300x200.png?text=Error"
    else:
        return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNcWg8qAAAB8gExB+L0HQAAAABJRU5ErkJggg=="

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to right top, #ffafbd, #ffc3a0, #ffafbd, #d4a5a5);
        background-attachment: fixed;
    }
    .main-title {
        font-family: 'Brush Script MT', cursive; 
        font-size: 60px !important;
        color: #FFFFFF;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
        font-weight: bold;
    }
    .sub-title {
        font-size: 25px !important;
        color: #FFFFFF;
        text-align: center;
        text-shadow: 1px 1px 2px #d4a5a5;
        margin-bottom: 20px;
    }
    .card-box {
        background-color: rgba(255, 255, 255, 0.85); 
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        color: #333333;
        font-size: 18px;
        text-align: center;
    }
    .polaroid {
        background-color: white;
        padding: 10px 10px 30px 10px;
        box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
        transform: rotate(-2deg); 
        margin: 10px;
        transition: transform 0.3s;
    }
    .polaroid:hover {
        transform: rotate(0deg) scale(1.05); 
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 30px;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MÚSICA (NUEVA CANCIÓN) ---
# Opción A: Archivo local (si tienes un archivo llamado cancion.mp3)
# Opción B: Un enlace directo a un MP3 (he puesto una melodía de piano romántica muy linda)
music_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" 

if os.path.exists("cancion.mp3"):
    st.audio("cancion.mp3", format='audio/mp3')
else:
    # He puesto esta canción por defecto, es más alegre y movida
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", format='audio/mp3')

st.caption("✨ Ponle play a la música antes de seguir bajando, mi reina ✨")

# --- CONTENIDO ---
st.markdown('<p class="main-title">¡Feliz Cumpleaños, Mi Reina! 👑🎂</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Cada segundo a tu lado es un regalo que agradezco al cielo.</p>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🌹 Nuestra Historia", "📸 Recuerdos", "💖 Por qué te amo"])

with tab1:
    st.markdown('<div class="card-box"><h3>Eres mi persona favorita</h3><p>Desde que llegaste a mi vida, todo tiene más color y sentido. No solo celebro tu cumple, celebro que existas.</p></div>', unsafe_allow_html=True)
    snoopy_data = cargar_imagen_local("snoopy.png")
    if "image" in snoopy_data:
        st.image(snoopy_data, width=350)
    else:
        st.error("⚠️ No encontré 'snoopy.png'")

with tab2:
    col1, col2, col3 = st.columns(3)
    fotos = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]
    textos = ["Donde todo empezó ❤️", "Tú y yo siempre ✨", "La más hermosa 😍"]
    
    for i, col in enumerate([col1, col2, col3]):
        with col:
            img = cargar_imagen_local(fotos[i])
            st.markdown(f'<div class="polaroid"><img src="{img}" style="width:100%"><p style="text-align:center">{textos[i]}</p></div>', unsafe_allow_html=True)

with tab3:
    st.markdown("""
        <div class="card-box" style="text-align: left;">
            <p>✨ Por cómo me haces reír incluso en los días malos.</p>
            <p>✨ Por tu forma tan única de ver el mundo.</p>
            <p>✨ Por ser mi apoyo incondicional.</p>
            <p>✨ Por ser la niña más inteligente y valiente.</p>
            <p>✨ Porque simplemente... eres tú.</p>
        </div>
    """, unsafe_allow_html=True)

# --- FINAL ---
st.write("---")
c_f1, c_f2, c_f3 = st.columns([1, 2, 1])
with c_f2:
    if st.button("🎁 ¡TU SORPRESA FINAL AQUÍ! 🎁", use_container_width=True):
        st.balloons()
        st.markdown("""
            <div style="background-color: #ffe4e1; padding: 30px; border-radius: 25px; border: 4px dashed #FF4B4B; text-align: center;">
                <h1 style="color: #FF4B4B;">¡TE AMO INFINITO! ❤️</h1>
                <p style="font-size: 20px;">Gracias por elegirme cada día. ¡Feliz cumpleaños, Lubaloo!</p>
                <p style="font-style: italic;">Atte: Justin</p>
            </div>
        """, unsafe_allow_html=True)
