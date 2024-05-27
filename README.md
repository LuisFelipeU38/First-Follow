# info de la materia: Leng. Formales y Compiladores
#
# Estudiante(s): Luis Felipe Urquijo, lfurquijov@eafit.edu.co
#                Jaime Uribe Mogollon, jruribem@eafit.edu.co
#
# Profesor: Oscar Eduardo Garcia Quintero
#
# Procesamiento de GLCs para generar sus primeros y siguientes
#
# 1. breve descripción de la actividad
Este proyecto proporciona un conjunto de scripts en Python para calcular los conjuntos `FIRST` y `FOLLOW` de una gramática libre de contexto.
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta (requerimientos funcionales y no funcionales)
- Procesamiento de Entrada (glcs.in):
El script lee el archivo glcs.in y procesa el número de casos, el número de no terminales, y las producciones de cada no terminal.
- Generación de Salida (pr_sig.out):
El script genera un archivo pr_sig.out que contiene el número de casos, el número de no terminales para cada caso, y los conjuntos FIRST y FOLLOW para cada no terminal en el formato especificado.
## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta  (requerimientos funcionales y no funcionales)
- Se cumplieron todos los aspectos de la actividad propuesta.
# 2. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
## Lenguaje de Programación
Python: El proyecto está desarrollado en Python, un lenguaje de programación interpretado, de alto nivel y con una sintaxis que favorece la legibilidad del código.
## Librerías y Paquetes
Para este proyecto no se utilizan librerías ni paquetes especiales más allá de las librerías estándar de Python. Esto cumple con la restricción de no usar bibliotecas especiales para gramáticas libres de contexto.
## Requisitos
Python 3.x: Asegúrate de tener instalado Python 3.x en tu sistema. Puedes verificar la versión instalada ejecutando python --version o python3 --version en la terminal.
## como se compila y ejecuta.
1. Instalar Python:
   - Asegúrate de tener Python 3.x instalado.
2. Clonar el Repositorio:
   - git clone https://github.com/LuisFelipeU38/First-Follow.git
   - cd First-Follow
## (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO)
1. main.py: Script principal que lee la gramática desde un archivo de entrada, calcula los conjuntos FIRST y FOLLOW, y escribe los resultados en un archivo de salida.
2. glcs.in: Archivo de entrada que contiene la gramática.
3. pr_sig.out: Archivo de salida que contiene los resultados de los conjuntos FIRST y FOLLOW.
## resultados o pantallazos 
![image](https://github.com/LuisFelipeU38/First-Follow/assets/83362726/8901ebc3-2668-4dec-91b9-cdac40c3e634)
## Conjuntos First and Follow esperados:
![image](https://github.com/LuisFelipeU38/First-Follow/assets/83362726/d7a04bc4-f9a4-4515-8771-7c48e3d47f2f)


