# -*- coding: utf-8 -*-
import re

class Table:
    def __init__(self): pass

    def printInfoTable(self,param):
            print("*"*40)
            print("{1} {0:36s} {1}".format("","*"))
            print("{1} {0:36s} {1}".format("Intérprete de Lenguajes","*"))
            print("{1} {0:36s} {1}".format("@authors:","*"))
            print("{1} {0:31s} {1}".format("\tlemartinezm@unah.hn","*"))
            print("{1} {0:31s} {1}".format("\tdaniel.arteaga@unah.hn","*"))
            print("{1} {0:31s} {1}".format("\teglopezl@unah.hn","*"))   
            print("{1} {0:31s} {1}".format("\tbrando.fernandez@unah.hn","*"))
            print("{1} {0:31s} {1}".format("\tcorreos","*"))
            print("{1} {0:36s} {1}".format("@version 0.0.1","*"))
            print("*"*40)
            print("{1} {0:36s} {1}".format("Opción Elegida:","*"))
            print("{1} {0:31s} {1}".format("\t%s" % param,"*"))
            print("{1} {0:36s} {1}".format("","*"))
            print("*"*40)

    def symbolTable(self,text):
        result = []

        text = re.sub(r"/\/.*/"," ",text)
        text = re.sub(r"\/\*[\s\S]*?\*\/"," ",text)
        text = re.sub(r"<"," < ",text)
        text = re.sub(r">"," > ",text)
        text = re.sub(r"\(" , " ( ", text)
        text = re.sub(r"\)" , " ) ", text)
        text = re.sub(r"\*" , " * ", text)
        text = re.sub(r","," , ",text)
        text = re.sub(r";"," ; ",text)
        text = re.sub(r"\s+"," ",text)

        tokens = re.split("( |\\\".*?\\\"|'.*?')", text)
        for token in tokens:
            token = ("%s".strip() % token).strip()
            if len(token) > 0:

                if re.match(r"(if|else|while|for|return|var|function|console.log|console.error)",token):
                    result += [["Keyword","%s" % token]]

                elif re.match(r"\"[^\"]*\"",token):
                    result += [["Identifier","%s" % token]]

                elif re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$",token):
                    result += [["Identifier","%s" % token]]
                    
                elif re.match(r"^(=|\+|\-|\*|==|<|>|\(|\)|{|})$",token):
                    result += [["Operator","%s" % token]]

                elif re.match(r"^\d+\.\d+$",token):
                    result += [["Number","%s" % token]]

                elif re.match(r"^\d+$",token):
                    result += [["Number","%s" % token]]

                elif re.match(r"^(;|,)$",token):
                    result += [["Operator","%s" % token]]

                else:
                    pass
        return result
