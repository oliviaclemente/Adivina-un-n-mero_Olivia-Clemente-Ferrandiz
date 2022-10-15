min=0
max=99
def pedir_numero(invitación, minimo, maximo):
  invitación += "entre" + str(minimo) + "y" + str(maximo) +     ":"
  while True:
    entrada = input(invitación)
    try: 
       entrada: int(invitación)
    except: 
       pass
    else:
       if minimo <= entrada <= maximo:
         return entrada
minimo=maximo=0
while True:
  minimo = pedir_numero("Añade el minimo:")
  maximo = pedir_numero("Añade el maximo:")
  if minimo < maximo:
    break

minimo= min
maximo= max
num= pedir_numero("Adivine un num", min,max)
while True:
  inte = pedir_numero("Adivine un num", min,max)
  if inte < num:
     print("num muy pequeño:")
  elif inte > num:
     print("num muy grande:")
  else:
    print("Perfecto!!")
    break
  