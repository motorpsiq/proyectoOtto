print("a) Triangulo")
print("b) Circulo")
print("c) Cuadrado")
print("d) Rombo")

respuesta=input("Que figura quiere calcular (escriba a b c d)" )
if respuesta == "A" or respuesta == "a":
   base = float(input("Escriba la base: "))
   altura = float(input("Escriba la altura: "))
   print(f"Un triangulo de base {base} y altura {altura} "
         f"tiene un area de {base * altura / 2}")
elif respuesta == "B" or respuesta == "b":
    radio = float(input("Escriba el radio: "))
    print(f"Un circulo de radio {radio} tiene un área de  "
          f"{3.141592 * radio**2}")
elif respuesta == "C" or respuesta == "c":
    lado = float(input("Escriba un lado " ))
    print(f"Un Cuadrado tiene en sus lados {lado} y la area es de  "
          f"{lado **2}")
elif respuesta == "D" or respuesta == "d":
    diagonal = float(input("Escriba los diagonal menor: "))
    diagonal2 = float(input("Escriba la digonal mayor: "))
    print(f"el rombo tiene una diagonal menor de {diagonal} y una diagonal mayor de {diagonal2} nos da una area de "
          f"{diagonal2 * diagonal /2}")
