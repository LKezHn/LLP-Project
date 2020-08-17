PAC II 2020 - LL 1100
@author Daniel Arteaga
@date 2020/08/16

Documentación Proyecto - Lenguajes de Programación:
===================================
* Acontinuación se muestra la documentación del proyecto de Lenguajes de Programación usando Lark.

Ruby y Bash:
============

Javascript:
====================================================
* Se lee la definición del proyecto para inmediantamente tener ideas claras de lo que se tiene que hacer y lo que no se debe de hacer.

* Se procede a estudiar la gramatica, sintaxis de el Lenguaje de Programación de Javascript y todo sus niveles de error para luego sea aplicado a Python Lark.

* <ins>Lluvia de Ideas:</ins>

    * ![image](https://drive.google.com/uc?id=1Uov1azXhZXwkJr7EGGHZQSZMBnND_lvM)

* <ins>Hallazgos encontrados:</ins>

    * **PLANIFICADO:** 

        * Dividir en partes la parte de Javascript donde se trabajara la gramatica y semantica aparte y luego se trabaja la tabla de simbolos.

        * Usar la tecnicas aprendidas en clase para poder realizar la gramatica y semantica correcta.

        * Hacer uso de la documentación disponible de Python Lark para facilitar el uso del mismo y poder reducir la semantica y gramatica.

        * Verificar la gramatica de Javascript a la hora de implementarla para evitar ambiguedades, errores y confusiones.

        * Investigar como funciona el Lenguaje de Javascript, si su ejecución es en tiempo real, como funcionan los conficionales, etc.

        * Empezar a programar la funcionalidad de todos los componentes que tiene Javascript empezando por impresión de string,cadenas y demas, así mismo como los condicionales y funciones.

    * **NO PLANIFICADO:**
        * Al tener lo basico de la gramatica y semantica se pudieron visualizar alguno escenarios en donde fallaba por ejemplo:
            
            * if's aninados, varios condicionales dentro de una sola función, ¿ que pasa dentro de un condicional hay otro?

            * Definición de variables dentro de una función.

            * Impresión y ejecución de todo lo que hay dentro de una función y condicional.

        * Al tener claro que Lark trabaja con àrboles se procede a buscar la manera en que recursivamente se pueda buscar dentro de los àrboles todo aquello que sea un condicional y se ejecute.

        * Funciones recursivas

        * Llamado de funciones con valores temporales.
