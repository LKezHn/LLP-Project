# -*- coding: utf-8 -*-

import re
from ..lark import Transformer, v_args, Tree

"""
    Clase encargada de revisar la semántica de un codigo, utilizando funcionalidades de Lark.
    @uthor lemartinezm|unah.hn daniel.arteaga@unah.hn eglopezl@unah.hn brando.fernandez@unah.hn
    @version 0.0.1

"""
@v_args(inline=True)
class RecognizerSemantic(Transformer):
    def __init__(self):
        self.variables = {}
        self.functions = {}

    """
        Método encargado de guardar la declaracion de una funcion: nombre, numero de parametros.
        @param name Es el nombre dado a la funcion.
        @param params Numeero de parámetros que se definen para esa función.
        @param instructions Instrucciones que debe realizar la funcion creada.
        @param end Fin de la función.
        @author lemartinezm@unah.hn
    """
    def createfunction(self, name, params, instructions, end):
        #? Para saber cuantos parametros se definen en la funcion
        if isinstance(params,Tree):
            value = len(params.children)
        else: value = 1

        self.functions[name] = value
        
    """
        Método que se encarga de verificar si una función llamada fue declarada con anterioridad.
        @param name Nombre de la función que se quiere ejecutar.
        @param params Numero de argumentos pasados a la funcion llamada.
        @return Exception si el nombre de la función no se encuentra en el diccionario donde se guardan las funciones
        declaradas.
        @return Exception si el numero de parámetros en la función no coincide con el numero de parámetros definidos en la
        declaracion de la función.
        @author lemartinezm@unah.hn
    """
    def callfunction(self, name, params):
        if name in self.functions:
            if isinstance(params, Tree):
                if self.functions[name] == len(params.children):
                    pass
            elif self.functions[name] == 1:
                pass
            else:
                raise Exception("Faltan parametros")
        else:
            raise Exception("No existe la funcion")

    def sum(self,A,B):

        pass#return float(A) + float(B) 

    def sub(self,A,B):

        pass#return float(A) + float(B)

    def mul(self,A,B):

        pass#return float(A) * float(B)

    def div(self,A,B):

        pass#return float(A) / float(B)

    def mod(self,A,B):

        pass#return float(A) % float(B)

    def assignvar(self,name,value):

        self.variables[name] = value

    def getvar(self,name):

        pass#return self.variables[name]   

    def print(self,param):
        pass#print("%s" % self.cleanParam(param))

    def printvar(self,name):

        pass#print("%s" % self.getvar(name))

    def cleanParam(self,param):

        if re.match(r"^(\"[^\"]*\")|('[^']*'))$",param):

            return param[1:-1]
            return param                        


