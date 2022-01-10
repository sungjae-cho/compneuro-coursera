import pickle
import matplotlib.pyplot as plt
import numpy as np

def check_data(data_path):
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    if data_path == 'tuning_3.4.pickle':
        print("data.keys()", data.keys())
        print("data['stim'].shape", data['stim'].shape)
        print("data['neuron1'].shape", data['neuron1'].shape)
        print("data['neuron2'].shape", data['neuron2'].shape)
        print("data['neuron3'].shape", data['neuron3'].shape)
        print("data['neuron4'].shape", data['neuron4'].shape)
        print("data['stim']", data['stim'])
        print("data['neuron1']", data['neuron1'])
        print("data['neuron2']", data['neuron2'])
        print("data['neuron3']", data['neuron3'])
        print("data['neuron4']", data['neuron4'])
        print("Types of stimuli:", data['neuron1'].shape[1])
        print("Trials of each stimulus:", data['neuron1'].shape[0])
    elif data_path == 'pop_coding_3.4.pickle':
        print("data.keys()", data.keys())
        for k in sorted(data.keys()):
            print("data[{}].shape".format(k), data[k].shape)
            print("data[{}]".format(k), data[k])
        print("Dimension of basis vectors:", data['c1'].shape[0])
        print("Trials of the myterious mystery stimulus", data['r1'].shape[0])
    else:
        print("Wrong data path!")
        exit()

def problem7():
    with open('tuning_3.4.pickle', 'rb') as f:
        data = pickle.load(f)
    fig, ax = plt.subplots()
    for i in range(1,5):
        key = 'neuron{}'.format(i)
        x = data['stim']
        y = data[key].mean(axis=0)
        ax.plot(x, y, label=key)
    leg = ax.legend()
    plt.xlabel('[Stimulus] Air direction (°)')
    plt.ylabel('[Response] Mean firing rate (Hz)')
    fig.tight_layout()
    plt.savefig('results_7.png')
    plt.show()

def problem8():
    with open('tuning_3.4.pickle', 'rb') as f:
        data = pickle.load(f)

    yx_max = 0
    fig, ax = plt.subplots()
    for i in range(1,5):
        key = 'neuron{}'.format(i)
        # Multiply spike rate by 10 seconds
        # 10 seconds: Recoding duration
        spikes = data[key] * 10
        x_mean = spikes.mean(axis=0)
        y_var = spikes.var(axis=0)
        ax.plot(x_mean, y_var, 'o', label=key)
        yx_max = max(yx_max, x_mean.max(), y_var.max())
    yx = np.arange(0, yx_max, 0.1)
    ax.plot(yx, yx, label="y=x")

    leg = ax.legend()
    plt.xlabel('Mean of spikes per 10 seconds')
    plt.ylabel('Variance of spikes per 10 seconds')
    fig.tight_layout()
    plt.savefig('results_8.png')
    plt.show()

def problem9():
    with open('tuning_3.4.pickle', 'rb') as f:
        data_t = pickle.load(f)
    with open('pop_coding_3.4.pickle', 'rb') as f:
        data_p = pickle.load(f)

    r_max = dict()
    r_mean = dict()
    pop_vec = np.zeros_like(data_p['c1'])
    for i in range(1,5):
        key = 'neuron{}'.format(i)
        r_max[i] = data_t[key].max()
        print("r_max[{}]".format(i), r_max[i])

        key = 'r{}'.format(i)
        r_mean[i] = data_p[key].mean()
        print("r_mean[{}]".format(i), r_mean[i])

        print("r_mean[{}] / r_max[{}]".format(i, i), r_mean[i] / r_max[i])

        key = 'c{}'.format(i)
        basis_vec = data_p[key] # basis vector
        pop_vec += (r_mean[i] / r_max[i]) * basis_vec

    print("pop_vec", pop_vec)
    x, y = pop_vec
    tan = x / y
    deg_pop_vec = np.rad2deg(np.arctan(tan))

    if x > 0 and y < 0:
        deg_pop_vec += 180
    elif x < 0 and y < 0:
        deg_pop_vec += 180

    print("deg_pop_vec", deg_pop_vec)
    print("round(deg_pop_vec)", round(deg_pop_vec, 0))

    j_min = np.absolute(data_t['stim'] - deg_pop_vec).argmin()
    closest_stim_deg = data_t['stim'][j_min]
    print("Closest stimulus degree to deg_pop_vec", closest_stim_deg)

if __name__ == "__main__":
    check_data('uning_3.4.pickle')
    problem7()
    problem8()
    check_data('pop_coding_3.4.pickle')
    problem9()
