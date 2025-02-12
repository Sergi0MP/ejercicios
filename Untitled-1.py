def S(n): return n + 1
def A(n): return max(n - 1, 0)

def suma(a, b): return a if b == 0 else suma(S(a), A(b))
def multiplicacion(a, b): return 0 if b == 0 else suma(a, multiplicacion(a, A(b)))
def resta(a, b): return a if b == 0 else resta(A(a), A(b))
def division(a, b):
    if b == 0: raise ValueError("No se puede dividir por cero")
    return 0 if a < b else S(division(resta(a, b), b))

def main():
    print("Calculadora con sucesora y antecesora")
    while True:
        try:
            a, b = map(int, input("Ingrese dos números naturales separados por un espacio: ").split())
            if a < 0 or b < 0: raise ValueError("Solo se permiten números naturales.")
            op = input("Operación (suma, multiplicacion, resta, division): ").strip().lower()
            resultado = {"suma": suma, "multiplicacion": multiplicacion, "resta": resta, "division": division}.get(op, lambda x, y: "Operación invalida")(a, b)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")
        if input("¿Otra operación? (sí/no): ").strip().lower() not in ["sí", "si"]:
            break

if __name__ == "__main__":
    main()
