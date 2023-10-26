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

    result2 = C.dot(w) - np.multiply(A.dot(w), B.dot(w)) == 0
    assert result2.all(), "system contains an inequality"

def test_polynomial():

    # Transforming:
    # out = 5*x^3 - 4*y^2*x^2 + 13*x*y^2 + x^2 - 10*y
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

    result2 = C.dot(w) - np.multiply(A.dot(w), B.dot(w)) == 0
    assert result2.all(), "system contains an inequality"

def test_polynomial_alt():

    # Transforming:
    # out = 5*x^3 - 4*y^2*x^2 + 13*x*y^2 + x^2 - 10*y
    # out = 5*v1*x - 4*v2*v1 + 13*x*v2 + v1 - 10*y

    # v1 = x*x
    # v2 = y*y
    # v3 = 4*v1*v2
    # v4 = -13*x*v2
    
    # v3 + v4 - v1 + 10*y + out = 5*v1*x
    # out + 10*y - v1 + v3 + v4  = 5*v1*x

    # Our witness vector is: [1 out x y v1 v2 v3 v4]

    A = np.array([[0,0,1,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0],
                  [0,0,0,0,4,0,0,0],
                  [0,0,-13,0,0,0,0,0],
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
                  [0,1,0,10,-1,0,1,1]])
    
    # pick random values for x and y
    x = random.randint(1,1000)
    y = random.randint(1,1000)

    v1 = x*x
    v2 = y*y
    v3 = 4*v1*v2
    v4 = -13*x*v2
    out = 5*x*x*x - 4*y*y*x*x + 13*x*y*y + x*x - 10*y

    w = np.array([1, out, x, y, v1, v2, v3, v4])

    result = C.dot(w) == np.multiply(A.dot(w),B.dot(w))
    assert result.all(), "result contains an inequality"

    result2 = C.dot(w) - np.multiply(A.dot(w), B.dot(w)) == 0
    assert result2.all(), "system contains an inequality"

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

def test_polynomial2():

    # Transforming:
    # 0 = y(y-1)(y-2)
    # 0 = y^3 - 3*y^2 + 2y
    # 0 = y*v2 - 3*v2 + 2*y

    # Transforming:
    # out =  1/2 * x*(1-y)(2-y) + x^2*(y)*(2-y) +  (-1/2)* x^3*(y)*(1-y)
    # out =  1/2 *(x^3)(y^2) + (-1/2) *(x^3)(y) + (-1)*y^2*x^2 + 2*x^2*y +  1/2(x)(y^2) + (-3/2)(x)(y) + x
    # out =  1/2 *(v7)(y) + (-1/2) *(v7) + (-1)*(v6) + 2*(v5) +  1/2(v4) + (-3/2)(v1) + x

    # v1 = x * y
    # v2 = y * y
    # v3 = x * x
    # v4 = v1 * y = x * y^2
    # v5 = v1 * x = x^2 * y
    # v6 = v1 * v1 = (x^2)(y^2)
    # v7 = v1 * v3 = (x^3)(y)

    # v7 + 2v6 -4v5 -(1)v4 + 3v1 - 2x + 2out = (v7)(y)
    # out - x + 1/2 *(v7) + v6 -2v5 -(1/2)v4 + (3/2)v1  =  1/2 *(v7)(y)

    # 3 * v2 - 2y = y * v2

    # Our witness vector is: [1 out x y v1 v2 v3 v4 v5 v6 v7]

    A = np.array([[0,0,1,0,0,0,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,1/2],
                  [0,0,0,0,0,1,0,0,0,0,0]
                  ])
    
    #            [1 out x y v1 v2 v3 v4 v5 v6 v7]
    B = np.array([[0,0,0,1,0,0,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0,0],
                  [0,0,0,0,0,0,1,0,0,0,0],
                  [0,0,0,1,0,0,0,0,0,0,0],
                  [0,0,0,1,0,0,0,0,0,0,0]
                  ])
    
    #            [1 out x y v1 v2 v3 v4 v5 v6 v7]
    C = np.array([[0,0,0,0,1,0,0,0,0,0,0],
                  [0,0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,0,0,1,0,0,0,0],
                  [0,0,0,0,0,0,0,1,0,0,0],
                  [0,0,0,0,0,0,0,0,1,0,0],
                  [0,0,0,0,0,0,0,0,0,1,0],
                  [0,0,0,0,0,0,0,0,0,0,1],
                  [0,1,-1,0,3/2,0,0,-1/2,-2,1,1/2],
                  [0,0,0,-2,0,3,0,0,0,0,0]
                  ])
    
    # pick random values for x 
    x = random.randint(1,1000)
    # pick random values for y (must be between 1 and 2) 
    y = random.randint(1,2)

    v1 = x*y
    v2 = y*y
    v3 = x*x
    v4 = v1*y
    v5 = v1*x
    v6 = v1*v1
    v7 = v1*v3
    out = 1/2 *x*x*x*y*y + (-1/2) *x*x*x*y + (-1)*y*y*x*x + 2*x*x*y +  1/2*x*y*y + (-3/2)*x*y + x

    w = np.array([1, out, x, y, v1, v2, v3, v4, v5, v6, v7])

    result = C.dot(w) == np.multiply(A.dot(w),B.dot(w))
    assert result.all(), "result contains an inequality"

    result2 = C.dot(w) - np.multiply(A.dot(w), B.dot(w)) == 0
    assert result2.all(), "system contains an inequality"