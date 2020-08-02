# -*- coding: utf-8 -*-

import re

from ..lark import Transformer, v_args, Tree
@v_args(inline=True)
class RecognizerSemantic(Transformer):
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def createfunction(self, name, params, instructions, end):
        #? Para saber cuantos parametros se definen en la funcion
        if isinstance(params,Tree):
            value = len(params.children)
        else: value = 1

        self.functions[name] = value
        
    def callfunction(self, name, params):
        if name in self.functions:
            if isinstance(params, Tree):
                if self.functions[name] == len(params.children):
                    pass
            elif self.functions[name] == 1:
                pass
            else:
                raise Exception("faltan parametros")
        else:
            raise Exception("No existe la funcion")
