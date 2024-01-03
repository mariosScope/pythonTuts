#Learn the basics of python in less than 40 minutes. 
#Start knowing the print command. 

print("Hola mundo")

#Interesting, later we'll see why there is not colon at the end. 

#el pinguino de mario is the sauce of this tutorial set. 
import time

print("Prueba")

#time.sleep(4) #avoid waiting 4 secs

print("Otro mensaje.")

print(5+5)#Esto lo calcularía supuestamente. 

######
#Variables ya!
######

var1 = 5
var2 = 3

print(var1+var2)
print("El resultado de sumar variables es: ",var1+var2)
print(f"El resultado de sumar var1: {var1} y var2: {var2} es: {var1+var2}")

nombre = input("Introduce tu nombre: ")
edad = int(input("Dime tu edad: "))
estatura = float(input("Y tu estatura: "))
print(f"El nombre es: {nombre} y tienes {edad} años con {estatura} metros de estatura")



#Listas
print("WORKING WITH LISTS NOW...")
lista = [1,2,3,45,6,4]
print(lista)
for item in lista:
    print(item)


#Working with files in dir: 

import os
listaDir = os.listdir()
print(listaDir)

#TUPLAS!

tupla = (1,"Hola", "otro mensaje")
print("....WORKING WITH TUPLAS NOW...")
print(tupla)
print("....tUPLAS ARE INMUTABLE......")


#Loops! For and Whiles...!

#Functions: 
def saludos():
    print("Saluditos ")
    print("soes todo!")

def despedidas():
    print("adios")
    print("BYE BYES!")

saludos()
despedidas()

#Condicionales! If y esas cosas.
# elif es elseif
