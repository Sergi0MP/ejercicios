mcd= lambda a, b: a if b== 0 else mcd(b, a % b)

numero1 = int(input("ingrese el primer numero entero: "))
numero2 = int(input("ingrese el segundo numero entero: "))

resultado = mcd(numero1, numero2)
print(f"el mcd de {numero1} y {numero2} es {resultado}")