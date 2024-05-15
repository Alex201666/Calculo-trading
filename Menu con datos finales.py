import os
import pandas as pd

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

while True:
    # Mostrar menú de opciones
    print("Menú:")
    print("1. Calcular saldo total")
    print("2. Número de operaciones totales realizadas")
    print("3. Generar archivo con los resultados (FINAL.xlsx)")
    print("4. Salir")

    # Solicitar la opción al usuario
    opcion = input("Seleccione una opción (1, 2, 3, 4): ")

    # Opción 1: Calcular saldo total
    if opcion == "1":
        # Separar resultados positivos y negativos en diferentes columnas
        df["Positivos"] = df["Resultado con símbolo"].apply(lambda x: float(x[1:]) if x.startswith('+') else 0)
        df["Negativos"] = df["Resultado con símbolo"].apply(lambda x: float(x[1:]) if x.startswith('-') else 0)

        # Calcular la suma de los resultados positivos y negativos
        suma_positivos = df["Positivos"].sum()
        suma_negativos = df["Negativos"].sum()

        # Calcular el saldo total
        saldo_total = suma_positivos - suma_negativos

        # Agregar el símbolo "+" o "-" al saldo total
        saldo_total_con_simbolo = "+" + str(saldo_total) if saldo_total >= 0 else str(saldo_total)

        # Mostrar el saldo total
        print("Saldo total:", saldo_total_con_simbolo)

    # Opción 2: Número de operaciones totales realizadas
    elif opcion == "2":
        # Obtener el número de filas del DataFrame menos la primera (encabezados de columna)
        num_operaciones = len(df) - 1
        print("Número de operaciones totales realizadas:", num_operaciones)

    # Opción 3: Generar archivo con los resultados
    elif opcion == "3":
        # Ruta del archivo de salida
        output_file_path = os.path.join(os.path.dirname(input_file_path), "FINAL.xlsx")
        # Guardar el DataFrame con los resultados en un nuevo archivo Excel
        df.to_excel(output_file_path, index=False)
        print(f"Archivo '{output_file_path}' generado con éxito.")

    # Opción 4: Salir del programa
    elif opcion == "4":
        print("Saliendo del programa...")
        break

    # Opción inválida
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1, 2, 3, 4).")
