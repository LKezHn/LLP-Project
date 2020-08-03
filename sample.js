var carName = "Volvo";
var carName = 1;
var carName = true;
var carName = null;
var n = 5;
var prueba = 2+2;
var test = "hola";
var test2 = "adios";

/* 
    ejemplo
*/

console.log(test2.length);
console.log(test + test2);
console.log(carName.length);
console.log(4);
console.log(2+6);
console.log(n);
console.log(prueba + n);
console.log("string" + n);

function factorial(n)
{
    if (n==1) return 1;
    if (n<1) return 0;
    return n*factorial(n-1);
}

function isInStock(n,m)
{
    if (n>m)
    {
        console.log("Hay en Stock!");
    }
    else
    {
        console.error("No hay en Stock!");
    }
}

isInStock(7,6);
factorial(n);