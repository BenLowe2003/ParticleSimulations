


test_dt = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800, 409600, 819200, 1638400, 3276800, 6553600, 13107200, 26214400, 52428800, 104857600]
errors = [2.2277600628413246e+22, 4.455520415776612e+22, 8.9110411216462e+22, 1.7822082533384477e+23, 3.564416535686301e+23, 7.128833100381817e+23, 1.4257666229773016e+24, 2.858574071692206e+24, 5.745311437653537e+24, 1.1490622878229504e+25, 2.343185842133009e+25, 4.68637168456399e+25, 1.0093723628612563e+26, 2.3071368294338302e+26, 4.614273658904334e+26, 9.228547317845344e+26, 3.691418927145472e+27, 1.4765675708596557e+28, 5.906270283441558e+28, 2.362508113377209e+29, 9.450032453510011e+29]


from math import log10, exp
from matplotlib import pyplot as plt
from EphemeridTestTimestep import test_dt, errors



x = []
xticks = [ i for i in range(2,6)]
xnames = [ "{:.0e}".format(10 ** t, 5) for t in xticks]

yticks = [i for i in range(22, 26)]
ynames = [ "{:.0e}".format(10 ** t)  for t in yticks]

y = []

for i in range(11):
    x.append(log10(test_dt[i]))
    if errors[i] !=0:
        y.append(log10(errors[i]))
    else:
        y.append(0.0)



plt.plot(x, y)
plt.xticks(xticks, xnames)
plt.yticks(yticks, ynames)
plt.xlabel("timestep (seconds)")
plt.ylabel("average squred error (metres)")
plt.title("Error From True Ephemerids Values For Different Timesteps")
plt.show()
