# Escribir un programa que pregunte el correo electrónico del usuario
# en la consola y muestre por pantalla otro correo electrónico con el
# mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo_electronico = input(" ingresa tu correo electrónico: ")
print(correo_electronico[:correo_electronico.find('@')] + '@ceu.es')
