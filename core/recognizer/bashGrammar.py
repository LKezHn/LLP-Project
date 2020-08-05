# -*- coding: utf-8 -*-


"""
    ! Bash Grammar
    ? Strings, booleans, variables, numbeers and null
    ? echo
    ? conditional
    ? loops
    ? define function
    ? function call
    ? comments
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
        | definefunction
        | callfunction
        | return

    //Definition of an arithmeticoperation
    ?arithmeticoperation: arithmeticoperationatom
        | arithmeticoperation"+"arithmeticoperationatom -> sum
        | arithmeticoperation"-"arithmeticoperationatom -> sub
        | arithmeticoperation"*"arithmeticoperationatom -> mul
        | arithmeticoperation"/"arithmeticoperationatom -> div
        | arithmeticoperation"%"arithmeticoperationatom -> mod

    //Definition of an arithmeticoperationatom
    ?arithmeticoperationatom: "$"var -> getvar
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

    //Definition of while loop
    ?while: "while" "["? condition "]"? "do" loopinstruction LOOPEND

    //Definition of until loop
    ?until: "until" "["? condition "]"? "do" loopinstruction LOOPEND  

    //Definition of define function
    ?definefunction: var "("?")"? "{" functioninstruction "}" -> createfunction
        | "function" var "("?")"? "{" functioninstruction "}" -> createfunction

    //Definetion of a call of function
    ?callfunction: var -> callfunction
        | var params

    //Define params
    ?params: string
        | number
        | var
        | callfunction
        | string params
        | number params
        | var params
        | callfunction params      

    //Definition of return
    ?return: string
        | number
        | var
        | boolean

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

    //Define a function instruction
    ?functioninstruction: exp*
        | /[^}]/*


    //Definition of an instruction
    ?instruction: exp*
        | /[^(END)]/*

    END: "fi"           

    //Definition of a variable
    ?var: /[a-zA-Z][\w_]*/
        | /[A-Z][A-Z0-9]*/

    //Definition of a value
    ?value: string
        | boolean
        | number
        | null

    //Definition of a string
    ?string: /"[^"]*"/
        | /'[^']*'/

    //Definition of a boolean
    ?boolean: /(true)|(false)/

    //Definition of a number
    ?number: /\d+(\.\d)?/
        | /\d+(\.\d+)/

    //Definition of null
    ?null: /""/    

    //Ignore spaces,tabs and brakelines
    %ignore /\s/

    //Define comment comments
    COMMENT: "#" /[^\\n]/* 
        | OPEN /[^(CLOSE)]/* CLOSE

    OPEN: ":" "'" "comment"

    CLOSE: "'" "uncomment"    

    //ignore comments
    %ignore COMMENT  

"""

