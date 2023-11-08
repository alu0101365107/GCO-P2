# Pactica de GCO pruebas de Jacob
import numpy as np
import json
import math
import sys
import argparse
import functions

# Funcion que limpia los documentos, quitandoles las stopWords
def clean_documents(document, stop_words):
    # Leemos el documento y lo guardamos en una variable
    document = functions.read_document(document)
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
def lematizar(document, corpus_file):
    # Leemos el documento y el corpus
    # document = readDocument(document_file)
    corpus = functions.read_corpus(corpus_file)
    # Hago un bucle que recorra el documento y si ve la palabra en el corpus la cambia por su valor
    for it, value in corpus.items():
        document = document.replace('\n' + it + " ", '\n' + value + " ")
        document = document.replace(" " + it + " ", " " + value + " ")
        document = document.replace(" " + it + '\n', " " + value + '\n')
    return document

# Funcion que genera la matriz y el vector de palabras
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

# Funcion que genera la matriz TF, segun la formula dada en los apuntes
def get_tf(matrix):
  matrix_tf = []
  for row in matriz:
    aux_matrix_tf = []
    for value in row:
      if value > 0:
        aux_matrix_tf.append(1 + math.log10(value))
      else:
        aux_matrix_tf.append(0)
    matrix_tf.append(aux_matrix_tf)
  return matrix_tf

# Funcion que genera la matriz IDF, segun la formula dada en los apuntes
def get_idf(matrix_file):
    N = len(matrix_file)
    num_document = len(matrix_file[0])
    # Inicializar un vector IDF con ceros
    vector_idf = np.zeros(num_document)
    for j in range(num_document):
        # Contar cuántos documentos contienen el término en la columna j
        document_with_term = sum(1 for i in range(N) if matrix_file[i][j] > 0)
        if document_with_term > 0:
            # Calcular el IDF y almacenarlo en el vector IDF
            vector_idf[j] = math.log10(N / document_with_term)
    return vector_idf

# Funcion que genera la matriz TF-IDF
def matriz_tf_idf(matrix_tf, matrix_idf):
    matrix_tfidf = matrix_tf * np.array(matrix_idf)
    return matrix_tfidf

# Funcion que calcula la similitud coseno entre dos documentos
def similarity_cos(documet1, document2):
    value = 0
    for i in range(len(documet1)):
        value += documet1[i] * document2[i]
    return value

# Funcion que calcula la similitud coseno entre todos los documentos
def comp_doc(normalized_matrix):
  result = []
  for i in range(len(normalized_matrix)):
    for j in range(i + 1, len(normalized_matrix)):
      result.append("Documento " + str(i + 1) + " con el documento " + str(j + 1) + ": " + format(similarity_cos(normalized_matrix[i], normalized_matrix[j]), ".4f"))
  return result

# Funcion que calcula la longitud de los vectores, ultima cokumna de la matriz diapositiva de los apuntes numero 129
def len_vectors(matrix):
    tmp_matriz = []
    for i in range(len(matrix)):
        value = 0
        for j in range(len(matrix[i])):
            value += matrix[i][j] ** 2
        value = math.sqrt(value)
        tmp_matriz.append(value)
    return tmp_matriz

# Funcion que normaliza la matriz
def normalizes(matrix, len_vector):
    result = []
    for i in range(len(matrix)):
      row = []
      for j in range(len(matrix[i])):
        row.append(matrix[i][j] / len_vector[i])
      result.append(row)
    return result
   
# Main del programa
if __name__ == "__main__":
  # Leemos los argumentos pasados por terminal
  parser = argparse.ArgumentParser()
  parser.add_argument('--f', type=str, help='Nombre del fichero de lectura')
  parser.add_argument('--c', type=str, help='Nombre del fichero que sera usado como corpus')
  parser.add_argument('--s', type=str, help='Nombre del fichero con las stop words')
  args = parser.parse_args(sys.argv[1:])
  # Guardamos los argumentos en variables
  document_file = args.f
  corpus_file = args.c
  stop_words_file = args.s
  result_file = open("result-" + args.f, "w", encoding="utf8")
  # Leemos las stop_words y lo dejamos limpio para trabajar con ellas
  stop_words_read = functions.read_document(stop_words_file)
  stop_words = stop_words_read.replace('\r', ' ').split('\n')
  # Limpiamos el documento, es decir, le quitamos las stop_words y los ".", ",", ":", ";"
  document_clean = clean_documents(document_file, stop_words)
  lematizacion = lematizar(document_clean, corpus_file)
  # Generamos la matriz y el vector de palabras
  matriz, words = generate_matriz(lematizacion)
  # Generamos la matriz TF, IDF, TF-IDF, la longitud de los vectores y la matriz normalizada
  matriz_tf = get_tf(matriz)
  matriz_idf = get_idf(matriz)
  matriz_tfidf = matriz_tf_idf(matriz_tf, matriz_idf)
  len_vector = len_vectors(matriz_tf)
  matriz_normalizada = normalizes(matriz_tf, len_vector)
  # Calculamos la similitud coseno entre todos los documentos
  pares = comp_doc(matriz_normalizada)
  # Escribimos los resultados en el fichero
  result_file = functions.write_results_file(result_file, lematizacion, words, matriz_tf, matriz_idf, matriz_tfidf, len_vector, matriz_normalizada, pares)
  