// My solution:

#include <stdio.h>

unsigned int factorial(unsigned int x)
{
    if (x > 1)
    {
        return x * factorial(x-1);
    }

    return x;
}

int main() {
    /* testing code */
    printf("1! = %i\n", factorial(1));
    printf("3! = %i\n", factorial(3));
    printf("5! = %i\n", factorial(5));
}

////////////////////////////////////////////////////////////////////////////

// Their solution:

#include <stdio.h>

int factorial(int number);

int main() {
    /* testing code */
    printf("1! = %i\n", factorial(1));
    printf("3! = %i\n", factorial(3));
    printf("5! = %i\n", factorial(5));
}

int factorial(int number){
    int f = number;
    if(number > 1){
        f *= factorial(number-1);
    }
return f;
}