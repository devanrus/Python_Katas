import re

def travel(r, zipcode):

    split_dir = r.split(",")
    direcciones, numeros = [], []

    for i in range(len(split_dir)):

        numero = re.findall(r'\d+', split_dir[i])[0]
        cp = ' '.join(re.findall(r'[A-Z]{2} \d{5}',split_dir[i]))
        direccion = ' '.join(re.findall(r'\w[a-z.]+', split_dir[i]))

        if cp == zipcode:
            direcciones.append(direccion)
            numeros.append(numero)

    return zipcode + ":" + ",".join(direcciones) + "/" + ",".join(numeros)
