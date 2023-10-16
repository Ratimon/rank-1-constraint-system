pragma circom 2.0.8;

template Polynomial() {
    signal input x;
    signal input y;
    
    signal v1;
    signal v2;
    signal v3;
    signal v4;
    
    signal output out;
    
    v1 <== x * x;
    v2 <== y * y;
    v3 <== v1 * v2;
    v4 <== x * v2;

    // Transforming:  out = 5*x^3 - 4*y^2*x^2 + 13*x*y^2 + x^2 - 10*y
    // out = 5*v1*x - 4*v2*v1 + 13*x*v2 + v1 - 10*y
    // out = 5*v1*x - 4*v3 + 13*v4 + v1 - 10*y
    // 4*v3 - 13*v4 - v1 + 10*y + out 
    
    out <== 5* v1 * x - 4 * v3 + 13 * v4 + v1 - 10 * y;
}

component main = Polynomial();