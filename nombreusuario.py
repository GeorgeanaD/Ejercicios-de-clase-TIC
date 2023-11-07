def contrasena():
  palabra =input("introduce tu nombre: ")
  apellido= input("introduce tu apellido: ")
  cadena= palabra[0:3]+apellido[0:3]
  print("tu nuevo nombre es: ",cadena)
  nuevaCadena = cadena.upper()
  print("EN MAYÚSCULAS: ", nuevaCadena)
  
contrasena()