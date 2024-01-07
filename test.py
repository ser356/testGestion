from random import sample, shuffle
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ListProperty
from kivy.clock import Clock

# Colores en formato RGBA
color_fondo = [0.95, 0.95, 0.95, 1]  # Fondo claro
color_texto = [0.0, 0.0, 0.0, 1]  # Texto oscuro suave
color_correcto = [0.33, 0.66, 0.41, 1]  # Verde suave
color_incorrecto = [0.76, 0.33, 0.33, 1]


class TestApp(App):
    question_color = ListProperty([1, 1, 1, 1])  # Color blanco por defecto

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.index = 0  # Inicializar índice de pregunta actual
        self.score = 0  # Inicializar puntaje
        self.fallo = 0
        self.puntuacion = 0

    def build(self):

        self.title = "Test de Gestión de Proyectos"
        self.root = BoxLayout(orientation="vertical")
        self.start_test()
        return self.root

    def start_test(self):
       
        # ... tus definiciones previas de 'questions', 'options', 'correct_answers'
        self.questions = [
            "¿Qué permite la medición de aspectos del proceso de software?",
            "¿Qué método de estimación se basa en la experiencia de proyectos anteriores para realizar estimaciones?",
            "¿Cuál es la principal entrada en los modelos de coste?",
            "¿Qué modelo de estimación utiliza curvas de Rayleigh?",
            "¿Qué tipo de pronóstico utiliza modelos donde la información del pasado se utiliza para predecir el desempeño futuro?",
            "¿Qué mide el Valor Ganado (EV) en el análisis del valor ganado?",
            "En la gestión de riesgos, ¿cómo se categoriza un riesgo que puede ser identificado por adelantado basándose en la experiencia previa?",
            "¿Qué aspecto NO es considerado en la medición del Error Relativo Medio (RRM) en la evaluación de la exactitud de la estimación?",
            "¿Qué indica el 'cono de incertidumbre' en la estimación de proyectos?",
            "En el método de la curva de aprendizaje, ¿qué supone el aprendizaje constante?",
            "¿Qué metodología de estimación utiliza como base la función de densidad de probabilidad para el tiempo de finalización?",
            "¿Cuál es la principal ventaja de expresar las estimaciones como un rango en lugar de un número simple?",
            "¿Qué representa la mediana en el contexto de las estimaciones de proyectos?",
            "¿Cómo se denomina el proceso de comparar los valores reales con los valores estimados para evaluar la exactitud de las estimaciones?",
            "¿Qué medida se utiliza para evaluar la calidad de la predicción en un conjunto de proyectos?",
            "¿Qué representa el factor de calidad de la estimación en la gestión de proyectos?",
            "¿Cómo afecta el 'cono de incertidumbre' a la estimación de recursos en un proyecto?",
            "¿Qué tipo de técnica de estimación se basa en descomponer el proyecto en componentes más pequeños?",
            "¿En qué se diferencia el modelo COCOMO 2.0 del modelo COCOMO original?",
            "¿Qué tipo de análisis se utiliza para determinar todas las posibles causas de un problema en la gestión de proyectos?",
            "¿Qué técnica de estimación implica comparar el proyecto actual con proyectos pasados?",
            "¿En qué se basa el método de la curva de aprendizaje para estimar el esfuerzo?",
            "¿Qué indica un valor alto en la métrica de Magnitud del Error Relativo (MRE) en la estimación de proyectos?",
            "¿Cuál es el propósito de reestimar frecuentemente en la gestión de proyectos?",
            "¿Qué representa el 'Presupuesto hasta la conclusión' (BAC) en el análisis del valor ganado?",
            "¿Qué mide la Estimación hasta la conclusión (ETC) en el análisis del valor ganado?",
            "¿Cómo afecta el tamaño del proyecto al modelo COCOMO?",
            "¿Cuál es el principal riesgo asociado a la gestión inexacta de estimaciones en un proyecto?",
            "¿Qué enfoque de estimación utiliza el método Delphi?",
            "¿Cómo se utiliza el análisis de regresión en la estimación de costes de proyectos?",
            "¿Cuál es el principal desafío al estimar costes en las primeras etapas de un proyecto?",
            "¿Cómo influye la complejidad del software en el modelo COCOMO?",
            "¿Qué método se utiliza para estimar el esfuerzo necesario para el entrenamiento del personal en el método de la curva de aprendizaje?",
            "¿Qué se debe hacer cuando una estimación de proyecto resulta ser inexacta?",
            "¿Qué indicador se utiliza para medir el rendimiento del costo en el análisis del valor ganado?",
            "¿Cómo se calcula la Estimación a la Conclusión (EAC) en la gestión de proyectos?",
            "¿Qué representa una alta probabilidad en la gestión de riesgos de un proyecto?",
            "¿Cómo afectan los cambios en el alcance del proyecto a las estimaciones?",
            "¿Cuál es el propósito de las revisiones técnicas en la gestión de proyectos?",
            "¿Qué enfoque de estimación utiliza datos históricos para predecir el esfuerzo futuro?",
            "¿Qué mide el Factor de Acoplamiento (FA) en las métricas MOOD para sistemas orientados a objetos?",
            "En el contexto de las métricas para sistemas orientados a objetos, ¿qué representa el número ciclomático según McCabe?",
            "¿Qué indica una alta Proporción de Métodos Ocultos (PMO) en las métricas MOOD para sistemas orientados a objetos?",
            "Según las métricas de Lorenz y Kidd para sistemas orientados a objetos, ¿qué mide el Índice de Especialización (IE)?",
            "¿Cuál es el objetivo principal de medir la productividad en la gestión de proyectos de software?",
            "En las métricas MOOD, ¿qué mide la Proporción de Atributos Ocultos (PAO)?",
            "Según el modelo COCOMO, ¿qué factor influye en la estimación del esfuerzo de un proyecto de software?",
            "¿Qué representa la métrica 'Complejidad Ciclomática' en el análisis de software?",
            "En el contexto de la medición de la usabilidad de aplicaciones web, ¿qué indica una alta eficiencia relativa del usuario?",
            "¿Cuál es el propósito de medir la densidad de defectos en un producto de software?",
            "¿Qué mide el número de hijos (NH) en el conjunto de métricas CK para sistemas orientados a objetos?",
            "En las métricas orientadas a clases, ¿qué indica un alto valor en la métrica de falta de cohesión (MFC)?",
            "En el modelo de calidad del producto ISO/IEC 25000, ¿qué atributo de calidad se asocia con la 'Fiabilidad'?",
            "¿Cuál es la finalidad de medir el Factor de Polimorfismo (FP) en las métricas MOOD para sistemas orientados a objetos?",
            "Según las métricas de Lorenz y Kidd, ¿qué mide el Número de Operaciones Invalidadas por una Subclase (NOI)?",
            "¿Qué representa la métrica 'Profundidad del Anidamiento (α)' en el análisis de software?",
            "En la gestión de proyectos de software, ¿qué se busca evaluar con la métrica 'Esfuerzo Productivo'?",
            "¿Cuál es el objetivo de medir la 'Deuda Técnica' en un proyecto de software?",
            "¿Qué evalúa la métrica 'Complejidad Esencial' de McCabe en el software?",
            "¿Qué evalúa la métrica 'Número de Dependencias In (NdepIn)' en las métricas para diagramas UML de Marchesi?",
            "¿Qué indica un alto valor en la métrica de 'Fan-in' en el diseño arquitectónico de sistemas orientados a objetos?",
            "¿Qué mide la 'Efectividad de las Tareas' en la medición de usabilidad de aplicaciones web?",
            "En la gestión de proyectos de software, ¿cuál es el propósito de medir la 'Eficacia Temporal'?",
            "¿Qué evalúa la métrica 'Número de Clases Clave' (NCC) en proyectos orientados a objetos según Lorenz y Kidd?",
            "¿Cuál es la finalidad de la métrica 'Índice de Madurez del Software' según IEEE Std. 982.1?",
            "¿Qué mide el 'Factor de Reutilización de Métodos' (FRM) en las métricas MOOD para sistemas orientados a objetos?",
            "En el modelo COCOMO II, ¿cuál es el propósito de la 'Escala de Precisión de Estimación' (EPE)?",
            "¿Qué aspecto evalúa la métrica 'Tiempo de Respuesta Promedio' en la usabilidad de aplicaciones web?",
            "En el ámbito de las métricas de diseño arquitectónico, ¿qué representa el 'Número de Relaciones de Uso' (NRU)?",
            "¿Cuál es el propósito de la métrica 'Índice de Satisfacción del Usuario' en la evaluación de software?",
            "¿Qué indica un alto valor en la métrica de 'Fan-in' en el diseño arquitectónico de sistemas orientados a objetos?",
            "¿Qué mide la 'Efectividad de las Tareas' en la medición de usabilidad de aplicaciones web?",
            "En la gestión de proyectos de software, ¿cuál es el propósito de medir la 'Eficacia Temporal'?",
            "¿Qué evalúa la métrica 'Número de Clases Clave' (NCC) en proyectos orientados a objetos según Lorenz y Kidd?",
            "¿Cuál es la finalidad de la métrica 'Índice de Madurez del Software' según IEEE Std. 982.1?",
            "¿Qué mide el 'Factor de Reutilización de Métodos' (FRM) en las métricas MOOD para sistemas orientados a objetos?",
            "En el modelo COCOMO II, ¿cuál es el propósito de la 'Escala de Precisión de Estimación' (EPE)?",
            "¿Qué aspecto evalúa la métrica 'Tiempo de Respuesta Promedio' en la usabilidad de aplicaciones web?",
            "En el ámbito de las métricas de diseño arquitectónico, ¿qué representa el 'Número de Relaciones de Uso' (NRU)?",
            "¿Cuál es el propósito de la métrica 'Índice de Satisfacción del Usuario' en la evaluación de software?",
            "¿Qué representa la métrica 'Profundidad del Anidamiento (α)' en el análisis de software?",
            "En la gestión de proyectos de software, ¿qué se busca evaluar con la métrica 'Esfuerzo Productivo'?",
            "¿Cuál es el objetivo de medir la 'Deuda Técnica' en un proyecto de software?",
            "¿Qué evalúa la métrica 'Complejidad Esencial' de McCabe en el software?",
            "¿Qué evalúa la métrica 'Número de Dependencias In (NdepIn)' en las métricas para diagramas UML de Marchesi?",
            "¿Qué evalúa el 'Número Medio de Parámetros por Operación' en las métricas orientadas a operaciones para sistemas orientados a objetos?",
            "¿Qué indica una alta medida en la métrica 'Número de Partes Directas' (NODP) en la agregación orientada a objetos?",
            "En las métricas MOOD, ¿cuál es la finalidad de medir la 'Proporción de Atributos Ocultos' (PAO)?",
            "¿Qué mide la 'Complejidad de Datos' en las métricas de diseño arquitectónico para sistemas orientados a objetos?",
            "¿Cuál es la función de las métricas 'NAC' y 'NAP' en las métricas de Genero et al. para diagramas UML?",
            "¿Cuál es la función principal de los indicadores de proceso en la medición del software?",
            "En el contexto de la medición del software, ¿qué papel juegan los indicadores de proyecto?",
            "¿Qué es un modelo en el marco de las medidas y modelos en la ingeniería del software?",
            "De acuerdo con Fenton y Pfleeger (1997), ¿qué define el proceso de medición en el desarrollo de software?",
            "¿Qué tipo de escala clasifica las entidades medidas en categorías sin un orden inherente?",
            "Según McGarry et al. (2002), ¿cuál es un componente clave en la planificación de las mediciones?",
            "En la ejecución de las mediciones, ¿qué proceso se implica según el contexto de medición del software?",
            "¿Qué asegura el establecimiento y mantenimiento de un compromiso en el proceso de medición del software?",
            "¿Qué caracteriza la evaluación periódica de las mediciones en la ingeniería del software?",
            "En el contexto de las medidas y modelos, ¿qué característica tiene la escala absoluta?",
            "¿Qué peligro en las mediciones describe el efecto de que el acto de medir puede influir en el comportamiento?",
            "¿Cómo se define una métrica de vanidad en el proceso de medición?",
            "En términos de mediciones directas e indirectas, ¿qué no implica una medida directa?",
            "En el marco del proceso de medición, ¿qué actividad se relaciona con la captura y visualización de los datos de forma apropiada?",
            "De las propiedades de las medidas, ¿cuál asegura que la recogida se haga según las reglas exactas de la definición o de la métrica?",
            "¿Qué aspecto de las métricas del software se asocia con la clasificación de atributos internos?",
            "¿Qué dimensión de las métricas del software incluye entidades como productos y procesos?",
            "¿Qué indica una medida correcta en el contexto de la clasificación de las métricas del software?",
            "¿Qué métrica de medición de software se enfoca en la identificación y seguimiento del progreso de los riesgos a lo largo del proyecto?",
            "¿Cuál es el propósito principal de la métrica de 'complejidad ciclomática' en el contexto de la medición del software?",
            "¿Qué indica una alta métrica de 'deuda técnica' en la gestión de proyectos de software?",
            "¿Cómo se relaciona la 'efectividad de las tareas' en la medición de usabilidad de aplicaciones web con la experiencia general del usuario?",
            "En la estimación de riesgos en gestión de proyectos, ¿qué métrica se utiliza para priorizar los riesgos basados en su impacto y probabilidad?",
            "¿Qué métrica de diseño arquitectónico mide la utilización de un módulo por otros módulos en un sistema orientado a objetos?",
            "¿Cuál es el objetivo de la métrica 'número medio de parámetros por operación' en las métricas orientadas a operaciones?",
            "En la gestión de proyectos de software, ¿qué evalúa la métrica 'variabilidad de los requisitos'?",
            "¿Cómo afecta la métrica 'fan-in' en el diseño arquitectónico de sistemas orientados a objetos a la mantenibilidad del software?",
            "¿Qué aspecto del modelo de calidad ISO/IEC 25000 se evalúa con el criterio de 'completitud' en la 'adecuación funcional'?",
            "¿Qué representa la métrica 'Altura de Agregación (HAgg)' en un diagrama UML de agregación?",
            "¿Cómo se define la 'Número de Partes (NP)' en el contexto de métricas UML según Genero et al.?",
            "¿Cuál es la diferencia entre 'Número de Asociaciones de una Clase (NAC)' y 'Número de Asociaciones en un Paquete (NAP)'?",
            "¿Qué mide la métrica 'Número de Dependencias In (NDepIn)' en las métricas de dependencia UML?",
            "¿En las métricas de Marchesi, cómo se define 'CL1' y qué representa?",
            "¿Qué representa la métrica 'Número de guiones de escenario (NGE)' según Lorenz y Kidd?",
            "¿Qué métrica de Binder 1994 mide el número de clases que pueden acceder a atributos de otras clases?",
            "¿Qué se evalúa cuantitativamente según el PMI en el proceso de estimación de un proyecto?",
            "¿Cuál es el propósito principal de la estimación en proyectos según la diapositiva presentada?",
            "Según la diapositiva, ¿qué permite realizar la medición de determinados aspectos del proceso de software?",
            "¿Qué indica la precisión en el contexto de medidas o estimaciones?",
            "¿Qué representa la exactitud en el contexto de medidas o estimaciones?",
            "En la estimación del tiempo necesario para finalizar un proyecto, ¿qué determina la función de densidad de probabilidad representada en la diapositiva?",
            "Según la diapositiva de evaluación de estimación, ¿cómo se calcula el Error relativo medio (R̅E)?",
            "¿Qué factores se consideran al aplicar la cantidad correcta de recursos para la estimación de proyectos?",
            "¿Qué aspecto NO es un factor que afecta la precisión requerida de la estimación?",
            "¿Cuál es la principal diferencia entre las estimaciones preliminares y las más detalladas en la estimación de costes?",
            "¿Qué técnica de estimación se basa en la comparación del proyecto propuesto con proyectos anteriores?",
            "¿En qué se basa el método de la curva de aprendizaje para determinar el tiempo de producción?",
            "Según la diapositiva sobre el Modelo 1 de la curva de aprendizaje, ¿cómo se calcula el tiempo total necesario para realizar todas las operaciones?",
            "¿Qué diferencia principal existe entre los modelos de coste y los modelos restrictivos en la clasificación proporcionada?",
            "¿Qué técnica de estimación propusieron Bailey y Basili para obtener un modelo de coste a partir de sus propios datos?",
            "En el modelo COCOMO original, ¿qué tipos de proyectos se definen para el modo orgánico?",
            "¿Qué es el 'Delivered Source Instructions (DSI)' en el contexto del modelo COCOMO original básico?",
            "Según el Modelo COCOMO original II, ¿cómo se calcula el esfuerzo en el modelo intermedio?",
            "En el modelo COCOMO original II para la duración del proyecto, ¿qué representa la 'a' en la ecuación D = a (E)^b?",
            "¿Qué se introduce en el Modelo COCOMO 2.0 para la etapa de diseño inicial?",
            "Dentro del Modelo COCOMO 2.0, ¿qué representa la estimación del esfuerzo de desarrollo basada en las líneas de código fuente (SLOC)?",
            "¿Qué caracteriza al modelo SLIM desarrollado por Putnam para la estimación de esfuerzo en proyectos de software?",
            "En el modelo SLIM de Putnam, ¿cómo se relaciona el tamaño del software con el esfuerzo total y el tiempo de finalización?",
            "¿Qué se estima utilizando Use Case Points (UCP) en el contexto de la gestión de proyectos?",
            "Según la gráfica proporcionada, ¿cómo varía el esfuerzo por tamaño de Caso de Uso (CU) en diferentes tipos de proyectos?",
            "¿Qué es un Punto de Historia (PH) en las estimaciones basadas en Puntos de Historia?",
            "¿Cómo utilizan los modelos de minería de datos los algoritmos de aprendizaje automático para la estimación de proyectos?",
            "En el contexto de la minería de datos, ¿qué representan los árboles de decisión para la estimación del tamaño del software?",
            "¿Qué tipo de lista se recomienda crear durante la Identificación de Riesgos?",
            "¿Qué dos aspectos se cuantifican en el Análisis de Riesgos?",
            "En la clasificación de riesgos, ¿qué indica un impacto 'Crítico'?",
            "¿Cómo se calcula la Exposición al Riesgo según Känsälä, 1997?",
            "¿Qué estrategia de gestión de riesgos implica aceptar un riesgo y sus posibles consecuencias?",
            "¿Cuál es el objetivo principal de la monitorización de riesgos?",
            "¿Qué acción se requiere cuando un riesgo excede el valor umbral durante la monitorización?",
            "¿Qué se debe establecer primero en el proceso de Priorización de Riesgos?",
            "¿Qué opción NO es una estrategia de Planificación de la gestión de riesgos?",
            "¿Qué técnica utiliza un mazo de cartas con la numeración de la sucesión de Fibonacci para la estimación de riesgos?",
            "¿Qué metodología no se menciona en la lista de chequeo para la Identificación de Riesgos?",
            "¿Qué atributo no es considerado en la clasificación de riesgos?",
            "¿Qué factor no forma parte de la fórmula de exposición al riesgo propuesta por Känsälä?",
            "En el contexto de gestión de riesgos, ¿qué no se considera parte de la planificación?",
            "¿Qué elemento no es parte del proceso de Resolución de riesgos?",
            "¿Qué acción no está incluida en las opciones de respuesta ante un riesgo identificado en el proceso de Control de riesgos?",
            "¿Cuál de los siguientes no es un paso en el proceso de Monitorización de riesgos?",
            "¿Qué no se debe hacer al Priorizar riesgos según su impacto?",
            "¿Qué estrategia no es parte del Control de riesgos?",
            "¿Cuál de las siguientes no es una técnica de estimación de riesgos?",
        ]

        self.options = [
            [
                "a) Mejorar la interfaz de usuario",
                "b) Predecir fases futuras del proyecto",
                "c) Reducir la cantidad de personal necesario",
            ],
            ["a) Descomposición", "b) Opinión de expertos", "c) Analogía"],
            [
                "a) Número de empleados",
                "b) Medida del tamaño del producto",
                "c) Duración del proyecto",
            ],
            [
                "a) Modelo SLIM",
                "b) Modelo COCOMO",
                "c) Estimaciones basadas en Casos de Uso",
            ],
            [
                "a) Pronósticos cualitativos",
                "b) Pronósticos causales",
                "c) Pronósticos cuantitativos",
            ],
            [
                "a) El costo total previsto del proyecto",
                "b) El valor del trabajo realizado hasta la fecha",
                "c) El costo real del trabajo realizado hasta la fecha",
            ],
            ["a) Riesgo impredecible", "b) Riesgo conocido", "c) Riesgo predecible"],
            ["a) Valor real", "b) Valor estimado", "c) Duración del proyecto"],
            [
                "a) La disminución del riesgo a lo largo del tiempo",
                "b) El aumento de la precisión de las estimaciones con el tiempo",
                "c) La variabilidad de los costes del proyecto",
            ],
            [
                "a) Un incremento constante en la eficiencia",
                "b) Una disminución constante en el esfuerzo",
                "c) Un cambio constante en los recursos del proyecto",
            ],
            [
                "a) Modelo SLIM",
                "b) Estimación del tamaño",
                "c) Análisis del valor ganado",
            ],
            [
                "a) Mayor precisión",
                "b) Mejor gestión del riesgo",
                "c) Reducción de costes",
            ],
            [
                "a) El valor más probable",
                "b) El límite superior de la estimación",
                "c) El costo total del proyecto",
            ],
            [
                "a) Análisis de varianza",
                "b) Evaluación de la exactitud",
                "c) Error relativo medio",
            ],
            [
                "a) Magnitud media del error relativo",
                "b) Calidad de la predicción",
                "c) Factor de la calidad de la estimación",
            ],
            [
                "a) La eficiencia del proceso de estimación",
                "b) La fiabilidad de la información usada",
                "c) El riesgo inherente al proyecto",
            ],
            [
                "a) Aumenta la precisión con el tiempo",
                "b) Disminuye el riesgo a medida que avanza el proyecto",
                "c) Reduce la necesidad de reestimar",
            ],
            ["a) Opinión de expertos", "b) Descomposición", "c) Modelos empíricos"],
            [
                "a) Diferente enfoque en la medición del tamaño",
                "b) Variación en los factores de ajuste",
                "c) Cambios en la estructura del modelo",
            ],
            [
                "a) Diagrama de Ishikawa",
                "b) Análisis de Pareto",
                "c) Diagrama de Gantt",
            ],
            ["a) Descomposición", "b) Analogía", "c) Modelo COCOMO"],
            [
                "a) Repetición de operaciones",
                "b) Eficiencia del equipo",
                "c) Tiempo de desarrollo",
            ],
            [
                "a) Estimaciones precisas",
                "b) Estimaciones inexactas",
                "c) Proyecto bien gestionado",
            ],
            [
                "a) Mejorar la comunicación",
                "b) Ajustar los recursos",
                "c) Aumentar la precisión de las estimaciones",
            ],
            [
                "a) Coste previsto para terminar el trabajo",
                "b) Coste total previsto para el proyecto",
                "c) Valor del trabajo ya realizado",
            ],
            [
                "a) Coste previsto para terminar el trabajo restante",
                "b) Coste total estimado al final del proyecto",
                "c) Coste actual del trabajo realizado",
            ],
            [
                "a) Cambia los factores de ajuste",
                "b) Afecta la duración estimada",
                "c) Modifica la ecuación de esfuerzo",
            ],
            [
                "a) Sobrecostos",
                "b) Retrasos en el cronograma",
                "c) Disminución de la calidad",
            ],
            [
                "a) Comparación con estándares",
                "b) Consenso de expertos",
                "c) Análisis histórico",
            ],
            [
                "a) Identificar factores clave",
                "b) Crear una ecuación matemática",
                "c) Ajustar el tamaño del proyecto",
            ],
            [
                "a) Definir el alcance del proyecto",
                "b) Limitada información disponible",
                "c) Variabilidad en los requisitos del cliente",
            ],
            [
                "a) Aumenta el factor de escala",
                "b) Reduce el esfuerzo total",
                "c) No tiene efecto",
            ],
            [
                "a) Aprendizaje constante",
                "b) Aprendizaje acelerado",
                "c) Modelos matemáticos",
            ],
            [
                "a) Continuar con la misma estimación",
                "b) Ajustar la estimación",
                "c) Comenzar un nuevo proyecto",
            ],
            [
                "a) Valor Ganado (EV)",
                "b) Índice de Desempeño del Costo (CPI)",
                "c) Costo Real del Trabajo Realizado (ACWP)",
            ],
            [
                "a) Suma de AC y ETC",
                "b) BAC dividido por CPI",
                "c) AC más BAC menos EV",
            ],
            ["a) Riesgo bajo", "b) Riesgo medio", "c) Riesgo alto"],
            ["a) No afectan", "b) Reducen la precisión", "c) Aumentan el costo"],
            [
                "a) Evaluar la calidad del software",
                "b) Planificar el cronograma",
                "c) Revisar los requisitos",
            ],
            ["a) Analogía", "b) Modelos empíricos", "c) Estimación delphi"],
            [
                "a) La proporción de métodos ocultos en el sistema",
                "b) La proporción entre el máximo número posible de acoplamientos en el sistema y el número real de acoplamientos no imputables a la herencia",
                "c) El número de métodos heredados redefinidos en el sistema",
            ],
            [
                "a) La cantidad de recursos requeridos para una solución óptima de un problema",
                "b) El número de caminos linealmente independientes en el grafo de flujo de un programa",
                "c) La medida del tamaño físico del producto de software",
            ],
            [
                "a) Un bajo nivel de encapsulamiento en el sistema",
                "b) Una alta complejidad en el sistema",
                "c) Un alto nivel de encapsulamiento en el sistema",
            ],
            [
                "a) La cantidad de operaciones invalidadas por una subclase",
                "b) El número de operaciones añadidas por una subclase",
                "c) La calidad de la herencia en función del número de métodos heredados redefinidos y el nivel de la clase en la jerarquía",
            ],
            [
                "a) Evaluar el costo total del proyecto",
                "b) Determinar la eficiencia del equipo de desarrollo",
                "c) Calcular la relación entre el tamaño del software y el esfuerzo invertido",
            ],
            [
                "a) La cantidad de atributos accesibles públicamente en el sistema",
                "b) El grado de visibilidad de los atributos en todas las clases",
                "c) La cantidad de atributos heredados en el sistema",
            ],
            [
                "a) La experiencia del equipo en el lenguaje de programación",
                "b) El número total de líneas de código del proyecto",
                "c) El presupuesto total asignado al proyecto",
            ],
            [
                "a) El número de defectos conocidos en el software",
                "b) La cantidad de recursos utilizados en el software",
                "c) La complejidad de flujo de control en un programa",
            ],
            [
                "a) Un bajo tiempo necesario para completar exitosamente una transacción",
                "b) Un alto porcentaje de eficiencia en comparación con usuarios expertos",
                "c) Una gran cantidad de transacciones completadas con éxito",
            ],
            [
                "a) Identificar el número total de defectos en el software",
                "b) Evaluar la calidad del software en función de los defectos conocidos",
                "c) Determinar el costo de corrección de los defectos",
            ],
            [
                "a) La cantidad de superclases que una clase tiene",
                "b) El número de descendientes inmediatos de una clase",
                "c) El total de métodos heredados por una clase",
            ],
            [
                "a) Una alta cohesión y bajo acoplamiento en la clase",
                "b) Una baja cohesión y alto acoplamiento en la clase",
                "c) Un elevado número de métodos y atributos en la clase",
            ],
            [
                "a) Mantenibilidad y portabilidad",
                "b) Usabilidad y eficiencia",
                "c) Madurez, disponibilidad, tolerancia a fallos y capacidad de recuperación",
            ],
            [
                "a) Evaluar la cantidad de métodos y atributos heredados en el sistema",
                "b) Determinar el grado de polimorfismo debido a la herencia en el sistema",
                "c) Calcular la proporción de métodos ocultos en el sistema",
            ],
            [
                "a) La cantidad de operaciones propias de una subclase",
                "b) El número total de operaciones en una subclase",
                "c) La cantidad de operaciones heredadas que son sustituidas en la subclase",
            ],
            [
                "a) La cantidad de niveles en la jerarquía de clases de un programa",
                "b) El número de veces que un método se invoca recursivamente",
                "c) La cantidad de bucles o ciclos anidados en una función",
            ],
            [
                "a) La cantidad de horas trabajadas por el equipo de desarrollo",
                "b) La eficiencia en el uso de recursos en el proyecto",
                "c) El trabajo realizado que contribuye directamente a los resultados del proyecto",
            ],
            [
                "a) Calcular el costo de las características no implementadas",
                "b) Evaluar el costo adicional por no abordar problemas en su primera aparición",
                "c) Determinar el presupuesto necesario para completar el proyecto",
            ],
            [
                "a) La complejidad inherente al problema que el software resuelve",
                "b) La complejidad debida a la estructura de control del software",
                "c) El grado de estructuración de un programa en términos de control de flujo",
            ],
            [
                "a) La cantidad de clases que dependen de una clase dada",
                "b) El número de clases de las que depende una clase dada",
                "c) El total de dependencias en un paquete de clases",
            ],
            [
                "a) Un módulo tiene muchas dependencias externas",
                "b) Un módulo es ampliamente utilizado por otros módulos del sistema",
                "c) Un módulo tiene una estructura interna compleja",
            ],
            [
                "a) El tiempo promedio para completar tareas específicas",
                "b) El porcentaje de tareas completadas con éxito por los usuarios",
                "c) La satisfacción del usuario con la interfaz de la aplicación web",
            ],
            [
                "a) Evaluar la puntualidad en la entrega de las fases del proyecto",
                "b) Medir la relación entre el tiempo invertido y los resultados obtenidos",
                "c) Calcular la duración total del proyecto",
            ],
            [
                "a) El total de clases en el sistema",
                "b) Las clases que son fundamentales para el dominio del problema",
                "c) El número de clases que tienen múltiples responsabilidades",
            ],
            [
                "a) Medir la estabilidad del software en base a los cambios entre liberaciones",
                "b) Evaluar la calidad del código en términos de prácticas de programación",
                "c) Determinar el nivel de actualización tecnológica del software",
            ],
            [
                "a) La cantidad de métodos que son reutilizados en diferentes clases",
                "b) La proporción de métodos que pueden ser heredados y reutilizados en el sistema",
                "c) El número total de métodos definidos en el sistema",
            ],
            [
                "a) Determinar la precisión de las estimaciones de costo y esfuerzo",
                "b) Evaluar el tamaño del proyecto en líneas de código",
                "c) Medir la complejidad de los módulos del software",
            ],
            [
                "a) La velocidad de carga de las páginas web",
                "b) El tiempo medio que tarda el sistema en responder a las entradas del usuario",
                "c) La eficiencia del usuario al navegar por la aplicación web",
            ],
            [
                "a) La cantidad de relaciones de herencia en un sistema",
                "b) El total de relaciones entre módulos que no son de herencia",
                "c) El número de clases que usan una clase específica",
            ],
            [
                "a) Medir la facilidad de uso del software desde la perspectiva del usuario",
                "b) Evaluar la efectividad del software en cumplir con las necesidades del usuario",
                "c) Calcular el tiempo promedio que un usuario pasa en el software",
            ],
            [
                "a) Un módulo tiene muchas dependencias externas",
                "b) Un módulo es ampliamente utilizado por otros módulos del sistema",
                "c) Un módulo tiene una estructura interna compleja",
            ],
            [
                "a) El tiempo promedio para completar tareas específicas",
                "b) El porcentaje de tareas completadas con éxito por los usuarios",
                "c) La satisfacción del usuario con la interfaz de la aplicación web",
            ],
            [
                "a) Evaluar la puntualidad en la entrega de las fases del proyecto",
                "b) Medir la relación entre el tiempo invertido y los resultados obtenidos",
                "c) Calcular la duración total del proyecto",
            ],
            [
                "a) El total de clases en el sistema",
                "b) Las clases que son fundamentales para el dominio del problema",
                "c) El número de clases que tienen múltiples responsabilidades",
            ],
            [
                "a) Medir la estabilidad del software en base a los cambios entre liberaciones",
                "b) Evaluar la calidad del código en términos de prácticas de programación",
                "c) Determinar el nivel de actualización tecnológica del software",
            ],
            [
                "a) La cantidad de métodos que son reutilizados en diferentes clases",
                "b) La proporción de métodos que pueden ser heredados y reutilizados en el sistema",
                "c) El número total de métodos definidos en el sistema",
            ],
            [
                "a) Determinar la precisión de las estimaciones de costo y esfuerzo",
                "b) Evaluar el tamaño del proyecto en líneas de código",
                "c) Medir la complejidad de los módulos del software",
            ],
            [
                "a) La velocidad de carga de las páginas web",
                "b) El tiempo medio que tarda el sistema en responder a las entradas del usuario",
                "c) La eficiencia del usuario al navegar por la aplicación web",
            ],
            [
                "a) La cantidad de relaciones de herencia en un sistema",
                "b) El total de relaciones entre módulos que no son de herencia",
                "c) El número de clases que usan una clase específica",
            ],
            [
                "a) Medir la facilidad de uso del software desde la perspectiva del usuario",
                "b) Evaluar la efectividad del software en cumplir con las necesidades del usuario",
                "c) Calcular el tiempo promedio que un usuario pasa en el software",
            ],
            [
                "a) La cantidad de niveles en la jerarquía de clases de un programa",
                "b) El número de veces que un método se invoca recursivamente",
                "c) La cantidad de bucles o ciclos anidados en una función",
            ],
            [
                "a) La cantidad de horas trabajadas por el equipo de desarrollo",
                "b) La eficiencia en el uso de recursos en el proyecto",
                "c) El trabajo realizado que contribuye directamente a los resultados del proyecto",
            ],
            [
                "a) Calcular el costo de las características no implementadas",
                "b) Evaluar el costo adicional por no abordar problemas en su primera aparición",
                "c) Determinar el presupuesto necesario para completar el proyecto",
            ],
            [
                "a) La complejidad inherente al problema que el software resuelve",
                "b) La complejidad debida a la estructura de control del software",
                "c) El grado de estructuración de un programa en términos de control de flujo",
            ],
            [
                "a) La cantidad de clases que dependen de una clase dada",
                "b) El número de clases de las que depende una clase dada",
                "c) El total de dependencias en un paquete de clases",
            ],
            [
                "a) La complejidad de las operaciones en una clase",
                "b) El número promedio de argumentos en los métodos de una clase",
                "c) El nivel de interacción entre diferentes clases",
            ],
            [
                "a) Un gran número de clases compuestas en el sistema",
                "b) Un alto grado de reutilización de componentes",
                "c) Muchas clases que forman parte directa de una clase compuesta",
            ],
            [
                "a) Determinar la cantidad de atributos heredados en el sistema",
                "b) Evaluar el nivel de encapsulamiento de atributos en las clases",
                "c) Medir la cantidad de atributos accesibles públicamente en el sistema",
            ],
            [
                "a) La interacción entre diferentes módulos del sistema",
                "b) El nivel de dependencia de los módulos respecto a sus datos",
                "c) La complejidad asociada a las estructuras de datos utilizadas en los módulos",
            ],
            [
                "a) Evaluar la complejidad y tamaño de las clases y paquetes",
                "b) Medir la eficiencia y efectividad de las relaciones de herencia",
                "c) Calcular el nivel de acoplamiento entre clases y paquetes",
            ],
            [
                "a) Asignar números a elementos de software",
                "b) Mejorar los procesos de software a largo plazo",
                "c) Evaluar la calidad del código fuente",
            ],
            [
                "a) Determinar la eficiencia de las herramientas de desarrollo",
                "b) Evaluar el estado del proyecto en curso y gestionar riesgos",
                "c) Medir la satisfacción del cliente con el producto final",
            ],
            [
                "a) Una herramienta específica para el desarrollo de software",
                "b) Una abstracción de la realidad para observar detalles específicos",
                "c) Un tipo de software utilizado en el desarrollo ágil",
            ],
            [
                "a) Seleccionar métricas para la gestión de proyectos",
                "b) Asignar números o símbolos a atributos del mundo real",
                "c) Evaluar el rendimiento del equipo de desarrollo",
            ],
            ["a) Escala Nominal", "b) Escala Ordinal", "c) Escala de Ratio"],
            [
                "a) Seleccionar las herramientas de desarrollo adecuadas",
                "b) Identificar las necesidades de información del proyecto",
                "c) Determinar el cronograma del proyecto",
            ],
            [
                "a) Recopilación y análisis de datos de rendimiento",
                "b) Recolección de datos de medida y presentación de resultados",
                "c) Seguimiento del avance del proyecto según los KPIs",
            ],
            [
                "a) El cumplimiento de los plazos de entrega del software",
                "b) La efectividad de la implementación del programa de medida",
                "c) La adopción de metodologías de desarrollo por el equipo",
            ],
            [
                "a) El impacto de las métricas en las ventas de software",
                "b) La mejora de las medidas específicas según sea necesario",
                "c) La rentabilidad de las soluciones de software",
            ],
            [
                "a) Se basa en el recuento del número de elementos en una entidad",
                "b) Mide las diferencias entre valores de la escala",
                "c) Clasifica entidades en categorías que implican un orden",
            ],
            [
                "a) Efecto Hawthorne",
                "b) Métrica de vanidad",
                "c) Sesgo de confirmación",
            ],
            [
                "a) Datos que no se alinean con los objetivos del proyecto",
                "b) Datos que no proporcionan información útil para la toma de decisiones",
                "c) Datos que sobrestiman el rendimiento",
            ],
            [
                "a) Involucrar otra entidad o atributo",
                "b) Incluir la duración del proceso de prueba",
                "c) Medir la estabilidad de requisitos",
            ],
            [
                "a) Aseguramiento de la calidad de los datos",
                "b) Almacenamiento y gestión de los datos",
                "c) Capturar y visualizar los datos de forma apropiada",
            ],
            ["a) Precisión", "b) Exactitud", "c) Corrección"],
            [
                "a) Calidad y coste",
                "b) Modularidad y complejidad",
                "c) Productividad y fiabilidad",
            ],
            ["a) Recursos", "b) Entidades", "c) Procesos"],
            [
                "a) Los datos son reproducibles",
                "b) Los datos son consistentes",
                "c) Los datos son recogidos adecuadamente",
            ],
            [
                "a) Complejidad Ciclomática",
                "b) Deuda Técnica",
                "c) Efectividad de las Tareas",
            ],
            [
                "a) Control de calidad del código",
                "b) Mantenibilidad del software",
                "c) Complejidad del flujo de control",
            ],
            [
                "a) Retrasos en el cronograma",
                "b) Costos adicionales futuros",
                "c) Calidad del código fuente",
            ],
            [
                "a) Eficiencia de la interfaz de usuario",
                "b) Satisfacción del usuario",
                "c) Conversión de usuario",
            ],
            ["a) Impacto acumulativo", "b) Exposición al riesgo", "c) Costo-beneficio"],
            ["a) Cohesión de módulos", "b) Fan-in", "c) Acoplamiento entre módulos"],
            [
                "a) Complejidad de métodos",
                "b) Eficiencia de comunicación",
                "c) Interacción entre clases",
            ],
            [
                "a) Estabilidad de los requisitos del proyecto",
                "b) Calidad de los requisitos",
                "c) Ambigüedad de los requisitos",
            ],
            [
                "a) Flexibilidad del diseño",
                "b) Robustez del sistema",
                "c) Complejidad del diseño",
            ],
            [
                "a) Funcionalidad del software",
                "b) Eficiencia del software",
                "c) Fiabilidad del software",
            ],
            [
                "a) Número de clases 'parte' directas en una jerarquía",
                "b) Número máximo de clases desde la clase hasta las hojas",
                "c) Número de clases 'agregados' en un paquete",
            ],
            [
                "a) Número de clases 'parte' directas e indirectas",
                "b) Número de clases hojas en una jerarquía",
                "c) Número de relaciones de agregación en un paquete",
            ],
            [
                "a) NAC mide las asociaciones en un paquete, mientras que NAP las de una clase",
                "b) NAC y NAP son equivalentes y pueden usarse indistintamente",
                "c) NAC es el total de asociaciones de una clase, NAP es el total dentro de un paquete",
            ],
            [
                "a) Número de clases que dependen de la clase dada",
                "b) Número de clases a las que la clase dada depende",
                "c) Número de clases raíz en la jerarquía de herencia",
            ],
            [
                "a) Número ponderado de responsabilidades de una clase, heredadas o no",
                "b) Número de dependencias directas de las clases",
                "c) Porcentaje de responsabilidades heredadas respecto al número total de ellas",
            ],
            [
                "a) Número total de clases en el sistema",
                "b) Un guión de escenario describiendo interacción con la aplicación",
                "c) Número de clases que no pertenecen a ningún paquete",
            ],
            [
                "a) Carencia de cohesión en métodos (CCM)",
                "b) Acceso público a datos miembro (APD)",
                "c) Complejidad de operación (CO)",
            ],
            [
                "a) Alcance y calidad del proyecto",
                "b) Costes del proyecto, recursos, esfuerzo o duraciones",
                "c) Riesgos y viabilidad del proyecto",
            ],
            [
                "a) Maximizar el rendimiento y eficiencia",
                "b) Reducir costes e incrementar niveles de servicio y de calidad",
                "c) Garantizar el cumplimiento de plazos",
            ],
            [
                "a) Una predicción de costes operativos",
                "b) Una visión de alto nivel de lo que sucederá durante el desarrollo",
                "c) Decisiones de diseño arquitectónico",
            ],
            [
                "a) Variabilidad de la medida",
                "b) Unidades o número de cifras significativas de una medida",
                "c) Consistencia de la medida",
            ],
            [
                "a) Proporción de medidas dentro de un rango aceptable",
                "b) Cercanía de una medida a su objetivo real",
                "c) Homogeneidad de los datos medidos",
            ],
            [
                "a) El tiempo óptimo para la entrega del proyecto",
                "b) La probabilidad de completar el proyecto en un intervalo de tiempo",
                "c) La duración máxima permitida del proyecto",
            ],
            [
                "a) Suma de todos los errores relativos dividido por el número de estimaciones",
                "b) Suma de los valores estimados dividido por el número de estimaciones",
                "c) Suma de los valores reales dividido por el número de estimaciones",
            ],
            [
                "a) Magnitud del proyecto y riesgo de estimaciones inexactas",
                "b) Incertidumbre del proyecto y número total de tareas",
                "c) Costo total y eficacia del equipo de proyecto",
            ],
            [
                "a) Riesgo inherente al proyecto",
                "b) Efectividad del proceso de estimación",
                "c) El presupuesto total disponible",
            ],
            [
                "a) Las preliminares son menos exactas y las detalladas requieren planificación de tareas individuales",
                "b) Las preliminares se basan en modelos y las detalladas en descomposición",
                "c) Las preliminares se usan para estimar el tamaño y las detalladas para estimar el costo",
            ],
            ["a) Opinión de expertos", "b) Analogía", "c) Modelos"],
            [
                "a) Experiencia pasada y eficiencia promedio",
                "b) Número de veces que se repite una operación y coste por unidad",
                "c) Tiempo de operación inicial y tasa de aprendizaje",
            ],
            [
                "a) Sumando el tiempo de todas las operaciones individuales",
                "b) Multiplicando el número de operaciones por el tiempo medio de operación",
                "c) Integrando la función de tiempo sobre el número de operaciones",
            ],
            [
                "a) Los modelos de coste están basados en datos empíricos y los restrictivos en la relación tiempo-esfuerzo",
                "b) Los modelos de coste usan la curva de aprendizaje y los restrictivos no",
                "c) Los modelos de coste se aplican al inicio del proyecto y los restrictivos al final",
            ],
            [
                "a) Modelo de regresión lineal",
                "b) Modelo de ajuste de esfuerzo (FAE)",
                "c) Técnica Delphi",
            ],
            [
                "a) Proyectos pequeños con muchas restricciones",
                "b) Proyectos pequeños, mucha experiencia, pocas restricciones",
                "c) Proyectos intermedios, varios niveles de experiencia, requisitos poco y medio rígidos",
            ],
            [
                "a) Directrices para la implementación de software",
                "b) Instrucciones de código fuente entregadas",
                "c) Índice de Desarrollo de Software",
            ],
            ["a) E = a (KDSI)^b", "b) E = a (KDSI)^bF", "c) E = (a (KDSI)^b)/F"],
            [
                "a) Coeficiente de esfuerzo",
                "b) Exponente de la duración",
                "c) Duración en meses",
            ],
            [
                "a) Puntos de función",
                "b) Líneas de código",
                "c) Modelos de arquitectura alternativos",
            ],
            [
                "a) Estimación del tamaño del proyecto",
                "b) Estimación del esfuerzo de desarrollo en meses-persona",
                "c) Estimación de los costes operacionales",
            ],
            [
                "a) Utiliza una colección de curvas de Rayleigh por cada actividad de desarrollo",
                "b) Incluye la especificación de requisitos en el modelo",
                "c) Específico para proyectos pequeños",
            ],
            [
                "a) El tamaño es directamente proporcional al esfuerzo y al tiempo de finalización",
                "b) El tamaño es inversamente proporcional al esfuerzo y al tiempo de finalización",
                "c) El tamaño es proporcional al cubo de la raíz cuarta del tiempo de finalización",
            ],
            [
                "a) El tamaño del código fuente",
                "b) El esfuerzo de desarrollo",
                "c) El número de errores por línea de código",
            ],
            [
                "a) Es constante sin importar el tipo de proyecto",
                "b) Aumenta con la complejidad del proyecto",
                "c) Disminuye a medida que el tamaño del CU aumenta",
            ],
            [
                "a) Esfuerzo para completar una tarea de programación",
                "b) Medida relativa del esfuerzo requerido para desarrollar una historia de usuario",
                "c) Tiempo estimado para la entrega del proyecto",
            ],
            [
                "a) Para estimar el coste basado en la complejidad del código",
                "b) Para realizar estimaciones sobre nuevos proyectos utilizando datos de proyectos pasados",
                "c) Para predecir la duración de las tareas de desarrollo basándose en el rendimiento pasado",
            ],
            [
                "a) El tamaño de los equipos de desarrollo",
                "b) Los valores de los atributos que proporcionan la separación de los datos en diferentes clases",
                "c) La probabilidad de éxito del proyecto",
            ],
            [
                "a) Lista de riesgos potenciales",
                "b) Lista de chequeo de elementos de riesgo",
                "c) Lista de riesgos confirmados",
            ],
            [
                "a) Probabilidad e Impacto",
                "b) Costo y Duración",
                "c) Recursos y Alcance",
            ],
            [
                "a) Pérdida del sistema mayor al 50%",
                "b) Costo menor al 10%",
                "c) Recuperación de la capacidad operativa",
            ],
            [
                "a) Impacto multiplicado por Probabilidad",
                "b) Costo dividido por Tiempo",
                "c) Probabilidad más Impacto",
            ],
            ["a) Mitigar", "b) Transferir", "c) Aceptar"],
            [
                "a) Evaluar la efectividad de los planes de mitigación",
                "b) Incrementar el presupuesto de riesgos",
                "c) Capacitar al equipo en gestión de riesgos",
            ],
            [
                "a) Reevaluar el análisis de riesgos",
                "b) Implementar medidas correctivas",
                "c) Notificar a los stakeholders",
            ],
            [
                "a) Identificación de riesgos",
                "b) Evaluación de la probabilidad",
                "c) Ordenación por magnitud de impacto",
            ],
            ["a) Investigar", "b) Aceptar", "c) Ignorar"],
            ["a) Diagramas de Ishikawa", "b) Planning Poker", "c) Análisis SWOT"],
            [
                "a) Tamaño del producto",
                "b) Entorno de desarrollo",
                "c) Metodologías ágiles",
            ],
            ["a) Probabilidad", "b) Marco de tiempo", "c) Número de afectados"],
            ["a) Magnitud del impacto", "b) Costo de mitigación", "c) Probabilidad"],
            [
                "a) Establecer un plan de contingencia",
                "b) Realizar un análisis de impacto",
                "c) Definir un umbral de aceptación de riesgos",
            ],
            [
                "a) Evitar el riesgo",
                "b) Desarrollar una métrica de rendimiento",
                "c) Transferir el riesgo",
            ],
            [
                "a) Reasignar recursos",
                "b) Contratar un seguro",
                "c) Renegociar los objetivos del proyecto",
            ],
            [
                "a) Actualizar el registro de riesgos",
                "b) Celebrar una reunión de retrospectiva",
                "c) Ajustar los umbrales de riesgo",
            ],
            [
                "a) Utilizar un software de gestión de proyectos",
                "b) Considerar la opinión de expertos",
                "c) Ignorar riesgos con bajo impacto",
            ],
            [
                "a) Eliminación del riesgo",
                "b) Aumento de la reserva de contingencia",
                "c) Acelerar el cronograma",
            ],
            ["a) Análisis PERT", "b) Técnica de Delphi", "c) Prueba de penetración"],
        ]

        self.correct_answers = [
            "b",  # Respuesta correcta para la pregunta 1
            "c",  # Respuesta correcta para la pregunta 2
            "b",  # Respuesta correcta para la pregunta 3
            "a",  # Respuesta correcta para la pregunta 4
            "c",  # Respuesta correcta para la pregunta 5
            "b",  # Respuesta correcta para la pregunta 6
            "b",  # Respuesta correcta para la pregunta 7
            "c",  # Respuesta correcta para la pregunta 8
            "b",  # Respuesta correcta para la pregunta 9
            "a",  # Respuesta correcta para la pregunta 10
            "b",
            "b",
            "a",
            "c",
            "b",
            "a",
            "a",
            "b",
            "c",
            "a",
            "b",
            "a",
            "b",
            "c",
            "b",
            "a",
            "a",
            "b",
            "b",
            "b",
            "b",
            "a",
            "a",
            "b",
            "b",
            "c",
            "c",
            "b",
            "a",
            "b",
            "b",
            "b",
            "c",
            "c",
            "c",
            "b",
            "a",
            "c",
            "b",
            "b",
            "b",
            "b",
            "c",
            "b",
            "c",
            "a",
            "c",
            "b",
            "c",
            "a",
            "b",
            "b",
            "b",
            "b",
            "a",
            "b",
            "a",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "a",
            "b",
            "a",
            "b",
            "b",
            "b",
            "a",
            "c",
            "b",
            "c",
            "a",
            "b",
            "c",
            "b",
            "c",
            "a",
            "b",
            "b",
            "b",
            "b",
            "a",
            "b",
            "b",
            "b",
            "b",
            "a",
            "a",
            "b",
            "a",
            "c",
            "c",
            "b",
            "b",
            "c",
            "b",
            "c",
            "b",
            "b",
            "b",
            "b",
            "a",
            "a",
            "b",
            "a",
            "b",
            "a",
            "c",
            "a",
            "a",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "a",
            "a",
            "c",
            "a",
            "b",
            "b",
            "c",
            "a",
            "b",
            "b",
            "b",
            "b",
            "c",
            "a",
            "b",
            "a",
            "c",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "a",
            "a",
            "a",
            "c",
            "a",
            "b",
            "c",
            "c",
            "b",
            "c",
            "c",
            "b",
            "b",
            "b",
            "c",
            "b",
            "c",
            "c",
            "c"
            # ... Agregar el resto de las respuestas correctas
        ]
        combined_list = list(zip(self.questions, self.options, self.correct_answers))
        shuffle(combined_list)

        # Seleccionar un subconjunto aleatorio de 20 preguntas si hay suficientes preguntas
        total_preguntas = min(3, len(combined_list))
        combined_list = sample(combined_list, total_preguntas)

        # Separar las listas combinadas de nuevo
        self.questions, self.options, self.correct_answers = zip(*combined_list)

        # Convertir de tuplas a listas
        self.questions = list(self.questions)
        self.options = [list(option) for option in self.options]
        self.correct_answers = list(self.correct_answers)

        self.layout = BoxLayout(orientation="vertical")
        self.question_label = Label(
            text=self.questions[self.index], color=self.question_color
        )
        self.layout.add_widget(self.question_label)

        self.buttons = []
        for option in self.options[self.index]:
            btn = Button(text=option, color=[0, 0, 0, 1])  # Color negro por defecto
            btn.bind(on_press=self.check_answer)
            self.layout.add_widget(btn)
            self.buttons.append(btn)

        # Botón para pasar a la siguiente pregunta
        pass_btn = Button(text="Pasar pregunta", color=[0, 0, 0, 1])
        pass_btn.bind(on_press=self.schedule_next_question)
        self.layout.add_widget(pass_btn)

        self.root = self.layout

    def check_answer(self, instance):
        selected_option = instance.text[0].lower()
        is_correct = selected_option == self.correct_answers[self.index].lower()

        # Restablece el color de todos los botones a color de fondo antes de cambiar de color
        for btn in self.buttons:
            btn.background_color = color_fondo  # Fondo claro
            btn.color = color_texto  # Texto oscuro suave

        if is_correct:
            instance.background_color = (
                color_correcto  # Verde suave para la opción correcta
            )
            self.score += 1
        else:
            instance.background_color = (
                color_incorrecto  # Rojo suave para la opción incorrecta
            )
            # Encuentra y colorea la opción correcta
            for btn in self.buttons:
                if btn.text[0].lower() == self.correct_answers[self.index].lower():
                    btn.background_color = (
                        color_correcto  # Verde suave para la opción correcta
                    )

        # Espera 1 segundo antes de pasar a la siguiente pregunta
        # Espera 1 segundo antes de pasar a la siguiente pregunta
        Clock.schedule_once(self.next_question, 1)

    def schedule_next_question(self, instance=None):
        # Espera 1 segundo antes de pasar a la siguiente pregunta
        Clock.schedule_once(self.next_question, 1)

    def next_question(self, dt):
        # Restablece el color de fondo de todos los botones antes de actualizar la pregunta
        for btn in self.buttons:
            btn.background_color = color_fondo  # Fondo claro
            btn.color = color_texto  # Texto oscuro suave

        self.index += 1
        if self.index < len(self.questions):
            self.update_question()
        else:
            self.puntuacion = (
                self.score * 10 / len(self.questions) - self.fallo * 0.25,
            )

            self.show_score()

    def update_question(self):
        # Actualiza la pregunta y resetea el color de la pregunta a blanco
        self.question_label.text = self.questions[self.index]
        self.question_label.color = [1, 1, 1, 1]  # Restablecer color a blanco
        for i, btn in enumerate(self.buttons):
            btn.text = self.options[self.index][i]

    def show_score(self):
        # Crea un popup para mostrar la puntuación final
        content = BoxLayout(orientation="vertical")
        score_label = Label(
            text=f"Tu puntuación es: {self.score} de {len(self.questions)}\n"
            + f"Tu puntuación es: {self.puntuacion} de 10"
        )
        content.add_widget(score_label)
        restart_btn = Button(text="Reiniciar test", size_hint=(1, 0.15))
        restart_btn.bind(on_press=self.restart_test)

        self.popup = Popup(
            title="Resultado del cuestionario", content=content, size_hint=(0.75, 0.5)
        )
        self.popup.open()

    def restart_test(self, instance):
        # Cierra el popup y reinicia el test
        if self.popup:
            self.popup.dismiss()
            self.popup = None
        self.score = 0
        self.index = 0
        self.fallo = 0
        self.puntuacion = 0
        self.build()

# ... resto de tu código de QuizApp


if __name__ == "__main__":
        TestApp().run()
