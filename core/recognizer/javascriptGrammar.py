# -*- coding: utf-8 -*-
#Gramatica de Javascript

"""
! Terminado:
    * Comentarios simples o múltiples.
    * Asignaciones (cadenas, booleanos, números, nulo).
    * Comparaciones simples (==, <, >, <=, >=) de un condicional a la vez.
    * Declaración y ejecución de funciones de hasta 2 parámetros (sin parámetros por defecto). El tipo de dato de los parámetros es el mismo que el de las asignaciones.
    * Generación de mensajes de salida (console.log y console.error). Deberá controlar el color de la salida en Linux para identificar el tipo de mensaje. Estos métodos nativamente permiten más de un parámetro.

! Parcialmente Terminado
    * Estructuras de control de flujo (if, while, for).
        * Falta: while y for.

! Por empezar
    * Llamado y Ejecución de funciones (recursivas o no).
    * Length de cualquier objeto.

! Observaciones
    * En el sample.js las instrucciones: 'console.log' y 'console.error', se ejecutan aun dentro de la estructura if ya que aun no se entiende cuando se debe entrar o no a una estructura de flujo.
"""

javascriptGrammar = """

    ?start: exp+ function+ exp+
        | exp+ cl+ exp+
        | exp+ function+ exp+
        | exp+

    ?exp: cond
        | varkeyword identifier eos -> assignvarnone
        | varkeyword identifier opcompare string eos -> assignvar
        | varkeyword identifier opcompare string opsum identifier eos -> assignvaralt
        | varkeyword identifier opcompare arithmeticoperation eos -> assignvar
        | varkeyword identifier opcompare bool eos -> assignvar 

        | consolelog leftpar string rightpar eos -> print_
        | consolelog leftpar string opsum identifier rightpar eos -> print_alt

        | consolelog leftpar identifier rightpar eos -> printvar
        | consolelog leftpar identifier "+" identifier rightpar eos -> printvar_alt

        | consoleerror leftpar string rightpar eos -> print_error

        | funcname leftpar (int | float) "," (int | float) rightpar eos
        | funcname leftpar (int | float) "," identifier rightpar eos
        | funcname leftpar identifier "," (int | float) rightpar eos
        | funcname leftpar identifier "," identifier rightpar eos
   
    ?cl: "class" funcname leftbrace function+ rightbrace

    ?function: funkeyword funcname leftpar identifier rightpar leftbrace infunc+ rightbrace
        | funkeyword funcname leftpar identifier "," identifier rightpar leftbrace infunc+ rightbrace
        | funkeyword funcname leftpar rightpar leftbrace infunc+ rightbrace

    ?funcname: identifier -> createfunc

    ?infunc: exp+ returnkeyword exp eos
        | exp+ returnkeyword identifier opmult identifier leftpar arithmeticoperation rightpar eos 
        | exp+
        
    ?cond: ifkeyword leftpar identifier opgrtrthan identifier rightpar returnkeyword (int | float) eos -> ifcondgnames
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

        | ifkeyword leftpar identifier opgrtrthan identifier rightpar leftbrace (exp+) rightbrace "else" leftbrace (exp+) rightbrace 
        | ifkeyword leftpar identifier oplessthan identifier rightpar leftbrace (exp+) rightbrace "else" leftbrace (exp+) rightbrace
        | ifkeyword leftpar identifier opcompare identifier rightpar leftbrace (exp+) rightbrace "else" leftbrace (exp+) rightbrace

    ?ciclicOperation: whilekeyword leftpar identifier ">" identifier rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier opgrtrthan (int | float) rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier oplessthan identifier rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier oplessthan (int | float) rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier opgrtrthanequal identifier rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier opgrtrthanequal (int | float) rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier oplessthanequal identifier rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier oplessthanequal (int | float) rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier opcompare identifier rightpar leftbrace exp+ rightbrace
        | whilekeyword leftpar identifier opcompare (int | float) rightpar leftbrace exp+ rightbrace

    ?arithmeticoperation: arithmeticoperationatom

        | arithmeticoperation opsum arithmeticoperationatom -> sum
        | arithmeticoperation opsub arithmeticoperationatom -> sub
        | arithmeticoperation opmult arithmeticoperationatom -> multi
        | arithmeticoperation opdiv arithmeticoperationatom -> div

    ?arithmeticoperationatom: identifier -> getvar
        | int
        | float
        | leftpar arithmeticoperation rightrightbrace 
        | opsub arithmeticoperationatom       

    ?string: /"[^"]*"/
        | /'[^']*'/

    ?identifier: /[a-zA-Z]\w*/

    !bool: "true" 
        | "false"
        | "null"

    !opsum: "+"

    !opsub: "-"

    !opmult: "*"

    !opdiv: "/"

    !funkeyword: "function"

    !returnkeyword: "return"

    !whilekeyword: "while"

    !ifkeyword: "if"

    !varkeyword: "var"

    !consolelog: "console" "." "log"

    !consoleerror: "console" "." "error"

    !leftpar: "("

    !rightpar: ")"

    !leftbrace: "{"

    !rightbrace: "}"

    !opcompare: "=="

    !opgrtrthan: ">"

    !oplessthan: "<"

    !opgrtrthanequal: ">="

    !oplessthanequal: "<="

    !eos: ";"

    ?float: /\d+(\.\d+)?/

    ?int: /\d+/

    COMMENT: /\/.*/
    %ignore COMMENT

    COMMENTWO: /\/\*[\s\S]*?\*\//
    %ignore COMMENTWO

    %ignore /\s+/
"""
