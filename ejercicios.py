"""
3. Dada la siguiente lista:
Frutas = [“manzana”, “platano”, “fresa” ]
 Imprimir el segundo ítem
 Comprobar si “patata” está en la lista en caso negativo imprime mensaje indicando
que patata no es una fruta
 Cambiar el valor de “manzana” por “kiwi”
 Usar el método append() para añadir a la lista la “naranja”
 Usar el método insert() para añadir el limón en el tercer puesto de la lista
 Usar el método remove() para eliminar la “fresa”
 Imprimir los ítems de la lista usando un bucle
"""
'''
Frutas = ["manzana", "platano", "fresa"]
print(Frutas[1])

if (not Frutas.__contains__("patata")):
    print("Patata no es una fruta")

Frutas.append("naranjas")
Frutas.insert(2, "limón")
Frutas.remove("fresa")

for fruta in Frutas:
    print(fruta)
'''
'''
4. Dado el siguiente diccionario:
Coche = {“marca”: “Ford”, “modelo”: “Mustang”}
 Usar el método get para imprimir el valor de la clave “modelo”
 Añadir la clave/valor: “color” : “rojo” al diccionario de coche
'''
'''
Coche = {"marca": "Ford", "modelo": "Mustang"}
print(Coche.get("modelo"))
Coche["color"] = "rojo"
print(Coche)
'''
'''
5. Dados dos números a y b, imprimir “Hola” si a es mayor que b y “Adiós” si a es menor
que b
'''

a = 5
b = 6

if a > b:
    print("Hola")
else:
    print("Adiós")

'''
6. Imprimir los 6 primeros números enteros
'''

for x in range(6):
    print(x)

'''
7. Dado un número indicar si es par o impar
'''
x = 5
if (x % 2 == 0):
    print("Es par")
else:
    print("Es impar")

'''
8. Imprimir los números impares desde el 50 hasta la unidad y calcular su suma
'''
suma = 0
for x in range(51):
    if (x % 2 != 0):
        print(x)
        suma += x
print(suma)

'''
9. Calcular el factorial de un número
'''


def factorial():
    print("Factorial: ")
    y = 50
    num = 1
    for x in range(y):
        num = num * (x + 1)
        print(f"{x + 1}! = {num}")
    print(num)


factorial()

'''
10. Escribir una función que tome un carácter y devuelva True si es una vocal, de lo 
contrario devuelve False
'''


def checkCaracter(caracter):
    caracter = caracter.lower()
    caracteres = ["a", "e", "i", "o", "u"]
    if (caracter in caracteres):
        print(True)
    else:
        print(False)


checkCaracter("z")

'''
11. Escribir una funcion sum() y una función multip() que sumen y multipliquen 
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería 
devolver 10 y multip([1,2,3,4]) debería devolver 24
'''

numeros = [2, 4, 5, 7]


def sum(numeros):
    x = 0
    for num in numeros:
        x += num
    return x


print(sum(numeros))

'''
12. Definir una función generar_n_caracteres() que tome un entero n y devuelva el 
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería 
devolver "xxxxx".
'''


def generar_n_caracteres(numVeces, num):
    mostrar = ""
    for i in range(numVeces):
        mostrar += num
    print(mostrar)


generar_n_caracteres(5, "x")

'''
13. Escribir una función mas_larga() que tome una lista de palabras y devuelva la más
larga.
'''


def mas_larga(lista):
    palabra = ""
    for p in lista:
        if (len(p) > len(palabra)):
            palabra = p
    print(palabra)


lista = ["murciélago", "avión", "uno", "dos", "supercalifragilisticexpialidocious", "sge", "amor"]
print("palabra más larga: ")
mas_larga(lista)

'''
14. Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene 
que evaluar la cadena y decir cuántas letras mayúsculas tiene. 
'''


def ingresa_cadena():
    numMayus = 0
    cadena = input("Ingresa cadena: ")
    for i in range(len(cadena)):
        if cadena[i] == cadena[i].upper():
            numMayus += 1
    print(cadena, "tiene", numMayus, "mayúsculas")


# ingresa_cadena()

'''
15. Escriba una función es_bisiesto() que determine si un año determinado es un año 
bisiesto. Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 
400
'''


def es_bisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 and anio % 400 == 0:
        print(anio, " es bisiesto")
    else:
        print("no es bisiesto")


es_bisiesto(2014)

'''
16. Calcular la letra que corresponde a un dni:
http://www.interior.gob.es/web/servicios-al-ciudadano/dni/calculo-del-digito-de-control-delnif-nie para consultar el algoritmo de cálculo
 Se solicita la introducción del DNI por teclado (el formato correcto es una sucesión 
de 8 números enteros NNNNNNNN)
 Si el formato del DNI es correcto se calcula la letra que corresponde y se escribe 
por pantalla “La letra que corresponde al DNI introducido es” X y el NIF completo 
es NNNNNNNNX
 Si el formato del DNI es incorrecto se escribe por pantalla “Formato de DNI 
incorrecto” y se vuelve a solicitar la introducción del DNI.
'''


def calcular_letra_dni():
    while True:
        dni = input("Introduzca su DNI (formato: 8 números enteros): ")
        if dni.isdigit() and len(dni) == 8:
            dni = int(dni)
            letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
            letra = letras[dni % 23]
            print(f"La letra que corresponde al DNI introducido es {letra} y el NIF completo es {dni}{letra}")
            break
        else:
            print("Formato de DNI incorrecto. Inténtelo de nuevo.")


# calcular_letra_dni()

'''
17. Realizar una calculadora:
 Se solicita la introducción de los dos operandos y el operador por teclado
 Se muestra el resultado de la operación de tal forma: “La operación es: “
“El resultado es 
'''


def opera(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b if b != 0 else "Error: No se puede dividir entre cero."
    }.get(operador, lambda: None)()


print(opera("suma", 4, 5))
