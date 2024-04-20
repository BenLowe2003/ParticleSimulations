
from matplotlib import pyplot as plt
from EphemerisTestIntegrator import integrator_names, errors_real, errors_ref, times

integrator_names = ['euler_forwards','euler_back','semi_implicit_euler',
                                     'midpoint','rk4'] 


plt.bar(integrator_names, errors_real)
plt.xlabel("Integration Method")
plt.ylabel("Average Error (metres)")
plt.title("Error From True Ephemerids Value For Different Integrators")
plt.show()

plt.bar(integrator_names, errors_ref)
plt.xlabel("Integration Method")
plt.ylabel("Average Error (metres)")
plt.title("Error From Refrence Simulation For Different Integrators")
plt.show()

plt.bar(integrator_names, times)
plt.xlabel("Integration Method")
plt.ylabel("Time To Complete Integration (seconds)")
plt.title("Duration For Different Integrators To Complete")
plt.show()
