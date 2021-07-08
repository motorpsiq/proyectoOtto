"""print("ingresa el monto gastado en el comercio")
gasto = float(input())
if gasto >= 1200:
    abonar = gasto - (gasto * 15 /100)
    print("entraste en promo")
if gasto < 1200:
    abonar = gasto
print("debera abonar", abonar)""" 

print("ingresa el monto gastado en el comercio")
gasto = float(input())
if gasto >= 1200:
    abonar = gasto - (gasto * 15 /100)
    print("entraste en promo")
else:
    abonar = gasto
print("debera abonar", abonar)