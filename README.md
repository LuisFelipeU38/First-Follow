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
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
- Procesamiento de Entrada (glcs.in):
El script lee el archivo glcs.in y procesa el número de casos, el número de no terminales, y las producciones de cada no terminal.
- Generación de Salida (pr_sig.out):
El script genera un archivo pr_sig.out que contiene el número de casos, el número de no terminales para cada caso, y los conjuntos FIRST y FOLLOW para cada no terminal en el formato especificado.
