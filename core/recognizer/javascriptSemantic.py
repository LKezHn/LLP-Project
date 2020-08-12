# -*- coding: utf-8 -*-
import re
from ..lark import Transformer, v_args

errorMessage = "\033[1;31m%s"
class javascriptSemantic (Transformer):

    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.paramidentifier = {}

    def sum (self,param):
        new,new2 = int(param[0]), int(param[2]) 
        return float(new) + float(new2)

    def sub (self,param):
        new,new2 = int(param[0]), int(param[2]) 
        return float(new) - float(new2)

    def multi(self,param):
        new,new2 = int(param[0]), int(param[2]) 
        return (float(new)*float(new2))

    def div(self,param):
        new,new2 = int(param[0]), int(param[2]) 
        return (float(new)/float(new2))

    #Imprime el length de un string o numero.
    def length(self,param):
        if(self.getvar(param[2]) is None):
            print('Null has no length attribute.')
        elif(isinstance(self.getvar(param[2]),bool)):
            print('Boolean has no length attribute.')
        else:
            print (len(self.cleanParam(self.getvar(param[2]))))
    
    #Asigna valor a una variable.
    def assignvar(self, param):
        if(isinstance(param[3],str)):
            self.variables[param[1]] = self.cleanParam(param[3])
        else:
            self.variables[param[1]] = param[3]

    #Declaración de una variable con alguna otra variable o string.
    def assignvaralt(self, param):
        self.variables[param[0]] = ("%s %s" % (param[1],self.getvar(param[2])))
    
    #Devuelve el valor de una variable.
    def getvar(self, param):
        try:
            return self.variables[param[0]]
        except:
            return self.variables[param]
    
    #Impresión de 'console.log' con una cadena.
    def print_(self, param):
        print("%s" % self.cleanParam(param[2]))

    #Impresión de 'console.log' con un numero.
    def printnum(self,param):
        print(int(param[2]))

    #Impresión de 'console.log' con dos numeros.
    def printnum_alt(self,param):
        print(int(param[2])+int(param[3]))

    #Impresión de 'console.log' con una cadena.
    def print_error(self, param):
        print(errorMessage % self.cleanParam(param[2]))

    #Impresión de 'console.log' con concatenado de una cadena o variable.
    def print_alt(self, param):
        print("%s %s" % (self.cleanParam(param[2]),self.getvar(param[4])))
    
    #Impresión de 'console.log' de una variable.
    def printvar(self, param):
        print("%s" % self.cleanParam((self.getvar(param[2]))))

    #Impresión de 'console.log' con concatenado de dos variables.
    def printvar_alt(self, param):
        if(isinstance(self.getvar(param[2]),str) and isinstance(self.getvar(param[3]),str)):
            print("%s %s" % (self.cleanParam(self.getvar(param[2])),self.cleanParam(self.getvar(param[3]))))
        else:
            print(int(self.getvar(param[2]))+int(self.getvar(param[3])))

    #Limpia las ' "" ' y " '' " a la hora de impresión.
    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            return param[1:-1]
        return param

    def createfunc(self,param): 
        if(len(param) == 8):
            self.functions[param[1]] = param[3]
            self.variables[param[1]] = param[3]
        elif(len(param) == 9):
            self.functions[param[1]] = param[3],param[4]
            self.variables[param[1]] = param[3],param[4]
            #self.variables[param[3]] = None
            #self.variables[param[4]] = None
        elif(len(param) == 7):
            self.functions[param[1]] = 0
            self.variables[param[1]] = 0

    #Ejecución de una función.
    def funcexists(self,param):
        if param[0] in self.functions:
            try:
                param1 = int(param[2])
                param2 = int(param[3])
                if(isinstance(param1,int) and isinstance(param2,int)):
                    print(self.variables)
                    
                    for key, value in self.variables.items():
                        print(key,value)

                    #si es variable y luego numero.
                    #if(isinstance(int(self.getvar(param[2])),int) and isinstance(param2,int)):
                        #self.functions[param[0]] = int(self.getvar(param[2])), new

            except:
                pass
        else:
            raise Exception ("La función no existe.")


    def ifelse(self,param):
        count = 1
        for i in range (len(param)):
            if(param[i] == '>'):
                if(int(self.getvar(param[2])) > int(self.getvar(param[4]))):
                    while param[6+count] != '}':
                        print(param[6+count]) 
                        count += 1
                else:
                    try:
                        while param[18+count] != '}':
                            print(param[18+count]) 
                            count += 1
                    except:
                        while param[10+count] != '}':
                            print(param[10+count]) 
                            count += 1

            elif(param[i] == '<'):
                if(int(self.getvar(param[2])) < int(self.getvar(param[4]))):
                    while param[6+count] != '}':
                        print(param[6+count]) 
                        count += 1
                else:
                    try:
                        while param[19+count] != '}':
                            print(param[19+count]) 
                            count += 1
                    except:
                        while param[10+count] != '}':
                            print(param[10+count]) 
                            count += 1

            elif(param[i] == '=='):
                if(int(self.getvar(param[2])) == int(self.getvar(param[4]))):
                    while param[6+count] != '}':
                        print(param[6+count]) 
                        count += 1
                else:
                    try:
                        while param[18+count] != '}':
                            print(param[18+count]) 
                            count += 1
                    except:
                        while param[10+count] != '}':
                            print(param[10+count]) 
                            count += 1

    #Para '>'
    def ifcondgnames(self, param):
        if(isinstance(param[2],str) and isinstance(param[4],str)):
            if(int(self.getvar(param[2])) > int(self.getvar(param[4]))):
                print(param[7])
            else:
                pass     

    #Para '>'
    def ifcondg(self,param):
        if(isinstance(param[2],str) and isinstance(param[4],str)):
            if(int(self.getvar(param[2])) > int(param[4])):
                print(param[7])
            else:
                pass     

    #Para '=='
    def ifcondenames(self,param):
        if(isinstance(param[2],str) and isinstance(param[4],str)):
            if(int(self.getvar(param[2])) == int(self.getvar(param[4]))):
                print(param[7])
            else:
                pass   

    #Para '=='
    def ifconde(self,param):
        if(isinstance(param[2],str)):
            if(int(self.getvar(param[2])) == int(param[4])):
                print(param[7])
            else:
                pass
    
    #Para '<'
    def ifcondlnames(self, param):
        if(isinstance(param[2],str)):
            if(int(self.getvar(param[2])) < int(self.getvar(param[4]))):
                print(param[7])
            else:
                pass

    #Para '<'
    def ifcondl(self,param):
        if(isinstance(param[2],str)):
            if(int(self.getvar(param[2])) < int(param[4])):
                print(param[7])
            else:
                pass

    def whiles(self,param):
        increment = int(self.getvar(param[2]))
        for i in range (len(param)):
            try:
                if(isinstance(int(self.getvar(param[2])),int) and param[3] == '>' and isinstance(int(param[4]),int)):
                    while(increment > int(param[4])):
                        print(param[7])
                        increment += 1

                elif(isinstance(int(self.getvar(param[2])),int) and param[3] == '<' and isinstance(int(param[4]),int)):
                
                    while(increment < int(param[4])):
                        print(param[7])
                        increment += 1

                elif(isinstance(int(self.getvar(param[2])),int) and param[3] == '==' and isinstance(int(param[4]),int)):
                
                    while(increment < int(param[4])):
                        print(param[7])
                        increment += 1
            except:
                pass

            try:
                if(isinstance(int(self.getvar(param[2])),int) and param[3] == '>' and isinstance(int(self.getvar(param[4])),int)):

                    while(increment > int(self.getvar(param[4]))):
                        print(param[7])
                        increment += 1

                elif(isinstance(int(self.getvar(param[2])),int) and param[3] == '<' and isinstance(int(self.getvar(param[4])),int)):
                
                    while(increment < int(self.getvar(param[4]))):
                        print(param[7])
                        increment += 1

                elif(isinstance(int(self.getvar(param[2])),int) and param[3] == '==' and isinstance(int(self.getvar(param[4])),int)):
                
                    while(increment < int(self.getvar(param[4]))):
                        print(param[7])
                        increment += 1
            except:
                pass

    def fors(self,param):
        increment = int(self.getvar(param[2]))
        for increment in range(int(param[8])):
            print(param[13])


    def returnrecur(self, param):
        #print(param[3],param[7])
        pass
    
    def boolt(self,A):
        return True
    
    def boolf(self,A):
        return False
    
    def booln(self,A):
        return None
    
    def eos(self,param):
        return param[0]

    def consolelogfunc(self,param):
        print(self.cleanParam(param[2]))

    def consoleloglengthfunc(self,param):
        if(self.getvar(param[2]) is None):
            print('Null has no length attribute.')
        elif(isinstance(self.getvar(param[2]),bool)):
            print('Boolean has no length attribute.')
        else:
            print(len(self.cleanParam(self.getvar(param[2]))))

    def consolelogatomfunc(self,param):
        print(int(param[2])+int(param[3]))

    def consolelogsifunc(self,param):
        print("%s %s" % (self.getvar(param[4]),self.cleanParam(param[2])))

    def consolelogidentfunc(self,param):
        print(self.cleanParam(self.getvar(param[2])))

    def consolelogident_altfunc(self, param):
        if(isinstance(self.getvar(param[2]),str) and isinstance(self.getvar(param[3]),str)):
            print("%s %s" % (self.cleanParam(self.getvar(param[2])),self.cleanParam(self.getvar(param[3]))))
        else:
            print(int(self.getvar(param[2]))+int(self.getvar(param[3])))

    def consoleerrorfunc(self,param):
        print(self.cleanParam(param[2]))

    def consolelogcond(self,param):
        return self.cleanParam(param[2])

    def consoleloglengthcond(self,param):
        if(self.getvar(param[2]) is None):
            return('Null has no length attribute.')
        elif(isinstance(self.getvar(param[2]),bool)):
            return('Boolean has no length attribute.')
        else:
            return(len(self.cleanParam(self.getvar(param[2]))))

    def consolelogatomcond(self,param):
        return (int(param[2])+int(param[3]))

    def consolelogsicond(self,param):
        return("%s %s" % (self.getvar(param[4]),self.cleanParam(param[2])))

    def consolelogidentcond(self,param):
        return self.cleanParam(self.getvar(param[2]))

    def consolelogident_altcond(self, param):
        if(isinstance(self.getvar(param[2]),str) and isinstance(self.getvar(param[3]),str)):
            return("%s %s" % (self.cleanParam(self.getvar(param[2])),self.cleanParam(self.getvar(param[3]))))
        else:
            return(int(self.getvar(param[2]))+int(self.getvar(param[3])))

    def consoleerrorcond(self,param):
        return self.cleanParam(param[2])

    def opsum(self,param):
        return param[0]

    def opsub(self,param):
        return param[0]

    def opmult(self,param):
        return param[0]

    def opdiv(self,param):
        return param[0]

    def ifw(self,param):
        return param[0]

    def elsew(self,param):
        return param[0]

    def funcw(self,param):
        return param[0]

    def retw(self,param):
        return param[0]

    def whilew(self,param):
        return param[0]

    def leftpar(self,param):
        return param[0]

    def rightpar(self,param):
        return param[0]

    def varkeyword(self,param):
        return param[0]

    def leftbrace(self,param):
        return param[0]

    def rightbrace(self,param):
        return param[0]

    def opequals(self,param):
        return param[0]

    def opcompare(self,param):
        return param[0]

    def opgrtrthan(self,param):
        return param[0]

    def oplessthan(self,param):
        return param[0]

    def forw(self,param):
        return param[0]
