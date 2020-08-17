PAC II 2020 - LL 1100
@author Daniel Arteaga, Luis Martinez
@date 2020/08/16

Documentación Proyecto - Lenguajes de Programación:
===================================
* Acontinuación se muestra la documentación del proyecto de Lenguajes de Programación usando Lark.

Forma de Trabajo
======
* Se decide dividir el proyecto, separándolo en dos partes:
    
    * **Interpretación y Demostración** lo cual se refiere a lo relacionado con el Lenguaje Javascript.
    * **Reconocimiento** que se refiere a lo relacionado con los Lenguajes Ruby y Bash.

    Asignando cada parte a un equipo de trabajo de dos personas. Cada equipo decide de que manera trabajar su parte del proyecto, asi como las tareas específicas que debe realizar cada integrante.

Ruby y Bash:
============
* Se lee la definición del proyecto para poder entender lo que se pide hacer con respecto al apartado de reconocimiento del lenguaje Ruby y Bash.

* Se procede a estudiar la gramática y sintaxis de los lenguajes Ruby y Bash, enfocandose más en las instrucciones que debe comprender el apartado de Reconocimiento, mencionadas en la definición del proyecto.

* <ins>Hallazgos encontrados:</ins>
    
    * **PLANIFICADO:**

        * Dividir el trabajo de realizar la gramática de Ruby y Bash, asignando una única gramática por integrante.

    * **NO PLANIFICADO:**

        * Al encontrarse con un conflicto con la gramática de comentarios de múltiples líneas en Ruby se comienza a investigar la forma en la que trabaja Python Lark para poder solucionar el conflicto.

        * Al tener la gramática del lenguaje Ruby terminada, se encuentra un error al poder llamar a funciones no definidas o código perteneciente a otro Lenguaje, e.g.: `console.log("Hello World")` , por lo que se empieza a buscar la solución a éste error.

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
