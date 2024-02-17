# -*- coding: utf-8 -*-
"""punto 1.5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X7Ed7ZM0BcEq2fttGivEuFm6eh-b58vK
"""

def palabras_con_mismos_caracteres(lista): # Lista
  lista_copia = [] # Lista copia
  lista_pal_rep = [] # Lista por si hay palabras repetidas
  lista_repetidos = [] # Lista de caracteres repetidos

  for n in lista: # Ciclo for para cada palabra de la lista
    n = ''.join(sorted(n)) # Organiza la palabra en orden alfabetico (paz = apz)
    lista_copia.append(n) # Se agrega en la lista copia

  for j in range(len(lista)): # Ciclo para dato 1
    for l in range(len(lista)): # Ciclo para dato 2
      if j == l: # Si estan en la misma posición
        continue # Continuamos, DUHHH seria bobo comparar dos cosas
      else: # En caso de que no
        if lista[j] == lista[l]: # Si hay dos elementos iguales que no sean de la misma posición
          if lista[j] in lista_pal_rep: # Si ya esta el elemento no lo agrega
            continue # Continua al siguiente dato
          else: # En caso de que no
            lista_pal_rep.append(lista[j]) # Agrega el elemento a la lista de palabras repetidas

  for i in range(len(lista_copia)): # Ciclo 1 para dato 1
    for k in range(len(lista_copia)): # Ciclo para datos 2
      if i == k: # Si estan en la misma posición
        continue # Continuamos, DUHHH seria bobo comparar dos cosas
      else: # En caso de que no
        if lista_copia[i] == lista_copia[k]: # Si hay dos elementos iguales que no sean de la misma posición
          if lista[i] in lista_repetidos: # Si ya esta el elemento no lo agrega
            continue # Continua al siguiente dato
          else: # En caso de que no
            lista_repetidos.append(lista[i]) # Agrega el elemento a la lista de repetidos

  lista_repetidos = lista_repetidos + lista_pal_rep # Sumamos la lista de repetidos con la lista de palabras repetidas
  return lista_repetidos

if __name__ == "__main__": # Función main
  datos = int(input("Ingresa las pañabras que deseas agregar: ")) # Ingrese el número de palabras que quiere agregar
  lista = [] # Lista vacia
  for n in range(datos): # Ciclo for para agregar el número de datos
    palabra = input("Ingresa el número: ") # Ingresa las palabras
    lista.append(palabra) # Agregarlo a la lista
  print("Esta es tu lista: \n"+ str(lista)) # Imprime la lista
  ejec =  palabras_con_mismos_caracteres(lista) # Ejecuta el resultado
  print("La lista de palabras que repiten caracteres es: \n"+ str(ejec)) # Imprime el resultado final