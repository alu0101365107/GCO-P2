"""
El software debe proporcionar como salida lo siguiente: 
  - La matriz de utilidad con la predicción de los elementos faltantes en la matriz original.
  - La similaridad entre cada usuario y sus vecinos de acuerdo a la métrica elegida.
  - Los vecinos seleccionados en el proceso de predicción.
  - El cálculo de cada predicción de la matriz de utilidad en base a los vecinos seleccionados.

Como resultado de esta práctica debes entregar lo siguiente:
  - Enlace a repositorio GitHub público con el código fuente del sistema recomendador implementado. Incluye en el README.md del repositorio:
  - Instrucciones de instalación de dependencias, despliegue, etc. del software creado.
  - Descripción del código desarrollado.
  - Ejemplo de uso.
  - Un informe en PDF describiendo el análisis realizado en varios ejemplos y las conclusiones extraídas.
"""
import sys
#import functions
import argparse
import json
import operator
import math


def TFJson(files):
  tf_matrix = {}
  tf_words = {}
  for document, words in files.items():
    for word, count in words.items():
      tf_words.update({word: 1 + math.log10(count)})
    tf_matrix.update({document: tf_words})
    tf_words = {}
  return tf_matrix

def IDFJson(files):
  itf_matrix = {}
  itf_words = {}
  for document, words in files.items():
    total = sum(words.values())
    for word, count in words.items():
      itf_words.update({word: math.log10(total/count)})
    itf_matrix.update({document: itf_words})
    itf_words = {}
  return itf_matrix

## El DF es la suma de las veces que aparece esa palabra en todos los documentos
# El IDF seria calcular el DF / 


#### Programa principal ####
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--f', type=str, help='Nombre del fichero de lectura')
  parser.add_argument('--f2', type=str, help='Nombre del fichero de lectura')
  args = parser.parse_args(sys.argv[1:])

  special_chars = [',', '?', ':', '.', ";", "%"]

  file_stop_words = open('stop_words/stop-words-en.txt')
  stop_words = [word for word in file_stop_words.readlines()]
  file_stop_words.close()

  
  with open('corpus/corpus-en.txt', "r") as file  :
    lemma_dict = json.load(file)
  # for word, lemma in lemma_dict.items():
    # print('Palabra {} se convierte en {}'.format(word, lemma))
  #   lemma_dict[word] = lemma
  # for value in lemma_dict:
  #   print(value)

  allWords = {}
  allFiles = {}
  for file in vars(args):
    f = open(getattr(args, file), "r")
    for line in f.readlines():
      for word in line.lower().split(" "): #Ponemos todas minisculas y separamos la linea por espacios
        if (word[-1] in special_chars):  #Comprobamos que el ultimo caracter de la palabra no sea especial
          word = word[:-1]
        if (len(word) > 2 and word[len(word) - 2] == "."):
          word = word[:-2]
        if not word in stop_words: #Si la palabra no esta en las de parada, metemos esa palabra
          if word in lemma_dict: #Lematizamos si es necesario y tenemos la lematización para esa palabra
            if lemma_dict[word] in allWords:
              allWords[lemma_dict[word]] += 1
            else:
              objectWord = {lemma_dict[word]: 1}
              allWords.update(objectWord)
          else:
            if word in allWords:
              allWords[word] += 1
            else:
              objectWord = {word: 1}
              allWords.update(objectWord)
    sortedAllWords =  dict(sorted(allWords.items(), key=operator.itemgetter(1), reverse=True))
    allFiles.update({getattr(args, file): sortedAllWords})
    allWords = {}
    f.close()
  idf = IDFJson(allFiles)
  for document, words in TFJson(allFiles).items():
    print("El documento {} tiene las siguientes palabaras".format(document))
    for word, count in words.items():
      print("La palabra {} aparece {} con un TF de {} y un IDF de {}".format(word, allFiles[document][word], round(count, 3), round(idf[document][word], 3)))
    print()
  # for line in lines:
  #   print(line)