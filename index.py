# Definición inicial de la lista
numeros = [10, 5, 7, 2 , 1]
print(f'el valor original de la lista es : {numeros}')

# Modificación: Se cambia el primer elemento (índice 0)
numeros [0] = 111
print(f'el valor actual es : {numeros}')

# Copia de valor: El valor del índice 4 se asigna al índice 1
numeros[1] = numeros[4]
print(f'el nuevo valor es : {numeros}')

print(f'\nlongitud de la lista : {len(numeros)}')

# Eliminación: Se remueve el elemento en la posición 1, desplazando los demás
del(numeros[1])
print(f'nueva longitud : {len(numeros)}')
print(f'\n\nnueva lista es : {numeros}')

# Acceso inverso: Uso de índices negativos para leer desde el final
print(f'{numeros[-1]}')
print(f'{numeros[-2]}')
