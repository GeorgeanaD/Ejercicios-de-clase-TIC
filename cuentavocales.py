#este programa cuenta el numero de aes en una palabra
def cuenta_voc():
  #leemos una palabra
  palabra= input("dime una palabra: ")
  #inicilaizamos una varibale que almacene el numero de aes
  numVoc=0
  #recorremos la palabra y preguntamos si la letra es una a

  for cont in range(0,len(palabra)):
    if(palabra[cont]=="A" or palabra[cont]=="a") or (palabra[cont]=="E" or palabra[cont]=="e") or (palabra[cont]=="I" or palabra[cont]=="i") or (palabra[cont]=="U" or palabra[cont]=="u"):
      numVoc= numVoc+1
  print("La palabra",palabra, "tiene ", str(numVoc), "vocales")

  #mostramos el num de aes
cuenta_voc()