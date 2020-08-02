# -*- coding: utf-8 -*-
"""
    ! Gramaticas terminadas:
    ? Strings, booleanos, ints, floats
    ? Asignación de variables, Método puts
    ? Condicional if
    ? Bucles for y while
    ? Comentarios (Revisar)
    ? Comparaciones
    ? Operaciones aritméticas
    ? Definicion de funcion

    TODO: Falta hacer la gramatica de llamado a funcion, concatenacion en strings.
    TODO: Corregir gramatica de comentario de multiples lineas
"""


rubyGrammar = """

    ?start : exp+

    ?exp : var "=" string -> assignvar
        | var "=" boolean -> assignvar
        | var "=" arithmeticoperation  -> assignvar
        | "puts" "("? string ")"?   -> print
        | "puts" "("? var ")"?  -> printvar
        | arithmeticoperation
	    | conditional
        | loop
        | definefunction
        | return

    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperation "+" arithmeticoperationatom -> sum
        | arithmeticoperation "-" arithmeticoperationatom  -> sub
        | arithmeticoperation "*" arithmeticoperationatom  -> mult
        | arithmeticoperation "/" arithmeticoperationatom  -> div

    ?arithmeticoperationatom: var -> getvar
        | number
        | "-" arithmeticoperation
        | "(" arithmeticoperation ")"
    
    ?return: "return" string
        | "return" number
        | "return" boolean

    ?definefunction: "def" var "("?  params ")"? instruction END 

    ?params: string
        | number
        | var
        | string "," params
        | number "," params
        | var "," params

    ?loop: for
        | while

    ?for: "for" var "in" "(" int ".." int ")" instruction END
    
    ?while: "while" "("? condition ")"? instruction END

    
    ?conditional: "if" "("? condition ")"? instruction END

    ?condition: var compare var
        | var compare number
        | var equals boolean
        | var equals string
        | string equals string
        | number compare number
        
    ?compare: ">"
        | "<"
        | "<="
        | ">="
        | equals
       
    ?equals: "=="
    
    ?instruction: exp*
        | /[^(END)]/*
    
    END: "end"
    
    // Definicion de una cadena
    ?string: /"[^"]*"/
        | /'[^']*'/
        
    
    // Definicion de variable
    ?var: /[a-zA-Z]\w*/

    // Definicion de numero
    ?number: int
        | float

    ?int: /\d+/

    ?float: /\d+(\.\d+)/

    ?boolean: /[(True)|(False)]/
    	
    // Ignorar espacios
    COMMENT: "#" /[^\\n]/*
        | OPEN /[^(CLOSE)]/* CLOSE
    
    OPEN: /\// "comment"
    
    CLOSE: "uncomment" /\//
      
    %ignore COMMENT
    %ignore /\s+/

"""