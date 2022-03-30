# -*- coding: utf-8 -*-
"""Clase 4 - Controladores de Flujo 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Obj3xcYaiARNbCbEYAxtDBHfhE3SwxPA

#Repaso de la clase anterior
"""

#variables

doc = int ( input("\nPor favor, ingresar su documento:\n") )

altura = float ( input("\nPor favor, ingresar tu altura:\n") )   

peso = float ( input("\nPor favor, ingresar tu peso:\n") )

lista_datos_persona = [doc, altura, peso]

lista_datos_persona

lista_datos_persona[1]

sum(lista_datos_persona)

#Estados lógicos---- 0 - 1  ---- False --- True

peso == altura

#IMC
#Fórmula: peso (kg) / [estatura (m)]^2

imc = peso/(altura)**2
print(imc)

#Nivel de IMC ---> Que hacer en caso de...?

#print
"""
print("Datos",altura,peso)            #separar con comas
print("Datos"+str(altura)+str(peso))  #separar con + (concatenar)
print(f"Datos: {altura} {peso}")      #utilizar el fstring

"""
#end sirve para separar impresiones con caracteres
print("22",end="-")
print("02",end="-")
print("2022")

"""##if"""

numero = int(input("Ingrese un número: "))

if numero>15:
  print("Todo ok")

#¿Numero par? -- print("Es par")

if numero % 2 == 0:
  print("Es par")

#¿Múltiplo de 3?
if numero%3==0:
  print("Es múltiplo de 3")

#¿Múltiplo de 6?
if numero%2==0 and numero%3==0:
  print("Sí, es múltiplo de 6")

#Ejercicio
#Contraseña: Mayor a 8 caracteres 

contraseña = input("Cree su contraseña: ")

if len(contraseña)>8:
  print("Contraseña correcta")

print("FIN.")

"""## else"""

numero = int(input("Ingrese un número: "))

if numero>15:
  print("Todo ok")

else:
  print("Todo mal")

#Entrar al boliche/discoteca/antro

#Condición: Mayor de edad

edad = int(input("Ingrese su edad: "))

if edad>=18:
  print("Puede pasar.")   #Estará bien?
else:
  print("No puedes pasar.")

#el número mayor
print("Ingrese 3 números distintos")
n1 = int(input("Ingrese el número 1: "))
n2 = int(input("Ingrese el número 2: "))
n3 = int(input("Ingrese el número 3: "))

"""

if n1>n2 and n1>n3:
  print(f"El mayor es {n1}")

if n2>n1 and n2>n3:
  print(f"El mayor es {n2}")

if n3>n1 and n3>n2:
  print(f"El mayor es {n3}")

"""
if n1>n2:

  if n1>n3:
    print(f"El mayor es {n1}")

  else:
    print(f"El mayor es {n2}")

else:

  if n2>n3:
    print(f"El mayor es {n2}")
  
  else:
    print(f"El mayor es {n3}")


#RETO ADICIONAL: el numero menor  - el numero del medio

"""##elif"""

#comandos

comando = input("Ingrese un comando: ")

if comando == "ENTRAR":
		print("Bienvenido al sistema.")
  
elif comando == "SALUDO" or comando=="saludo":
		print("Hola! ¿Cómo estás?")
  
elif comando == "SALIR":
		print("Saliendo del sistema.")
  
else:
		print("No se reconoce el comando.")

#Ejemplo de uso del if/else/elif
#15/08/2000

fecha_nacimiento = input("¿Cuál es tu fecha de nacimiento? ")
dia = int(fecha_nacimiento[0:2])
mes = int(fecha_nacimiento[3:5])
año = int(fecha_nacimiento[6:])

diaActual = 22
mesActual = 2
añoActual = 2022

if añoActual-año>18:
  print("Puede pasar.")  

elif añoActual-año==18:

  if mes<mesActual:
    print("Puede pasar.") 
  
  elif mes == mesActual:

    if dia<=diaActual:
      print("Puede pasar.")
    else:
      print("NO ENTRADA.")
  
  else:
    print("NO ENTRADA")

else:
  print("NO ENTRADA.")

"""## Desafíos"""

#Desafío 1
edad = int(input("¿Cuál es tu edad?"))

if edad>=18:
  print("Eres mayor de edad.")   
else:
  print("No eres mayor de edad.")

#Desafío 2 -- Elaborado por el tutor Matías

"""https://colab.research.google.com/drive/1d2rXNf7bLLJJg_ePH5mVl6ufeAfiQ09t?usp=sharing#scrollTo=c9e7fec0"""