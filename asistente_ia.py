import streamlit as st
import fitz  # PyMuPDF
import io
import re
from temas import temas

st.set_page_config(page_title="Asistente de Estudio IA", page_icon="📘")
st.title("📘 Asistente de Estudio con IA")
st.markdown("Sube tu archivo PDF para analizar el contenido y generar recursos de estudio.")

# ---- Subir PDF ----
pdf_file = st.file_uploader("📎 Sube tu archivo PDF aquí", type=["pdf"])

# ---- Extraer texto del PDF ----
def extraer_texto_pdf(file):
    texto = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

# ---- Detectar tema según palabras clave ----
def detectar_tema(texto):
    texto = texto.lower()
    if "velocidad constante" in texto and "aceleración" in texto:
        return "MRU"
    # puedes añadir más detecciones como MRUV, MCU, etc.
    return None

if pdf_file:
    texto = extraer_texto_pdf(pdf_file)
    tema = detectar_tema(texto)

    if tema and tema in temas:
        st.success(f"✅ Tema detectado: {tema}")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📄 Resumen"):
                st.subheader("📄 Resumen del Tema")
                st.markdown(temas[tema]["resumen"])

        with col2:
            if st.button("❓ Preguntas"):
                st.subheader("❓ Preguntas de Opción Múltiple")
                for i, p in enumerate(temas[tema]["preguntas"], 1):
                    st.markdown(f"**{i}. {p['pregunta']}**")
                    st.radio("Selecciona una opción:", p["opciones"], key=f"preg{i}")
                    st.markdown(f"✅ Respuesta correcta: **{p['respuesta']}**")

        with col3:
            if st.button("💡 Flashcards"):
                st.subheader("💡 Flashcards")
                for fc in temas[tema]["flashcards"]:
                    with st.expander(fc["concepto"]):
                        st.write(fc["definicion"])
    else:
        st.warning("⚠ No se pudo detectar un tema conocido en el PDF.")
