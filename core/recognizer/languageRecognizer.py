# -*- coding: utf-8 -*-

from ..lark import Lark, Transformer

class LanguageRecognizer:
    def __init__(self): pass

    def recognize(self,filename,content):
        
        # TODO: Hacer las funcioines de procesamiento caracter a caracter para detectar el lenguaje
        
        language : str = "Ruby" #* Seria el lenguaje detectado por elñ analisis
        self.printResults(language,filename,content)

    def printResults(self, language: str, filename : str, content : str) -> str:
        print("Resultados")
        print("*"*60)
        print("*\t%s" % language)
        print("*"*60)
        print("*\t%s" % filename)
        print("*"*60)
        print(content)
        print("*"*60)