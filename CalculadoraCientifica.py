import colorama
from colorama import Fore

# Comprobamos que los números introducidos son enteros o flotantes
def suma(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError

    return a + b

# Comprobamos que los números introducidos son enteros o flotantes
def resta(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError

    return a - b

# Comprobamos que los números introducidos son enteros o flotantes
def multiplicacion(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError

    return a * b

# Comprobamos que los números introducidos son enteros o flotantes
def division(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    if b == 0:
        return "No se puede dividir entre 0"
    else:
        return a / b

# La raíz cuadrada no es más que elevar cualquier número a 0.5.
# Usaremos la función pow() de python que devuelve el valor de un número elevado a una potencia especificada.
# Este método también lo podríamos realizar con "**" que funciona igual que pow().
def raiz_cuadrada(a):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError

    return pow(a, 0.5)

# También podemos realizar la raíz cuadrada con el método de aproximación babilónico
def raiz_cuadradaBabilonico(a):

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError

    x = a / 2

    for i in range(20):
        if x * x == a:
            return x
        else:
            x = (x + (a/x)) / 2
    return x



# Comienza la calculadora

arrancarCalculadora = True

while arrancarCalculadora:
    print(Fore.LIGHTCYAN_EX + """
        Bienvenido a la calculadora. Selecciona la operación que deseas realizar:
        
        1) Sumar
        2) Restar
        3) Multiplicar 
        4) Dividir
        5) Raíz cuadrada método pow()
        6) Raíz cuadrada método aproximáción babilónico
        7) Apagar calculadora
        """)
    opcion = int(input("Elige una opción: ") )

    if(opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4):
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
    elif (opcion == 5 or opcion == 6):
        n3 = float(input("Introduce un número: ") )


    if opcion == 1:
        print(" ")
        print(Fore.GREEN + "RESULTADO: La suma de",n1,"+",n2,"es igual a ", suma(n1, n2))
    elif opcion == 2:
        print(" ")
        print(Fore.GREEN + "RESULTADO: La resta de",n1,"-",n2,"es igual a ",resta(n1, n2))
    elif opcion == 3:
        print(" ")
        print(Fore.GREEN + "RESULTADO: El producto de",n1,"*",n2,"es igual a ",multiplicacion(n1, n2))
    elif opcion == 4:
        print(" ")
        print(Fore.GREEN + "RESULTADO: La división de",n1,"*",n2,"es igual a ",division(n1, n2))
    elif opcion == 5:
        print(" ")
        print(Fore.GREEN + "RESULTADO: La raíz cuadrada (método pow()) de",n3,"es ",raiz_cuadrada(n3))
    elif opcion == 6:
        print(" ")
        print(Fore.GREEN + "RESULTADO: La raíz cuadrada (aproximación babilónico) de",n3,"es ",raiz_cuadradaBabilonico(n3))
    elif opcion == 7:
        print(" ")
        print(Fore.RED + "Apagando calculadora....")
        arrancarCalculadora = False
    else:
        print("Opción incorrecta")
