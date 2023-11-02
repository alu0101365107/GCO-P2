# Pactica de GCO pruebas de Jacob
import numpy as np
import json

# Funcion que lee el documento
def readDocument(document_file):
    with open('stop_words/stop-words-en.txt', 'r') as file:
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
    with open(document, 'r') as file:
        document = file.read()
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
#documento = ("./documents-01.txt")
#cleanDocuments(documento, stop_words)

# Funcion que lematiza el documento, es decir coge la palabra que esta en el corpus y la sustituye por la que nos indica.
def Lematizar(document_file, corpus_file):
    with open(document_file, 'r') as input_file:
        document = input_file.read()
    with open(corpus_file, 'r') as file:
        corpus = json.load(file)
    # Hago un bucle que recorra el documento y si ve la palabra en el corpus la cambia por su valor
    for it, value in corpus.items():
        document = document.replace('\n' + it + " ", '\n' + value + " ")
        document = document.replace(" " + it + " ", " " + value + " ")
        document = document.replace(" " + it + '\n', " " + value + '\n')
# def main():
    #

#main()

with open('stop_words/stop-words-en.txt', 'r') as file:
    content = file.read()
content = content.replace('\r', '')
stop_words = content.split('\n')
with open('corpus/corpus-en.txt', 'r') as file:
    lematizacion = json.load(file)