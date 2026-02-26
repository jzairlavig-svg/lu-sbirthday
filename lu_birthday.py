import streamlit as st
import os
import base64
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Feliz Cumpleaños", layout="wide")

def cargar_imagen(ruta):
    if os.path.exists(ruta):
        with open(ruta, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{data}"
    return ""

# --- ESTILOS CSS PARA LOGRAR EL LOOK DE LA IMAGEN ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #a74c7a 0%, #d66d9b 50%, #f0a1bf 100%);
    }
    .main-card {
        background-color: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        color: #333;
    }
    .side-text {
        color: #444;
        font-size: 18px;
        line-height: 1.6;
    }
    .polaroid {
        background: white;
        padding: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        text-align: center;
        border-radius: 5px;
    }
    .polaroid img {
        width: 100%;
        border-radius: 3px;
    }
    h1 { color: white; text-align: center; font-family: 'Arial'; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown("<h1>¡Feliz Cumpleaños, Mi Reina! ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:20px;'>Hoy el mundo es más bonito contigo en él.</p>", unsafe_allow_html=True)

st.write("---")

# --- DISEÑO DE COLUMNAS (IZQUIERDA: TEXTO Y SNOOPY | DERECHA: CONTENIDO) ---
col_izq, col_espacio, col_der = st.columns([1, 0.1, 2])

with col_izq:
    st.markdown("""
        <div class="main-card">
            <p class="side-text">
                <b>Mi amor, mi compañera, mi todo.</b><br><br>
                Parece que fue ayer cuando te conocí y mira dónde estamos hoy. 
                Celebrar tu cumpleaños no es solo celebrar un año más, es celebrar 
                el regalo que es tenerte en mi vida.<br><br>
                "Eres la casualidad más bonita que me ha pasado."
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Espacio
    
    # SNOOPY EN GRANDE
    snoopy_img = cargar_imagen("snoopy.png")
    if snoopy_img:
        st.markdown(f'<img src="{snoopy_img}" style="width:100%; max-width:350px; display:block; margin:auto;">', unsafe_allow_html=True)
    else:
        st.error("Falta snoopy.png")

with col_der:
    # --- PESTAÑAS DENTRO DE LA COLUMNA DERECHA ---
    tab1, tab2 = st.tabs(["📸 Nuestros Recuerdos", "🌹 ¿Por qué Tú?"])
    
    with tab1:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        fotos = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]
        captions = ["El comienzo de todo ❤️", "Momentos inolvidables ✨", "Mi vista favorita 😍"]
        
        for i, col in enumerate([c1, c2, c3]):
            img_data = cargar_imagen(fotos[i])
            if img_data:
                col.markdown(f"""
                    <div class="polaroid">
                        <img src="{img_data}">
                        <p style="margin-top:10px; font-size:14px; color:#666;">{captions[i]}</p>
                    </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown(f"""
            <div class="main-card">
                <h3 style="color:#d66d9b;">🌹 5 Razones por las que te amo:</h3>
                <ul style="font-size:18px; line-height:2;">
                    <li>✨ Por la forma en que tus ojos brillan al sonreír.</li>
                    <li>✨ Porque tienes el corazón más noble que conozco.</li>
                    <li>✨ Por cómo me apoyas y celebras mis victorias.</li>
                    <li>✨ Por tu inteligencia, tu fuerza y tu dulzura.</li>
                    <li>✨ Simplemente, por ser tú. No cambiaría nada.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

st.write("---")

# --- BOTÓN FINAL ---
_, col_boton, _ = st.columns([1, 2, 1])
with col_boton:
    if st.button("🎁 ¡TOCA AQUÍ PARA TU SORPRESA FINAL! 🎁", use_container_width=True):
        st.balloons()
        st.markdown("""
            <div style="background-color: white; padding: 30px; border-radius: 20px; text-align: center; border: 4px dashed #d66d9b;">
                <h2 style="color: #d66d9b;">¡TE AMO INFINITO! ❤️</h2>
                <p style="font-size:20px;">Eres la persona más increíble del universo. ¡Feliz día!</p>
            </div>
        """, unsafe_allow_html=True)
