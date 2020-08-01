# -*- coding: utf-8 -*-

#! Bash Grammar

bashGrammar = """

    //Initial axiom
    ?start: exp+

    //Definition of an expression
    ?exp: var"="value

    //Definition of a variable
    ?var: //

    //Definition of a value
    ?value: string
        |boolean
        |number
        |null

    //Definition of a string
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Definition of a boolean
    ?boolean: /(true)|(false)/

    //Definition of a number
    ?number: /\d+(\.\d)?/

    //Ignore spaces,tabs and brakelines
    %ignore /\s/




"""

