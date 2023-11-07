def suma_gauss():
  n_final= input("dime hasta que numero")
  suma_acumulada=0
  for cont in range (1, n_final+ 1):
    suma_acumulada = suma_acumulada+ cont
  print("la suma de los numeros hasta, n_final")
  print ( "=", suma_acumulada)
suma_gauss()

