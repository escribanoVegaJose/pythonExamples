
# Lists

# 1º parte, conceptos básicos
# - explicación 
# - índice, valor + ejemplo
listaCompra= ['manzana','peras','platanos', 1, False, 1.0, True, 'lejia','pipas']
# - Crear listas vacías. 
empty_list = []
print(listaCompra)
# - lista con diferentes objetos 
listaConOtraLista=["string", 0, listaCompra] 

# 2º parte operadores que nos permiten manipular los datos de una lista. 
# - get, editar , eliminar , añadir
# get, coger un valor de la lista 
# print(listaConOtraLista[2][2])

# editar
listaCompra[7]= 'lavavajillas'

#eliminar
listaCompra.remove('platanos')
#añadir 
# insert
listaCompra.insert(2, 'platanos de canarias')
print(listaCompra)

# tamaño de la lista 
print(len(listaCompra))
# index
print(listaCompra.index('platanos de canarias'))

list2= [1,2,3,1,1,1]
# max 
print(max(list2))
# min
print(min(list2))
# count
print(list2.count(1))

# reverse
listaCompra.reverse()
print(listaCompra)
# - operaciones matemáticas sobre la lista 
print(list2 * 3)
# - operador in ya visto en bucles for
print("pipas" in listaCompra)