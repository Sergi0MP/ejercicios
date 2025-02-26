factorial = lambda n: 1 if n==0 else n* factorial(n - 1)

numero= int(input("ingrese un numero entero: "))

print(f"El factorial de {numero} es {factorial(numero)}")