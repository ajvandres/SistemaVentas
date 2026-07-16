ventas = []

ventas.append({"producto": "Mouse", "cantidad": 2, "precio": 1500})
ventas.append({"producto": "Teclado", "cantidad": 5, "precio": 1800})

acumulado = sum(itemCant["cantidad"*"precio"] for itemCant in ventas)# * itemPrec["precio"] for itemPrec in ventas)
print(acumulado)