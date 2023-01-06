import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('WebAgg')

plt.figure()
xs = np.arange(0,10, .1)
plt.plot(xs, np.sin(xs))
plt.show()
print("end")