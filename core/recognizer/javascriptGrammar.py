# -*- coding: utf-8 -*-
#Gramatica de Javascript

"""
Terminado
=========
* Comentarios simples o múltiples.
* Asignaciones (cadenas, booleanos, números, nulo).
* Comparaciones simples (==, <, >, <=, >=) de un condicional a la vez.
* Declaración y ejecución de funciones de hasta 2 parámetros (sin parámetros por defecto). El tipo de dato de los parámetros es el mismo que el de las asignaciones.
* Generación de mensajes de salida (console.log y console.error). Deberá controlar el color de la salida en Linux para identificar el tipo de mensaje. Estos métodos nativamente permiten más de un parámetro.

Parcialmente Terminado
======================
* Estructuras de control de flujo (if, while, for).
    * Falta: while y for.

Por empezar
===========
* Llamado y Ejecución de funciones (recursivas o no).
* Length de cualquier objeto.

Observaciones
=============
* En el sample.js las instrucciones: 'console.log' y 'console.error', se ejecutan aun dentro de la estructura if ya que aun no se entiende cuando se debe entrar o no a una estructura de flujo.
"""

grammar = """

    //Definicion de una expresion.
    ?start: exp+ function+ exp+
        | exp+ cl+ exp+
        | exp+ function+ exp+
        | exp+

    //Definición de una expresión.
    ?exp: cond
        | "var" name ";" -> assignvarnone
        | "var" name "=" string ";" -> assignvar
        | "var" name "=" string "+" name ";" -> assignvaralt
        | "var" name "=" arithmeticoperation ";" -> assignvar
        | "var" name "=" bool ";" -> assignvar 

        | "console" "." "log" "(" string ")" ";" -> print_
        | "console" "." "log" "(" string "+" name ")" ";" -> print_alt

        | "console" "." "log" "(" name ")" ";" -> printvar
        | "console" "." "log" "(" name "+" name ")" ";" -> printvar_alt

        | "console" "." "error" "(" string ")" ";" -> print_error

        | funcname "(" number "," number ")" ";"
        | funcname "(" number "," name ")" ";"
        | funcname "(" name "," number ")" ";"
        | funcname "(" name "," name ")" ";"

    //Definicion de una clase.    
    ?cl: "class" funcname "{" function+ "}"

    //Definicon de una funcion.
    ?function: "function" funcname "(" name ")" "{" infunc+ "}"
        | "function" funcname "(" name "," name ")" "{" infunc+ "}"
        | "function" funcname "(" ")" "{" infunc+ "}"

    //Def
    ?funcname: name -> createfunc

    //Def
    ?infunc: exp+ "return" exp ";"
        | exp+ "return" name "*" name "(" arithmeticoperation ")" ";" 
        | exp+
        

    //Definicion de condicionales.
    ?cond: "if" "(" name ">" name ")" "return" number ";" -> ifcondg
        | "if" "(" name ">" name ")" "return" name ";" -> ifcondg
        | "if" "(" name ">" number ")" "return" number ";" -> ifcondg
        | "if" "(" name ">" number ")" "return" name ";" -> ifcondg

        | "if" "(" name "==" name ")" "return" number ";" -> ifconde
        | "if" "(" name "==" name ")" "return" name ";" -> ifconde
        | "if" "(" name "==" number ")" "return" number ";" -> ifconde
        | "if" "(" name "==" number ")" "return" name ";" -> ifconde

        | "if" "(" name "<" name ")" "return" number ";" -> ifcondl
        | "if" "(" name "<" name ")" "return" name ";" -> ifcondl
        | "if" "(" name "<" number ")" "return" number ";" -> ifcondl
        | "if" "(" name "<" number ")" "return" name ";" -> ifcondl

        | "if" "(" name ">" name ")" "{" exp+ "}" "else" "{" exp+ "}" 
        | "if" "(" name "<" name ")" "{" exp+ "}" "else" "{" exp+ "}"
        | "if" "(" name "==" name ")" "{" exp+ "}" "else" "{" exp+ "}"

    //Definicion de bool
    ?bool: "true" 
        | "false"
        | "null"

    //Definición de operación aritmética/
    ?arithmeticoperation: arithmeticoperationatom

        | arithmeticoperation "+" arithmeticoperationatom -> sum

        | arithmeticoperation "-" arithmeticoperationatom -> sub

        | arithmeticoperation "*" arithmeticoperationatom -> multi

        | arithmeticoperation "/" arithmeticoperationatom -> div

    //Definición de un átomo de operación aritmética.
    ?arithmeticoperationatom: name -> getvar
        | number
        | "(" arithmeticoperation ")" 
        | "-" arithmeticoperationatom       

    //Definición de una cadena.
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Definición de variable.
    ?name: /[a-zA-Z]\w*/

    //Definicion de numero.
    ?number: /\d+(\.\d+)?/

    //Ignorar comentarios
    COMMENT: /\/.*/
    %ignore COMMENT

    //Ignorar comentarios de multiples lineas
    COMMENTWO: /\/\*[\s\S]*?\*\//
    %ignore COMMENTWO

    //Ignorar espacios, saltos de linea y tabulados.
    %ignore /\s+/
"""
