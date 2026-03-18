from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from deep_translator import GoogleTranslator
import streamlit.components.v1 as components

st.title('Análisis de Sentimiento')

# Lottie animation
lottie_html = """
<script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.3/dist/dotlottie-wc.js" type="module"></script>
<dotlottie-wc src="https://lottie.host/3d7cd9d4-c409-4dcc-8598-2605ccdfadea/h4oQM8hK4O.lottie" style="width: 300px;height: 300px" autoplay loop></dotlottie-wc>
"""
components.html(lottie_html, height=350)

image = Image.open('emoticones.jpg')
st.image(image)
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = GoogleTranslator(source='es', target='en')

with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        trans_text = translator.translate(text)
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x > 0.0 and x <=1.0:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x >=-1 and x <= 0:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

lottie_html = """
<script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.3/dist/dotlottie-wc.js" type="module"></script>
<dotlottie-wc src="https://lottie.host/3aa56635-c331-4118-8f05-96256fe71008/5UZl7vAMBu.lottie" style="width: 300px;height: 300px" autoplay loop></dotlottie-wc>
"""
components.html(lottie_html, height=350)
