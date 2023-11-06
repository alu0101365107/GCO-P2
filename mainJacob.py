# Pactica de GCO pruebas de Jacob
import numpy as np
import json
import math
import sys
import argparse

# Funcion que lee el documento
def read_document(document_file):
    with open(document_file, 'r') as file:
        content = file.read()
    return content

# Funcion que lee el corpus
def Read_corpus(corpus_file):
    with open(corpus_file, 'r') as file:
        corpus = json.load(file)
    return corpus



# Funcion que limpia los documentos, quitandoles las stopWords
def clean_documents(document, stop_words):
    # Leemos el documento y lo guardamos en una variable
    document = read_document(document)
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
    corpus = Read_corpus(corpus_file)
    # Hago un bucle que recorra el documento y si ve la palabra en el corpus la cambia por su valor
    for it, value in corpus.items():
        document = document.replace('\n' + it + " ", '\n' + value + " ")
        document = document.replace(" " + it + " ", " " + value + " ")
        document = document.replace(" " + it + '\n', " " + value + '\n')
    return document

def generate_matriz(document):
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
def write_document(document, name):
    with open(name, 'w') as file:
        file.write(document)

def print_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

# Funcion que genera la matriz TF, segun la formula dada en los apuntes
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

# Funcion que genera la matriz IDF, segun la formula dada en los apuntes
def idf(matriz_file):
    N = len(matriz_file)
    num_document = len(matriz_file[0])
    # Inicializar un vector IDF con ceros
    vector_idf = np.zeros(num_document)
    for j in range(num_document):
        # Contar cuántos documentos contienen el término en la columna j
        document_with_term = sum(1 for i in range(N) if matriz_file[i][j] > 0)
        if document_with_term > 0:
            # Calcular el IDF y almacenarlo en el vector IDF
            vector_idf[j] = math.log10(N / document_with_term)
    return vector_idf

def matriz_TF_IDF(matriz_tf, matriz_idf):
    matriz_tfidf = matriz_tf * np.array(matriz_idf)
    return matriz_tfidf


def similarity_cos(documet1, document2):
    value = 0
    for i in range(len(documet1)):
        value += documet1[i] * document2[i]
    return value

def comp_doc(normalized_matrix):
  result = []
  for i in range(len(normalized_matrix)):
    for j in range(i + 1, len(normalized_matrix)):
      result.append("Doc " + str(i + 1) + " con el " + str(j + 1) + ": " + format(similarity_cos(normalized_matrix[i], normalized_matrix[j]), ".4f"))
  return result


def len_vectors(matriz):
    tmpMatriz = []
    for i in range(len(matriz)):
        value = 0
        for j in range(len(matriz[i])):
            value += matriz[i][j] ** 2
        value = math.sqrt(value)
        tmpMatriz.append(value)
    return tmpMatriz

def normalizar(matriz, len_vector):
    result = []
    for i in range(len(matriz)):
      row = []
      for j in range(len(matriz[i])):
        row.append(matriz[i][j] / len_vector[i])
      result.append(row)
    return result


# Main del programa
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--f', type=str, help='Nombre del fichero de lectura')
  parser.add_argument('--c', type=str, help='Nombre del fichero que sera usado como corpus')
  parser.add_argument('--s', type=str, help='Nombre del fichero con las stop words')
  args = parser.parse_args(sys.argv[1:])

#   document_file = "./ejemplo.txt"
#   corpus_file = "./corpus/corpus-en.txt"
#   stop_words_file = "./stop_words/stop-words-en.txt"
  document_file = args.f
  corpus_file = args.c
  stop_words_file = args.s
  # Leemos las stop_words y lo dejamos limpio para trabajar con ellas
  stop_words_read = read_document(stop_words_file)
  stop_words = stop_words_read.replace('\r', ' ').split('\n')
  # Limpiamos el documento, es decir, le quitamos las stop_words y los ".", ",", ":", ";"
  document_clean = clean_documents(document_file, stop_words)
  lematizacion = Lematizar(document_clean, corpus_file)
  matriz, words = generate_matriz(lematizacion)
  # Generamos la matriz TF
  matriz_tf = TF(matriz)
  matriz_idf = idf(matriz)
  matriz_tf_idf = matriz_TF_IDF(matriz_tf, matriz_idf)
  len_vector = len_vectors(matriz_tf)
  matriz_normalizada = normalizar(matriz_tf, len_vector)
  pares = comp_doc(matriz_normalizada)
  print(pares)
main()