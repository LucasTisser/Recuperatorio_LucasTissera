def inicializar_matriz(cant_filas:int, cant_col:int, valor_inicial:any) -> list:
    empresa = []
    for i in range(cant_filas):
        deposito = [valor_inicial] * cant_col
        empresa += [deposito]
    return empresa

def cargar_stock(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0:
                productos = int(input(f"Ingrese cantidad de productos a agregar al deposito de Rosario: "))
                matriz[i][j] += productos
            elif i == 1:
                productos = int(input(f"Ingrese cantidad de productos a agregar al deposito de Cordoba: "))
                matriz[i][j] += productos
            elif i == 2:
                productos = int(input(f"Ingrese cantidad de productos a agregar al deposito de Salta: "))
                matriz[i][j] += productos
            elif i == 3:
                productos = int(input(f"Ingrese cantidad de productos a agregar al deposito de Bahia Blanca: "))
                matriz[i][j] += productos
    return matriz

def mostrar_depositos_stock_5000(matriz: list) -> list:
    for i in range(len(matriz)):
        acumulador = 0
        for j in range(len(matriz[i])):
            acumulador += matriz[i][j] 
        if acumulador > 5000 :
            if i == 0:
                deposito = "Rosario"
                print(f"El deposito de {deposito} tiene mas de 5000 unidades, {acumulador} en total")
            elif i == 1:
                deposito = "Cordoba"
                print(f"El deposito de {deposito} tiene mas de 5000 unidades, {acumulador} en total")
            elif i == 2:
                deposito = "Salta"
                print(f"El deposito de {deposito} tiene mas de 5000 unidades, {acumulador} en total")
            elif i == 3:
                deposito = "Bahia Blanca"
                print(f"El deposito de {deposito} tiene mas de 5000 unidades, {acumulador} en total")

def mostrar_insumos_stock_3000(matriz: list) -> list :
    for i in range(len(matriz)):
        acumulador = 0
        for j in range(len(matriz[i])):
            acumulador += matriz[i][j] 
        if acumulador > 3000 :
            if i == 0:
                deposito = "Rosario"
                print(f"El deposito de {deposito} tiene mas de 3000 unidades, {matriz[i]} son los productos")
            elif i == 1:
                deposito = "Cordoba"
                print(f"El deposito de {deposito} tiene mas de 3000 unidades, {matriz[i]} son los productos")
            elif i == 2:
                deposito = "Salta"
                print(f"El deposito de {deposito} tiene mas de 3000 unidades, {matriz[i]} son los productos")
            elif i == 3:
                deposito = "Bahia Blanca"
                print(f"El deposito de {deposito} tiene mas de 3000 unidades, {matriz[i]} son los productos")

def identificar_deposito_mayor_cantidad_insumo(matriz: list) -> str:
    acumulador_general = []
    for i in range(len(matriz)):
        acumulador = 0
        for j in range(len(matriz[i])):
            acumulador += matriz[i][j]
        acumulador_general += [acumulador]
        #Incompleto

matriz_vacia = inicializar_matriz(4,5,0)
productos_cargados = cargar_stock(matriz_vacia)
insumos_stock_3000 = mostrar_insumos_stock_3000(productos_cargados)
depositos_stock_5000 = mostrar_depositos_stock_5000(productos_cargados)
identifica_deposito_mayor_cantidad_insumo = identificar_deposito_mayor_cantidad_insumo(productos_cargados)