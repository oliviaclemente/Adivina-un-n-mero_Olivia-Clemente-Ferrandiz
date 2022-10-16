import random
numAleatorio = random.randint(1,99)

def intro():
  print("*"*10, "Adivina el num",""*10)

intro()
def juego():
  int= 0
  while True:
    num = int(input("Añade un num entre 0 y 99: "))
    if num > numAleatorio:
      int += 1
      print("Demasiado grande")
    elif num < numAleatorio:
      int += 1 
      print("Demasiado pequeño")
    else:
      int += 1
      print(f"Ganador!!, el num aleatorio era...{numAleatorio}.")
      input("Intro para salir")
      break

juego()