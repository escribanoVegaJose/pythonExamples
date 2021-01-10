# FUNCIONES
# ¿Qué es una función y para qué sirve?, normas de un código limpio
# Estructura de una función, parámetros de entrada y salida
# estructura -> 
# def  nombre_función (parámetro 1, parámetro 2):

# Ejemplo de las diferentes combinaciones
itemsAvailableList= ["sartén", "hacha", "ruedas", "té"]


# no param de entrada, no devuelve nada
def welcomeMessage():
  print("Bienvenido a shopping market, cargando información...")
  print("por favor, introduzca su nombre de usuario: ")
  
# sí param de entrada, no devuelve nada
def requestUsername(username):
  print ("nombre de usuario disponible, "+username)
  
# sí param de entrada, sí devuelve un valor
def isAvailable (item):
  return item in itemsAvailableList
  
# main
welcomeMessage()
userName = input()
requestUsername(userName)
print("por favor, introduzca el producto que desea comprobar: ")
userBuy= input()
print (isAvailable(userBuy))



 