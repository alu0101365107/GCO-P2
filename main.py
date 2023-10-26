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
import functions
import argparse
import json


#### Programa principal ####
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--f', type=str, help='Nombre del fichero de lectura')
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

  lines = []
  f = open(args.f, "r")
  for line in f.readlines():
    for word in line.lower().split(" "): #Ponemos todas minisculas y separamos la linea por espacios
      if (word[-1] in special_chars):  #Comprobamos que el ultimo caracter de la palabra no sea especial
        word = word[:-1]
      if not word in stop_words: #Si la palabra no esta en las de parada, metemos esa palabra
        if word in lemma_dict: #Lematizamos si es necesario y tenemos la lematización para esa palabra
          print("La palabra {}, se convierte en {}".format(word, lemma_dict[word]))
          lines.append(lemma_dict[word])
        else:
          print("Se mete la palabra {}".format(word))
          lines.append(word)

  f.close()
  # for line in lines:
  #   print(line)