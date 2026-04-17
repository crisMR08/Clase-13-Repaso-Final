from datetime import datetime, date
import csv
import pandas as pd


def ingresar_ventas():
    """Función para ingresar nuevas ventas y guardarls en un archivo CSV."""
    Ventas = []  # Lista para almacenar las ventas ingresadas
    IVA = 0.13  # Tasa de IVA del 13%
    fecha = ""
    cliente = ""
    while True:
        try:
            nombre_producto = input("Ingrese el nombre del producto: ").upper()
            cantidad = int(input("Ingrese la cantidad vendida: "))
            precio = float(input("Ingrese el precio unitario: "))
            if fecha == "" or cliente == "":
                fecha = datetime.strptime(
                    input("Ingrese la fecha de la venta (YYYY-MM-DD): "), "%Y-%m-%d"
                ).date()
                cliente = input("Ingrese el nombre del cliente: ")

            # Validaciones de datos
            if cantidad <= 0:
                print("❌ La cantidad debe ser un número positivo.")
                continue
            if precio < 0:
                print("❌ El precio debe ser un número positivo.")
                continue
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingrese los datos correctamente.")
            continue

        # Crear un diccionario con los datos de la venta
        venta = {
            "Producto": nombre_producto,
            "Cantidad": cantidad,
            "Precio": precio,
            "Fecha": fecha,
            "Cliente": cliente,
        }
        Ventas.append(venta)
        continuar = input("¿Desea ingresar otra venta? (s/n): ").lower()
        if continuar != "s":
            if not guardar_ventas(Ventas):
                print(
                    "❌ Error al guardar las ventas INGRESE NUEVAMENTE LOS PRODUCTOS."
                )
                break
            print("\n-- Ticket de Venta --")
            print(f"Cliente: {Ventas[0]['Cliente']} | Fecha: {Ventas[0]['Fecha']} ")
            for venta in Ventas:
                # Imprime los detalles de cada venta ingresada en un sola linea con formato de ticket
                print("-" * 100)
                print(
                    f"Producto: {venta['Producto']} | Cantidad: {venta['Cantidad']} | Precio: ${venta['Precio']:.2f} | Subtotal: ${venta['Cantidad'] * venta['Precio']:.2f}"
                )
            subtotal = sum(
                v["Cantidad"] * v["Precio"] for v in Ventas
            )  # Calcula el subtotal sumando el precio total de cada venta (cantidad * precio)
            iva = (
                subtotal * IVA
            )  # Calcula el IVA multiplicando el subtotal por la tasa de IVA (13%)
            print("""Subtotal: ${:.2f}""".format(subtotal))
            print("""IVA (13%): ${:.2f}""".format(iva))
            print("Total a pagar: ${:.2f}".format(subtotal + iva))
            break


def guardar_ventas(Ventas):
    """ "Función para guardar las ventas en un archivo CSV."""
    ARCHIVO_CSV = "ventas.csv"
    if not (Ventas):
        print("No hay ventas para guardar.")
        return False
    try:
        # Abrir el archivo CSV en modo escritura y guardar las ventas utilizando csv.DictWriter
        with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
            campos = ["Producto", "Cantidad", "Precio", "Fecha", "Cliente"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            if archivo.tell() == 0:  # Si el archivo está vacío, escribir la cabecera
                writer.writeheader()
            for venta in Ventas:
                writer.writerow(venta)
            print(f"Ventas guardadas exitosamente en {ARCHIVO_CSV}.")
            return True
    except Exception as e:
        print(f"Error al guardar las ventas en el archivo CSV: {e}")
        return False


def cargar_ventas(archivo_csv="ventas.csv"):
    """Funciónn para cargar las ventas desde un archivo CSV."""
    try:
        ventas = pd.read_csv(archivo_csv)
        print(f"Se cargaron {len(ventas)} registros desde {archivo_csv}.")
        return ventas
    except FileNotFoundError:
        print(f"❌ El archivo {archivo_csv} no se encontró.")
        return None
    except Exception as e:
        print(f"Error al cargar las ventas desde el archivo CSV: {e}")
        return None


if __name__ == "__main__":
    print(cargar_ventas())