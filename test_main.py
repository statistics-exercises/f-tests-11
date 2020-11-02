import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_error_sum_of_squares(self) : 
        tvar, samples = 0, np.zeros([10,20])
        for i in range(10) : 
            samples[i,:] = np.random.normal(size=20)
            tvar = tvar + (len(samples[i,:])-1)*sample_variance( samples[i,:] )
        self.assertTrue( np.abs( tvar - error_sum_of_squares(samples))<1e-7, "Your code for calculating the error sum of squares is not correct"  )
        
    def test_treatment_sum_of_squares(self) : 
        tvar, samples = 0, np.zeros([10,20])
        for i in range(10) : samples[i,:] = np.random.normal(size=20)
        mu = np.zeros(10)
        for i in range(10) : mu[i] = sum( samples[i,:] ) / len( samples[i,:] )
        fmu, t = sum(mu) / len(mu), 0 
        for i in range(10) : t = t + 20*(mu[i] - fmu)*(mu[i] - fmu)
        self.assertTrue( np.abs( t - treatment_sum_of_squares(samples) )<1e-7, "Your code for calculating the treatment sum of squares is not correct" )
