myStr = "hola mundo"

#dir -> obtiene la lista de funciones disponibles de un string (en este caso)
#print (dir(myStr))

# print (myStr.upper())
# print (myStr.lower())
# print (myStr.swapcase())
# print (myStr.capitalize())

# print (myStr.replace("hola", "Hello").upper())
# print (myStr.count("o"))
# print (myStr.count(" "))

# print (myStr.startswith("hola"))
# print (myStr.endswith("Mundo"))

# #separa a partir de un espacio (por defecto)
# print (myStr.split())

# #separa a partir de una coma
# print (myStr.split(','))

# # buscar caracteres dentro del string
# # y devuelve la posicion del primer caracter encontrado
# print (myStr.find('o'))

# # largo de la cadena
# print (len(myStr))

# # obtener el indice del caracter
# print (myStr.index('u'))

# # es numero
# print (myStr.isnumeric())

# # es alfanumérico
# print (myStr.isalpha())

print (myStr[1])
print (myStr[-2])

print ("My name is: " + myStr)
print (f"My name is: {myStr}")
print ("My name is: {0}".format(myStr))