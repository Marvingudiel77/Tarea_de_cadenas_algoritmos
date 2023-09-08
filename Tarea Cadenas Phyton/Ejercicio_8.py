# Escribir un programa que pregunte por consola el precio de un producto
# en euros con dos decimales y muestre por pantalla el número de euros
# y el número de céntimos del precio introducido.

precio_del_producto = input(
    " Ingresa el precio total del producto con dos decimales: ")
print(precio_del_producto[:precio_del_producto.find('.')], 'euros y',
      precio_del_producto[precio_del_producto.find('.')+1:], 'céntimos.')
