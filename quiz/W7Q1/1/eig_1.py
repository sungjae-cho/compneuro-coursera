import numpy as np

Q = np.array(
    [
        [ 0.20,  0.10],
        [ 0.10,  0.15],
    ]
)

eig_vals, eig_vecs = np.linalg.eig(Q)
n_eig = eig_vals.shape[0]

print('Eigenvalues')
print(eig_vals)
print('Eigenvectors')
print(eig_vecs)

i_max = np.argmax(eig_vals)
print('The largest eigenvalue')
print(eig_vals[i_max])
print('The eigenvector of the largeest eigen value')
max_eig_vec = eig_vecs[:,i_max]
print(max_eig_vec)

print('The ratio of each row of the eigenvector to the given vectors w')
print('w that has the most similar ratios is the answer.')
print('#1')
w_1 = np.array([-1.5764, -1.2308])
print(max_eig_vec / w_1)
print('#2')
w_2 = np.array([-1.5155, -1.3051])
print(max_eig_vec / w_2)
print('#3')
w_3 = np.array([0.8944, 1.7889])
print(max_eig_vec / w_3)
print('#4')
w_4 = np.array([1.0515, 1.7013])
print(max_eig_vec / w_4)
