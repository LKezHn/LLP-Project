var carName = 1;
var carName = true;
var carName = null;
var n = 5;
var prueba = 2+1;
var prueba2 = 2-2;
var prueba3 = 5*2;
var test = "hola";
var test2 = "adios";

/* 
    ejemplo
*/

//console.log(4);
//console.log(2+6);
//console.log(n);
//console.log("string" + n);

//console.log(test2.length);
//console.log(test + test2);
//console.log(carName.length);
//console.log(prueba + n);


function factorial(n)
{
    if (n==1) return 1;
    if (n<1) return 0;
    return n*factorial(n-1);
}

function test()
{
    console.log("hola");
}

function isInStock(n,m)
{
    if (n>m)
    {
        console.log(test2.length);
        console.log(carName.length);
        console.log(4);
        console.log(2+6);
        console.log("string" + n);
        console.log(n);
        console.log(prueba + n);
        console.log(test + test2);
        console.log("Hay en Stock!");
    }
    else
    {
        console.error("No hay en Stock!");
    }
}

isInStock(n,6);
factorial(n);