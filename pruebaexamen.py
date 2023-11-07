def numero():
  numero1=input("Dime un numero para sumar sus cifras")
  suma=0
  for cont in range (0,len(numero1)):
    suma= suma+ int(numero1[cont])
  print("la suma de sus cifras vale:"+str(suma))
numero()
  
