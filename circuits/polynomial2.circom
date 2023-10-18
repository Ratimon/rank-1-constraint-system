pragma circom 2.0.8;

include "node_modules/circomlib/circuits/comparators.circom";

template Polynomial2() {
    signal input x;
    signal input y;

    // Transforming:
    // 0 = y(y-1)(y-2)
    // 0 = y^3 - 3*y^2 + 2y
    // 0 = y*v2 - 3*v2 + 2*y

    // Transforming:
    // out =  1/2 * x*(1-y)(2-y) + x^2*(y)*(2-y) +  (-1/2)* x^3*(y)*(1-y)
    // out =  1/2 *(x^3)(y^2) + (-1/2) *(x^3)(y) + (-1)*y^2*x^2 + 2*x^2*y +  1/2(x)(y^2) + (-3/2)(x)(y) + x
    // out =  1/2 *(v7)(y) + (-1/2) *(v7) + (-1)*(v6) + 2*(v5) +  1/2(v4) + (-3/2)(v1) + x

    // v1 = x * y
    // v2 = y * y
    // v3 = x * x
    // v4 = v1 * y = x * y^2
    // v5 = v1 * x = x^2 * y
    // v6 = v1 * v1 = (x^2)(y^2)
    // v7 = v1 * v3 = (x^3)(y)

    // c = y*v2 - 3*v2 + 2*y

    signal v1;
    signal v2;
    signal v3;
    signal v4;
    signal v5;
    signal v6;
    signal v7;
    signal c;
    
    signal output out;

    v1 <== x * y;
    v2 <== y * y;
    v3 <== x * x;
    v4 <== v1 * y;
    v5 <== v1 * x;
    v6 <== v1 * v1;
    v7 <== v1 * v3;

    c  <== y*v2 - 3*v2 + 2*y;

    // We check that c is not zero.
    // In other words, we check that y = 0 , y = 1, y = 2 
    // we use component so 
    component isZero = IsZero();

    isZero.in <== c;
    isZero.out === 1;

    // isZero.out ==> out

    // out =  1/2 *(v7)(y) + (-1/2) *(v7) + (-1)*(v6) + 2*(v5) +  1/2(v4) + (-3/2)(v1) + x
    out <== (1/2) * v7 * y - (1/2) * v7 - v6 + 2*v5 + (1/2) * v4 - (3/2) * v1 + x;
}

component main = Polynomial2();