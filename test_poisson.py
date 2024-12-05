import pytest
import numpy as np

from poisson import solve_poisson, errornorm

def test_exact_solution():
    """
        Test that P2 elements recover the quadratic solution exactly up to rounding error.
    """
    uh, ue = solve_poisson(n=4, degree=2)
    error_H1 = errornorm(uh, ue, "H1")

    assert error_H1 < 1e-12
    
    

def test_convergence_P1():
    """Test that
    """
    uh, ue = solve_poisson(n=32, degree=1)
    error1_H1 = errornorm(uh, ue, "H1")
    error1_L2 = errornorm(uh, ue, "L2")

    uh, ue = solve_poisson(n=32, degree=1)
    error2_H1 = errornorm(uh, ue, "H1")
    error2_L2 = errornorm(uh, ue, "L2")

    eoc_H1 = (np.log(error1_H1)-np.log(error1_H1))/np.log(2)
    eoc_L2 = (np.log(error2_L2)-np.log(error2_H1))/np.log(2)

#python -m pytest