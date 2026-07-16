
menu = """Bienvenido Andres
1. Agregar venta
2. Ver ventas
3. Total vendido
4. Salir\n"""

ventas = []

while True:
    opcion = input(menu).strip() # strip borra espacios en blanco externos
    if opcion == "4":
        break
    
    elif opcion == "1":   # Agregar venta
        
        while True:
            producto = input("producto: ").strip()
            if producto != "":
                break
            else:
                print("No se admiten productos sin valor")
        
        while True:  
            try:                      
                cantidad = int(input("cantidad: "))
                if cantidad <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error: ingresar número válido")                
        
        while True:  
            try:
                precio = float(input("precio: "))
                if precio <= 0.0:
                    raise ValueError
                break
            except ValueError:
                print("Error: ingresar número válido")        
        
        ventas.append({"producto": producto, "cantidad": cantidad, "precio": precio})
                
            
        
    
    elif opcion == "2":  # Ver ventas        
        if len(ventas) == 0:
            print("No hay ventas cargadas")
        else:    
            for i, registro in enumerate(ventas):
                    print(f"{i+1}"
                            ,registro["producto"]
                            ,registro["cantidad"]
                            ,registro["precio"]
                            ,sep = " - ")

    elif opcion == "3":    # Total vendido
        acumulado = sum(item["cantidad"] for item in ventas * item["precio"] for item in ventas)
    
    else:
        print("elija una opcion valida")        

print()
print("fin del programa")