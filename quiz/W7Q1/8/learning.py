import pickle
import numpy as np
from tqdm import tqdm

lr = 1 # learning rate
alpha = 1 # alpha
dt = 0.01 # delta t (time)
max_iterations = 10**5

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)
inputs = data['c10p1']
N = inputs.shape[0] # The number of samples
dim = inputs.shape[1]
# Make each dimension of inputs have the zero mean.
print('Type constant to subtract from inputs')
constant = float(input())
for i in range(inputs.shape[1]):
    inputs[:,i] = inputs[:,i] - constant

w = np.random.standard_normal(dim) # Initialization from the standard normal distribution.

print('w(0)', w)

print('Iterations')
for iter in tqdm(range(max_iterations)):
    i = iter % N
    u = inputs[i,:]
    v = np.dot(u, w)
    w += dt * lr * (v * u - alpha * (v**2) * w)

print('w({})'.format(iter), w)
print('The ratio w[0]/w[1]', w[0]/w[1])
