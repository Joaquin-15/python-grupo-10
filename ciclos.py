# condicion = input('Desea salir del programa ? (si/no): ')

# print(type(90))
# print(type('90'))
# print(type("90"))
    
#  Ciclos: While y For
# While: El bucle while se ejecuta siempre y cuando la condicion sea verdadera

# while not (condicion != 'si'):
#     # Bloque de codigo
#     nota = int(input('Ingresa la nota del estudiante: '))
#     if nota >= 90:
#         print('Excelente')
#     elif nota >= 80:
#         print('Muy bien')
#     elif nota >= 70:
#         print('Bien')
#     else:
#         print('Necesitas mejorar un poco')

#     condicion = input('Desea salir del programa ? (si/no): ')


    
# For: El bucle for se utiliza para iterar sobre una secuencia de elementos.
# frutas = ['manzana', 'pera', 'uva', 'sandia', 'melon']

# for fruta in frutas:
#     print(fruta)
    
# limite = int(input('Ingrese el limite del rango: '))
# for i in range(limite):
#     print("Numero: ",i+1)

# limite = int(input('Ingrese el limite del rango: '))
# for i in range(limite):
#     if i == 5:
#         break
#     print("Numero con break: ",i+1)

# limite = int(input('Ingrese el limite del rango: '))
# for i in range(limite):
#     if i == 5:
#         continue
#     print("Numero con continue: ",i+1)

#  Bucles anidados o matrices
# filas = int(input('Ingrese el numero de Filas: '))
# columnas = int(input('Ingrese el numero de Columnas: '))

# for i in range(filas):
#     for j in range(columnas):
#         print('Fila: ',i,' Columna: ',j)

# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9,10]
# ]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print('Fila: ',i,' Columna: ',j,' Valor: ',matriz[i][j])

# for i in range(2):
#     for j in range(3):
#         if(i == j):
#             print(matriz[i][j])

# for i in range(len(matriz)):
#     print(matriz[i][i])

listaDeUsuarios = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'Maria', 'edad': 30},
    {'nombre': 'Pedro', 'edad': 35},
    {'nombre': 'Ana', 'edad': 40}
]

for usuario in listaDeUsuarios:
    # print('Nombre: ',usuario['nombre'],' Edad: ',usuario['edad'])
    print('Nombre: ',usuario.get('nombre','no existe esta propiedad'),' Edad: ',usuario.get('edad','no existe esta propiedad'))