# -*- coding: utf-8 -*-

from ..lark import Lark, Transformer
from .javascriptSemantic import javascriptSemantic
from .rubyGrammar import *
from .javascriptGrammar import *
from .RecognizerSemantic import RecognizerSemantic

class LanguageRecognizer:
    def __init__(self):
        """
            #! La idea es que si al terminar de analizar los dos atributos son falsos entonces retorne que el archivo no pertenece a ninguno.
            #! Y cuando uno de los dos sea verdadero entonces ese es el lenguaje detectado.
        """
        self.isRuby : bool = True
        self.isBash : bool = True
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


    def recognize(self,filename,content):
        
        # TODO: Hacer las funciones de procesamiento caracter a caracter para detectar el lenguaje.
        parser = Lark(rubyGrammar, parser="lalr",transformer = RecognizerSemantic())
        language = parser.parse
        sample = content

        try:
            language(sample)
        except Exception as e:
            self.isRuby = False
            self.error = e

        if self.isRuby:
            self.printResults("Ruby",filename, content)
        #! Aqui seria el analisis de Bash, y si no es ninguno lanza la excepcion
        else:
            raise Exception(self.error) #*Debug

    def printResults(self, language: str, filename : str, content : str) -> str:
        print("Resultados")
        print("-"*40)
        print("\tLenguaje: %s" % language)
        print("-"*40)
        print("\tNombre de archivo: %s" % filename)
        print("-"*40)
        print(content)
        print("-"*40)
