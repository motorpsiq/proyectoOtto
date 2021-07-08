print("ingresa el monto gastado en el kiosko")
gasto = float(input())
print("e = Efectivo")
print("t = Tarjeta")
resp = input("Como desea pagar, elija la opcion deseada: ")
if resp == "e" or resp == "E": 
    abonar = gasto - (gasto * 10 /100)
    print("entraste en promo ", abonar)
if resp == "t" or resp == "T":
    abonar = gasto + (gasto * 15 /100)
    print("la tarjeta pone el interes del 15, el total es ", abonar ,"pesos")