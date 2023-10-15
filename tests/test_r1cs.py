import numpy as np
import random

def test_simple_r1cs():
    # Transforming:  out = x * y * z * u

    # v1 = x * y
    # v2 = z * z
    # out = v1 * v2

    A = np.array([[0,0,1,0,0,0,0,0],
              [0,0,0,0,1,0,0,0],
              [0,0,0,0,0,0,1,0]])
                
    B = np.array([[0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1]])
                
    C = np.array([[0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,1],
                [0,1,0,0,0,0,0,0]])

    # Our witness vector is: [1 out x y z u v1 v2]

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