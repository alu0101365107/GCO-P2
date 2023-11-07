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
def read_corpus(corpus_file):
    with open(corpus_file, 'r') as file:
        corpus = json.load(file)
    return corpus

def print_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def get_similarity_value(entry):
    parts = entry.split(": ")
    if len(parts) == 2:
        return float(parts[1])
    return 0.0

def write_results_file(result_file, lematizacion, words, matriz_tf, matriz_idf, matriz_tf_idf, len_vector, matriz_normalizada, pares):
    pares_sorted = sorted(pares, key=get_similarity_value, reverse=True)
    data_to_write = [
        ("-- Documentos lematizados --", lematizacion),
        ("\n-- Palabras unicas --", ' '.join(words)),
        ("\n-- Matriz TF --", '\n'.join(' '.join("{:.5f}".format(num) for num in vector) for vector in matriz_tf)),
        ("\n-- Matriz IDF --", '\n'.join("{:.5f}".format(value) for value in matriz_idf)),
        ("\n-- Matriz TF-IDF --", '\n'.join(' '.join("{:.5f}".format(num) for num in vector) for vector in matriz_tf_idf)),
        ("\n-- Len del vector por documento --", '\n'.join("{:.5f}".format(value) for value in len_vector)),
        ("\n-- Matriz normalizada --", '\n'.join(' '.join("{:.5f}".format(num) for num in vector) for vector in matriz_normalizada)),
        ("\n-- Similitud coseno ordenada --", '\n'.join("{}".format(sim) for sim in pares_sorted))
    ]
    for title, content in data_to_write:
        result_file.write(f"{title}\n{content}\n")
    return result_file