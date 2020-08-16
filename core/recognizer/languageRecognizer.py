# -*- coding: utf-8 -*-

from ..lark import Lark, Transformer
from .javascriptSemantic import javascriptSemantic
from .rubyGrammar import *
from .bashGrammar import *
from .javascriptGrammar import *
from .RecognizerSemantic import RecognizerSemantic

"""
    Clase encargada de realizar los diferentes análisis para poder reconocer si el codigco analizado pertenece al lenguaje
    Ruby, Bash o Javascript
    @author lemartinezm|unah.hn daniel.arteaga@unah.hn eglopezl@unah.hn brando.fernandez@unah.hn
    @version 0.0.1
"""
class LanguageRecognizer:
    def __init__(self):
        self.isJavascript : bool = True
        self.error = None

    def recognizeJS(self,filename,content):
        errorMessage = "\033[1;31mError: %s."
        if(filename.endswith('.js')):

            parser = Lark(javascriptGrammar, parser="lalr",transformer = javascriptSemantic())
            language = parser.parse
            sample = content
            try:
                language(sample)
            except Exception as e:
                self.isJavascript = False
                quit(errorMessage % e)
        else:
            self.isJavascript = False
            quit(errorMessage % "El archivo no pertenece al lenguaje de Javascript")


    """
        Método encargado de reconocer mediante el análisis sintáctico y semántico si el código leído pertenece
        al lenguaje Ruby o Bash.
        Imprime los resultados si se ha detectado uno de los dos lenguajes antes mencionados, sino lanza una excepción.
        @param filename Refiere al nombre del archivo que se quiere analizar.
        @param content Es el contenido que contiene el archivo que ser quiere analizar.
        @author lemartinezm@unah.hn
    """
    def recognize(self,filename : str,content : str):
        if self.analyze(rubyGrammar, content):
           self.printResults("Ruby",filename, content)
        elif self.analyze(bashGrammar, content):
           self.printResults("Bash",filename, content)
        else:
            raise Exception("El archivo no pertenece al lenguaje Ruby ni al lenguaje Bash") #Debug

    """
        Método encargado de imprimir los resultados si el comtenido analizado pertenece al lenguaje Ruby o Bash, imprime
        imformación como el lenguaje detectado, nombre de archivo y contenido
        @param language Es el lenguaje detectado por el análisis, éste puede ser Ruby o Bash.
        @param filename Nombre del archivo analizado.
        @param content Contenido leido del archivo analizado.
        @author lemartinezm@unah.hn
    """
    def printResults(self, language: str, filename : str, content : str) -> str:
        print("Resultados")
        print("*"*40)
        print("\tLenguaje: %s" % language)
        print("*"*40)
        print("\tNombre de archivo: %s" % filename)
        print("*"*40)
        print(content)
        print("*"*40)

    """
        Método encargado de realizar el análisis sintactico y semantico mediante el uso de Lark, de un contenido para comprobar si
        cumple con la gramática solicitada.
        @author
        @param grammar Archivo que contiene la gramática que se quiere usar para el analisis.
        @param content El contenido que se quiere analizar.
        @return True si el contenido cumple con la gramática.
        @return False si el contenido no cumple con la gramatica. 
    """
    def analyze(self, grammar : str, content : str):
        parser = Lark(grammar, parser="lalr",transformer = RecognizerSemantic())
        language = parser.parse
        sample = content

        try:
            language(sample)
        except Exception as e:
            return False
        return True