# Pactica de GCO pruebas de Jacob
import numpy as np
import json
import math

# Funcion que lee el documento
def readDocument(document_file):
    with open(document_file, 'r') as file:
        content = file.read()
    return content

# Funcion que lee el corpus
def ReadCorpus(corpus_file):
    with open(corpus_file, 'r') as file:
        corpus = json.load(file)
    return corpus



# Funcion que limpia los documentos, quitandoles las stopWords
def cleanDocuments(document, stop_words):
    # Leemos el documento y lo guardamos en una variable
    document = readDocument(document)
    document = " " + document
    # Compruebo que si no tiene \n al final se lo añado, para saber en todo momento donde estan los articulos y pueda limpiar bien los documentos
    if not document.endswith("\n"):
        document += "\n"
    # Eliminamos las , . : ; de los documentos
    document = document.replace(',', '')
    document = document.replace('.', '')
    document = document.replace(':', '')
    document = document.replace(';', '')
    # Pasamos todas las palabras a minusculas
    document = document.lower()
    # Eliminamos las stopwords
    for stop_word in stop_words:
        document = document.replace(" " + stop_word + " ", " ")
        document = document.replace('\n' + stop_word + " ", "\n")
        document = document.replace(" " + stop_word + '\n', "\n")
    return document

# Funcion que lematiza el documento, es decir coge la palabra que esta en el corpus y la sustituye por la que nos indica.
def Lematizar(document, corpus_file):
    # Leemos el documento y el corpus
    # document = readDocument(document_file)
    corpus = ReadCorpus(corpus_file)
    # Hago un bucle que recorra el documento y si ve la palabra en el corpus la cambia por su valor
    for it, value in corpus.items():
        document = document.replace('\n' + it + " ", '\n' + value + " ")
        document = document.replace(" " + it + " ", " " + value + " ")
        document = document.replace(" " + it + '\n', " " + value + '\n')
    return document

def generateMatriz(document):
    # Obtengo todas las palabras (columna)
    words = document.replace('\n', ' ').split(' ')
    # Elimino los espacion en las palabras [ a ] -> [a]    
    for i in range(len(words)):
        words[i] = words[i].strip()
    # Elimino las palabras repetidas
    words = np.unique(words)
    # El primer elemento es un espacio en blanco, lo elimino
    words = words[1:]
    # Creo la matriz
    result = []
    # spliteo por los \n para obtener cada articulo y eliminamos el ultimo elemento que es un espacio en blanco
    document = document.split('\n')[:-1]
    for i in range(len(document)):
        auxDoc = document[i].replace('\n', ' ').split(' ')
        tmpMatriz = []
        for j in range(len(words)):
            contador = 0
            for k in range(len(auxDoc)):
                if words[j] == auxDoc[k].strip():
                    contador += 1
            tmpMatriz.append(contador)
        result.append(tmpMatriz)
    return result, words

# Funcion write que guarda el docuemnto en un fichero.txt para poder visualizarlo
def writeDocument(document, name):
    with open(name, 'w') as file:
        file.write(document)

def printMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

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

def main():
  document_file = "./documents-01.txt"
  corpus_file = "./corpus/corpus-en.txt"
  stop_words_file = "./stop_words/stop-words-en.txt"
  # Leemos las stop_words y lo dejamos limpio para trabajar con ellas
  stop_words_read = readDocument(stop_words_file)
  stop_words = stop_words_read.replace('\r', ' ').split('\n')
  # Limpiamos el documento, es decir, le quitamos las stop_words y los ".", ",", ":", ";"
  document_clean = cleanDocuments(document_file, stop_words)
  lematizacion = Lematizar(document_clean, corpus_file)
  matriz, words = generateMatriz(lematizacion)
  # Generamos la matriz TF
  matrizTF = TF(matriz)
  printMatriz(matrizTF)
  # print(words[31])
main()


## Dried es la posision 31 de la matriz TF
# El valor de Tf de dried debe de ser 