import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("datos/ventas.csv")

# Calcular ventas totales
df["total"] = df["cantidad"] * df["precio"]
ventas_totales = df["total"].sum()

# Ventas por producto
ventas_por_producto = df.groupby("producto")["total"].sum()

print("Ventas totales:", ventas_totales)
print("\nVentas por producto:")
print(ventas_por_producto)

# Gráfico
ventas_por_producto.plot(kind="bar", title="Ventas por producto")
plt.ylabel("Monto vendido")
plt.tight_layout()
plt.savefig("resultados/ventas_por_producto.png")
plt.close()
