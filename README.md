# ejercicios
este programa implmenta una calculadora con operaciones basicas, como suma, resta, multiplicacion y division pero usando dos funciones fundamentales
-Sucesora (S)
-Antecesora (A)

S(n) -> Devuelve n + 1
A(n) → Devuelve n - 1 (no permite negativos)

suma(a, b) → Realiza la suma de a y b sumando 1 a "a" y restando 1 a "b" hasta que b llegue a 0

multiplicacion(a, b) → Calcula a * b mediante sumas repetidas. Si b es 0, devuelve 0

resta(a, b) → Resta b de a restando 1 a ambos números hasta que b sea 0.

division(a, b) → Calcula a / b restando b repetidamente de a y contando las veces que esto es posible antes de que a sea menor que b.

Para la interaccion con el usuario pide que ingrese dos numeros naturales separados por un espacio, despues de esto el programa pregunta que operacion desea realizar, y el usuario debe escribir la operacion que desee
despues de esto da el resultado de la operacion elegida por el usuario, pero si el usuario intente dividir entre 0 aparecera un mensaje de error, y por ultimo el programa pregunta si desea hacer otra operacion, si el usuario escribe NO ahi se finaliza el programa
