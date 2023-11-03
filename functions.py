import numpy as np
import math


# Funcion TF
def TF(matriz):
  matrizTF = []
  for row in matriz:
    auxMatrizTF = []
    for value in row:
      if value > 0:
        auxMatrizTF.append(1 + math.log10(value))
      else:
        auxMatrizTF.append(0)
    matrizTF.append(auxMatrizTF)
  return matrizTF

# Ejemplo de uso ejemplo de clase
#matriz_entrada = np.array([[21, 24, 0, 2 ,2], [24, 59, 2, 1, 0], [40, 115, 8, 10 ,19], [4, 28, 5, 0, 1],
#                           [8, 48, 4, 3, 4], [17, 49, 8, 0, 5]])
# resultado = TF(matriz_entrada)
# print(np.array(resultado))

# Funcion IDF
def IDF(matriz):
  N = len(matriz)
  vectorIDF = []
  for j in range(len(matriz[0])):
    contador = 0
    for i in range(len(matriz)):
      if matriz[i][j] != 0:
        contador += 1
    vectorIDF.append(math.log10(N / contador))
  print(N)
  return vectorIDF

# Ejemplo de uso ejemplo de clase
# matriz_entrada = np.array([[5000, 500000, 10000, 500000, 7000]])
resultado = IDF(matriz_entrada)
print(np.array(resultado))

def eliminar_palabras_de_parada(documentos, palabras_de_parada):
    # Agregar un carácter de nueva línea al final del documento si no está presente.
    if documentos[-1] != '\n':
        documentos += '\n'

    # Eliminar , . : y ;
    for char in [',', '.', ':', ';']:
        documentos = documentos.replace(char, '')

    # Normalizar todas las palabras a minúsculas.
    documentos = documentos.lower()

    # Eliminar las palabras de parada.
    for palabra in palabras_de_parada:
        documentos = documentos.replace('\n' + palabra + ' ', '\n')
        documentos = documentos.replace(' ' + palabra + ' ', ' ')
        documentos = documentos.replace(' ' + palabra + '\n', '\n')

    return documentos


# Main
