temas = {
    "MRU": {
        "resumen": """
**📌 Definición:**  
Movimiento en línea recta con velocidad constante y aceleración nula.

**🧾 Ecuación clave:**  
x(t) = x₀ + vt

**🧠 Características:**
- Velocidad constante
- Trayectoria rectilínea
- Aceleración cero
""",
        "preguntas": [
            {
                "pregunta": "¿Cuál es la característica principal del MRU?",
                "opciones": ["Aceleración constante", "Velocidad variable", "Velocidad constante", "Movimiento circular"],
                "respuesta": "Velocidad constante"
            },
            {
                "pregunta": "¿Cuál es la aceleración en el MRU?",
                "opciones": ["Nula", "Constante", "Variable", "Depende de la masa"],
                "respuesta": "Nula"
            },
            {
                "pregunta": "¿Cuál es la ecuación general del MRU?",
                "opciones": ["x = x₀ + at", "x = x₀ + vt", "x = x₀ + ½at²", "v = v₀ + at"],
                "respuesta": "x = x₀ + vt"
            },
            {
                "pregunta": "En el MRU, ¿cómo es la trayectoria?",
                "opciones": ["Parabólica", "Curva", "Rectilínea", "Oscilatoria"],
                "respuesta": "Rectilínea"
            },
            {
                "pregunta": "¿Qué valor tiene la aceleración en MRU?",
                "opciones": ["Mayor a cero", "Menor a cero", "Cero", "Depende de la velocidad"],
                "respuesta": "Cero"
            }
        ],
        "flashcards": [
            {"concepto": "Velocidad constante", "definicion": "La velocidad no cambia con el tiempo."},
            {"concepto": "Aceleración nula", "definicion": "No hay variación de la velocidad."},
            {"concepto": "Trayectoria recta", "definicion": "El objeto se mueve en línea recta."},
            {"concepto": "Ecuación MRU", "definicion": "x(t) = x₀ + vt"}
        ]
    },

    "MRUV": {
        "resumen": """
**📌 Definición:**  
Movimiento rectilíneo con aceleración constante.

**🧾 Ecuaciones clave:**  
v = v₀ + at  
x = x₀ + v₀t + ½at²  
v² = v₀² + 2a(x - x₀)

**🧠 Características:**
- Velocidad cambia uniformemente
- Aceleración constante
- Movimiento en línea recta
""",
        "preguntas": [
            {
                "pregunta": "¿Cuál es la característica principal del MRUV?",
                "opciones": ["Aceleración nula", "Velocidad constante", "Aceleración constante", "Movimiento circular"],
                "respuesta": "Aceleración constante"
            },
            {
                "pregunta": "¿Qué ecuación relaciona desplazamiento con aceleración en el MRUV?",
                "opciones": ["x = x₀ + vt", "v² = v₀² + 2a(x - x₀)", "F = ma", "x = v/t"],
                "respuesta": "v² = v₀² + 2a(x - x₀)"
            },
            {
                "pregunta": "¿Cuál es la unidad de aceleración en el SI?",
                "opciones": ["m/s", "m²/s²", "m/s²", "kg·m/s²"],
                "respuesta": "m/s²"
            },
            {
                "pregunta": "¿Cómo varía la velocidad en el MRUV?",
                "opciones": ["Es constante", "Cambia uniformemente", "Oscila", "No cambia"],
                "respuesta": "Cambia uniformemente"
            },
            {
                "pregunta": "¿Qué representa 'a' en la fórmula v = v₀ + at?",
                "opciones": ["Velocidad", "Desplazamiento", "Tiempo", "Aceleración"],
                "respuesta": "Aceleración"
            }
        ],
        "flashcards": [
            {"concepto": "Aceleración constante", "definicion": "La aceleración no varía con el tiempo."},
            {"concepto": "v = v₀ + at", "definicion": "Ecuación para velocidad final en MRUV."},
            {"concepto": "x = x₀ + v₀t + ½at²", "definicion": "Ecuación para posición en MRUV."},
            {"concepto": "v² = v₀² + 2a(x - x₀)", "definicion": "Relación entre velocidad y posición."}
        ]
    },

    "Caída Libre": {
        "resumen": """
**📌 Definición:**  
Movimiento vertical bajo la acción de la gravedad (g = 9.8 m/s²), sin considerar la resistencia del aire.

**🧾 Ecuaciones clave (caso especial de MRUV):**  
v = v₀ + gt  
h = v₀t + ½gt²  
v² = v₀² + 2gh

**🧠 Características:**
- Movimiento vertical
- Aceleración constante (gravedad)
- Velocidad aumenta en caída
""",
        "preguntas": [
            {
                "pregunta": "¿Qué valor se usa comúnmente para la gravedad en la Tierra?",
                "opciones": ["10 m/s²", "9.8 m/s", "9.8 m/s²", "8.9 m/s²"],
                "respuesta": "9.8 m/s²"
            },
            {
                "pregunta": "¿Qué tipo de movimiento es la caída libre?",
                "opciones": ["MRU", "MRUV", "Movimiento uniforme", "Movimiento circular"],
                "respuesta": "MRUV"
            },
            {
                "pregunta": "¿Qué pasa con la velocidad durante la caída?",
                "opciones": ["Se mantiene", "Aumenta", "Disminuye", "Oscila"],
                "respuesta": "Aumenta"
            },
            {
                "pregunta": "¿Qué fuerza actúa en la caída libre?",
                "opciones": ["Electromagnética", "Normal", "Gravitatoria", "Centrífuga"],
                "respuesta": "Gravitatoria"
            },
            {
                "pregunta": "¿Cuál es la fórmula para la altura en función del tiempo?",
                "opciones": ["h = v₀t + ½gt²", "h = v₀ + gt", "h = v²/2g", "h = gt²"],
                "respuesta": "h = v₀t + ½gt²"
            }
        ],
        "flashcards": [
            {"concepto": "Gravedad (g)", "definicion": "Aceleración constante de 9.8 m/s² hacia el centro de la Tierra."},
            {"concepto": "Caída libre", "definicion": "Movimiento vertical bajo solo la fuerza de gravedad."},
            {"concepto": "v = v₀ + gt", "definicion": "Velocidad final en caída libre."},
            {"concepto": "h = v₀t + ½gt²", "definicion": "Altura en función del tiempo."}
        ]
    }
}
