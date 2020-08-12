# -*- coding: utf-8 -*-
#Gramatica de Javascript

"""
! Terminado:
    * Comentarios simples o múltiples.
    * Asignaciones (cadenas, booleanos, números, nulo).
    * Comparaciones simples (==, <, >, <=, >=) de un condicional a la vez.
    * Declaración y ejecución de funciones de hasta 2 parámetros (sin parámetros por defecto). El tipo de dato de los parámetros es el mismo que el de las asignaciones.
    * Generación de mensajes de salida (console.log y console.error). Deberá controlar el color de la salida en Linux para identificar el tipo de mensaje. Estos métodos nativamente permiten más de un parámetro.
    * Length de cualquier objeto.

! Parcialmente Terminado
    * Estructuras de control de flujo (if, while, for). 
        * Falta la interpretación de los tres.

! Por empezar
    * Ejecución de funciones (recursivas o no).
"""

javascriptGrammar = """

    ?start: exp+ function+ exp+ function+ exp+
        | function+
        | exp+

    ?exp: varkeyword identifier opequals string eos -> assignvar
        | varkeyword identifier opequals string opsum identifier eos -> assignvaralt
        | varkeyword identifier opequals arithmeticoperation eos -> assignvar
        | varkeyword identifier opequals bool eos -> assignvar 

        | consolelog leftpar string rightpar eos -> print_
        | consolelog leftpar string "," identifier leftpar identifier rightpar rightpar eos 
        | consolelog leftpar string opsum identifier rightpar eos -> print_alt

        | consolelog leftpar identifier rightpar eos -> printvar
        | consolelog leftpar identifier "+" identifier rightpar eos -> printvar_alt

        | consolelog leftpar arithmeticoperation rightpar eos -> printnum
        | consolelog leftpar arithmeticoperation "+" arithmeticoperation rightpar eos -> printnum_alt

        | consoleerror leftpar string rightpar eos -> print_error

        | identifier leftpar (int | float) "," (int | float) rightpar eos -> funcexists
        | identifier leftpar (int | float) "," identifier rightpar eos -> funcexists
        | identifier leftpar identifier "," (int | float) rightpar eos -> funcexists
        | identifier leftpar identifier "," identifier rightpar eos -> funcexists
        | identifier leftpar identifier rightpar eos -> funcexists
        | identifier leftpar (int | float) rightpar eos

        | length

        | cond

        | whileoperation

        | foroperation

    ?function: funkeyword identifier leftpar paramidentifier rightpar leftbrace infunc* rightbrace -> createfunc
        | funkeyword identifier leftpar paramidentifier "," paramidentifier rightpar leftbrace infunc* rightbrace -> createfunc
        | funkeyword identifier leftpar rightpar leftbrace infunc* rightbrace -> createfunc

    ?infuncexp: cond
        | consolelog leftpar string rightpar eos -> consolelogfunc
        | consoleerror leftpar string rightpar eos -> consoleerrorfunc
        | consolelog leftpar identifier "." "length" rightpar eos -> consoleloglengthfunc
        | consolelog leftpar string opsum identifier rightpar eos -> consolelogsifunc

        | consolelog leftpar identifier rightpar eos -> consolelogidentfunc
        | consolelog leftpar identifier "+" identifier rightpar eos -> consolelogident_altfunc

        | consolelog leftpar arithmeticoperation rightpar eos -> consolelogfunc
        | consolelog leftpar arithmeticoperation "+" arithmeticoperation rightpar eos -> consolelogatomfunc

    ?infunc: infuncexp+ 
        | infuncexp+ returnkeyword infuncexp eos 
        | infuncexp+ returnkeyword identifier opmult identifier leftpar arithmeticoperation rightpar eos -> returnrecur
        
    ?cond: (ifkeyword leftpar identifier opgrtrthan identifier rightpar leftbrace inif* rightbrace elsekeyword leftbrace inif* rightbrace) -> ifelse
        |  (ifkeyword leftpar identifier oplessthan identifier rightpar leftbrace inif* rightbrace elsekeyword leftbrace inif* rightbrace) -> ifelse
        |  (ifkeyword leftpar identifier opcompare identifier rightpar leftbrace inif* rightbrace elsekeyword leftbrace inif* rightbrace) -> ifelse

        | ifkeyword leftpar identifier opgrtrthan identifier rightpar returnkeyword (int | float) eos -> ifcondgnames
        | ifkeyword leftpar identifier opgrtrthan identifier rightpar returnkeyword identifier eos -> ifcondgnames
        | ifkeyword leftpar identifier opgrtrthan (int | float) rightpar returnkeyword (int | float) eos -> ifcondg
        | ifkeyword leftpar identifier opgrtrthan (int | float) rightpar returnkeyword identifier eos -> ifcondg

        | ifkeyword leftpar identifier opcompare identifier rightpar returnkeyword (int | float) eos -> ifcondenames
        | ifkeyword leftpar identifier opcompare identifier rightpar returnkeyword identifier eos -> ifcondenames
        | ifkeyword leftpar identifier opcompare (int | float) rightpar returnkeyword (int | float) eos -> ifconde
        | ifkeyword leftpar identifier opcompare (int | float) rightpar returnkeyword identifier eos -> ifconde

        | ifkeyword leftpar identifier oplessthan identifier rightpar returnkeyword (int | float) eos -> ifcondlnames
        | ifkeyword leftpar identifier oplessthan identifier rightpar returnkeyword identifier eos -> ifcondlnames
        | ifkeyword leftpar identifier oplessthan (int | float) rightpar returnkeyword (int | float) eos -> ifcondl
        | ifkeyword leftpar identifier oplessthan (int | float) rightpar returnkeyword identifier eos -> ifcondl
        

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

    ?whileoperation: whilekeyword leftpar identifier opgrtrthan identifier rightpar leftbrace inif* increment rightbrace -> whiles
        | whilekeyword leftpar identifier opgrtrthan (int | float) rightpar leftbrace inif* increment rightbrace -> whiles
        | whilekeyword leftpar identifier oplessthan identifier rightpar leftbrace inif* increment rightbrace -> whiles
        | whilekeyword leftpar identifier oplessthan (int | float) rightpar leftbrace inif* increment rightbrace -> whiles
        | whilekeyword leftpar identifier opcompare identifier rightpar leftbrace inif* increment rightbrace -> whiles
        | whilekeyword leftpar identifier opcompare (int | float) rightpar leftbrace inif* increment rightbrace -> whiles

    ?foroperation: forkeyword leftpar identifier opequals (int | float) eos identifier oplessthan (int | float) eos increment rightpar leftbrace inif* rightbrace -> fors


    ?arithmeticoperation: arithmeticoperationatom

        | arithmeticoperation opsum arithmeticoperationatom -> sum
        | arithmeticoperation opsub arithmeticoperationatom -> sub
        | arithmeticoperation opmult arithmeticoperationatom -> multi
        | arithmeticoperation opdiv arithmeticoperationatom -> div

    ?arithmeticoperationatom: identifier -> getvar
        | int
        | float
        | leftpar arithmeticoperation rightbrace 
        | opsub arithmeticoperationatom       

    ?string: /"[^"]*"/
        | /'[^']*'/

    ?identifier: /[a-zA-Z]\w*/

    ?paramidentifier: /[a-zA-Z]\w*/ 

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

    !opgrtrthanequal: ">="

    !oplessthanequal: "<="

    !eos: ";" -> eos

    ?float: /\d+(\.\d+)?/

    ?int: /\d+/

    COMMENT: /\/.*/
    %ignore COMMENT

    COMMENTWO: /\/\*[\s\S]*?\*\//
    %ignore COMMENTWO

    %ignore /\s+/
"""
