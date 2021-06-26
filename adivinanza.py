import random
numero = (random.randint(0,66))
print('Bienvenidos al juego de la "adivina el numero"')
print("Empezamos...")
print("Estoy pensando en un numero entre 0 y 66, cual es?")
print("-------------------------")
print("-------------------------")
print("-------------------------")
print("-------------------------")
fin = 0
while (fin == 0):
    minumero = int(input("Ingresa el numero que crees correcto:  "))
    if minumero < numero:
        print("El numero es mas alto!!!... ")
    if minumero > numero:
        if minumero > 66:
            print("El numero es entre 1 y 66!!!!")
        else:
            print("El numero es mas bajo!!!... ")
    if minumero == numero:
        print("BIEN Ganaste!!")
        print("el numero es el", numero)
        fin = 1

        
         