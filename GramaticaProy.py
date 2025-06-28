# Definición de la clase que representa una gramática formal
class Gramatica:
    def __init__(self):
        # # Constructor: se inicializan todos los atributos de la gramática
        self.vocabulario = set()        # Conjunto de símbolos (terminales + no terminales)
        self.terminales = set()         # Conjunto de símbolos terminales
        self.simbolo_inicial = ''       # Símbolo inicial (ej. S)
        self.producciones = {}          # Diccionario de reglas de producción (P)
        self.frases_generadas = []      # Lista para guardar frases generadas

    def ingresar(self):
        # Permite al usuario ingresar los componentes de la gramática
        print("\n--- Ingreso de la Gramática G = (V, T, S, P) ---")
        self.vocabulario = set(input("Vocabulario (separado por espacios): ").split()) # {'a','b','A','B','S'}
        self.terminales = set(input("Terminales (separado por espacios): ").split()) # {'a','b'}
        self.simbolo_inicial = input("Símbolo inicial: ") # 'S'
        self.producciones = {}  # Limpia las reglas anteriores

        # Ingreso de reglas de producción (pueden ser múltiples por no terminal)
        print("Producciones (ej: S->aA). Escriba 'fin' para terminar.") 
        while True:
            regla = input("Regla: ") # S->ABa A->BB B->ab AB->b "fin"
            if regla.lower() == "fin":
                break # Si el usuario escribe "fin" (en mayúsculas o minúsculas), se sale del bucle
            if "->" in regla:
                izq, der = regla.split("->")
                izq = izq.strip() # # Elimina espacios en blanco alrededor del símbolo no terminal
                der = der.strip()
                if izq in self.producciones: # Verifica si la clave izq (un símbolo no terminal) ya existe 
                    self.producciones[izq].add(der) # Si ya existe, agrega la nueva producción al conjunto de producciones 
                else:
                    self.producciones[izq] = {der} # Si no existe, crea un nuevo conjunto con la producción "S": {'ABa'}
            else:
                print("❗ Formato incorrecto. Use el formato A->cadena")

    def mostrar(self):
        # Muestra la gramática actual ingresada
        print("\n--- Gramática actual ---")
        print("Vocabulario:", self.vocabulario)
        print("Terminales:", self.terminales)
        print("Símbolo inicial:", self.simbolo_inicial)
        print("Producciones:")
        #Recorre cada símbolo y su lista de reglas
        for izq, derechos in self.producciones.items():
            #Recorre cada producción individual
            for der in derechos:
                #Muestra la regla en el formato típico de una gramática
                print(f"{izq} -> {der if der != '' else 'ε'}")  # Muestra εpsilon si es cadena vacía

    def modificar(self):
        # Permite modificar cualquier componente de la gramática
        while True:
            print("\n--- Modificar gramática ---")
            print("1. Modificar vocabulario")
            print("2. Modificar terminales")
            print("3. Modificar símbolo inicial")
            print("4. Modificar producciones")
            print("5. Salir")
            opcion = input("Opción: ")
            if opcion == "1":
                self.vocabulario = set(input("Nuevo vocabulario: ").split())
            elif opcion == "2":
                self.terminales = set(input("Nuevos terminales: ").split())
            elif opcion == "3":
                self.simbolo_inicial = input("Nuevo símbolo inicial: ")
            elif opcion == "4":
                print("\n--- Nuevas reglas de producciones ---")
                # Se inicializa un diccionario vacío 
                self.producciones = {}  # Solo limpia y vuelve a ingresar producciones
                print("Ingrese nuevas reglas de producción (ej: A->aB). Escriba 'fin' para terminar.")
                while True:
                    regla = input("Regla: ") # S->ABa A->BB B->ab AB->b "fin"
                    if regla.lower() == "fin":
                        break # Si el usuario escribe "fin" (en mayúsculas o minúsculas), se sale del bucle
                    if "->" in regla:
                        izq, der = regla.split("->")
                        izq = izq.strip() # # Elimina espacios en blanco alrededor del símbolo no terminal
                        der = der.strip()
                        if izq in self.producciones: # Verifica si la clave izq (un símbolo no terminal) ya existe 
                            self.producciones[izq].add(der) # Si ya existe, agrega la nueva producción al conjunto de producciones 
                        else:
                            self.producciones[izq] = {der} # Si no existe, crea un nuevo conjunto con la producción "S": {'ABa'}
                    else:
                        print("❗ Formato incorrecto. Use el formato A->cadena")
            elif opcion == "5":
                # Sale del submenú
                break
            else:
                print("Opción inválida.")

    def verificar_frase(self):
        # Determina si una frase dada pertenece a la gramática (por derivación)
        frase = input("Ingrese la frase que desea verificar: ")
        max_pasos = 1000
        lista = [self.simbolo_inicial]  # Cola de derivaciones
        pasos = 0
        indice = 0
        derivadas_visitadas = set()  # Para evitar repeticiones infinitas

        while indice < len(lista) and pasos < max_pasos:
            actual = lista[indice]
            indice += 1
            pasos += 1
            print(f"Paso {pasos}: {actual}")
            if actual == frase:
                print("✅ La frase SÍ pertenece a la gramática. 🥳")
                return
            # Evitar procesar la misma derivación más de una vez
            if actual in derivadas_visitadas:
                continue
            derivadas_visitadas.add(actual)

            # Reemplaza subcadenas usando las producciones
            for i in range(len(actual)):
                for j in range(i + 1, len(actual) + 1):
                    subcadena = actual[i:j]
                    if subcadena in self.producciones:
                        for prod in self.producciones[subcadena]:
                            nueva = actual[:i] + prod + actual[j:]
                            lista.append(nueva)

        print("❌ La frase NO pertenece a la gramática. 🤡")

    def generar_frases(self, cantidad=10):
        print(f"\n--- Generando hasta {cantidad} frases válidas ---")
        max_longitud = 300000
        generadas = set()
        pendientes = [self.simbolo_inicial]
        visitados = set()

        while pendientes and len(generadas) < cantidad:
            actual = pendientes.pop(0)

            # Evitar repeticiones inútiles
            if actual in visitados:
                continue
            visitados.add(actual)

            # Si ya es terminal completamente, lo agregamos
            if all(c in self.terminales for c in actual):
                generadas.add(actual)
                print("✔", actual)
                continue

            # Si excede longitud razonable, descartamos
            if len(actual) > max_longitud:
                continue

            # Reemplazar subcadenas como en verificar_frase
            for i in range(len(actual)):
                for j in range(i + 1, len(actual) + 1):
                    subcadena = actual[i:j]
                    if subcadena in self.producciones:
                        for prod in self.producciones[subcadena]:
                            nueva = actual[:i] + prod + actual[j:]
                            pendientes.append(nueva)

        self.frases_generadas = list(generadas)

        if not generadas:
            print("❌ No se pudieron generar frases válidas.")
        elif len(generadas) < cantidad:
            print(f"⚠ Solo se pudieron generar {len(generadas)} frases válidas.")

    def menu(self):
        # Menú principal del programa
        while True:
            print("\n========== MENÚ ========== \n")
            print("1. Ingresar gramática ✍")
            print("2. Mostrar gramática 👀")
            print("3. Modificar gramática 🖊")
            print("4. Verificar si una frase pertenece 👌")
            print("5. Generar 10 frases válidas ヾ(•ω•`)o")
            print("6. Salir 💔 ")
            opcion = input("Opción: ")

            if opcion == "1":
                self.ingresar()
            elif opcion == "2":
                self.mostrar()
            elif opcion == "3":
                self.modificar()
            elif opcion == "4":
                self.verificar_frase()
            elif opcion == "5":
                self.generar_frases()
            elif opcion == "6":
                print("\nGracias por usar el programa. ¡Hasta luego! 👋(❁´◡`❁)\n")
                break
            else:
                print("❌ Opción inválida. Intente de nuevo.")

# Inicia el programa
if __name__ == "__main__":
    g = Gramatica()
    g.menu()
