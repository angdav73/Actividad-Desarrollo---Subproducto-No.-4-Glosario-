from flask import Flask, render_template

app = Flask(__name__)


# ==============================
# GLOSARIO DE INTELIGENCIA ARTIFICIAL
# ==============================

conceptos = [

    {
        "termino": "Inteligencia Artificial (IA)",
        "categoria": "Fundamentos",
        "definicion": "Es un campo interdisciplinario dedicado al diseño de sistemas capaces de realizar tareas asociadas con la inteligencia humana, como aprender, razonar, reconocer patrones, comprender lenguaje, resolver problemas y tomar decisiones.",
        "ejemplo": "Un asistente virtual que comprende una pregunta, analiza la información y proporciona una respuesta.",
        "fuente": "IBM"
    },

    {
        "termino": "Machine Learning / Aprendizaje automático",
        "categoria": "Machine Learning",
        "definicion": "Consiste en entrenar algoritmos para que puedan realizar predicciones o tomar decisiones basándose en datos, permitiendo que las computadoras aprendan sin estar programadas explícitamente para cada tarea.",
        "ejemplo": "Un sistema que aprende a identificar si un correo electrónico es spam analizando miles de mensajes.",
        "fuente": "IBM"
    },

    {
        "termino": "Aprendizaje profundo (Deep Learning)",
        "categoria": "Machine Learning",
        "definicion": "Subconjunto del machine learning que utiliza redes neuronales con múltiples capas para procesar datos y realizar tareas complejas.",
        "ejemplo": "Un sistema que reconoce rostros en fotografías utilizando una red neuronal profunda.",
        "fuente": "IBM"
    },

    {
        "termino": "Red neuronal",
        "categoria": "Machine Learning",
        "definicion": "Modelo de machine learning compuesto por capas de nodos interconectados que procesan datos y permiten identificar patrones y relaciones complejas.",
        "ejemplo": "Una red neuronal puede analizar imágenes para identificar si contienen un automóvil.",
        "fuente": "IBM"
    },

    {
        "termino": "Aprendizaje supervisado",
        "categoria": "Machine Learning",
        "definicion": "Técnica de machine learning que utiliza conjuntos de datos etiquetados para entrenar algoritmos capaces de clasificar información o predecir resultados.",
        "ejemplo": "Entrenar un sistema utilizando fotografías previamente etiquetadas como perro o gato.",
        "fuente": "IBM"
    },

    {
        "termino": "Aprendizaje no supervisado",
        "categoria": "Machine Learning",
        "definicion": "Forma de aprendizaje en la que los sistemas pueden trabajar con grandes cantidades de datos no etiquetados y extraer características o patrones para realizar predicciones.",
        "ejemplo": "Agrupar clientes de una tienda según sus hábitos de compra sin proporcionar categorías previamente.",
        "fuente": "IBM"
    },

    {
        "termino": "Procesamiento de Lenguaje Natural (PLN)",
        "categoria": "IA Generativa",
        "definicion": "Área que permite a las computadoras comprender y comunicarse mediante el lenguaje humano. IBM lo relaciona con el machine learning y el aprendizaje profundo.",
        "ejemplo": "Un chatbot que comprende una pregunta escrita por una persona y responde utilizando lenguaje natural.",
        "fuente": "IBM"
    },

    {
        "termino": "IA generativa",
        "categoria": "IA Generativa",
        "definicion": "Tipo de inteligencia artificial capaz de crear contenido original, como texto, imágenes, video o audio, a partir de instrucciones o solicitudes del usuario.",
        "ejemplo": "Una herramienta que genera una imagen a partir de una descripción escrita.",
        "fuente": "IBM"
    },

    {
        "termino": "Modelo fundacional",
        "categoria": "IA Generativa",
        "definicion": "Modelo de aprendizaje profundo que sirve como base para desarrollar diferentes aplicaciones de IA generativa.",
        "ejemplo": "Un modelo entrenado con grandes cantidades de información que posteriormente puede adaptarse para diferentes aplicaciones.",
        "fuente": "IBM"
    },

    {
        "termino": "Modelo de lenguaje grande (LLM)",
        "categoria": "IA Generativa",
        "definicion": "Modelo fundacional utilizado principalmente para aplicaciones de generación de texto y entrenado con grandes cantidades de datos.",
        "ejemplo": "Un modelo que genera respuestas, resume documentos o ayuda a redactar textos.",
        "fuente": "IBM"
    },

    {
        "termino": "Agente de IA",
        "categoria": "Agentes",
        "definicion": "Programa de IA autónomo que puede realizar tareas y alcanzar objetivos en nombre de un usuario o sistema, utilizando herramientas y diseñando su propio flujo de trabajo.",
        "ejemplo": "Un agente que organiza información, utiliza herramientas y completa una tarea siguiendo un objetivo.",
        "fuente": "IBM"
    },

    {
        "termino": "IA agéntica",
        "categoria": "Agentes",
        "definicion": "Sistema compuesto por múltiples agentes de IA cuyos esfuerzos son coordinados para conseguir tareas complejas u objetivos mayores.",
        "ejemplo": "Varios agentes especializados que colaboran para investigar, analizar información y elaborar un resultado.",
        "fuente": "IBM"
    },

    {
        "termino": "Agente inteligente",
        "categoria": "Agentes",
        "definicion": "Entidad capaz de percibir su entorno mediante sensores y actuar sobre él. Puede percibir su ambiente y actuar mediante efectores o actuadores.",
        "ejemplo": "Un robot que utiliza sensores para detectar obstáculos y modificar su movimiento.",
        "fuente": "Libro de Inteligencia Artificial"
    },

    {
        "termino": "Sistemas expertos",
        "categoria": "Fundamentos",
        "definicion": "Sistemas de IA orientados a resolver problemas específicos utilizando conocimiento especializado. Utilizan una base de conocimientos y un motor de inferencia.",
        "ejemplo": "Un sistema que utiliza conocimiento médico para ayudar a analizar determinados síntomas.",
        "fuente": "Libro de Inteligencia Artificial"
    },

    {
        "termino": "Algoritmos evolutivos",
        "categoria": "Algoritmos",
        "definicion": "Algoritmos basados en procesos de evolución que pueden darse a nivel de individuos o poblaciones, tomando inspiración de procesos biológicos o culturales.",
        "ejemplo": "Un algoritmo que mejora progresivamente diferentes soluciones de un problema mediante procesos inspirados en la evolución.",
        "fuente": "Libro de Inteligencia Artificial"
    },

    {
        "termino": "Algoritmos genéticos",
        "categoria": "Algoritmos",
        "definicion": "Técnicas de Inteligencia Artificial que realizan búsquedas inspiradas en la herencia genética y en el principio de supervivencia de los individuos más aptos. Trabajan sobre una población de posibles soluciones.",
        "ejemplo": "Encontrar una combinación óptima de variables mediante selección, cruza y mutación.",
        "fuente": "Libro de Inteligencia Artificial"
    },

    {
        "termino": "Minería de datos",
        "categoria": "Datos",
        "definicion": "Es la aplicación del aprendizaje automático sobre grandes volúmenes de datos con el objetivo de extraer información útil.",
        "ejemplo": "Analizar las compras de los clientes para encontrar patrones de consumo.",
        "fuente": "Libro de Inteligencia Artificial"
    },

    {
        "termino": "Sistemas multiagentes",
        "categoria": "Agentes",
        "definicion": "Son sistemas formados por múltiples agentes autónomos que tienen diferentes funciones y pueden interactuar entre ellos y con su entorno.",
        "ejemplo": "Varios agentes que cooperan para resolver diferentes partes de un problema complejo.",
        "fuente": "Libro de Inteligencia Artificial"
    },

    {
        "termino": "Lógica difusa",
        "categoria": "Fundamentos",
        "definicion": "Es un área de la Inteligencia Artificial que permite trabajar con situaciones en las que los valores no necesariamente se representan únicamente como verdaderos o falsos.",
        "ejemplo": "Un sistema de temperatura que puede considerar que una habitación está parcialmente caliente en lugar de clasificarla solamente como caliente o fría.",
        "fuente": "Libro de Inteligencia Artificial"
    },

    {
        "termino": "Programación lógica",
        "categoria": "Fundamentos",
        "definicion": "Es un enfoque de programación relacionado con la representación del conocimiento mediante lógica, hechos y reglas. Prolog está orientado a problemas relacionados con el cálculo de predicados y las deducciones.",
        "ejemplo": "Utilizar hechos y reglas para que un programa pueda realizar deducciones sobre determinada información.",
        "fuente": "Libro de Inteligencia Artificial"
    }

]


# ==============================
# PÁGINA PRINCIPAL
# ==============================

@app.route("/")
def inicio():

    return render_template(
        "index.html",
        conceptos=conceptos
    )


# ==============================
# INICIAR APLICACIÓN
# ==============================

if __name__ == "__main__":
    app.run(debug=True)