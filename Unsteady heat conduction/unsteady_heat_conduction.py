
# author : Shubham Singh Tomar
# trying to make sense of unsteady heat conduction (fingers crossed !)


from scipy import *
from pylab import *
import matplotlib.pyplot as plt
#========================================================================
#Input constants
#========================================================================
dtau = 0.001 # Set dimensionless time increments
dx = 0.05    # Set dimensionless length increments
Tmax = 0.95  # Set maximum dimensionless temperature
M = 21       # Counter for length discretization
#========================================================================
#Calculate parameters
#========================================================================
dx = 1.0/(M-1)
dx_x = 1.0/(M-1)
ratio = dtau/(dx**2)
const = 1.0 - 2.0*ratio
#========================================================================
#Set counters to zero
#========================================================================
i = 0
tau = 0.0
#========================================================================
# Set up arrays for solution and print
#========================================================================
Tnew = zeros(M, dtype = float)
T = zeros(M, dtype = float)
T[0] = 1.0
T[-1] = 1.0
print "T initial = ", T
#========================================================================
# I just pick 400 on trial and error for the total array
#========================================================================
T_sol = zeros((400,M), dtype = float)
T_sol[:,0] = 1.0
T_sol[:,-1] = 1.0
#========================================================================
# While loop to iterate until mid-point temperature reaches Tmax
#========================================================================
while T[10] < Tmax:
    i = i + 1
    tau = tau + dtau
#========================================================================
# Calculate new tempertures
#========================================================================
    for j in range(1,M-1):
        Tnew[j] = ratio*(T[j-1] + T[j+1]) + const*T[j]
#========================================================================
# Substitute new Temperatures in array for T
#========================================================================
    for k in range(1,M-1):
        T[k] = Tnew[k]
        T_sol[i,k] = T[k]

print "Tau and T_final =", tau, T_sol[i,:]
#========================================================================
# Set up array for spatial values of x to plot
#========================================================================
x = [i*dx_x for i in range(M-1)]
x.append(1.0)
#========================================================================
# Plot the solutions
#=======================================================================
plot(x,T_sol[50,:])
plot(x,T_sol[100,:])
plot(x,T_sol[150,:])
plot(x,T_sol[250,:])
plot(x,T_sol[i,:])
#legend(['Tau = 0.5','Tau = 0.1','Tau = 0.15','Tau = 0.25',
#'Tau = final time'])
title('Normalized Slab Temperatures')
plt.show()
grid()
