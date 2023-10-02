#Define una variable de cada tipo de primitivo
numeros=24
decimales=24.6
mujer=False
oraion ="str"

#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
concatena = oraion + " " +str(numeros) + " " +str(decimales)+" "+str(mujer)
print(concatena)
#Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
# investigacion = "int" = Python para losnumeros enteros "int" no hay límite .
# "float"=Los float a diferencia de los int tienen unos valores mínimo y máximos que pueden representar. La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308.

#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable.

n = 24
respuesta =  0
for i in range (2,24+1,2):

    respuesta += i

    print(respuesta)