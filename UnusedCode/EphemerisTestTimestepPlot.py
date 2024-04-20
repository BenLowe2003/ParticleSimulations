from math import log10, exp
from matplotlib import pyplot as plt
from EphemerisTestTimestep import test_dt, errors

x = test_dt
y = errors


plt.plot(x, y)

plt.ylim(0, errors[-1] + 1e15)
plt.xlabel("Timestep (seconds)")
plt.ylabel("Average Error (metres)")
plt.title("Error From True Ephemerids Values For Different Timesteps")
plt.show()

