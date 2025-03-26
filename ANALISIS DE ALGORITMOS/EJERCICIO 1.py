#1
diasSemana = [''] * 7
for i in range(7):
    diasSemana[i] = input(f"Ingrese el nombre del día {i+1}: ")

print("Los  días de la semana son :", diasSemana)
 
#2
import numpy as np
dias_laborables = np.array(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'])

for i in range(len(dias_laborables)):
    dias_laborables[i] = dias_laborables[i].upper()

print("Los días laborables en mayúsculas:", dias_laborables)

#3
numeros_enteros = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros_enteros.append(numero)

numeros_pares = []
numeros_impares = []

for numero in numeros_enteros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Array original:", numeros_enteros)
print("Números pares:", numeros_pares)
print("Números impares:", numeros_impares)
#4 
numeros_enteros = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros_enteros.append(numero)

suma_pares = 0
suma_impares = 0

for numero in numeros_enteros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("Array original:", numeros_enteros)
print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)

#5
def rotar(lst1, lst2):

    if len(lst1) > 0 and len(lst2) > 0:
        
        nombre_rotado1 = lst1.pop(0)
        lst2.append(nombre_rotado1)

        nombre_rotado2 = lst2.pop(0)
        lst1.append(nombre_rotado2)
    else:
        print("Ambas listas deben tener al menos un nombre.")

ocupados = input("Ingrese nombres para el equipo 'ocupados' separados por coma: ").split(', ')
libres = input("Ingrese nombres para el equipo 'libres' separados por coma: ").split(', ')

print("Array Ocupados antes:", ocupados)
print("Array Libres antes:", libres)

rotar(ocupados, libres)

print("Array Ocupados después:", ocupados)
print("Array Libres después:", libres)

#6
asistentes_html = ["Jim", "Ani", "Lucas", "Miky", "Judas"]
asistentes_css = ["Ani", "Salomon", "Miky", "Miguel", "Jhina"]

asistentes_comunes_set = set(asistentes_html) & set(asistentes_css)

asistentes_comunes = sorted(list(asistentes_comunes_set))

print("Asistentes a ambos cursos:", asistentes_comunes)

#7
def gestionar_lista_compra(lista_compra):
    pendientes = []
    for articulo in lista_compra:
        if not articulo["estado"]:
            pendientes.append(articulo["nombre"])
    return pendientes

entrada_usuario = input("Ingrese productos y su estado (nombre1,True/False;nombre2,True/False;...): ")

articulos = [articulo.split(',') for articulo in entrada_usuario.split(';')]
lista_compra = [{"nombre": nombre, "estado": estado.lower() == "true"} for nombre, estado in articulos]

pendientes = gestionar_lista_compra(lista_compra)

print("Lista de pendientes:", pendientes)

#8 
def precio(articulo, articulos, precios):
    if articulo in articulos:
        indice = articulos.index(articulo)
        return precios[indice]
    else:
        return -1
    
articulos = input("Ingrese nombres de artículos separados por comas: ").split(',')
precios = [float(precio) for precio in input("Ingrese precios correspondientes separados por comas: ").split(',')]
nombre_articulo = input("Ingrese el nombre del artículo para obtener el precio: ")

resultado = precio(nombre_articulo, articulos, precios)
print(f"El precio de {nombre_articulo} es: {resultado}")
#9
def obtener_extremos_edad(lista_familia):
    if not lista_familia:
        return None, None

    miembro_mayor = max(lista_familia, key=lambda x: x.get('EDAD'))
    miembro_menor = min(lista_familia, key=lambda x: x.get('EDAD'))

    return miembro_mayor, miembro_menor
familia = [
    {"NOMBRE": "Pietro", "EDAD": 25},
    {"NOMBRE": "Lucas", "EDAD": 45},
    {"NOMBRE": "Juanita", "EDAD": 85},
   
]

mayor, menor = obtener_extremos_edad(familia)
print("Miembro de mayor edad:", mayor)
print("Miembro de menor edad:", menor)