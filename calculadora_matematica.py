\print ("¡Bienvenido a nuestra calculadora matematica!")
def Menu():
print """
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir"""



def Calculadora():



"""Funcion Para Calcular Operaciones Matematicas"""



Menu()
opc = int(input("Selecione Opcion\n"))
while (opc >0 and opc <5):



"""Funcion para sumar"""
x = int(input("Ingrese Numero\n"))
y = int(input("Ingrese Otro Numero\n"))
if (opc==1):
print "La Suma es:", x+y

"""Funcion para restar"""
opc = int(input("Selecione Opcion\n"))
elif(opc==2):
print "La Resta es:",x-y



Calculadora()
