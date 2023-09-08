# Escribir un programa que pregunte por consola por los productos de una
# cesta de la compra, separados por comas, y muestre por pantalla cada uno
# de los productos en una línea distinta.

Productos_comprados = input(
    ' ingrese el nombre de los productos comprados separados por comas  ')
print(Productos_comprados.replace(',', '\n'))
