# Función lambda para definir la función cuyo raíz queremos encontrar
funcion = lambda x: x**3 - x - 2

# Función lambda para implementar el Algoritmo de Bisección
biseccion = lambda f, a, b, tol: (lambda x: x if abs(f(x)) < tol else biseccion(f, (a + b) / 2, b, tol) if f(a) * f((a + b) / 2) < 0 else biseccion(f, a, (a + b) / 2, tol))((a + b) / 2)

# Solicitar al usuario que ingrese los extremos del intervalo y la tolerancia
a = float(input("Ingrese el extremo inferior del intervalo: "))
b = float(input("Ingrese el extremo superior del intervalo: "))
tol = float(input("Ingrese la tolerancia: "))

# Calcular y mostrar la raíz utilizando el Algoritmo de Bisección
raiz = biseccion(funcion, a, b, tol)
print(f"La raíz de la función en el intervalo [{a}, {b}] con una tolerancia de {tol} es aproximadamente {raiz}")
