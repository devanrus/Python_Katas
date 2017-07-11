def find_missing_numbers(arr):

    if arr:
        incompleto, completo = arr, []
        minimo, maximo = min(incompleto), max(incompleto)

        for b in range (minimo,maximo+1):
            completo.append(b)

        faltante = [item for item in completo if item not in incompleto]

        return faltante
    else:
        return arr
