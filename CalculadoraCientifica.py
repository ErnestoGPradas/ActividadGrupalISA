# Comprobamos que los números introducidos son enteros o flotantes
def suma(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError

    return a + b
