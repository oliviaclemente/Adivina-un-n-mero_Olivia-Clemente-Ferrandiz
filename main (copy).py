def pedir_numero():
  while True:
    entrada = input("Introduzca un num del 0 al 99:")
    try: 
     entrada: int(entrada)
    except: 
     pass
    else:
     if 0 <= entrada <= 99:
       return entrada
print("Intentar adivinar num:")
num= pedir_numero()
while True:
  inte = pedir_numero()
  if inte < num:
     print("num muy pequeño:")
  elif inte > num:
     print("num muy grande:")
  else:
    print("Perfecto!!")
    break
  