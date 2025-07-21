import streamlit as st
import fitz  # PyMuPDF
import csv
import io
from datetime import datetime
from temas import temas

st.set_page_config(page_title="Asistente de Estudio IA", page_icon="📘")
st.title("📘 Asistente de Estudio con IA")

# 🧑‍🎓 Nombre del estudiante
nombre_estudiante = st.text_input("👤 Ingresa tu nombre:")

# 📎 Subir PDF
pdf_file = st.file_uploader("📎 Sube tu archivo PDF aquí", type=["pdf"])

def extraer_texto_pdf(file):
    texto = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

# 🔍 Detectar tema del contenido
def detectar_tema(texto):
    texto = texto.lower()
    if "velocidad constante" in texto and "aceleración nula" in texto:
        return "MRU"
    elif "aceleración constante" in texto and "v = v₀ + at" in texto:
        return "MRUV"
    elif "gravedad" in texto or "caída libre" in texto or "9.8" in texto:
        return "Caída Libre"
    return None

# 📥 Guardar resultados
def guardar_resultado(nombre, tema, puntaje, total):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fila = [nombre, tema, puntaje, total, fecha]
    with open("resultados.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fila)

# 🚀 Procesar archivo PDF
if pdf_file and nombre_estudiante:
    texto = extraer_texto_pdf(pdf_file)
    tema = detectar_tema(texto)

    if tema and tema in temas:
        st.success(f"✅ Tema detectado: {tema}")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📄 Ver Resumen"):
                st.subheader("📄 Resumen del Tema")
                st.markdown(temas[tema]["resumen"])

        with col2:
            if st.button("💡 Ver Flashcards"):
                st.subheader("💡 Flashcards")
                for fc in temas[tema]["flashcards"]:
                    with st.expander(fc["concepto"]):
                        st.write(fc["definicion"])

        with col3:
            if st.button("❓ Empezar Preguntas"):
                st.session_state["mostrar_preguntas"] = True
                st.session_state["indice"] = 0
                st.session_state["puntaje"] = 0
                st.session_state["respondido"] = False
                st.session_state["tema"] = tema

# 💬 Preguntas una por una
if "mostrar_preguntas" in st.session_state and st.session_state["mostrar_preguntas"]:
    preguntas = temas[st.session_state["tema"]]["preguntas"]
    i = st.session_state["indice"]

    if i < len(preguntas):
        p = preguntas[i]
        st.markdown(f"### Pregunta {i + 1}: {p['pregunta']}")
        respuesta_usuario = st.radio("Selecciona una opción:", p["opciones"], key=f"preg{i}")

        if not st.session_state["respondido"]:
            if st.button("Responder"):
                if respuesta_usuario == p["respuesta"]:
                    st.success("✅ ¡Correcto!")
                    st.session_state["puntaje"] += 1
                else:
                    st.error(f"❌ Incorrecto. Respuesta correcta: {p['respuesta']}")
                st.session_state["respondido"] = True
        else:
            if st.button("Siguiente"):
                st.session_state["indice"] += 1
                st.session_state["respondido"] = False
    else:
        total = len(preguntas)
        puntaje = st.session_state["puntaje"]
        st.success(f"🎉 Has terminado. Tu puntaje: **{puntaje} de {total}**")

        # Guardar resultado
        guardar_resultado(nombre_estudiante, st.session_state["tema"], puntaje, total)

        if st.button("Volver a intentar"):
            del st.session_state["mostrar_preguntas"]
            del st.session_state["indice"]
            del st.session_state["puntaje"]
            del st.session_state["respondido"]
