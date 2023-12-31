#Busqueda Binaria:

# Resuleve el problema de dos escaleras recostadas contra la pared, se asume el angulo que forma la escalera mas corta con
# el piso -teta- y la distancia entre las dos escaleras esta dada por -w- 


import math

def calculate_h_and_w(L1,L2,teta):

	v = L2 * math.sin(teta)
	w = L2 * math.cos(teta)
	teta1 = math.acos(w/L1)
	z = L1* math.sin(teta1)
	alfa = math.pi- teta - teta1
	x = w * math.sin(teta)/math.sin(alfa)
	h = x*z/L1	

	calculos = [h, w]
	return calculos

def run1():
	epsilon = float(input('valor del paso: '))

	altura_distancia = []

	altura_objetivo = 8.0
	low = 0.0
	high = math.radians(89.0)
	teta = (low + high)/2	

 
	# Longitud de las escaleras
	L2 = 20
	L1 = 30

	altura_distancia = calculate_h_and_w(L1, L2, teta)

	while(abs(altura_objetivo - altura_distancia[0]) >= epsilon):
		print(f' Low = {math.degrees(low)}, High = {math.degrees(high)}, Angulo = {math.degrees(teta)}  altura = {altura_distancia[0]}')

		if altura_distancia[0] < altura_objetivo:
			low = teta
		else:
			high = teta		

		teta = (low + high)/2	
		altura_distancia = calculate_h_and_w(L1,L2, teta)

	print(f' \n distancia entre las dos escaleras es {altura_distancia[1]}')	


#	print(f'\n h = {"% 4.3f" %h}x = {"% 4.3f" %x} alfa = {"% 4.3f" %math.degrees(alfa)}, w = {"% 5.4f" %w}, teta1 = {"% 4.3f" %math.degrees(teta1)}, z = {"% 4.3f" %z}, angulo = {"% 4.3f" %math.degrees(teta)}')


#		print(f'\n  z = {z}, v = {v},   z(2)-v(2) = {z**2 - v**2}, x = {x}, y = {y}')
#	print(f'\n  v = {"% 4.3f" %v}, w = {"% 4.3f" %w}, teta1 = {"% 4.3f" %math.degrees(teta1)}, z = {"% 4.3f" %z}, angulo = {"% 4.3f" %math.degrees(teta)}')




if __name__ == '__main__':
	run1()


#epsilon = 0.1
#paso = epsilon**2 
#respuesta = 0.0

#while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
#    print(abs(respuesta**2 - objetivo), respuesta)
#    respuesta += paso

#if abs(respuesta**2 - objetivo) >= epsilon:
#    print(f'No se encontro la raiz cuadrada {objetivo}')
#else:
#    print(f'La raiz cudrada de {objetivo} es {respuesta}')
#print(math.sqrt(objetivo))    