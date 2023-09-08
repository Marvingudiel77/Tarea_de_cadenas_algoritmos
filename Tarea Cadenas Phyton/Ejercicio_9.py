# Escribir un programa que pregunte al usuario la fecha de su nacimiento
# en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando el día
# o el mes se introduzcan con un solo carácter.

Fecha_de_nacimiento = input(
    " Ingresa la fecha de tu nacimiento con el siguiente formato: dia/mes/año ")
print('Día', Fecha_de_nacimiento[:2])
print('Mes', Fecha_de_nacimiento[3:5])
print('Año', Fecha_de_nacimiento[6:])
