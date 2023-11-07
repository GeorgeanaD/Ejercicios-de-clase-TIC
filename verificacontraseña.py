#este programa lee una contraseña y dice si es valida o no de acuerdo 
#con los siguientes criterios: 
def verificaContraseña():
  contrasena = input("Ingrese una contraseña: ")
  validez=True #defino una variable que me dice si la contraseña es correcta , 
  #la doy por correcta mientras no se demuestre lo contrario
  longitud= len(contrasena)
  if (longitud <= 8):
    validez=False
    print("longitud incorrecta")
  
  if (contrasena.islower()) or (contrasena.isupper()):
      validez= False
      print("no contiene al menos una minuscula y mayuscula")
  no_numero=0
  for cont in range(0,longitud):
    if (contrasena[cont].isnumeric()):
      no_numero=no_numero+1
      
    if(longitud==no_numero):
          validez=False
          print("NO cumple el criterio de contener al menos un número")
  if(contrasena.isnumeric):
    validez= False
    print("añade caracteres especiales")
  if (validez==True):
    print("Contraseña valida")
  else:
    print("contraseña invalida")
verificaContraseña()
  