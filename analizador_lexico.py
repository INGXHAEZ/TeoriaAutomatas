import re

tokens = {
    "CadenaTexto": r"\".*?\"",
    "Numero": r"\d+(\.\d+)?",
    "OperadorAritmetico": r"[\+\-\*/]",
    "OperadorRelacional": r"(==|!=|<=|>=|<|>)",
    "SimboloAgrupacion": r"[\(\)\{\}\[\];]",
    "Asignacion": r"=",
    "Identificador": r"[a-zA-Z_][a-zA-Z0-9_]*",
}

palabras_control = {"si", "sino", "mientras", "para"}
palabras_funciones = {"func", "retorn", "vacio"}
tipos_dato = {"ent", "deci", "flota", "cade"}
estructura_programa = {"inicio_programa", "fin_programa"}

regex_general = "|".join(f"(?P<{key}>{value})" for key, value in tokens.items())

def analizar_codigo(codigo):
    palabras = re.finditer(regex_general, codigo)
    for match in palabras:
        tipo = match.lastgroup
        valor = match.group()

        if tipo == "Identificador":
            if valor in palabras_control:
                tipo = "Palabra clave de control"
            elif valor in palabras_funciones:
                tipo = "Palabra clave de función"
            elif valor in tipos_dato:
                tipo = "Tipo de dato"
            elif valor in estructura_programa:
                tipo = "Estructura del programa"

        print(f"Token válido: '{valor}' → {tipo}")

    no_validos = re.sub(regex_general, "", codigo)
    for c in no_validos.strip():
        if not c.isspace():
            print(f"Error léxico: '{c}' no reconocido.")

with open("programa.txt", "r") as archivo:
    contenido = archivo.read()
    analizar_codigo(contenido)
