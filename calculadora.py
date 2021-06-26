print("Esta es una calculadora....")
print("Ingrese 1 para sumar...")
print("Ingrese 2 para restar...")
print("Ingrese 3 para multiplicar...")
print("Ingrese 4 para dividir...")

operacion = int(input(""))
if operacion == 1:
    numero1 = float(input("Ingrese el primer numero a sumar:  "))
    numero2 = float(input("Ingrese el segundo numero a sumar:  "))
    suma = numero1 + numero2
    print("la suma es:  " , suma)
    
if operacion == 2:
    numero1 = float(input("Ingrese el minuendo:  "))
    numero2 = float(input("Ingrese el sustraendo:  "))
    resta = numero1 - numero2
    print("la resta es:  " , resta)

if operacion == 3:
    numero1 = float(input("Ingrese el multiplicando :  "))
    numero2 = float(input("Ingrese el multiplicador :  "))
    multiplicacion = numero1 * numero2
    print("la multiplicacion es:  " , multiplicacion)


if operacion == 4:
    numero1 = float(input("Ingrese el dividendo :  "))
    numero2 = float(input("Ingrese el divisor :  "))
    division = numero1 / numero2
    print("la division es:  " , division)



