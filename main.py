# -*- coding: utf-8 -*-
import sys
from core.recognizer.languageRecognizer import LanguageRecognizer 
from core.table.Table import Table


errorMessage = "\033[1;31mError: %s." 



if(len(sys.argv[1:]) != 2):
    quit(errorMessage % "El programa necesita dos parámetros")
else:
    if sys.argv[1] == "--what-language-is-this":
        (Table()).printInfoTable(sys.argv[1])
        filename = sys.argv[2]
        try:
            f = open(filename,"r")
            (LanguageRecognizer()).recognize(filename,f.read())
        except Exception as e:
            quit(errorMessage % e)

    elif(sys.argv[1] == "--symbols-table"):
        (Table()).printInfoTable(sys.argv[1])
        filename = sys.argv[2]
        try:
            f = open(filename,"r")
            (LanguageRecognizer()).recognizeJS(filename,f.read())
        except Exception as e:
            quit(errorMessage % e)
    else:
        quit(errorMessage % "Parámetro incorrecto")
        