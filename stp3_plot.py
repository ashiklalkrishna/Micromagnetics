import matplotlib.pyplot as plt
import numpy as np

t_flwr = np.loadtxt ("D:/Desktop/Micromagnetics/stp3_flwr.out/table.txt", skiprows=1)
t_vor = np.loadtxt ("D:/Desktop/Micromagnetics/stp3_vor.out/table.txt", skiprows=1)

Ef=t_flwr[:,4]
Lf=t_flwr[:,5]
Ev=t_vor[:,4]
Lv=t_vor[:,5]

plt.plot(Lf,Ef,label="Initial state = Flower", marker='.')
plt.plot(Lv,Ev,label="Initial state = Vortex", marker='.')
plt.title ('Stp3 - Phase transion from Flower to Vortex state')
plt.legend()
plt.grid()
plt.show()
