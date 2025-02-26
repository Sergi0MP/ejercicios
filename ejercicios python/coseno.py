from math import factorial, pi

taylor_cos_term = lambda n, x: ((-1)**n * x**(2*n)) / factorial(2*n)

taylor_cos = lambda x, m: sum(taylor_cos_term(n, x) for n in range(m))
x = float(input("Ingrese el valor de x (en radianes): "))
m = int(input("Ingrese el número de términos del polinomio de Taylor: "))

resultado = taylor_cos(x, m)
print(f"El valor aproximado de cos({x}) utilizando {m} términos del polinomio de Taylor es {resultado}")
