# -*- coding: utf-8 -*-
import re
from ..lark import Transformer, v_args

errorMessage = "\033[1;31m %s"

@v_args(inline=True)
class javascriptSemantic (Transformer):

    def __init__(self):
        self.variables = {}
        self.functions = {}

    def sum (self,A,op,B):
        return float(A) + float(B)

    def sub (self, A, op, B):
        return float(A) - float(B)

    def multi(self,A, op, B):
        return (float(A)*float(B))

    def div(self,A, op, B):
        return (float(A)/float(B))

    #Imprime el length de un string o numero.
    def length(self,param,param2,param3,param4,param5):
        if(self.getvar(param3) is None):
            pass
        elif(isinstance(self.getvar(param3),bool)):
            pass
        else:
            print(len(self.cleanParam(self.getvar(param3))))
    
    #Asigna valor a una variable.
    def assignvar(self, keyword, name, param, value, param2):
        self.variables[name] = value

    #Declaración de una variable con alguna otra variable o string.
    def assignvaralt(self, name, value, concat):
        self.variables[name] = ("%s %s" % (value,self.getvar(concat)))
    
    #Devuelve el valor de una variable.
    def getvar(self, name):
        return self.variables[name]
    
    #Impresión de 'console.log' con una cadena.
    def print_(self, param,param2,value,param4,param5):
        print("%s" % self.cleanParam(value))

    #Impresión de 'console.log' con un numero.
    def printnum(self,param,param2,value,param4,param5):
        print(int(value))

    #Impresión de 'console.log' con dos numeros.
    def printnum_alt(self,param,param2,value,value2,param5,param6):
        print(int(value)+int(value2))

    #Impresión de 'console.log' con una cadena.
    def print_error(self, param,param2,value,param4,param5):
        print(errorMessage % self.cleanParam(value))

    #Impresión de 'console.log' con concatenado de una cadena o variable.
    def print_alt(self, param, param2,value,param4,value2,param6,param7):
        print("%s %s" % (self.cleanParam(value),self.getvar(value2)))
    
    #Impresión de 'console.log' de una variable.
    def printvar(self, param,param2,value,param4,param5):
        print("%s" % self.cleanParam((self.getvar(value))))

    #Impresión de 'console.log' con concatenado de dos variables.
    def printvar_alt(self, param,param2,value,value2,param5,param6):
        if(isinstance(self.getvar(value),str) and isinstance(self.getvar(value2),str)):
            print("%s %s" % (self.cleanParam(self.getvar(value)),self.cleanParam(self.getvar(value2))))
        else:
            print(int(self.getvar(value))+int(self.getvar(value2)))
    
    #Limpia las ' "" ' y " '' " a la hora de impresión.
    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            return param[1:-1]
        return param

    #Guarda el nombre de la función.
    def createfunc(self,param,name,param3,funcparam,param5,param6,param7,param8): 
        self.functions[name] = funcparam 
        #name es el nombre de la función y funcparam es el parametro de la función.
    
    def createfuncs(self,param,name,param3,funcparam,funcparam2,param6,param7,param8,param9):
        self.functions[name] = funcparam, funcparam2

    def createfun(self,param,name,param3,param4,param5,param6,param7):
        self.functions[name] = 0

    #Devuelve el nombre de la función.
    def getfunc(self,name):
        return self.functions[name]

    #Ejecución de una función.
    def exefunc(self,name,param2,param3,param4,param5):
        if name in self.functions:
            pass
            #si la función existe hacer el llamado y ejecutarla.
        else:
            raise Exception ("La función no existe")

    def boolt(self,A):
        return True
    
    def boolf(self,A):
        return False
    
    def booln(self,A):
        return None