import matplotlib.pyplot as plt
import numpy as np 

def error_sum_of_squares( data ) : 
  # Your code to calculate the error sum of squares goes here
  
def treatment_sum_of_squares( data ) :
  # Your code to calculate the treatment sum of squares goes here 
  

# This generates the graph of the error sum of squares that is described above
# you should not modify anything from here onwards
xvals, sse, sst, sstc = np.linspace(0,4,5), np.zeros(5), np.zeros(5), np.zeros(5)
for i in range(5) :
  samples = np.zeros([20,10])
  for j in range(10) : 
    samples[:,j] = np.random.normal( j*i, 1, size=20 )
  sse[i] = error_sum_of_squares( samples )
  sst[i] = treatment_sum_of_squares( samples )
  sstc[i] = sse[i] + sst[i] 
  
plt.plot( xvals, sse, 'ko' )
plt.plot( xvals, sst, 'ro' )
plt.plot( xvals, sstc, 'bo' )
plt.savefig("sum_of_squares.png")
