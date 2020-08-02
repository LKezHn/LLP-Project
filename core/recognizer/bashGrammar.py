# -*- coding: utf-8 -*-


"""
    ! Bash Grammar
    TODO: Comments
    TODO: Function Definitio
    TODO: Function Call

"""

bashGrammar = """

    //Initial axiom
    ?start: exp+

    //Definition of an expression
    ?exp: var"="value
        | "let" var"="arithmeticoperation -> assignvar
        | "echo" string -> print
        | "echo" "$"var -> printvar
        | conditional
        | loop

    //Definition of an arithmeticoperation
    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperation"+"arithmeticoperationatom -> sum
        | arithmeticoperation"-"arithmeticoperationatom -> sub
        | arithmeticoperation"*"arithmeticoperationatom -> mul
        | arithmeticoperation"/"arithmeticoperationatom -> div
        | arithmeticoperation"%"arithmeticoperationatom -> mod

    //Definition of an arithmeticoperationatom
    ?aritmeticoperationatom: "$"var -> get var
        | number 
        | "-"arithmeticoperation

    //Definition of a conditional
    ?conditional: "if" "["? condition "]"?";" "then" instruction END  

    //Definition of a loop
    ?loop: for
        | while
        | until

    //Definition of for
    ?for: "for" var "in" "$"var "do" loopinstruction LOOPEND
        | "for" var "in" "{"number".."number"}" "do" loopinstruction LOOPEND    

    ?while: "while" "["? condition "]"?" "do" loopinstruction LOOPEND

    ?until: "until" "["? condition "]"?" "do" loopinstruction LOOPEND   

    //Definition of a condition
    ?condition: "$"var compare "$"var
        | "$"var compare number
        | "$"var equals boolean
        | "$"var equals string
        | string equals string
        | number compare number
        | number equals number

    //Definition of compare
    ?compare: "-lt"
        | "-le"
        | "-ge"
        | "-gt"
        | "-ne"

    //Definition of equals
    ?equals: "-eq"      

    //Definition of loopinstruction
    ?loopinstruction: exp*
        |  /[^(LOOPEND)]/* 

    LOOPEND: "done"       


    //Definition of an instruction
    ?instruction: exp*
        | /[^(END)]/*

    END: "fi"           

    //Definition of a variable
    ?var: /[a-zA-Z][\w_]/
        | /[A-Z][A-Z0-9]*/

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
        | /\d+(\.\d+)/

    //Ignore spaces,tabs and brakelines
    %ignore /\s/




"""

