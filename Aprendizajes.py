git commit -m "validacion y logica de flujo a funcion, normaliz prodcuto"

	string.strip() # elimina espacios izquierda y derecha
    
    string.title() # formateo tipo Titulo
    
    while true:
        break   # la condicion de salida se pone dentro y no en la condicion externa
        
    try:
        sentencias
    except ValueError: # except debe indicar tipo de error
        acciones
        mensajeDeError
        
    # Listas
        
        ventas = []
        ventas.append({"producto": "_producto", "cantidad": "_cantidad"})
        
        registros = list(enumerate(ventas))  #lista, contiene tupla, contiene indice y elem dict
        # devuelve [(1,{key1: value1, key2: value2}),(2, {key1: value3, key2: value4})]
        
        for i, registro in enumerate(ventas):  # hace a nivel tupla, 1° indice, 2° registro dicc
            print(i+1, registro["producto"])  # elemento producto del dict
            
    # Sum()
        acumulado = sum(item["cantidad"] * item["precio"] for item in ventas)
        # sumatoria tipo excel power bi, columna generada cantidad * precio
        # select sum(cantidad * precio) from ventas
        

# En muchos casos se habla que es idiomatico en python, Pythonico        

# Return en una funcion equivale a un break