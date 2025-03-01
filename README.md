# Curso de Introducción a Python y su uso en el Análisis de Datos
### Facultad Matemáticas USC, curso 2024/2025
Bienvenido al repositorio con las slides para nuestro curso de Python! Hemos hecho open-source todo nuestro código para que en el futuro alguien pueda aprovecharse de este contenido al enseñar Python. Usamos [reveal.js](https://revealjs.com/) como framework principal para las diapositivas.

## Contenidos del Curso

El curso está dividido en dos partes principales:

### Parte 1: Introducción a Python y su ecosistema
1. Instalación y conceptos básicos ([clase1.html](clase1.html))

2. Control de flujo, funciones y tipos de datos básicos ([clase2.html](clase2.html))

3. I/O por consola y por archivos ([clase3.html](clase3.html))

4. Instalación de paquetes y ejecución en notebooks ([clase4.html](clase4.html))

### Parte 2: Python para estadística y ciencia de datos
5. Operaciones vectorizadas con NumPy ([clase5.html](clase5.html))

6. Uso de datasets de pandas para bases de datos tabulares ([clase6.html](clase6.html))

7. Modelos de regresión y clasificación con scikit-learn ([clase7.html](clase7.html))

8. Visualización de resultados con matplotlib y seaborn ([clase8.html](clase8.html))

### Tecnologías Utilizadas
Este curso utiliza las siguientes herramientas y tecnologías:

- Python y Jupyter Notebooks*
- Las librerías NumPy, pandas, scikit-learn, matplotlib, seaborn
- Reveal.js (para diapositivas interactivas)
- Gulp.js (para automatización de tareas)
- npm (gestor de paquetes de Node.js)

### Como ejecutar en localhost
Para visualizar las diapositivas en tu navegador, sigue estos pasos:

#### Clonar el repositorio
```bash
git clone https://github.com/xianacarrera/python_course_2025.git
cd python_course_2025
```

#### Instalar las dependencias

Asegúrate de tener **Node.js** instalado y ejecuta:
```bash
npm install
```

#### Iniciar el servidor
```bash
npm start
```
Esto iniciará un servidor local donde podrás acceder a las diapositivas a través de `http://localhost:8000/`.

