
def MostrarMenu():
  print("***************************")
  print("      SUPERCALCULADORA     ")
  print("***************************")
  print("1: SUMAR")
  print("2: RESTAR")
  print("3: MULTIPLICAR")
  print("4: DIVIDIR")
  print("---------------------------")
  print("ELIJA SU ELECCIÓN ")
  respuesta=input("ELIJA (1, 2, 3 , 4")
  return(respuesta)
def numeros():
  numero1= int(input("ELIJE UN NUMERO:"))
  numero2= int(input("ELIJE OTRO NUMERO:"))
  opcion=MostrarMenu()
  if opcion==1:
    respuesta=sumar(numero1,numero2)
  if opcion==2:
    respuesta=restar(numero1,numero2)
  if opcion==3:
    respuesta=multiplicar(numero1,numero2)
  if opcion==4:
    respuesta=dividir(numero1,numero2)
  print("Respuesta="+ str(respuesta))
  
def sumar(numero1,numero2):
  respuesta=0
  respuesta= numero1+numero2
  return(respuesta)
  
def restar(numero1,numero2):
  respuesta=0
  respuesta=numero1-numero2
  return(respuesta)
  
def multiplicar(numero1,numero2):
  respuesta=0
  respuesta=numero1*numero2
  return(respuesta)
  
def dividir(numero1,numero2):
  respuesta=0
  respuesta= numero1/numero2
  return(respuesta)
numeros()

  
  