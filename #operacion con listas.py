#operacion con listas
#Quintana Maria Jose
frutas = ['manzana', 'pera', 'uva', 'mango']
 
print(frutas[0]) # mostrar la primera fruta
print(frutas[-1]) # mostrar ultima fruta
 
frutas[1]= 'naranja' # notificacion de posición 1
frutas.append('kiwi') # Agregar al final
frutas.insert(1, 'fresa') # Insertar en posición 1
frutas.remove('uva') # Eliminar la 1ra.
frutas.pop(0) # Eliminar y retornar el indice