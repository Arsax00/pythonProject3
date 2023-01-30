archivo = open('C:/Users/Mañana_posx/Desktop/JordanaSara-P3/archivo1.txt','r')
list = archivo.readlines()
suma = 0

for i in range(len(list)):

 list[i] = int(list[i])


for linea in list:

 suma += linea

print(suma.__str__())
archivo.close()
