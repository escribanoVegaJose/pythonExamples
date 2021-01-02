# ¿En que se basan las sentencias de control de flujo?
# print ('¿Quieres acabar con el mundo?\n')
# .-Sentencias if
#  if condicionante:
#      sentencias
# .-Sentencias else
# .-Ejemplo donde se muestre un ejemplo y combinación con operadores lógicos
# inputUser = input()
# if inputUser == 'yes' or inputUser == 'y':
#     print('Lanzando misil...')
# elif inputUser == 'no' or inputUser == 'n':
#     print('Cancelando el lanzamiento')

# .-for loops
listaCompra = ['manzanas', 'peras', 'platanos']
for frutaDeLaLista in listaCompra:
    print(frutaDeLaLista+'\n')

# .-while loops
count= 1
while count <=5: 
    print(count)
    count+=1
print("se ha acabado")

# .-switch, interruptor con varias salidas(Entrada->Multi salidas)
diaElegido= int(input())

if diaElegido == 1:
	print('lunes')
elif diaElegido == 2:
	print('martes')
elif diaElegido == 3:
	print('miércoles')
elif diaElegido == 4:
	print('jueves')
elif diaElegido == 5:
	print('viernes')
elif diaElegido == 6:
	print('sábado')
elif diaElegido == 7:
	print('domingo')
else:
	print('no existe')