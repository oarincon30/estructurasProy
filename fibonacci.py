def fibo(n):

	f1 = 0
	f2 = 1
	i = 0

	while i < n:

			ft = f1 + f2
			f1 = f2
			f2 = ft
			i = i + 1

	print("el numero",n,"de la serie es: ", f1)


	pass

#def fibo_rec(n):
#	pass


print(fibo(6))
#print(fibo_rec(10))
