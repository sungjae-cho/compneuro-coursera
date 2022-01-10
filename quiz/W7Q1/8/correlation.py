import pickle
import numpy as np

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)
inputs = data['c10p1']
N = inputs.shape[0] # The number of samples
# Make each dimension of inputs have the zero mean.
print('Type constant to subtract from inputs')
constant = float(input())
for i in range(inputs.shape[1]):
    inputs[:,i] = inputs[:,i] - constant

# Make the correlation matrix of inputs
correlation = np.matmul(inputs.T, inputs) / N

# Compute the eigenvalues and eigenvectors of the correlation matrix.
eig_vals, eig_vecs = np.linalg.eig(correlation)
n_eig = eig_vals.shape[0]

for i in range(n_eig):
    print('Eigenvalue', i)
    print(eig_vals[i])
    print('Eigenvector', i)
    print(eig_vecs[:,i])

i_max = np.argmax(eig_vals)
print('The largest eigenvalue')
print(eig_vals[i_max])
print('The eigenvector of the largeest eigen value')
max_eig_vec = eig_vecs[:,i_max]
print(max_eig_vec)
print('max_eigenvector[0]/max_eigenvector[1]',max_eig_vec[0]/max_eig_vec[1])
