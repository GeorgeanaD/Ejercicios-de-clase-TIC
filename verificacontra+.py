#Este programa lee una contraseña y devuelve si es válida o no, de acuerdo con
#los siguientes criterios:
# 1.Más de 8 carácteres
# 2.Al menos una letra mayúscula X
# 3.Al menos una letra minúscula X
# 4.Al menos un número
# 5.Al menos un carácter especial X
# 6.No tiene espacios en blanco
#FUNCIONES

def verificaLongitud(contraseña):
    longitud=len(contraseña)
    respuesta=False
    if(longitud>=8):
      respuesta=True
      print("la contraseña mide, str(longitud), por lo tanto contiene mas de 8 caracteres")
      
    return(respuesta)
def verificaMayusculas(contraseña):
    respuesta=False
    for cont in range(0,len(contraseña)):
      if (contraseña[cont].isupper()):
        respuesta=True
        print("he encontrado una mayuscula")
    return(respuesta)
def verificaMinusculas(contraseña):
    respuesta=False
    for cont in range(0, len(contraseña)):
      if(contraseña[cont].islower()):
        respuesta=True
        print("he econtrado una minuscula")
    return(respuesta)
def verificaNumeros(contraseña):
    respuesta=False
    for cont in range (0,len(contraseña)):
      if (contraseña[cont].isnumeric()):
        respuesta=True
        print("he encontrado un numero ")
    return(respuesta)
    #verifica si contiene alguno de estos (lista) comparando estos caracteres con cont1
def verificaCaracteresExtraños(contraseña):
    respuesta=False
    lista= "! # $ % &  ( ) * + , - . /  ' : ; < = > ? @ [ ] ^ _` { | } ~  / "
    for cont1 in range (0,len(contraseña)): #la variable cont1 repasa las letras de la contraseña
      for cont2 in range (0,len(lista)):
        if(contraseña[cont1]==lista[cont2]):
          respuesta=True
          print("he encontrado caracteres extraños")
    return(respuesta)
#Programa principal
def verificaContraseña():
  contraseña=input("Ingrese una contraseña: ")
  respuesta=True#Defino una variable que me dice si es correcta
  #La doy por correcta mientras no se demuestre lo contrario
  validez=0
  if (verificaLongitud(contraseña)==True):
    validez=validez+1
  if (verificaMayusculas(contraseña)==True):
    validez=validez+1
  if (verificaMinusculas(contraseña)==True):
    validez=validez+1
  if (verificaNumeros(contraseña)==True):
    validez=validez+1
  if  (verificaCaracteresExtraños(contraseña)==True):
    validez=validez+1
  if(validez==5):
    print ("contraseña valida")
  else:
    print("contraseña invalida")
verificaContraseña()


    

    
    
      
      
    
    
