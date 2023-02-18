f = open("prueba.txt","r")
lineas = list(f)
f.close()
for item in lineas:
    print(item)
