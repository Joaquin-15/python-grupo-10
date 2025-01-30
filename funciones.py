# Funciones: Una funcion es un bloque de codigo que solo se ejecuta cuando es llamado, Podemos pasarle datos los cuales son conocido como parametros, una funcion puede devolver datos como resultado ( o lo que tambien se conoce como retornar ( return ))

# Sintaxis basica de una funcion
# 1. se coloca la palabra reservada def
# 2. nombre que le daremos a una funcion, no debe contener espacios
# 3. Parentesis y dentro de ellos puede haber o no un parametro ( lo cual es una variable que contendra datos)
# 4. se cierra con dos puntos ' : '
# 5. Respetar la sintaxis ya que funciona de la misma manera que los condicionales para hacerle saber que ese bloque de codigo pertenecera a esa funcion
# 6. Puede o no retornar algo.

# INFO EXTRA: Cuando una funcion tiene el return, se le llama funcion, pero cuando no retorna nada, se llama procedimiento

def nombre_funcion(parametro):
    #  cuerpo de la funcion ó el bloque de codigo
    pass


def saludo(nombre):
    # return "Hola Mundo!! " + valor
    return f"Hola, {nombre}"

# Cuando voy a mandar a ejecutar una funcion, solo debo colocar el nombre de la funcion con sus parentesis

# print(saludo('Adrian'))
# print(saludo('Manuel'))
# print(saludo('Kenyel'))


# def saludo_procedimiento(nombre, apellido):
#     print(f"Hola, {nombre} {apellido}")


# saludo_procedimiento('Caraballo', 'Adrian')
# saludo_procedimiento('Nelson', 'Xavier')
# saludo_procedimiento('Benjamin', 'Calderon')

def suma(a=1,b=3):
    return a + b

def resta(a, b):
    c = a - b
    c = c * 2
    return c

# print(suma(3,5))
# print(suma(1,3))
# print(suma(9,8))

# Argumentos nombrados
# print(resta(4,3))
# print(resta(3,4))
# print(resta(b=3,a=4)) # Argumentos nombrados en diferente orden.

# Funciones lambda: Las funciones lambda son pequeñas funciones anonimas que se definen con la palñabra clave lambda

multiplicar = lambda a, b: a * b

# print(f"El resultado de la multiplicacion es: {multiplicar(3,3)}")

def contador(maximo):
    count = 1
    
    while count <= maximo:
        print(count)
        # count += 1

# contador(10)

# Puntos para la proxima clase
# 1. Decoradores
# 2. Recursividad || MIEDO
# 3. Modulos


#  Recursividad:
# 1. Caso Base: Es la condicion que detiene la recursividad, Sin un caso base, la funcion se estaria llamando a si misma indefinidamente.
# 2. Caso recursivo.

# El factorial de un número n (denotado como n!) es el producto de todos los enteros positivos desde 1 hasta n.

# 5! = 5 x 4 x 3 x 2 x 1 = 120

# Solucion Iterativa ( sin recursividad )

def factorial_iterativo(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(result)
    print(f"{result}")
    
# factorial_iterativo(5)

# Solucion Recursiva:
def factorial_recursivo(n):
    # Caso Base
    if n == 0 or n == 1:
        return 1
    # Caso Recursivo
    else:
        return n * factorial_recursivo(n - 1)

print(factorial_recursivo(5))