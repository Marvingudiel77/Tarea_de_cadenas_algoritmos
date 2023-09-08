# Escribir un programa que pregunte el nombre del usuario en la consola
# y un número entero e imprima por pantalla en líneas distintas el nombre
# del usuario tantas veces como el número introducido.

nombre_de_usuario = input(" Ingresa Tu Nombre Porfavor ")
numero_entero = input(" Ingrese cuantas veces quiere imprimir su nombre ")
print((nombre_de_usuario + "\n") * int(numero_entero))
