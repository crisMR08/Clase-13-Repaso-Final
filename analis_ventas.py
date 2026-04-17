import pandas as pd
from gestion_ventas import cargar_ventas


def analizar_ventas():
    # 1. Leer las ventas desde el archivo CSV utilizando la función cargar_ventas
    # Estraer el DataFrame de ventas
    df = cargar_ventas("ventas.csv")

    # Trasformar
    if df is None:
        print("No hay ventas para analizar.")
        return

    print("\n--- Análisis de Ventas 📈---")

    # Crear columnas ingresos = cantidad * precio
    df["Ingresos"] = df["Cantidad"] * df["Precio"]

    # Total de ingresos
    total_ingresos = df["Ingresos"].sum()
    print(f"💰Total de Ingresos: **${total_ingresos:.2f}**")

    # Producto más vendido
    producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum().idxmax()
    print(f"📦 Producto más vendido: {producto_mas_vendido}")

    # Cliente con más compras
    cliente_top = df.groupby("Cliente")["Ingresos"].sum().idxmax()
    print(f"👤 Cliente con más compras: {cliente_top}")

    cliente_frecuente = df.groupby("Cliente")["Cliente"].count().idxmax()
    print(f"👤 Cliente con más frecuencia de compras: {cliente_frecuente}")

    print("\n --- Ventas Diarias ---")
    print(df.groupby("Fecha")["Ingresos"].sum().to_string())


if __name__ == "__main__":
    # Cargar las ventas desde el archivo CSV
    analizar_ventas()