archivo = open('C:/Users/Mañana_posx/Desktop/JordanaSara-P3/archivo3.txt','r')
while True:
  line= archivo.readline()

  if not line:
   break

  print(line.__str__())
  recuento = str(len(line))
  print("Palabras: "+recuento.__str__())

archivo.close()
