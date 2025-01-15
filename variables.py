# Caracteristicas de una variable

# 1. Nombre: Un nombre unico que se utiliza para identificarla en el codigo.
# 2. Valor: Una variable almacena un valor que ser un numero, una cadena de texto, una fecha, etc.
# 3. Tipo de dato: Una variable tiene un tipo de dato que determina el tipo de valor que puede almacenar.
# 4. Ambito: Una variable puede ser global o local ( determina en que parte del codigo esta disponible).


edad = "32"
nombre = "Sergio"
real = 3.14
booleano = False
lista = [1, 2, 3, 'Adrian', 'Sergio', 3.14, True, False]
tupla = (1, 2, 3)
diccionario = {"nombre": "Sergio", "edad": 32}

print(edad)
edad = 567
print('Valor de edad luego de reasignarlo',edad)

# print(nombre)
# print(real)
# print(booleano)
# print(lista)
# print(tupla)
# print(diccionario)
# int = entero
print('Variable edad',type(edad))
# str = string = cadena de texto
print('Variable nombre',type(nombre))
# float = decimal
print('Variable real',type(real))
# bool = booleano
print('Varable booleano',type(booleano))
# list = lista
print('Variable lista',type(lista))
# tuple = tupla
print('Variable tupla',type(tupla))
# dict = diccionario
print('Variable diccionario',type(diccionario))





