import statistics as stats
dato1 = int(input("Ingresa el primer numero "))
dato2 = int(input("Ingresa el segundo numero "))
dato3 = int(input("Ingresa el tercer numero "))
if dato1 > 0 and dato2 > 0 and dato3 >0:
    datos = [dato1, dato2, dato3]
    print(stats.mean(datos))  
else:
    print("ingresa valores positivos")

# promedio = sum(datos)/len(datos)
# print(promedio)