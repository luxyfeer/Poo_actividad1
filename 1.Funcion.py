# Programa función recursiva elevar:

while True:
	a = float (input ('Por favor ingrese la base:'))
	b = float (input ('Por favor ingrese la potencia:'))
	def power(a,b):
		s=a**b
		return s
	print(a,'^',b,'=',power(a,b))
	c = int (input ('¿Si desea continuar, escriba 1, de lo contrario escriba 0:  '))
	if c==0:
		print ('Programa terminado')
		break
	else:
		continue