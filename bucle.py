valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print("Email correcto")
else:
    print('Email incorrecto')


i=1
while i<=5:
    print("Ejecucion "+ str(i))
    i=i+1
print("end--+   ")

edad=int(input("Introduce tu edad: "))
while edad<5 or edad>100:
    print("edad no valida. vuelve a digitar edad")
    edad=int(input("Introduce tu edad: "))
print("edad digitada: "+str(edad))
