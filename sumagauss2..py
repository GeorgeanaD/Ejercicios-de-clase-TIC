#este programa suma los nuemros pares por un lado y los impares por otro
def sumagauss2():
  n_final= input("DIME HASTA QUE NUMERO QUIERES QUE CUENTE: ")
  suma_par=0 #es una variable que acumula la suma par
  suma_impar=0 #es una variable que acumula la suma impar
  for cont in range (1,int(n_final)+1):
    if (cont %2==0):
      suma_par=suma_par+cont
    else:
      suma_impar=suma_impar+cont
    #print("ESTA VEZ CON VALE =", str(cont))
    
  print("SUMA ACUMULADA = ", str(suma_acumulada))
sumagauss2()
  
  
  
