"""
Ejercicio 1: Formateador de Expedientes 

o Crear variables para el nombre, primer apellido, segundo apellido y año de nacimiento de un 
alumno. 

o Generar una cadena de expediente con el formato APELLIDO1_APELLIDO2_N (donde N 
es la inicial del nombre, todo en mayúsculas) y un código de usuario con el 
año de nacimiento formateado a 4 dígitos y el número de usuario formateado a 5 dígitos con 
ceros iniciales.
"""

# Creando variables
nombre = "Ana"
primer_apellido = "García" 
segundo_apellido = "López"
ano_nacimiento = 2007
numero_usuario = 23

# Generar cadena de expediente: APELLIDO1_APELLIDO2_N (todo en mayúsculas)
expediente = f"Expediente: {primer_apellido}_{segundo_apellido}_{nombre[0]}".upper()

# código de usuario con el año de nacimiento formateado a 4 dígitos y el número de usuario formateado a 5 dígitos con ceros iniciales
codigo = f"Código de usuario: {ano_nacimiento:04d}-{numero_usuario:05d}"

print(expediente)
print(codigo)