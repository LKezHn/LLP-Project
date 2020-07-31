# -*- coding: utf-8 -*-

#! Solo estan las gramaticas de variabñes, prints. y comentarios

rubyGrammar = """

    ?start : exp+

    ?exp : var "=" value

    ?var: /[a-zA-Z][\w_]*

    ?value: string
        | number
        | boolean

    ?string: /"[^"]*"/

    ?number: /[0-9]*/

    ?boolean: /[(true)|(false)]

    // Ignorar espacios
    COMMENT: "#" /[^\\n]/*
        | OPEN /[^(CLOSE)]/* CLOSE
    
    OPEN: /\// "comment"
    
    CLOSE: "uncomment" /\//
      
    %ignore COMMENT
    %ignore /\s+/

"""