import numpy as np
import random

def test_simple_r1cs():
    # Transforming:  out = x * y * z * u

    # v1 = x * y
    # v2 = z * z
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

def test_simple_r1cs_2():

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

