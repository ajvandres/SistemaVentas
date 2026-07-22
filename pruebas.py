ventas = []

ventas.append({"producto": "Mouse", "cantidad": 2, "precio": 1500})
ventas.append({"producto": "Teclado", "cantidad": 5, "precio": 1800})

# acumulado = sum(itemCant["cantidad"] * itemCant["precio"] for itemCant in ventas)
# print("Total Vendido:", f"{acumulado:.2f}")


listadoVentas = []
if not ventas:
    print("No hay ventas cargadas")
else:    
    for i, venta in enumerate(ventas):        
        listadoVentas.append(str(i+1) + " - "
                    +str(venta["producto"]) + " - " 
                    +str(venta["cantidad"]) + " - "
                    +str(venta["precio"])
                    )
print("".join(listadoVentas))
