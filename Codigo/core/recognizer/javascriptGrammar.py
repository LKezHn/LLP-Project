# -*- coding: utf-8 -*-
#Gramatica de Javascript
#Test

"""
! Terminado:
    * Comentarios simples o múltiples.
    * Asignaciones (cadenas, booleanos, números, nulo).
    * Comparaciones simples (==, <, >, <=, >=) de un condicional a la vez.
    * Declaración y ejecución de funciones de hasta 2 parámetros (sin parámetros por defecto). El tipo de dato de los parámetros es el mismo que el de las asignaciones.
    * Generación de mensajes de salida (console.log y console.error). Deberá controlar el color de la salida en Linux para identificar el tipo de mensaje. Estos métodos nativamente permiten más de un parámetro.
    * Length de cualquier objeto.
    * Estructuras de control de flujo (if, while, for)
    * Ejecucion de funciones (recursivas o no)

"""

javascriptGrammar = """

    ?start: function+ exp+ 
        | function+ 
        | exp+ 

    ?exp: varkeyword identifier opequals string eos -> assignvar
        | varkeyword identifier opequals string opsum identifier eos -> assignvaralt
        | varkeyword identifier opequals arithmeticoperation eos -> assignvar
        | varkeyword identifier opequals bool eos -> assignvar 

        | consolelog leftpar string rightpar eos -> print_
        | consolelog leftpar string "," identifier leftpar (identifier | int | float) rightpar rightpar eos -> printwithfunc
        | consolelog leftpar string opsum identifier rightpar eos -> print_alt

        | consolelog leftpar identifier rightpar eos -> printvar
        | consolelog leftpar identifier "+" identifier rightpar eos -> printvar_alt

        | consolelog leftpar arithmeticoperation rightpar eos -> printnum
        | consolelog leftpar arithmeticoperation "+" arithmeticoperation rightpar eos -> printnum_alt

        | consoleerror leftpar string rightpar eos -> print_error

        | identifier leftpar (int | float | identifier) "," (int | float | identifier) rightpar eos -> funcexists
        | identifier leftpar (identifier | int | float) rightpar eos -> funcexists

        | length

        | cond

        | while

        | for

    ?function: funkeyword identifier leftpar identifier rightpar leftbrace infunc* rightbrace -> createfunc
        | funkeyword identifier leftpar identifier "," identifier rightpar leftbrace infunc* rightbrace -> createfunc
        | funkeyword identifier leftpar rightpar leftbrace infunc* rightbrace -> createfunc

    ?infuncexp: cond+
        | while+
        | for+
        | consolelog leftpar string rightpar eos -> consolelogfunc
        | consoleerror leftpar string rightpar eos -> consoleerrorfunc
        | consolelog leftpar identifier "." "length" rightpar eos -> consoleloglengthfunc
        | consolelog leftpar string opsum identifier rightpar eos -> consolelogsifunc

        | consolelog leftpar identifier rightpar eos -> consolelogidentfunc
        | consolelog leftpar identifier "+" identifier rightpar eos -> consolelogident_altfunc

        | consolelog leftpar arithmeticoperation rightpar eos -> consolelogfunc
        | consolelog leftpar arithmeticoperation "+" arithmeticoperation rightpar eos -> consolelogatomfunc
        | varkeyword identifier opequals string eos 
        | varkeyword identifier opequals string opsum identifier eos 
        | varkeyword identifier opequals arithmeticoperation eos 
        | varkeyword identifier opequals bool eos 

    ?infunc: infuncexp+ 
        | infuncexp+ returnrecursive 

    ?returnrecursive: returnkeyword identifier opmult identifier leftpar arithmeticoperation rightpar eos -> returnrecur
        
    ?cond: ifkeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar leftbrace inif* rightbrace elsekeyword leftbrace inif* rightbrace
        |  ifkeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar leftbrace inif* rightbrace elsekeyword leftbrace inif* rightbrace
        |  ifkeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar leftbrace inif* rightbrace elsekeyword leftbrace inif* rightbrace
        |  ifkeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar leftbrace inif* rightbrace elsekeyword leftbrace inif* rightbrace
       
        | ifkeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar returnkeyword (int | float) eos 
        | ifkeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar returnkeyword identifier eos 
        | ifkeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar returnkeyword (int | float) eos 
        | ifkeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar returnkeyword identifier eos 
        | ifkeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar returnkeyword (int | float) eos 
        | ifkeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar returnkeyword identifier eos 
        | ifkeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar returnkeyword identifier eos
        | ifkeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar returnkeyword (int | float) eos
        

    ?increment: identifier "+" "+" ";" 
        | identifier "+" "+" 

    ?length: consolelog leftpar identifier "." "length" rightpar eos -> length

    ?inif: consolelog leftpar string rightpar eos -> consolelogcond
        | consoleerror leftpar string rightpar eos -> consoleerrorcond
        | consolelog leftpar identifier "." "length" rightpar eos -> consoleloglengthcond
        | consolelog leftpar string opsum identifier rightpar eos -> consolelogsicond

        | consolelog leftpar identifier rightpar eos -> consolelogidentcond
        | consolelog leftpar identifier "+" identifier rightpar eos -> consolelogident_altcond

        | consolelog leftpar arithmeticoperation rightpar eos -> consolelogcond
        | consolelog leftpar arithmeticoperation "+" arithmeticoperation rightpar eos -> consolelogatomcond
        | cond
        | while
        | for
        | varkeyword identifier opequals string eos -> assignvarinif
        | varkeyword identifier opequals string opsum identifier eos -> assignvarinif
        | varkeyword identifier opequals arithmeticoperation eos -> assignvarinif
        | varkeyword identifier opequals bool eos -> assignvarinif

    ?while: whilekeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar leftbrace inif* increment rightbrace
        | whilekeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar leftbrace inif* increment rightbrace 
        | whilekeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar leftbrace inif* increment rightbrace
        | whilekeyword leftpar identifier (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar leftbrace inif* increment rightbrace
        | whilekeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar leftbrace inif* rightbrace 
        | whilekeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) identifier rightpar leftbrace inif* rightbrace
        | whilekeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar leftbrace inif* rightbrace
        | whilekeyword leftpar (int | float) (opgrtrthan | oplessthan | opcompare | opgrtrthanequal | oplessthanequal) (int | float) rightpar leftbrace inif* rightbrace

    ?for: forkeyword leftpar identifier opequals (int | float) eos identifier (oplessthan | oplessthanequal)  ((int | float) | identifier) eos increment rightpar leftbrace inif* rightbrace 

    ?identifier: /[a-zA-Z]\w*/

    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperation opsum arithmeticoperationatom 
        | arithmeticoperation opsub arithmeticoperationatom 
        | arithmeticoperation opmult arithmeticoperationatom 
        | arithmeticoperation opdiv arithmeticoperationatom 

    ?arithmeticoperationatom: identifier 
        | int
        | float
        | leftpar arithmeticoperation rightbrace 
        | opsub arithmeticoperationatom       

    ?string: /"[^"]*"/
        | /'[^']*'/

    !bool: "true" -> boolt
        | "false" -> boolf
        | "null" -> booln

    !forkeyword: "for" -> forw

    !opsum: "+" -> opsum

    !opsub: "-" -> opsub

    !opmult: "*" -> opmult

    !opdiv: "/" -> opdiv

    !funkeyword: "function" -> funcw

    !returnkeyword: "return" -> retw

    !whilekeyword: "while" -> whilew

    !ifkeyword: "if" -> ifw
    
    !elsekeyword: "else" -> elsew

    !varkeyword: "var" -> varkeyword

    !consolelog: "console" "." "log" -> consolelog

    !consoleerror: "console" "." "error" -> consolerror

    !leftpar: "(" -> leftpar

    !rightpar: ")" -> rightpar

    !leftbrace: "{" -> leftbrace

    !rightbrace: "}" -> rightbrace

    !opequals: "=" -> opequals

    !opcompare: "==" -> opcompare

    !opgrtrthan: ">" -> opgrtrthan

    !oplessthan: "<" -> oplessthan

    !opgrtrthanequal: ">=" -> opgrtrthanequal

    !oplessthanequal: "<=" -> oplessthanequal

    !eos: ";" -> eos

    ?float: /\d+(\.\d+)/

    ?int: /\d+/

    COMMENT: /\/.*/
    %ignore COMMENT

    COMMENTWO: /\/\*[\s\S]*?\*\//
    %ignore COMMENTWO

    %ignore /\s+/
"""
