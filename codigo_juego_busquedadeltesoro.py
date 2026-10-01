#lidia paola perez mendez 5to perito contador C
# 1. PRIMERO: Clase Padre
class Inventario:
 
    def __init__(self):
        self.items = []
 
 
# 2. SEGUNDO: Clase Hija
class Puntos(Inventario):
 
    def __init__(self):
        super().__init__()
        self.puntos = 0
 
 
# 3. MENÚ PRINCIPAL
def menu():
    print("\n======================================")
    print("  BIENVENIDO A LA BÚSQUEDA DEL TESORO")
    print("======================================")
    print("1. Iniciar juego")
    print("2. Salir")
    print("======================================")
 
    opcion = input("Selecciona una opción: ")
 
    if opcion == "1":
        juego()
    elif opcion == "2":
        print("\n¡Gracias por jugar!")
    else:
        print("\n[Opción no válida]")
        menu()
 
 
# 4. TERCERO: Juego principal
def juego():
    p, v, pto = (0, 0), 3, Puntos()
 
    mapa = {
        (1, 0): ("obj", "Llave"),
        (0, 1): ("ene", "Orco"),
        (2, 2): ("tesoro", "Tesoro"),
    }
 
    dirs = {
        "norte": (0, 1),
        "sur": (0, -1),
        "este": (1, 0),
        "oeste": (-1, 0)
    }
 
    nombre = input("\nIngresa tu nombre: ")
 
    print(
        f"\n¡Bienvenido, {nombre}!\n"
        f"Pos: {p} | Vidas: {v} | "
        f"Pts: {pto.puntos} | Inv: {pto.items}"
    )
 
    while v > 0:
 
        m = input(
            "\nMovimiento (Norte/Sur/Este/Oeste): "
        ).strip().lower()
 
        if m not in dirs:
            print("[Movimiento no válido]")
            continue
 
        p = (
            p[0] + dirs[m][0],
            p[1] + dirs[m][1]
        )
 
        tipo, *nombre_item = mapa.pop(p, ("nada",))
 
        if tipo == "obj":
            pto.items.append(nombre_item[0])
            pto.puntos += 10
            print(f"¡Encontraste: {nombre_item[0]}!")
 
        elif tipo == "ene":
            v -= 1
            pto.puntos -= 5
            print(f"¡Enemigo!: {nombre_item[0]}")
 
        elif tipo == "tesoro":
            print(
                "¡FELICITACIONES! "
                "Has encontrado el tesoro. Ganaste."
            )
            return
 
        print(
            f"Pos: {p} | Vidas: {v} | "
            f"Pts: {pto.puntos} | Inv: {pto.items}"
        )
 
    print("¡HAS PERDIDO! Te quedaste sin vidas.")
 
 
# 5. CUARTO: Iniciar programa
menu()
 