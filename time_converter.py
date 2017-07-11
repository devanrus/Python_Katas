import re

def convert(time):
    
	hora = ''.join(re.findall(r'\d{2}[:]\d{2}[:]\d{2}', str(time)))
	get_mili = re.findall(r'[.]\d{3}', str(time))

	if get_mili:
		milisegundos = "," + ''.join(re.findall(r'\d+', ''.join(re.findall(r'[.]\d{3}', str(time)))   ))
	else:
		milisegundos = ",000"

	return hora + milisegundos
