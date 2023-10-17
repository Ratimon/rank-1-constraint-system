pragma circom 2.0.8;

template Polynomial2() {
    signal input x;
    signal input y;

    // Transforming:
    // 0 = y(y-1)(y-2)
    // 0 = y^3 - 3*y^2 + 2y

    // Transforming:
    // out =  1/2 * x*(1-y)(2-y) + x^2*(y)*(2-y) +  (-1/2)* x^3*(y)*(1-y)
    // out =  1/2 *(x^3)(y^2) + (-1/2) *(x^3)(y) + (-1)*y^2*x^2 + 2*x^2*y +  1/2(x)(y^2) + (-3/2)(x)(y) + x
    
    // v1 = x * y
    // v2 = x * x
    // v3 = v1 * y = x * y^2
    // v4 = v1 * x = x^2 * y
    // v5 = v1 * v1 = (x^2)(y^2)
    // v6 = v1 * v2 = (x^3)(y)

    
    signal output out;

    // We check that A is not zero.
    component isZero = IsZero();

    // isZero.in <== ;
    isZero.out === 0;


}

component main = Polynomial2();