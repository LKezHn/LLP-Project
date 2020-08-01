# -*- coding: utf-8 -*-
import re
from lark import Transformer, v_args

errorMessage = "\033[1;31mError: %s"

@v_args(inline=True)
class Semantic (Transformer):

    def __init__(self):
        self.variables = {}
        self.functions = {}

    def sum (self, A, B):
        return float(A) + float(B)

    def sub (self, A, B):
        return float(A) - float(B)

    def multi(self,A,B):
        return (float(A)*float(B))

    def div(self,A,B):
        return (float(A)/float(B))
    
    #Asigna valor a una variable.
    def assignvar(self, name, value):
        self.variables[name] = str(value)
    
    #Declaración de una variable sin valor. e.g.: 'var = n;'
    def assignvarnone(self, name):
        self.variables[name] = None

    #Declaración de una variable con alguna otra variable o string.
    def assignvaralt(self, name, value, concat):
        self.variables[name] = ("%s %s" % (value,self.getvar(concat)))
    
    #Devuelve el valor de una variable.
    def getvar(self, name):
        return self.variables[name]
    
    #Impresión de 'console.log' con una cadena.
    def print_(self, param):
        print("%s" % self.cleanParam(param))

    #Impresión de 'console.log' con una cadena.
    def print_error(self, param):
        print(errorMessage % self.cleanParam(param))

    #Impresión de 'console.log' con concatenado de una cadena o variable.
    def print_alt(self, param, concat):
        print("%s %s" % (self.cleanParam(param),self.getvar(concat)))
    
    #Impresión de 'console.log' de una variable.
    def printvar(self, name):
        print("%s" % self.cleanParam((self.getvar(name))))

    #Impresión de 'console.log' con concatenado de dos variables.
    def printvar_alt(self, name, concat):
        print("%s %s" % (self.cleanParam(self.getvar(name)),self.getvar(concat)))
    
    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            return param[1:-1]
        return param

    #Guarda el nombre de la función.
    def createfunc(self,val): 
        self.functions[val] = None

    #Devuelve el nombre de la función.
    def getfunc(self,val):
        return self.functions[val]

    #Condicional 'if' sin 'else'
    def ifcondl(self,param1,param2,returnedValue):
        if(self.getvar(param1) < param2):
            print(returnedValue)
        return False
    
    #Condicional 'if' sin 'else'
    def ifcondg(self,param1,param2,returnedValue):
        if(self.getvar(param1) > param2):
            print(returnedValue)
        return False

    #Condicional 'if' sin 'else'
    def ifconde(self,param1,param2,returnedValue):
        if(self.getvar(param1) == param2):
            print(returnedValue)
        return False