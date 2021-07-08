nombre=input("Digite su nombre: ")
print("Hola ",nombre)
horas=float(input("indique las horas: "))
if horas<12 and horas>4:
    salario=horas*200
else:
    salario=horas*150
print("Estimade 'jaja'," ,nombre, "su sueldo es de", salario)