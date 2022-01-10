import numpy as np

w = np.array(
    [
        [ 0.6,  0.1,  0.1,  0.1,  0.1],
        [ 0.1,  0.6,  0.1,  0.1,  0.1],
        [ 0.1,  0.1,  0.6,  0.1,  0.1],
        [ 0.1,  0.1,  0.1,  0.6,  0.1],
        [ 0.1,  0.1,  0.1,  0.1,  0.6]
    ]
)

u = np.array(
    [ 0.6,  0.5,  0.6,  0.2,  0.1]
)

m = np.array(
    [
        [-0.5,  0.0,  0.5,  0.5,  0.0],
        [ 0.0, -0.5,  0.0,  0.5,  0.5],
        [ 0.5,  0.0, -0.5,  0.0,  0.5],
        [ 0.5,  0.5,  0.0, -0.5,  0.0],
        [ 0.0,  0.5,  0.5,  0.0, -0.5]
    ]
)

m *= 0.5

eig_vals, eig_vecs = np.linalg.eig(m)
n_eig = eig_vals.shape[0]

v_ss = np.zeros(n_eig)

print('Eigenvalues')
print(eig_vals)
print('Eigenvectors')
print(eig_vecs)

h = np.matmul(w,u)
for i in range(n_eig):
    v_ss += np.dot(h, eig_vecs[:,i]) / (1 - eig_vals[i]) * eig_vecs[:,i]

print('v_ss')
print(v_ss)
for elm in v_ss:
    print(elm)
