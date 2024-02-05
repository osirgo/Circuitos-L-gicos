# Compuertas Lógicas - Funciones Lógicas

def Buffer(arg):
	'''
    Ingresa un valor lógico/booleano, y lo devuelve a la salida
    
    Argumento:
    arg. El valor a replicar
    
    Retorno:
    El mismo valor de la entrada
	'''
 
	if isinstance(arg, bool):
		return arg
	elif arg in (0, 1):
		return bool(arg)
	else:
		raise ValueError('La entrada no es booleana o binaria')

def Not(arg):
	'''
    Ingresa un valor lógico/booleano, y lo devuelve el inverso (negado)
    
    Argumento:
    arg. El valor a negar
    
    Retorno:
    El valor negado de la entrada
	'''
 
	if isinstance(arg, bool):
		return not(arg)
	elif arg in (0, 1):
		return not(bool(arg))
	else:
		raise ValueError('La entrada no es booleana o binaria')

def And(*args):
	'''
    Ingresa 2 o más valores lógicos y devuelve True si todos los valores/entradas son True
    
    Argumentos:
    *args. Una tupla de valores/entradas lógicas
    
    Retorno:
    True si todos los valores/entradas son True
    '''
    
	if len(args) >= 2:
		if all([isinstance(e, bool) or e == 1 or e == 0 for e in args]):
			return all([bool(e) for e in args])
		else:
			raise TypeError('Hay entradas no booleanas o no binarias')
	else:
			raise ValueError('Debe ingresar al menos 2 condiciones')

def Or(*args):
	'''
    Ingresa 2 o más valores lógicos y devuelve True si almenos 1 entrada/valor es True
    
    Argumentos:
    *args. Una tupla de valores/entradas lógicas
    
    Retorno:
    True si almenos 1 entrada/valor es True
    '''
    
	if len(args) >= 2:
		if all([isinstance(e, bool) or e == 1 or e == 0 for e in args]):
			if bool(sum((bool(e) for e in args))) == 0:
				return False
			else:
				return True
		else:
			raise TypeError('Hay entradas no booleanas o no binarias')
	else:
		raise ValueError('Debe ingresar al menos 2 condiciones')

def Nand(*args):
	'''
    Ingresa 2 o más valores lógicos y devuelve True si todos los valores/entradas son False
    
    Argumentos:
    *args. Una tupla de valores/entradas lógicas
    
    Retorno:
    True si todos los valores/entradas son False
    '''
    
	return not(And(*args))

def Nor(*args):
	'''
    Ingresa 2 o más valores lógicos y devuelve True si almenos 1 entrada/valor es False
    
    Argumentos:
    *args. Una tupla de valores/entradas lógicas
    
    Retorno:
    True si almenos 1 entrada/valor es False
    '''
    
	return not(Or(*args))

def Xor(*args):
	'''
    Ingresa 2 o más valores/entradas lógicas y devuelve True  
    si un número impar de sus entradas son verdaderas
    
    Argumentos:
    *args. Una tupla de valores/entradas lógicas
    
    Retorno:
    True si un número impar de sus entradas son verdaderas
    '''
    
	if len(args) >= 2:
		if all([isinstance(e, bool) or e == 1 or e == 0 for e in args]):
			if tuple(bool(e) for e in args).count(True)%2 == 0:
				return False
			else:
				return True
		else:
			raise TypeError('Hay entradas no booleanas o no binarias')
	else:
		raise ValueError('Debe ingresar al menos 2 condiciones')

def Xnor(*args):
	'''
    Ingresa 2 o más valores/entradas lógicas y devuelve True  
    si un número par de sus entradas son verdaderas
    
    Argumentos:
    *args. Una tupla de valores/entradas lógicas
    
    Retorno:
    True si un número par de sus entradas son verdaderas
    '''
    
	return not(Xor(*args))

def tabla(E):
	'''
    Genera una tabla/lista de condiciones para evaluar una compuerta lógica
    
    Argumento:
    E. Número de entradas/valores
    
    Retorna:
    Tabla/lista de combinaciones posibles de entradas/valores
    '''
    
	n = 2**E  # Número de filas (grupos de condiciones)
	T = [] # Tabla/Lista de condiciones

	'''
	Cada grupo i corresponde con el número de fila de la matriz T
	en números binarios

	M matriz auxiliar
	'''
	M = [bin(i)[2:].zfill(E) for i in range(n)] # Número i en binario
    
	for i in M:
		f = []  # Lista auxiliar, fila temporal de M
		for c in i:
			f.append(int(c))
		T.append(f)
		del(f)
	del(M)
	return T

def evaluar(T, funcion):
	'''
    Evalúa una tabla/lista de condiciones
    
    Argumentos:
    T. Tabla/lista de combinaciones posibles de entradas/valores
    
    Retorna:
    Valores de salida para cada grupo de condiciones/entradas 
    respecto a cada compuerta lógica
    '''
    
	F = {'Buffer':Buffer, 'Not':Not, 'And':And, 'Nand':Nand, 'Or':Or, 'Nor':Nor, 'Xor':Xor, 'Xnor':Xnor}
	f = funcion

	if isinstance(T, list):
		try:
			if (f in ('Buffer', 'Not')) and len(T[0]) > 1:
				print(f'La tabla de condiciones no corresponde con {f}')
			elif (f in ('And', 'Nand', 'Or', 'Nor', 'Xor', 'Xnor')) and len(T[0]) < 2:
				print(f'La tabla de condiciones no corresponde con {f}')
			else:
				for i in range(len(T)):
					try:
						print(F[f](*T[i]))
					except KeyError:
						print('Función no existe')
						break
		except TypeError:
			print('La tabla contiene datos inválidos')
	else:
		print('No ha ingresado una tabla de condiciones válidas')
