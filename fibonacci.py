def fibonacci(limite):
    # Inicializamos una lista para almacenar la secuencia de Fibonacci con los dos primeros elementos.
    secuencia = [0, 1]

    # Creamos un bucle para generar la secuencia hasta que el último número más el penúltimo número sean mayores que el límite.
    while secuencia[-1] + secuencia[-2] <= limite:
        # Calculamos el siguiente número en la secuencia sumando los dos últimos números y lo agregamos a la lista.
        siguiente_numero = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente_numero)  # Agregar el siguiente número a la lista de secuencia

    # Devolvemos la secuencia de Fibonacci hasta el límite ingresado.
    return secuencia

if __name__ == "__main__":
    try:
        while True:
            try:
                # Solicitamos al usuario que ingrese el número límite para la secuencia de Fibonacci.
                limite = int(input("Ingrese el número límite para generar la secuencia de Fibonacci -> "))
                if limite < 0:
                    # Verificamos si el número límite es negativo y mostramos un mensaje de error.
                    print("El número límite debe ser mayor a 0.")
                else:
                    # Generamos la secuencia de Fibonacci y la almacenamos en la variable 'fib_secuencia'.
                    fib_secuencia = fibonacci(limite)
                    # Mostramos la secuencia de Fibonacci hasta el límite ingresado.
                    print("Secuencia de Fibonacci hasta el límite {}: {}".format(limite, fib_secuencia))
                    break
            except ValueError:
                # Capturamos la excepción si el usuario ingresa un valor no numérico.
                print("Error: Ingresa un número válido.")
    except KeyboardInterrupt:
        # Capturamos la excepción si el usuario interrumpe el programa con la combinación de teclas Ctrl+C.
        print("\nCerrando Script...")
