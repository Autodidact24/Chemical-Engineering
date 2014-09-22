# Date : Oct 18
# Author : Shubham Singh Tomar

# Modeling Reactive distillation

# Starting out - Simple batch distillation problem


from scipy import *
from scipy.integrate import odeint
from pylab import *
import matplotlib.pyplot as plt

# Plugging-in contant values
D = 10
a = 2.41
W_int = 100
x_w_int = 0.5

t = range(0, 6, 1)

# Defining function for integration
def batch(x_w, t):
	W_t = -D*t + W_int
	y = a*x_w/ (1.0 + x_w*(a-1.0))

	dx_wdt = -(D/W_t)*(y - x_w)
	return dx_wdt

x_w_sol = odeint(batch, x_w_int, t)

# Plotting the solution
figure()
plot(t, x_w_sol, '-o')
xlabel('Time, hours')
ylabel('x_w')
grid()
plt.show()
