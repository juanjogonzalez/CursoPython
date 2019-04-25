#conjunto de elementos que no necesitan orden ni indice

colors = {'red', 'blue', 'green'}
print (type(colors))

colors.add('violet')
print (colors)
colors.remove('green')
print (colors)

del colors
print (colors)