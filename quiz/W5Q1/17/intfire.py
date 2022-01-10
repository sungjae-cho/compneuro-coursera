from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt


firing_rates = list()
I_list = list(range(0,100))

for I in I_list:
    # input current
    #I = 1 # nA

    # capacitance and leak resistance
    C = 1 # nF
    R = 40 # M ohms

    # I & F implementation dV/dt = - V/RC + I/C
    # Using h = 1 ms step size, Euler method

    V = 0
    tstop = 200
    abs_ref = 5 # absolute refractory period
    ref = 0 # absolute refractory period counter
    V_trace = []  # voltage trace for plotting
    V_th = 10 # spike threshold
    spiketimes = []

    for t in range(tstop):

       if not ref:
           V = V - (V/(R*C)) + (I/C)
       else:
           ref -= 1
           V = 0.2 * V_th # reset voltage

       if V > V_th:
           V = 50 # emit spike
           ref = abs_ref # set refractory counter
           spiketimes.append(t)

       V_trace += [V]

    firing_rates.append(len(spiketimes)/tstop*1000)

print('max(firing_rates)', max(firing_rates), 'Hz')
plt.xlabel('I (nA)')
plt.ylabel('Firing rate (Hz)')
plt.plot(I_list, firing_rates)
plt.show()
