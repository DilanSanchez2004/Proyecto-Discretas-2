# Función que pide al usuario cuántas tramas desea ingresar (entre 5 y 20)
def ingresar_datos(): 
    print("📦 Ingreso de número de tramas")
    num_tramas = int(input("🔢 ¿Cuántas tramas deseas ingresar? (entre 5 y 20): "))
    # El numero minimo de tramas debe de ser 5 y el maximo es de 20 tramas
    while num_tramas < 5 or num_tramas > 20:
        print("❌ Número fuera de rango.")
        num_tramas = int(input("🔁 Intenta nuevamente (entre 5 y 20): "))
    return num_tramas

# Función que pide al usuario ingresar las tramas de 32 bits
def validar_trama(trama):
    lista_trama = []
    print("\n📥 Ingreso de tramas (cada una debe tener 32 bits)")
    # Recorremos la cantidad de tramas que el usuario desea ingresar
    for i in range(trama):
        # Solicitamos al usuario que ingrese la trama i+1 (para que se vea desde 1 en lugar de 0)
        cont_trama = input(f"🧬 Trama {i + 1}: ")
        # Validamos que:
        # 1. Todos los caracteres ingresados estén en '0' o '1' (es decir, que sea binario)
        # 2. Que tenga exactamente 32 caracteres (longitud de la trama)
        while not all(bit in '01' for bit in cont_trama) or len(cont_trama) != 32:
            print("❌ Trama inválida. Asegúrate que tenga 32 bits con solo 0 y 1.")
            # Si no cumple, se vuelve a pedir al usuario que ingrese la trama nuevamente
            cont_trama = input(f"🔁 Ingresa de nuevo la trama {i + 1}: ")
        # Si la trama es válida, se guarda en la lista de tramas
        lista_trama.append(cont_trama)
    return lista_trama

# Función que pide los validadores (4 bits por cada trama)
def ingresar_validadores(num_tramas):
    # Creamos una lista vacía para almacenar los validadores que ingresa el usuario
    lista_validadores = []
    # Mostramos un mensaje informativo al usuario para que sepa qué está ingresando
    print("\n🧾 Ingreso de validadores (4 bits cada uno)")
    # Recorremos la cantidad de tramas para pedir un validador por cada una
    for i in range(num_tramas):
        # Pedimos al usuario el validador correspondiente a la trama actual
        validador = input(f"🧩 Validador para la trama #{i + 1}: ")
        # Validamos que el validador:
        # 1. Esté compuesto solo por bits (0 o 1)
        # 2. Tenga exactamente 4 bits de longitud
        while not all(bit in '01' for bit in validador) or len(validador) != 4:
            print("❌ Validador inválido. Debe tener exactamente 4 bits (solo 0 y 1).")
            # Si no cumple con las condiciones, volvemos a pedirlo
            validador = input(f"🔁 Intenta de nuevo el validador #{i + 1}: ")
        # Una vez validado, lo agregamos a la lista de validadores
        lista_validadores.append(validador)
    return lista_validadores

# Función que valida cada trama comparando sus bits de control con su validador correspondiente
def validar_tramas_completas(tramas, validadores):
    # Inicializamos un contador para llevar la cuenta de las tramas que sí son válidas
    tramas_validas = 0
    # Obtenemos el total de tramas que se están evaluando
    total = len(tramas)
    # Mensaje inicial que indica que empieza la validación de cada trama
    print("\n🧪 Resultados de Validación de Tramas")
    # Recorremos cada trama con su índice
    for i in range(total):
    # Extraemos los bits de control desde la posición 10 hasta la 14 (inclusive)
        bits_control = tramas[i][10:15]
        # Tomamos el validador correspondiente a esa trama
        validador = validadores[i]
        # Convertimos los bits de control y el validador a decimal para hacer los cálculos
        numero_control = int(bits_control, 2)
        numero_validador = int(validador, 2)
        # Verificamos si el número de control es múltiplo de 3
        es_multiplo_3 = (numero_control % 3 == 0)
        # Verificamos si la suma del número de control + validador es múltiplo de 5
        es_multiplo_5 = ((numero_control + numero_validador) % 5 == 0)
        # Si se cumplen ambas condiciones, la trama es válida
        if es_multiplo_3 and es_multiplo_5:
            print("   ✅ Trama válida")
            tramas_validas += 1  # Sumamos una trama válida
        else:
            # Si falla alguna condición, es inválida
            print("   ❌ Trama inválida")
    # Ahora evaluamos si la transmisión completa fue válida o no
    # Calculamos la cantidad de tramas inválidas
    errores = total - tramas_validas
    # Si el porcentaje de error es menor al 20%, se considera válida
    if errores / total < 0.2:
        print(f"Transmisión VÁLIDA ✅ (menos del 20% de error -> {errores / total}).")
    else:
        # Si hay demasiados errores, se marca como inválida
        print(f"Transmisión INVÁLIDA ❌ (más del 20% de error -> {errores / total}).")

# Menú principal del programa
def menu():
    while True:
        print("\n🌐 === MENÚ PRINCIPAL ===")
        print("\n Bienvenidos al chuzo calculador de tramas 🙂‍↕")
        print("1. Iniciar Validación de Tramas")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num_tramas = ingresar_datos()
            tramas = validar_trama(num_tramas)
            validadores = ingresar_validadores(num_tramas)
            validar_tramas_completas(tramas, validadores)
        elif opcion == "2":
            print("\n Como último mensaje de despedida del chuzo: ")
            print("\n👋 Gracias por usar el validador de tramas. ¡Hasta luego! \n")
            break
        else:
            print("❗ Opción inválida. Intente nuevamente.")

# Punto de inicio del programa
if __name__ == "_main_":
    menu()
