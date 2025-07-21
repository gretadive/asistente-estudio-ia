import streamlit as st
import fitz  # PyMuPDF
import csv
import io
from datetime import datetime
import sys
import os

# Asegurar path del archivo temas si está separado
sys.path.append(os.path.dirname(__file__))

temas = {
    "MRU": {
        "resumen": """
        - Movimiento con velocidad constante.
        - Aceleración igual a cero.
        - Fórmula: x(t) = x₀ + vt.
        """,
        "flashcards": [
            {"concepto": "Velocidad constante", "definicion": "La velocidad no cambia con el tiempo."},
            {"concepto": "Aceleración nula", "definicion": "No hay cambio en la velocidad del cuerpo."}
        ],
        "preguntas": [
            {
                "pregunta": "¿Qué característica tiene el MRU?",
                "opciones": ["Aceleración constante", "Velocidad constante", "Movimiento circular", "Aceleración variable"],
                "respuesta": "Velocidad constante"
            },
            {
                "pregunta": "¿Cuál es la aceleración en MRU?",
                "opciones": ["9.8 m/s²", "0 m/s²", "10 m/s²", "Depende de la masa"],
                "respuesta": "0 m/s²"
            },
            {
                "pregunta": "¿Cuál es la fórmula principal del MRU?",
                "opciones": ["v = d/t", "x(t) = x₀ + vt", "F = ma", "v = v₀ + at"],
                "respuesta": "x(t) = x₀ + vt"
            },
            {
                "pregunta": "¿Qué tipo de trayectoria tiene el MRU?",
                "opciones": ["Circular", "Rectilínea", "Parabólica", "Elíptica"],
                "respuesta": "Rectilínea"
            },
            {
                "pregunta": "¿Qué sucede si la velocidad es negativa en MRU?",
                "opciones": ["Se detiene", "Cambia de dirección", "Aumenta", "Acelera"],
                "respuesta": "Cambia de dirección"
            }
        ]
    },

    "MRUV": {
        "resumen": """
        - Movimiento con aceleración constante.
        - Fórmulas clave: 
            - v = v₀ + at
            - x = x₀ + v₀t + ½at²
        """,
        "flashcards": [
            {"concepto": "Aceleración constante", "definicion": "El cambio de velocidad por unidad de tiempo es constante."},
            {"concepto": "Velocidad inicial", "definicion": "La velocidad al comenzar el movimiento."}
        ],
        "preguntas": [
            {
                "pregunta": "¿Qué representa la 'a' en MRUV?",
                "opciones": ["Área", "Aceleración", "Altura", "Amplitud"],
                "respuesta": "Aceleración"
            },
            {
                "pregunta": "¿Cuál fórmula se usa en MRUV para calcular posición?",
                "opciones": ["x = vt", "x = x₀ + v₀t + ½at²", "v = d/t", "x = x₀ + vt"],
                "respuesta": "x = x₀ + v₀t + ½at²"
            },
            {
                "pregunta": "¿Qué ocurre si a = 0 en MRUV?",
                "opciones": ["Se convierte en MRU", "No hay movimiento", "Cae libremente", "Acelera más"],
                "respuesta": "Se convierte en MRU"
            },
            {
                "pregunta": "¿Cómo varía la velocidad en MRUV?",
                "opciones": ["Se mantiene constante", "Cambia linealmente", "Cambia aleatoriamente", "No varía"],
                "respuesta": "Cambia linealmente"
            },
            {
                "pregunta": "¿Cuál es la unidad de aceleración?",
                "opciones": ["m/s", "m/s²", "km/h", "m²/s"],
                "respuesta": "m/s²"
            }
        ]
    },

    "Caída Libre": {
        "resumen": """
        - Movimiento vertical bajo influencia de la gravedad.
        - Aceleración constante: g = 9.8 m/s².
        - Fórmulas: 
            - v = gt 
            - y = ½gt²
        """,
        "flashcards": [
            {"concepto": "Gravedad", "definicion": "Fuerza que atrae objetos hacia el centro de la Tierra."},
            {"concepto": "Aceleración de caída libre", "definicion": "9.8 m/s² en la superficie terrestre."}
        ],
        "preguntas": [
            {
                "pregunta": "¿Cuál es el valor de la gravedad en caída libre?",
                "opciones": ["10 m/s²", "8.9 m/s²", "9.8 m/s²", "0 m/s²"],
                "respuesta": "9.8 m/s²"
            },
            {
                "pregunta": "¿Qué dirección tiene la aceleración en caída libre?",
                "opciones": ["Hacia arriba", "Hacia los lados", "Hacia abajo", "Variable"],
                "respuesta": "Hacia abajo"
            },
            {
                "pregunta": "¿Cuál es la fórmula de la velocidad en caída libre?",
                "opciones": ["v = v₀ + at", "v = gt", "v = d/t", "v = √(2gh)"],
                "respuesta": "v = gt"
            },
            {
                "pregunta": "¿Qué tipo de aceleración tiene la caída libre?",
                "opciones": ["Variable", "Negativa", "Nula", "Constante"],
                "respuesta": "Constante"
            },
            {
                "pregunta": "¿Qué pasa con la velocidad al caer?",
                "opciones": ["Disminuye", "Se mantiene", "Aumenta", "Se vuelve cero"],
                "respuesta": "Aumenta"
            }
        ]
    }
}


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
    if "mru" in texto and "aceleración nula" in texto:
        return "MRU"
    elif "mruv" in texto and "v = v₀ + at" in texto:
        return "MRUV"
    elif "caída libre" in texto or "9.8" in texto:
        return "Caída Libre"
    return None

def guardar_resultado(nombre, tema, puntaje, total):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fila = [nombre, tema, puntaje, total, fecha]
    with open("resultados/resultados.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fila)

# Inicializar estado
for key in ["mostrar_preguntas", "indice", "puntaje", "respondido", "tema"]:
    if key not in st.session_state:
        st.session_state[key] = None

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
                if respuesta_usuario == p["respuesta"]:
                    st.success("✅ ¡Correcto!")
                    st.session_state["puntaje"] += 1
                else:
                    st.error(f"❌ Incorrecto. Respuesta correcta: {p['respuesta']}")
                st.session_state["respondido"] = True
        else:
            if st.button("➡️ Siguiente"):
                st.session_state["indice"] += 1
                st.session_state["respondido"] = False
                st.experimental_rerun()

    else:
        total = len(preguntas)
        puntaje = st.session_state["puntaje"]
        st.success(f"🎉 Has terminado. Tu puntaje: **{puntaje} de {total}**")

        # Guardar resultados automáticamente
        guardar_resultado(nombre_estudiante.strip(), st.session_state["tema"], puntaje, total)
        st.info("📝 Resultado guardado en `resultados/resultados.csv`.")

        if st.button("🔁 Volver a intentar"):
            for k in ["mostrar_preguntas", "indice", "puntaje", "respondido", "tema"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.experimental_rerun()
