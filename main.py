# -*- coding: utf-8 -*-
import sys
from core.recognizer.languageRecognizer import LanguageRecognizer 

errorMessage = "\033[1;31mError: %s." 

if(len(sys.argv[1:]) != 2):
    quit(errorMessage % "El programa necesita dos parámetros")
else:
    if sys.argv[1] == "--what-language-is-this":
        filename = sys.argv[2]
        try:
            f = open(filename,"r")
            (LanguageRecognizer()).recognize(filename,f.read())
        except Exception as e:
            quit(errorMessage % e)
    else:
        quit(errorMessage % "Parámetro incorrecto")
        