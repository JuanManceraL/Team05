from Syntax import parser

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

ruta_archivo = 'C:/Users/juanm/Documents/Escuela/7mo semestre/Compiladores/Syntax_Semantica_Analyzer_Team_5/ejemplo.c'
codigo = leer_archivo(ruta_archivo)

# Código de entrada para analizar
code = """int a;"""

"""
int a;
a = 5;
b = 10;
"""

# Ejecutar el analizador
parser.parse(codigo)