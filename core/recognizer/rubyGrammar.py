# -*- coding: utf-8 -*-
"""
    ! Gramaticas terminadas:
    ? Strings, booleanos, ints, floats
    ? Asignación de variables, Método puts
    ? Condicional if
    ? Bucles fopr y while
    ? Comentarios
    ? Comparaciones
    ? Operaciones aritméticas

    TODO: Falta hacer la gramatica de definicion de funcion, llamado a funcion, concatenacion en strings.
"""

rubyGrammar = """

    ?start : exp+

    ?exp : var "=" value
        | var "=" arithmeticoperation  -> assignvar
        | "puts" "("? string ")"?   -> print
        | "puts" "("? var ")"?  -> printvar
	    | conditional
        | loop

    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperation "+" arithmeticoperationatom -> sum
        | arithmeticoperation "-" arithmeticoperationatom  -> sub
        | arithmeticoperation "*" arithmeticoperationatom  -> mult
        | arithmeticoperation "/" arithmeticoperationatom  -> div

    ?arithmeticoperationatom: var -> getvar
        | number
        | "-" arithmeticoperationatom
        | "(" arithmeticoperationatom ")"

    ?var: /[a-zA-Z][\w_]*

    ?value: string
        | number
        | boolean
    

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