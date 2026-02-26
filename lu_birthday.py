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
        with open(ruta, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded_string}"
    # Si no encuentra tu foto, pondrá un cuadro gris con un mensaje
    return "https://via.placeholder.com/300x400.png?text=Falta+" + ruta

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Fondo degradado romántico */
    .stApp {
        background-image: linear-gradient(to right top, #ffafbd, #ffc3a0, #ffafbd, #d4a5a5);
        background-attachment: fixed;
    }
    
    /* Estilo para los títulos principales */
    .main-title {
        font-family: 'Brush Script MT', cursive; 
        font-size: 60px !important;
        color: #FFFFFF;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
        font-weight: bold;
        padding-bottom: 20px;
    }
    
    /* Estilo para subtítulos */
    .sub-title {
        font-size: 30px !important;
        color: #FFFFFF;
        text-align: center;
        text-shadow: 1px 1px 2px #d4a5a5;
    }
    
    /* Cajas de texto estilo "tarjeta" */
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

    /* Estilo para las fotos tipo Polaroid */
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
    
    /* Personalizar botones */
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

# --- MÚSICA DE FONDO ---
music_file = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 
if os.path.exists("cancion.mp3"): 
    music_file = "cancion.mp3"

st.audio(music_file, format='audio/mp3', start_time=0)
st.caption("🎵 Dale play para un poco de ambiente romántico 🎵")


# --- ENCABEZADO ---
st.markdown('<p class="main-title">¡Feliz Cumpleaños, Mi Reina! 👑🎂</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Hoy el mundo es más bonito porque tú estás en él.</p>', unsafe_allow_html=True)
st.write("---")


# --- ESTRUCTURA DE PESTAÑAS ---
tab1, tab2, tab3 = st.tabs(["🌹 El Inicio", "📸 Nuestros Recuerdos", "💖 ¿Por qué Tú?"])

# --- PESTAÑA 1: EL INICIO ---
with tab1:
    st.markdown("""
        <div class="card-box">
            <h3>Mi amor, mi compañera, mi todo.</h3>
            <p>Parece que fue ayer cuando te conocí, y mira dónde estamos hoy. 
            Celebrar tu cumpleaños no es solo celebrar un año más, es celebrar el regalo 
            que es tenerte en mi vida. Eres la casualidad más bonita que me ha pasado.</p>
        </div>
    """, unsafe_allow_html=True)
    col_gif1, col_gif2, col_gif3 = st.columns([1,2,1])
    with col_gif2:
        st.image("https://media.giphy.com/media/MDJ9IbxxU23l8sEdcK/giphy.gif", use_container_width=True)


# --- PESTAÑA 2: FOTOS TIPO POLAROID ---
with tab2:
    st.markdown('<div class="card-box"><p>Pequeños instantes de una gran historia de amor.</p></div>', unsafe_allow_html=True)
    
    # Aquí es donde se procesan las fotos locales usando la nueva función
    foto_1 = cargar_imagen_local("foto1.jpg")
    foto_2 = cargar_imagen_local("foto2.jpg")
    foto_3 = cargar_imagen_local("foto3.jpg")

    col_p1, col_p2, col_p3 = st.columns(3)
    
    with col_p1:
        st.markdown(f"""
            <div class="polaroid">
                <img src="{foto_1}" style="width:100%; height:auto; aspect-ratio: 3/4; object-fit: cover;">
                <div class="caption_pol">El comienzo de todo ❤️</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_p2:
        st.markdown(f"""
            <div class="polaroid">
                <img src="{foto_2}" style="width:100%; height:auto; aspect-ratio: 3/4; object-fit: cover; transform: rotate(3deg);">
                <div class="caption_pol">Momentos inolvidables ✨</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_p3:
        st.markdown(f"""
            <div class="polaroid">
                <img src="{foto_3}" style="width:100%; height:auto; aspect-ratio: 3/4; object-fit: cover;">
                <div class="caption_pol">Mi vista favorita 😍</div>
            </div>
        """, unsafe_allow_html=True)


# --- PESTAÑA 3: RAZONES ---
with tab3:
    st.markdown("""
        <div class="card-box" style="text-align: left;">
            <h3>👑 5 Razones (de un millón) por las que te amo:</h3>
            <ul>
                <li>✨ Por la forma en que tus ojos brillan cuando sonríes.</li>
                <li>✨ Porque tienes el corazón más noble que conozco.</li>
                <li>✨ Por cómo me apoyas en mis días difíciles y celebras mis victorias.</li>
                <li>✨ Por tu inteligencia, tu fuerza y tu dulzura.</li>
                <li>✨ Simplemente, por ser tú. No cambiaría nada.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


st.write("---")
st.write("")
st.write("")

# --- EL GRAN FINAL ---
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    if st.button("🎁 ¡TOCA AQUÍ PARA TU GRAN SORPRESA FINAL! 🎁", use_container_width=True):
        st.balloons()
        time.sleep(1)
        
        st.markdown("""
            <div style="background-color: #FFD700; padding: 30px; border-radius: 25px; border: 4px dashed #FF4B4B; text-align: center; box-shadow: 0 0 20px #FFD700; margin-top: 20px;">
                <img src="https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif" width="150" style="border-radius: 15px;">
                <h1 style="color: #FF4B4B; font-size: 40px; margin-top: 15px;">¡TE AMO INFINITO, LUBALOO! ❤️</h1>
                <p style="font-size: 22px; color: #333;">Que este nuevo año de vida te traiga salud, sueños cumplidos y que sigamos escribiendo esta historia juntos por muchísimo tiempo más.</p>
                <h2 style="color: #FF4B4B;">Feliz Cumpleaños, mi vida.</h2>
                <p style="font-size: 18px;">Atte: Justin, el chico más afortunado.</p>
            </div>
        """, unsafe_allow_html=True)
        st.toast('¡Eres la mejor! 🎉', icon='😍')
