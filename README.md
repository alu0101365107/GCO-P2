# Sistema de recomendación - Modelos basados en el contenido.
Este repositorio contiene la implementación de un sistema recomendador que tiene un modelo basado en el contenido. El sistema de recomendación se basa en la técnica de modelos basados en el contenido mediante una serie de operaciones que nos permiten calcular la similitud entre los usuarios.    

### 🚶🏽‍♂️Autores:
* [Hector Rodríguez Alonso](https://github.com/alu0101365107) (alu0101365107)
* [Jacob Santana Rodríguez](https://github.com/Jacobsrguez) (alu0101330426)
  
## 📌 Introducción
Nuestra aplicación se centra en un sofisticado sistema de recomendación basado en métodos de filtrado colaborativo. Este innovador sistema opera a través de la línea de comandos y recibe tres elementos esenciales: en primer lugar, el documento que será sometido a análisis; en segundo lugar, el corpus que alberga las palabras que se utilizarán para reemplazar ciertas términos específicos; por último, se recibe el documento que contiene las "stop_words", es decir, las palabras que se desean excluir del documento principal.

Una etapa fundamental de preprocesamiento de datos implica la normalización del texto en el documento, que incluye la conversión de todas las palabras a minúsculas y la eliminación de los signos de puntuación que pudieran ser considerados molestos, para lograr un formato óptimo y uniforme. 

Una vez que el documento ha sido formateado adecuadamente, se procede a aplicar las operaciones definidas en los parámetros proporcionados. Esto incluye la eliminación de las "stop_words" y la lematización del texto, lo que resulta en un documento completamente preparado para su análisis y operación.

---
## 🧰 Herramientas
Para el desarrollo de esta práctica, utilizamos las siguientes herramientas:
- Visual Studio Code: Editor de código ampliamente utilizado debido a su facilidad de uso y numerosas extensiones que simplifican el desarrollo.
- Visual Studio Live Share: Esta extensión de Visual Studio Code permitió la colaboración en tiempo real, lo que fue crucial para la comunicación y la resolución de problemas en un entorno colaborativo.
- Git: La elección de Git como sistema de control de versiones garantizó una gestión eficiente de las diferentes versiones del código y facilitó la colaboración en el proyecto, además de mantener un historial completo de cambios.
- Python: Se seleccionó Python como lenguaje de programación debido a su versatilidad y amplia comunidad de desarrollo, lo que facilitó la implementación de la práctica de manera efectiva.
---
## 📦 Instalacion de dependencias 
En esta aplicación, no hemos utilizado muchas dependencias, pero hemos hecho uso de NumPy, que ha sido especialmente valioso para realizar cálculos numéricos y manipular datos en las matrices.
Para instalar NumPy, simplemente ejecute el siguiente comando en su terminal:
```shell
   pip install numpy
```
---
## 
