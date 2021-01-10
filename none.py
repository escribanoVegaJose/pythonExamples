# valor que indica la ausencia del mismo

sumaDummy= 1+1
varNone= None

def functionWithoutReturn ():
  return

gettingValueNone = functionWithoutReturn()

if gettingValueNone == None:
 print ("El valor de la variable es : "+ str(gettingValueNone))
else: 
  print ("El valor de la variable es : indeterminado")
