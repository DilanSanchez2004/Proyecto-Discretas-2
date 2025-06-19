def ingresar_datos():
    num_tramas = int(input("¿Cuántas tramas deseas ingresar? (entre 5 y 20): "))
    while num_tramas < 5 or num_tramas > 20:
        num_tramas = int(input("Número inválido. Ingresa un valor entre 5 y 20: "))
    return num_tramas

def  validar_trama(trama):
    lista_trama = []
    for i in range(trama):
        cont_trama = input(f"Ingrese la trama {i + 1} (exactamente 32 bits con '0' o '1'): ")
        while not all(bit in '01' for bit in cont_trama) or len(cont_trama) != 32:
            cont_trama = input(f"Trama inválida. Ingrese la trama {i + 1} (exactamente 32 bits con '0' o '1'): ")
        lista_trama.append(cont_trama)
    return lista_trama

def ingresar_validadores(num_tramas):
    lista_validadores = []
    for i in range(num_tramas):
        validador = input(f"Ingrese el validador para la trama #{i+1} (4 bits): ")
        while not all(bit in '01' for bit in validador) or len(validador) != 4:
            validador = input(f"Validador inválido. Ingrese el validador para la trama #{i+1} (exactamente 4 bits): ")
        lista_validadores.append(validador)
    return lista_validadores

def validar_tramas_completas(tramas, validadores):
    tramas_validas = 0
    total = len(tramas)

    for i in range(total):
        bits_control = tramas[i][10:15]
        validador = validadores[i]

        numero_control = int(bits_control, 2)
        numero_validador = int(validador, 2)

        es_multiplo_3 = (numero_control % 3 == 0)
        es_multiplo_5 = ((numero_control + numero_validador) % 5 == 0)

        if es_multiplo_3 and es_multiplo_5:
            print(f"Trama #{i+1} es válida.")
            tramas_validas += 1
        else:
            print(f"Trama #{i+1} es inválida.")

    # Verificar si el total de errores es menor al 20%
    errores = total - tramas_validas
    if errores / total < 0.2:
        print(f"Transmisión válida (menos del 20% de error -> {errores / total}).")
    else:
        print(f"Transmisión inválida (más del 20% de error -> {errores / total}).")


if __name__ == "__main__":
    print("Bienvenido al validador de tramas")
    num_veces = ingresar_datos()
    lista_tramas = validar_trama(num_veces)
    lista_validadores = ingresar_validadores(num_veces)

    validar_tramas_completas(lista_tramas, lista_validadores)
