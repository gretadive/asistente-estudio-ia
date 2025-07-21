import streamlit as st
import fitz  # PyMuPDF
from datetime import datetime
import sys
import os

# Asegurar path del archivo temas si está separado
sys.path.append(os.path.dirname(__file__))

# --- Tus temas aquí (sin cambios, por brevedad, los dejé fuera del bloque) ---

# Configuración inicial
st.set_page_config(page_title="Asistente de Estudio IA", page_icon="📘")
st.title("📘 Asistente de Estudio con IA")

# Crear carpeta para guardar resultados si no existe
os.makedirs("resultados", exist_ok=True)

# 🧑‍🎓 Nombre del estudiante
nombre_estudiante = st.text_input("👤 Ingresa tu nombre:")

# 📎 Subir PDF
pdf_file = st.file_uploader("📎 Sube tu archivo PDF aquí", type=["pdf"])

# -------- FUNCIONES --------
def extraer_texto_pdf(file):
    texto = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

def detectar_tema(texto):
    texto = texto.lower()
    if "mru" in texto or "movimiento rectilíneo uniforme" in texto:
        if "velocidad constante" in texto or "aceleración nula" in texto:
            return "MRU"
    if "mruv" in texto or "movimiento rectilíneo uniformemente variado" in texto:
        if "v = v0 + at" in texto or "aceleración constante" in texto:
            return "MRUV"
    if "caída libre" in texto or "gravedad" in texto or "9.8" in texto or "aceleración gravitatoria" in texto:
        return "Caída Libre"
    return None

# 🔁 CAMBIO: Guardar resultados con respuestas detalladas
def guardar_resultado(nombre, tema, puntaje, total, respuestas):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ruta = "resultados/resultados.txt"
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(f"👤 Nombre: {nombre}\n")
        f.write(f"📅 Fecha: {fecha}\n")
        f.write(f"📚 Tema: {tema}\n")
        f.write(f"🏁 Puntaje: {puntaje} / {total}\n")
        f.write("📋 Detalle de respuestas:\n")
        f.write("-" * 50 + "\n")
        for i, r in enumerate(respuestas, 1):
            estado = "✅ Correcto" if r["correcto"] else "❌ Incorrecto"
            f.write(f"{i}. {r['pregunta']}\n")
            f.write(f"   ➤ Tu respuesta: {r['respuesta_usuario']}\n")
            f.write(f"   ✔ Correcta: {r['respuesta_correcta']} — {estado}\n\n")
        f.write("=" * 50 + "\n\n")

# Inicializar estados
for key in ["mostrar_preguntas", "indice", "puntaje", "respondido", "tema", "respuestas_usuario"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "respuestas_usuario" else []

# -------- PROCESAMIENTO DEL PDF --------
if pdf_file and nombre_estudiante.strip():
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
                st.session_state["respuestas_usuario"] = []  # 🔁 Limpiar respuestas anteriores

    else:
        st.warning("⚠ No se pudo detectar un tema válido en el PDF.")

# -------- PREGUNTAS UNA A UNA --------
if st.session_state["mostrar_preguntas"]:
    preguntas = temas[st.session_state["tema"]]["preguntas"]
    i = st.session_state["indice"]

    if i < len(preguntas):
        p = preguntas[i]
        st.markdown(f"### Pregunta {i + 1}: {p['pregunta']}")
        respuesta_usuario = st.radio("Selecciona una opción:", p["opciones"], key=f"preg{i}")

        if not st.session_state["respondido"]:
            if st.button("Responder"):
                correcta = respuesta_usuario == p["respuesta"]

                # 🔁 Guardar cada respuesta
                st.session_state["respuestas_usuario"].append({
                    "pregunta": p["pregunta"],
                    "respuesta_usuario": respuesta_usuario,
                    "respuesta_correcta": p["respuesta"],
                    "correcto": correcta
                })

                if correcta:
                    st.success("✅ ¡Correcto!")
                    st.session_state["puntaje"] += 1
                else:
                    st.error(f"❌ Incorrecto. Respuesta correcta: {p['respuesta']}")

                st.session_state["respondido"] = True
        else:
            if st.button("➡️ Siguiente"):
                st.session_state["indice"] += 1
                st.session_state["respondido"] = False
                st.rerun()

    else:
        total = len(preguntas)
        puntaje = st.session_state["puntaje"]
        st.success(f"🎉 Has terminado. Tu puntaje: **{puntaje} de {total}**")

        # 🔁 Guardar resultados con respuestas
        guardar_resultado(
            nombre_estudiante.strip(),
            st.session_state["tema"],
            puntaje,
            total,
            st.session_state["respuestas_usuario"]
        )

        st.info("📝 Resultado guardado en `resultados/resultados.txt`.")

        if st.button("🔁 Volver a intentar"):
            for k in ["mostrar_preguntas", "indice", "puntaje", "respondido", "tema", "respuestas_usuario"]:
                st.session_state[k] = None if k != "respuestas_usuario" else []
            st.rerun()
