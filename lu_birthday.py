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

# --- FUNCIÓN PARA CARGAR IMÁGENES LOCALES EN HTML ---
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

# --- ESTILOS CSS PERSONALIZADOS ---
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
        padding-bottom: 20px;
    }
    .sub-title {
        font-size: 30px !important;
        color: #FFFFFF;
        text-align: center;
        text-shadow: 1px 1px 2px #d4a5a5;
    }
    .card-box {
        background-color: rgba(255, 255, 255, 0.85); 
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        color: #333333;
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
    }
    .polaroid {
        background-color: white;
        padding: 10px 10px 30px 10px;
        box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
        transform: rotate(-2deg); 
        margin: 10px;
    }
    .polaroid:hover {
        transform: rotate(0deg) scale(1.05); 
        transition: transform 0.3s;
    }
    .caption_pol {
        text-align: center;
        font-family: 'Courier New', monospace;
        color: #555;
        margin-top: 10px;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 30px;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid white;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown('<p class="main-title">¡Feliz Cumpleaños, Mi Reina! 👑🎂</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Hoy el mundo es más bonito porque tú estás en él.</p>', unsafe_allow_html=True)
st.write("---")

# --- ESTRUCTURA DE PESTAÑAS ---
tab1, tab2, tab3 = st.tabs(["🌹 El Inicio", "📸 Nuestros Recuerdos", "💖 ¿Por qué Tú?"])

with tab1:
    st.markdown("""
        <div class="card-box">
            <h3>Mi amor, mi compañera, mi todo.</h3>
            <p>Parece que fue ayer cuando te conocí, y mira dónde estamos hoy. 
            Celebrar tu cumpleaños no es solo celebrar un año más, es celebrar el regalo 
            que es tenerte en mi vida. Eres la casualidad más bonita que me ha pasado.</p>
        </div>
    """, unsafe_allow_html=True)
    
    ruta_snoopy = "snoopy.png"
    snoopy_data = cargar_imagen_local(ruta_snoopy)
    
    if "image/png" in snoopy_data or "image/jpeg" in snoopy_data:
        st.markdown(f"""
            <div style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 20px;">
                <img src="{snoopy_data}" style="width: 350px; height: auto;">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ FALTA LA IMAGEN: Asegúrate de tener 'snoopy.png' en la carpeta.")

with tab2:
    st.markdown('<div class="card-box"><p>Pequeños instantes de una gran historia de amor.</p></div>', unsafe_allow_html=True)
    
    foto_1 = cargar_imagen_local("foto1.jpg")
    foto_2 = cargar_imagen_local("foto2.jpg")
    foto_3 = cargar_imagen_local("foto3.jpg")

    col_p1, col_p2, col_p3 = st.columns(3)
    
    with col_p1:
        st.markdown(f'<div class="polaroid"><img src="{foto_1}" style="width:100%; aspect-ratio: 2/3; object-fit: cover;"><div class="caption_pol">El comienzo de todo ❤️</div></div>', unsafe_allow_html=True)
    with col_p2:
        st.markdown(f'<div class="polaroid"><img src="{foto_2}" style="width:100%; aspect-ratio: 2/3; object-fit: cover; transform: rotate(3deg);"><div class="caption_pol">Momentos inolvidables ✨</div></div>', unsafe_allow_html=True)
    with col_p3:
        st.markdown(f'<div class="polaroid"><img src="{foto_3}" style="width:100%; aspect-ratio: 2/3; object-fit: cover;"><div class="caption_pol">Mi vista favorita 😍</div></div>', unsafe_allow_html=True)

with tab3:
    st.markdown("""
        <div class="card-box" style="text-align: left;">
            <h3>👑 5 Razones por las que te amo:</h3>
            <ul>
                <li>✨ Por la forma en que tus ojos brillan cuando sonríes.</li>
                <li>✨ Porque tienes el corazón más noble que conozco.</li>
                <li>✨ Por cómo me apoyas y celebras mis victorias.</li>
                <li>✨ Por tu inteligencia, tu fuerza y tu dulzura.</li>
                <li>✨ Simplemente, por ser tú.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# --- SECCIÓN BONITA ---
st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.6); padding: 20px; border-radius: 20px; text-align: center; margin: 30px 0px 20px 0px; box-shadow: 0 4px 15px rgba(255,105,180,0.2);">
        <img src="https://media.tenor.com/ef30B6bU-HMAAAAi/bubu-dudu.gif" width="120" style="margin-bottom: 10px;">
        <h2 style="color: #FF4B4B; font-family: 'Brush Script MT', cursive; font-size: 38px;">Cada instante a tu lado es magia pura ✨</h2>
    </div>
""", unsafe_allow_html=True)

# --- FINAL ---
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if st.button("🎁 ¡TOCA AQUÍ PARA TU GRAN SORPRESA FINAL! 🎁", use_container_width=True):
        st.balloons()
        time.sleep(1)
        st.markdown("""
            <div style="background-color: #ffe4e1; padding: 30px; border-radius: 25px; border: 4px dashed #FF4B4B; text-align: center; box-shadow: 0 0 30px #ffb6c1;">
                <h1 style="color: #FF4B4B; font-size: 40px;">¡TE AMO INFINITO, LUBALOO! ❤️</h1>
                <p style="font-size: 22px; color: #333;">Gracias por hacerme el chico más feliz del mundo. ¡Feliz Cumpleaños, mi vida!</p>
                <p style="font-size: 18px; font-style: italic;">Atte: Justin</p>
            </div>
        """, unsafe_allow_html=True)
        st.toast('¡Eres la mejor! 🎉', icon='😍')
