es_primo = lambda n: all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1


numero = int(input("Ingrese un número entero: "))


if es_primo(numero):
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")
