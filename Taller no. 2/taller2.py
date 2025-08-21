import csv


ARCHIVO = "clientes.csv"


def leer_clientes():
    clientes = []
    with open(ARCHIVO, newline='', encoding="utf-8") as file:
        lector = csv.DictReader(file)
        for fila in lector:
            clientes.append({
                "Cedula": fila["Cedula"],
                "Nombre": fila["Nombre"],
                "Saldo": float(fila["Saldo"])
            })
    return clientes

# Función 1: Buscar saldo por nombre
def buscar_saldo(nombre):
    clientes = leer_clientes()
    for cliente in clientes:
        if cliente["Nombre"].lower() == nombre.lower():
            return cliente["Saldo"]
    return None

# Función 2: Contar clientes con saldo mayor a 50
def contar_saldos_mayores():
    clientes = leer_clientes()
    return sum(1 for cliente in clientes if cliente["Saldo"] > 50)

# Función 3: Listar clientes ordenados por saldo ascendente
def listar_por_saldo():
    clientes = leer_clientes()
    clientes.sort(key=lambda x: x["Saldo"])
    return clientes


def menu():
    while True:
        print("\n--- MENÚ BANCO ---")
        print("1. Buscar saldo por nombre")
        print("2. Contar clientes con saldo mayor a 50")
        print("3. Listar clientes ordenados por saldo ascendente")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del cliente: ")
                saldo = buscar_saldo(nombre)
                if saldo is not None:
                    print(f"El saldo de {nombre} es: {saldo}")
                else:
                    print("Cliente no encontrado.")

            case "2":
                cantidad = contar_saldos_mayores()
                print(f"Clientes con saldo mayor a 50: {cantidad}")

            case "3":
                clientes = listar_por_saldo()
                print("\nClientes ordenados por saldo:")
                for cliente in clientes:
                    print(f"{cliente['Nombre']} - {cliente['Saldo']}")

            case "4":
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()

