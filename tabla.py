def tabla() :
  n_tabla=input(" Dime la tabla ")
  print("TABLA DEL:",str(n_tabla) )
  for cont in range (1,11) :
    print(str(n_tabla), "x", str(cont), "=",str(int(n_tabla)*cont))
tabla()