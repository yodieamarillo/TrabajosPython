## Yodie Amarillo

####
print("Pregunta 1")

cad1 =nombre=input("Nombre: ")
cad2 =edad=input ("Edad: ")
cad3= distrito=input("¿Dónde vives?: ")
print(cad1 +" tiene "+ cad2 +" años y vive en " + cad3+".")

####
print("Pregunta 2")
print("Para calcular el área del círculo, triángulo y cuadrado ingrese los siguientes datos:")
r=int(input("Radio del círculo= "))
b=int(input("Base del triángulo= "))
h=int(input("Altura del triángulo= "))
s=int(input("Lado del cuadrado= "))

import math
circle=math.pi*r**2
triangle=b*h/2
square=s**2

print("El área del círculo es " + str(circle) + " unidades.")
print("El área del triángulo es " + str(triangle) + " unidades.")
print("El área del cuadrado es " + str(square) + " unidades.")

####
print("Pregunta 3")

print("Ingrese 3 números:")

numero_1=int(input("Número 1= "))
numero_2=int(input("Número 2= "))
numero_3=int(input("Número 3= "))

suma=numero_1+numero_2+numero_3
resta=numero_3-numero_2
multip=numero_1*numero_2*numero_3
division=numero_1/numero_2
division_entera=numero_2//numero_3

numero1=str(numero_1)
numero2=str(numero_2)
numero3=str(numero_3)

print("La suma total es "+str(suma))
print("La resta entre " + numero3+" y "+ numero2 + " es " + str(resta))
print("La multiplicación entre todos los números ingresados es " + str(multip))
print("La división de " + numero1+" entre "+ numero2 + " es " + str(division))
print("La división entera de " + numero2+" entre "+ numero3 + " es " + str(division_entera))

####
print("Pregunta 4")

v=input("Ingrese un valor: ")
v1=type(v)

print("El valor ingresado es tipo "+ str(v1))

####
print("Pregunta 5")

import sys
print(sys.argv)

####
print("Pregunta 6")

n=int(input("Ingrese un número: "))
suma=n*(n+1)/2
suma_1=str(suma)
print("La suma de valores hasta el número ingresado es "+ suma_1)

####
print("Pregunta 7")

ingreso=input("Ingrese dos números: ")
valores=ingreso.split(' ')
n1=int(valores[0])
n2=int(valores[1])

if n1==n2:
     print("Los valores ingresados son iguales.") 
elif n1!=n2:
     print("Los valores ingresados son diferentes:")

if n1>n2:
     print("El número primer número es mayor que el segundo.")
elif n2>=n1:
     print("El segundo número es mayor o igual que el primero.")

####
print("Pregunta 8")

pw="contraseña"
pregunta=input("Ingrese la contraseña: ")
contraseña=pregunta.lower()
if pw==contraseña:
    print("La contraseña coincide.")
elif pw!=contraseña:
    print("La contraseña no coincide.")
