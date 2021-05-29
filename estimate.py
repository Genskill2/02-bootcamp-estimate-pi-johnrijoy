import math
import unittest
import random

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
# Solution Code
def wallis(n):
    '''
    input:
    n - number of iterations
    output:
    estpi - numerical estimate of pi using wallis formula
    '''
    estpi = 2 # variable used to store the value obtained from wallis formula iteratively
    for i in range(1, n+1):
        estpi *= (4*(i**2))/((4*(i**2))-1)
    
    return estpi

def monte_carlo(n):
    '''
    side of square is 1 unit
    Area of circle estimated by checking the the number of darts falling within the circular  region
    input:
    n - number of simulations
    output:
    estpi - numerical estimate of pi using monte carlo formula
    '''
    
    dsq = float(n) # darts in square region represent the square`s area
    dcr = 0.00 # darts in circular region represnting circles`s area
    
    for i in range(n):  # running monte carlo simulations
        x, y =  random.random(), random.random() # generating random points in plane
        
        r = ((x-0.5)**2 + (y-0.5)**2)**0.5 # finding distance of the point from circle`s centre
        
        if r <= 0.5:  # checking whether the point lies within the circle
            dcr += 1  
     
    estpi = 4*dcr/dsq
    return estpi 
    
if __name__ == "__main__":
    unittest.main()
