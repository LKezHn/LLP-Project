from tabulate import tabulate

def printTable(variables,functions,paramidentifiers):
    print("Tabla de simbolos para variables: ")
    print("\n")
    list = [["Identifier", "Value"]]
    for key in variables:
        list.append([key,variables[key]])
    print(tabulate(list,headers="firstrow"))

    print("\n")
    print("Tabla de funciones: ")
    print("\n")
    list = [["Function Identifier"]]
    for key in functions:
        list.append([key])
    print(tabulate(list,headers="firstrow"))

    print("\n")
    print ("Tabla de parametros de funciones")
    print("\n")
    list=[["Param Identifier","Value"]]
    for key in paramidentifiers:
        list.append([key,paramidentifiers[key]])
    print(tabulate(list,headers="firstrow"))