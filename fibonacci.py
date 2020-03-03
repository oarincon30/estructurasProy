def fiboCiclos(n):
	f1 = 1
	f2 = 1
	i = 1
	while i < n:

			ft = f1 + f2
			f1 = f2
			f2 = ft
			i = i + 1

	print("(Metodo Ciclos): El numero",n,"de la serie Fibonacci es:", f1)

def fiboRecursivo(n):
	if ((n==1) or (n==2)):
		return 1
	elif n>2:
		return (fiboRecursivo(n-1)+fiboRecursivo(n-2))

num=int(input("\nEscriba un numero mayor que cero: "))
while num < 1:
    num=int(input("\n Escriba un numero mayor que cero: "))

fiboCiclos(num)
print("(Metodo Recursivo): El numero",num,"de la serie Fibonacci es:",fiboRecursivo(num))
