def ingresar_datos():
    num_tramas = int(input("¿Cuántas tramas deseas ingresar? (entre 5 y 20): "))
    while num_tramas < 5 or num_tramas > 20:
        num_tramas = int(input("Número inválido. Ingresa un valor entre 5 y 20: "))
    return num_tramas

def  validar_trama(trama):
    lista_trama = []
    for i in range(trama):
        cont_trama = input(f"Ingrese la trama {i + 1} (debe contener '0' o '1'): ")
        while not all(bit in '01' for bit in cont_trama) or len(cont_trama) != 32:
            cont_trama = input(f"Trama inválida. Ingrese la trama {i + 1} (exactamente 32 bits con '0' o '1'): ")
        lista_trama.append(cont_trama)
    return lista_trama

def control_bits(trama):
    pass
        
        

if __name__ == "__main__":
    print("Bienvenido al validador de tramas")
    num_veces = ingresar_datos()
    print(validar_trama(num_veces))