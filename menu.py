# 1 Funciones

def esMayorACero(valor):
    return valor > 0

def pedirProducto():
    while True:
        producto = input("producto: ").strip().title()   # Normalizacion dejo para despues
        if producto:  # si la cadena esta vacia devuelve false
            return producto
        else:
            print("No se admiten productos sin valor")
            
def pedirValor(tipo, tipoDato):
    while True:  
        try:
            print(tipo, ": ",sep="", end="")
            valor = tipoDato(input())
            if esMayorACero(valor):
                return valor
            else:
                print("Error: ingresar valor mayor que cero")        
        except ValueError:
            print("Error: ingresar número válido")    



def crearVenta(producto, cantidad, precio):
    return {"producto": producto, "cantidad": cantidad, "precio": precio}
        

def mostrarVentas(ventas):    
    listadoVentas = []
    if not ventas:
        return ["No hay ventas cargadas"]
    else:    
        for i, venta in enumerate(ventas):
            listadoVentas.append(str(i+1) + " - "
                        +venta["producto"] + " - " 
                        +str(venta["cantidad"]) + " - "
                        +str(venta["precio"])
                        )
    return listadoVentas        
                
def calcularTotal(ventas):
    acumulado = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    return acumulado


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
        producto = pedirProducto()
        cantidad = pedirValor("cantidad", int)
        precio = pedirValor("precio", float)
        venta = crearVenta(producto, cantidad, precio)
        ventas.append(venta)
        print("Venta agregada")
    
    elif opcion == "2":
        listadoVentas = mostrarVentas(ventas)
        print("\n".join(listadoVentas))
    
    elif opcion == "3":
        totalVentas = calcularTotal(ventas)
        print("Total Vendido:", f"{totalVentas:.2f}")
        
    else:
        print("elija una opcion valida")
        
    print()        

print()
print("fin del programa")