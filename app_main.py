import os
from gestion_ventas import ingresar_ventas
from analis_ventas import analizar_ventas


def limpiar_pantalla():
    """Limpia la pantalla de la consola v1."""
    if os.name == "nt":  # Para Windows
        os.system("cls")
    else:  # Para Unix/Linux/Mac
        os.system("clear")


def menu():
    """Función principal del menú del sistema de gestión de ventas."""
    while True:
        limpiar_pantalla()
        print("\n --- 🛒 Menú Principal ---")
        print("1. Ingresar nuevas ventas (Guardar en ventas.csv)")
        print("2. Analizar ventas (Requiere archivo de ventas en formato CSV)")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ingresar_ventas()
        elif opcion == "2":
            analizar_ventas()
        elif opcion == "3":
            print("¡Gracias por usar el sistema de gestión de ventas! ¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida. Por favor, seleccione una opción del menú.")
        input("Presione Enter para continuar...")


if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de ventas!")
    menu()

