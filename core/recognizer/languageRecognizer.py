# -*- coding: utf-8 -*-

from ..lark import Lark, Transformer

class LanguageRecognizer:
    def __init__(self):
        """
            #! La idea es que si al terminar de analizar los dos atributos son falsos entonces retorne que el archivo no pertenece a ninguno.
            #! Y cuando uno de los dos sea verdadero entonces ese es el lenguaje detectado.
        """
        self.isRuby : bool = False
        self.isBash : bool = False
        self.isJavascript : bool = False

    def recognize(self,filename,content):
        
        # TODO: Hacer las funciones de procesamiento caracter a caracter para detectar el lenguaje.
        language : str = "Ruby" #* Seria el lenguaje detectado por el analisis
        self.printResults(language,filename,content)

    def printResults(self, language: str, filename : str, content : str) -> str:
        print("Resultados")
        print("-"*40)
        print("\tLenguaje: %s" % language)
        print("-"*40)
        print("\tNombre de archivo: %s" % filename)
        print("-"*40)
        print(content)
        print("-"*40)
