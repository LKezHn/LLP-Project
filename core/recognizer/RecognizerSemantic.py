# -*- coding: utf-8 -*-

import re

from ..lark import Transformer, v_args

@v_args(inline=True)
class RecognizerSemantic(Transformer):
    def __init__(self):
        self.variables = {}
        self.function = {}

    def sum(self,A,B):
        return float(A) + float(B)
    