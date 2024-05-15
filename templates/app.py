import os
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta del archivo de entrada
input_file_path = "C:\\Users\\alex1\\Desktop\\prueba\\eje2.ods"

# Cargar el archivo Excel
df = pd.read_excel(input_file_path)

# Función para aplicar el símbolo correspondiente según la dirección
def add_symbol(direction, result_dollars):
    if direction == "Buy":
        return "+" + str(result_dollars)
    elif direction == "Sell":
        return "-" + str(result_dollars)
    else:
        return str(result_dollars)

# Comprobar si la columna "Resultado en dólares" ya existe
if "Resultado en dólares" not in df.columns:
    # Multiplicar las columnas "Order amount" y "Average Price" para obtener el valor en dólares
    df["Resultado en dólares"] = df["Order amount"] * df["Average Price"]

# Aplicar la función a cada fila de la columna "Direction" si la columna "Resultado con símbolo" no existe
if "Resultado con símbolo" not in df.columns:
    df["Resultado con símbolo"] = df.apply(lambda row: add_symbol(row["Direction"], row["Resultado en dólares"]), axis=1)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        opcion = request.form["opcion"]
        if opcion == "1":
            # Tu lógica para la opción 1
            return render_template("resultado.html", resultado="Saldo total: " + str(saldo_total_con_simbolo))
        elif opcion == "2":
            # Tu lógica para la opción 2
            return render_template("resultado.html", resultado="Número de operaciones totales realizadas: " + str(num_operaciones))
        elif opcion == "3":
            # Tu lógica para la opción 3
            return render_template("resultado.html", resultado="Saldo total en el rango de fechas: " + str(saldo_total) + "\nNúmero de operaciones en el rango de fechas: " + str(num_operaciones))
        elif opcion == "4":
            # Tu lógica para la opción 4
            return render_template("resultado.html", resultado="Saldo total para el activo: " + str(saldo_total) + "\nNúmero de operaciones para el activo: " + str(num_operaciones))
        elif opcion == "5":
            # Tu lógica para la opción 5
            return render_template("resultado.html", resultado="Archivo 'FINAL.xlsx' generado con éxito.")
        elif opcion == "6":
            return render_template("resultado.html", resultado="Saliendo del programa...")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
