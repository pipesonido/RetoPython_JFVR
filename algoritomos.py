# Algoritmo 1
# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
# algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al
# final las dos variables (recuerda la asignación).


while True:
    try:
        A = int(input("Ingrese un número para la variable A  "))
        B = int(input("Ingrese un número para la variable B  "))
        C = A
        A = B
        B = C
        print("El nuevo valor de la variable A es ", A)
        print("El nuevo valor de la variable B es ", B)
        break
    except ValueError:
        print("Por favor ingrese solo números")
    
# Algoritmo 2
# Algoritmo que lea dos números, calculando y escribiendo el valor de su suma, resta,
# producto y división.

while True:
    try:
        A = int(input("Ingrese un primer número  "))
        B = int(input("Ingrese un segundo número   "))
        suma = A + B
        resta = A - B
        producto = A * B
        if B <= 0:
             division = 0
        else:
            division = A / B              
        print("La suma de los dos números es ", suma)
        print("La resta del primer número menos el segundo es ", resta)
        print("El producto entre los dos números es ", producto)
        print("La división del primer sobre el segundo número es ", division)
        break
    except ValueError:
        print("Por favor ingrese solo números")



# Algoritmo 3
# Algoritmo que lea dos números y nos diga cual de ellos es mayor o bien si son
# iguales (recuerda usar la estructura condicional SI)


while True:
    try:
        A = int(input("Ingrese un primer número  "))
        B = int(input("Ingrese un segundo número   "))        
        if A < B:
             print("El primer número es menor al segundo ")
        elif A > B:
             print("El primer número es mayor al segundo ")  
        else:
             print("Ambos números son iguales")
        break
    except ValueError:
        print("Por favor ingrese solo números")


# Algoritmo 4
# Algoritmo que lea tres números distintos y nos diga cual de ellos es el mayor
# (recuerda usar la estructura condicional Si y los operadores lógicos).

while True:
    try:
        A = int(input("Ingrese un primer número  "))
        B = int(input("Ingrese un segundo número   "))   
        C = int(input("Ingrese un tercer número   "))    
        if A > B and A > C:
             print("El primer número es el mayor de todos los números ingresados ")
        elif B > A and B > C:
             print("El segundo número es el mayor de todos los números ingresados")  
        elif C > A and C > B:
             print("El tercer número es el mayor de todos los números ingresados") 
        else:
             print("Todos números ingresados son iguales")
        break
    except ValueError:
        print("Por favor ingrese solo números")


# Algoritmo 5
# Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo,
# debe imprimir el producto de los tres y si no lo es, imprimirá la suma

while True:
    try:
        A = int(input("Ingrese un primer número  "))
        B = int(input("Ingrese un segundo número   "))   
        C = int(input("Ingrese un tercer número   "))    
        if A < 0:
            producto = A * B * C
            print("El producto de los números ingresados es ", producto)        
        else:
            producto = A + B + C
            print("La suma de los números ingresados es ", producto) 
        break
    except ValueError:
        print("Por favor ingrese solo números")


# Algoritmo 6
# Realizar un algoritmo que lea un número por teclado. En caso de que ese número
# sea 0 o menor que 0, se saldrá del programa imprimiendo antes un mensaje de error.
# Si es mayor que 0, se deberá calcular su cuadrado y la raiz cuadrada del mismo,
# visualizando el numero que ha tecleado el usuario y su resultado (“Del numero X, su
# potencia es X y su raiz X” ). Para calcular la raiz cuadrada se puede usar la función
# interna RAIZ(X) o con una potencia de 0,5.

import math
while True:
    try:
        A = int(input("Ingrese un número  "))        
        if A <= 0:            
            print("Error!!")        
        else:
            B = A ** 2
            C = math.sqrt(A)

            print("Del numero ", A, " su potencia es ", B, " y su raiz ", C ) 
        break
    except ValueError:
        print("Por favor ingrese solo números")


# Algoritmo 7
# Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el
# curso actual. Diseñar un algoritmo para este propósito (recuerda que para calcular el
# porcentaje puedes hacer una regla de 3).


while True:
    try:
        nino = int(input("Ingrese el número de niños del curso actual  ")) 
        nina = int(input("Ingrese el número de niñas del curso actual   "))  
        total = nino + nina
        if total > 0:            
            porNino = int((nino / total) * 100)
            porNina = int((nina / total) * 100)
            print("El porcentaje de niños para el curso actual es de ", porNino, "% y el procentaje de niñas para el mismo curso es de ", porNina, "%" ) 
        else:
            porNino = 0
            porNina = 0
            print("No se puede hacer un promedio cuando la cantidad de niños es CERO" )         
        break
    except ValueError:
        print("Por favor ingrese solo números")


# Algoritmo 8
# Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes
# de octubre. Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar
# al cliente.

texMeses = """
Por favor emplee la siguiente convención para definir cada mes:
        Enero => 1                     Julio => 7
        Febrero => 2                   Agosto => 8
        Marzo => 3                     Septiembre => 9
        Abril => 4                     Octubre => 10
        Mayo => 5                      Noviembre => 11
        Junio => 6                     Diciembre => 12
"""
while True:
    try:
        print(texMeses)
        mes = int(input("Ingrese el mes del importe según la convención  "))
        if mes < 0 or mes > 12:
            print("Los meses van de 1 a 12")
        else:
            importe = int(input("Ingrese el valor del importe  "))  
            descuento = int((importe * 15)/100)
            totalDescuento = importe - descuento
            if mes != 10:
                print("El valor a cobrar es ", importe)            
            else:
                print("El valor a cobrar es ", totalDescuento)
        break
    except ValueError:
        print("Por favor ingrese solo números")



# Algoritmo 9
# Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o
# impar. En el caso de ser 0, debe visualizar “el número no es par ni impar” (para que un
# numero sea par, se debe dividir entre dos y que su resto sea 0)

NumEnt = int(input("Escriba un número: "))
if NumEnt == 0:
    print(f"{NumEnt} el número no es par ni impar")
elif NumEnt % 2 == 0:
    print(f"{NumEnt} es par")
else:
    print(f"{NumEnt} es impar")


# Algoritmo 10
# Modificar el algoritmo anterior, de forma que si se teclea un cero, se vuelva a pedir
# el número por teclado (así hasta que se teclee un número mayor que cero) (recuerda
# la estructura mientras).


while True:
    try:
        NumEnt = int(input("Escriba un número mayor a 0: "))    
        while NumEnt == 0:                      
            print("¡El número debe ser mayor a 0! Inténte de nuevo Pendejo") 
            NumEnt = int(input("Escriba un número mayor a 0: "))
        else:
            if NumEnt % 2 == 0:
                print(f"{NumEnt} es par")
            else:
                print(f"{NumEnt} es impar")             
        break
    except ValueError:
        print("Por favor ingrese solo números")


# Algoritmo 11
# Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo
# de grado superior o no. Para acceder a un grado superior, si se tiene un titulo de
# bachiller, en caso de no tenerlo, se puede acceder si hemos superado una prueba de
# acceso


texMeses = """
Por favor emplee la siguiente convención para responder a las preguntas:
            Si => 1          No => 0
"""
while True:
    try:
        print(texMeses)
        titulo = int(input("¿Posee título de Bachiller?  "))
        if titulo == 1:
            print("Usted puede acceder a cursar un ciclo formativo de grado superior")
        else:
            prueba = int(input("¿Ha superado la prueba de acceso?  "))
            if prueba == 1:
                print("Usted puede acceder a cursar un ciclo formativo de grado superior")
            else:
                print("Usted no puede acceder a cursar un ciclo formativo de grado superior porque no cumple con lo requisitos necesarios")        
        break
    except ValueError:
        print("Por favor ingrese solo números de acuerdo con la convención")




# Algoritmo 12
# Desarrollar un algoritmo que nos calcule el cuadrado de los 9 primeros números
# naturales (recuerda la estructura desde-hasta)

for num in range (1, 9 + 1):
    print(f"Ahora num vale {num} y su cuadrado {num ** 2}")
print("Fin")
