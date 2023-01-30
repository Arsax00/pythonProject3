X= int(input("Escribe un número:"))
Z= int(input("Escribe otro número: "))
archivo= open('C:/Users/Mañana_posx/Desktop/JordanaSara-P3/archivo2.txt','w')
suma = X+Z
archivo.write("La suma de los números "+X.__str__()+" y "+Z.__str__()+" es: "+suma.__str__()+"\n")
resta = X-Z
archivo.write("La resta de los números "+X.__str__()+" y "+Z.__str__()+" es: "+resta.__str__()+"\n")
multi = X*Z
archivo.write("La multiplicación de los números "+X.__str__()+" y "+Z.__str__()+" es: "+multi.__str__()+"\n")
division = X/Z
archivo.write("La división de los números "+X.__str__()+" y "+Z.__str__()+" es: "+division.__str__()+"\n")
archivo.close()
