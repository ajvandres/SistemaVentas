# 1 Funciones

def validarCadenaVacia(cadena):
    return cadena != ""

def validarNumero(valor, referencia):
    return valor > referencia

def agregarVenta():
 
    while True:
        producto = input("producto: ").strip().title()
        if producto != "":
            break
        else:
            print("No se admiten productos sin valor")
    
    while True:  
        try:
            cantidad = int(input("cantidad: "))
            if validarNumero(cantidad, 0):
                break
            else:
                print("Error: ingresar valor mayor que cero")        
        except ValueError:
            print("Error: ingresar número válido")
    
    while True:  
        try:
            precio = float(input("precio: "))
            if validarNumero(precio, 0.0):
                break
            else:
                print("Error: ingresar valor mayor que cero")        
        except ValueError:
            print("Error: ingresar número válido")        
    
    ventas.append({"producto": producto, "cantidad": cantidad, "precio": precio})

def mostrarVentas():
    
    if not ventas:
        print("No hay ventas cargadas")
    else:    
        for i, registro in enumerate(ventas):
                print(f"{i+1}"
                        ,registro["producto"]
                        ,registro["cantidad"]
                        ,registro["precio"]
                        ,sep = " - ")
                
def calcularTotal():
    acumulado = sum(itemCant["cantidad"] * itemCant["precio"] for itemCant in ventas)
    print("Total Vendido:", f"acumulado: .2f")    

# 2 Datos

ventas = []

# 3 Programa Principal

menu = """Bienvenido Andres
1. Agregar venta
2. Ver ventas
3. Total vendido
4. Salir\n"""

while True:
    opcion = input(menu).strip() # strip borra espacios en blanco externos
    if opcion == "4":
        break
    
    elif opcion == "1":
        agregarVenta()        
    
    elif opcion == "2":
        mostrarVentas()
    
    elif opcion == "3":
        calcularTotal()
        
    else:
        print("elija una opcion valida")        

print()
print("fin del programa")