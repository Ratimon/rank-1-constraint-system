import numpy as np
import random

def test_multiply4():
    # Transforming:  out = x * y * z * u

    # v1 = x * y
    # v2 = z * u
    # out = v1 * v2

    # Our witness vector is: [1 out x y z u v1 v2]

    A = np.array([[0,0,1,0,0,0,0,0],
              [0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,1,0]])
                
    B = np.array([[0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1]])
                
    C = np.array([[0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,1],
                [0,1,0,0,0,0,0,0]])


    x = random.randint(1,100)
    y = random.randint(1,100)
    z = random.randint(1,100)
    u = random.randint(1,100)

    # compute the algebraic circuit
    out = x * y * z * u
    v1 = x*y
    v2 = z*u

    # create the witness vector
    w = np.array([1, out, x, y, z, u, v1, v2])

    # element-wise multiplication, not matrix multiplication
    result = C.dot(w) == np.multiply(A.dot(w), B.dot(w))

    assert result.all(), "system contains an inequality"

def test_polynomial():

    # Transforming:  out = 5*x^3 - 4*y^2*x^2 + 13*x*y^2 + x^2 - 10*y

    # v1 = x^2
    # v2 = y^2
    # out = 5*v1*x - 4*v2*v1 + 13*x*v2 + v1 - 10*y

    # v1 = x*x
    # v2 = y*y
    # v3 = v1*v2
    # v4 = x*v2
    # 4*v3 - 13*v4 - v1 + 10*y + out = 5*v1*x

    # Our witness vector is: [1 out x y v1 v2 v3 v4]

    A = np.array([[0,0,1,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0],
                  [0,0,0,0,1,0,0,0],
                  [0,0,1,0,0,0,0,0],
                  [0,0,0,0,5,0,0,0]])
    
    B = np.array([[0,0,1,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0],
                  [0,0,0,0,0,1,0,0],
                  [0,0,0,0,0,1,0,0],
                  [0,0,1,0,0,0,0,0]])
    
    C = np.array([[0,0,0,0,1,0,0,0],
                  [0,0,0,0,0,1,0,0],
                  [0,0,0,0,0,0,1,0],
                  [0,0,0,0,0,0,0,1],
                  [0,1,0,10,-1,0,4,-13]])
    
    # pick random values for x and y
    x = random.randint(1,1000)
    y = random.randint(1,1000)

    out = 5*x*x*x - 4*y*y*x*x + 13*x*y*y + x*x - 10*y
    v1 = x*x
    v2 = y*y
    v3 = v1*v2
    v4 = x*v2

    w = np.array([1, out, x, y, v1, v2, v3, v4])

    result = C.dot(w) == np.multiply(A.dot(w),B.dot(w))
    assert result.all(), "result contains an inequality"

def test_polynomial2():

    # fn main(x: field, y: field) -> field {
    #   assert!(y == 0 || y == 1 || y == 2);
    #   if (y == 0) {
    # 		return x; 
    # 	}
    # 	else if (y == 1) {
    # 	  return x**2;
    # 	} 
    # 	else {
    # 	  return x**3;
    # 	}
    # }


    # Transforming:
    # 0 = y(y-1)(y-2)
    # 0 = y^3 - 3*y^2 + 2y

    # out =  1/2 * x*(1-y)(2-y) + x^2*(y)*(2-y) +  (-1/2)* x^3*(y)*(1-y)
    # out =  1/2 *(x^3)(y^2) + (-1/2) *(x^3)(y) + (-1)*y^2*x^2 + 2*x^2*y +  1/2(x)(y^2) + (-3/2)(x)(y) + x

    # v1 = x * y
    # v2 = x * x
    # v3 = v1 * y = x * y^2
    # v4 = v1 * x = x^2 * y
    # v5 = v1 * v1 = (x^2)(y^2)
    # v6 = v1 * v2 = (x^3)(y)

    # out =  1/2 *(v6)(y) + (-1/2) *(v6) + (-1)*(v5) + 2*(v4) +  1/2(v3) + (-3/2)(v1) + x
    # 1/2 *(v6) + v5 -2v4 -(1/2)v3 + (3/2)v1 - x + out =  1/2 *(v6)(y)
    # v6 + 2v5 -4v4 -(1)v3 + 3v1 - 2x + 2out = (v6)(y)

    # Our witness vector is: [1 out x y v1 v2 v3 v4 v5 v6]

    A = np.array([[0,0,1,0,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,1/2]])
    
    B = np.array([[0,0,0,1,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,0,1,0,0,0,0],
                  [0,0,0,1,0,0,0,0,0,0]])
    
    # C = np.array([[0,0,0,0,1,0,0,0,0,0],
    #               [0,0,0,0,0,1,0,0,0,0],
    #               [0,0,0,0,0,0,1,0,0,0],
    #               [0,0,0,0,0,0,0,1,0,0],
    #               [0,0,0,0,0,0,0,0,1,0],
    #               [0,0,0,0,0,0,0,0,0,1],
    #               [0,2,-2,0,3,0,-1,-4,2,1]])
    
    C = np.array([[0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,0,1,0,0,0,0],
                  [0,0,0,0,0,0,1,0,0,0],
                  [0,0,0,0,0,0,0,1,0,0],
                  [0,0,0,0,0,0,0,0,1,0],
                  [0,0,0,0,0,0,0,0,0,1],
                  [0,1,-1,0,3/2,0,-1/2,-2,1,1/2]])
    
    # pick random values for x and y
    x = random.randint(1,1000)
    y = random.randint(1,1000)

    out = 5*x*x*x - 4*y*y*x*x + 13*x*y*y + x*x - 10*y
    v1 = x*y
    v2 = x*x
    v3 = v1*y
    v4 = v1*x
    v5 = v1*v1
    v6 = v1*v2
    # out = x*x*x*y*y - x*x*x*y + (-2)*y*y*x*x + 4*x*x*y +  x*y*y + (-3)*x*y + 2*x
    out = 1/2 *x*x*x*y*y + (-1/2) *x*x*x*y + (-1)*y*y*x*x + 2*x*x*y +  1/2*x*y*y + (-3/2)*x*y + x


    w = np.array([1, out, x, y, v1, v2, v3, v4, v5, v6])

    result = C.dot(w) == np.multiply(A.dot(w),B.dot(w))
    assert result.all(), "result contains an inequality"

