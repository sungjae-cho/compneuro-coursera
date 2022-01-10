import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu1 = 5
sigma1 = 0.5
penalty_w1 = 1
x1 = np.linspace(mu1 - 3*sigma1, mu1 + 3*sigma1, 100)
y1 = penalty_w1 * stats.norm.pdf(x1, mu1, sigma1)
plt.plot(x1, y1, label='P1')

mu2 = 7
sigma2 = 1
penalty_w2 = 0.5
x2 = np.linspace(mu2 - 3*sigma2, mu2 + 3*sigma2, 100)
y2 = penalty_w2 * stats.norm.pdf(x2, mu2, sigma2)
plt.plot(x2, y2, label='P2')

axvlines = [2.69, 5.667, 5.830, 5.978]
for x in axvlines:
    plt.axvline(x, color='red')

plt.savefig('plot_Gaussian.png')
plt.show()
