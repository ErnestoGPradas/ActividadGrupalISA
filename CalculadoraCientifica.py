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

    return a / b

# La raíz cuadrada no es más que elevar cualquier número a 0.5.
# Usaremos la función pow() de python que devuelve el valor de un número elevado a una potencia especificada.
# Este método también lo podríamos realizar con "**" que funciona igual que pow().
def raiz_cuadrada(a):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError

    return pow(a, 0.5)
