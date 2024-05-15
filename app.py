import os
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta del archivo de entrada
input_file_path = "C:\\Users\\alex1\\Desktop\\prueba\\FINAL.xlsx"

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        opcion = request.form["opcion"]
        if opcion == "1":
            # Tu lógica para la opción 1
            df["Positivos"] = df["Resultado con símbolo"].astype(str).apply(lambda x: float(x[1:]) if x.startswith('+') else 0)
            df["Negativos"] = df["Resultado con símbolo"].astype(str).apply(lambda x: float(x[1:]) if x.startswith('-') else 0)
            suma_positivos = df["Positivos"].sum()
            suma_negativos = df["Negativos"].sum()
            saldo_total = suma_positivos - suma_negativos
            saldo_total_con_simbolo = "+" + str(saldo_total) if saldo_total >= 0 else str(saldo_total)
            return render_template("resultado.html", resultado="Saldo total: " + saldo_total_con_simbolo)
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
