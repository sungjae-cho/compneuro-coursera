# 2. What do Neurons Encode? Neural Encoding Models (Adrienne Fairhall)

- This week focuses on finding mappings from stimuli to spikes, where we need analytic methods and information theoretical formulation.

## 2.1. What is the Neural Code?

<aside>
💡 neural code, stimulus, response, neural encoding, neural decoding, spike, firing rate, tuning curve

</aside>

- Issa, N. P., Rosenberg, A., & Husson, T. R. (2008). Models and measurements of functional maps in V1. *Journal of Neurophysiology*, *99*(6), 2745-2754.
    - Map of feature selectivity in primary visual cortex.
- Haxby, J. V., Gobbini, M. I., Furey, M. L., Ishai, A., Schouten, J. L., & Pietrini, P. (2001). Distributed and overlapping representations of faces and objects in ventral temporal cortex. *Science*, *293*(5539), 2425-2430.
    - Higher order feature selectivity.
- Quiroga, R. Q., Reddy, L., Kreiman, G., Koch, C., & Fried, I. (2005). Invariant visual representation by single neurons in the human brain. *Nature*, *435*(7045), 1102-1107.
    - The title itself: Invariant visual representation by single neurons in the human brain.

## 2.2. Neural Encoding: Simple Models

<aside>
💡 response model, [temporal/spatial] filtering, running average, leaky average

</aside>

## 2.3. Neural Encoding: Feature Selection

<aside>
💡 dimensionality reduction, spike-triggered average (STA), principal component analysis (PCA)

</aside>

- Spike-triggered average
    - is the average of time-framed stimuli triggering a spike. This can be used as a feature (vector) of given stimuli. Compared with spikes arising from white noise, spike-triggered average and Bayesian inference tells us what stimuli induce spikes.
- Koepsell, K., Wang, X., Vaingankar, V., Wei, Y., Wang, Q., Rathbun, D. L., ... & Sommer, F. T. (2009). Retinal oscillations carry visual information to cortex. *Frontiers in Systems Neuroscience*, *3*, 4.
    - Principal component analysis: spike sorting
- Fairhall, A. L., Burlingame, C. A., Narasimhan, R., Harris, R. A., Puchalla, J. L., & Berry, M. J. (2006). Selectivity for multiple stimulus features in retinal ganglion cells. *Journal of Neurophysiology*, *96*(5), 2724-2738.

## 2.4. Neural Encoding: Variability

<aside>
💡 Kullback-Leibler (KL) divergence, inter-spike interval (ISI) distributions, generalize linear model, time-rescaling theorem

</aside>

- This section introduces how to find what stimuli generate spikes of a neuron. You have to acquire the distribution of stimuli `P(stimulus)` and the conditional distribution of `P(spike|stimulus)` by injecting random stimuli following `P(stimulus)`. According to the Bayes rule, `P(stimulus|spike) = k*P(spike|stimulus)*P(stimulus)`. From this, we know how the activity of the given neuron varies depending on `stimulus`. From this variability, we can obtain an input/output curve.
- The Kullback-Leibler (KL) divergence from `P(stimulus|spike)` to `P(stimulus)` gives how stimuli and spikes are dependent. `KL=0` implies stimuli and spikes are independent. As KL grows, their dependence increases and the filter or transfer function from stimuli to spikes are more suitable.
- Maximize KL `KL(P(stimulus|spike)||P(stimulus))` = Maximize mutual intformation`MI(stimulus,spike)`
- Sharpee, T., Rust, N. C., & Bialek, W. (2004). Analyzing neural responses to natural signals: maximally informative dimensions. *Neural Computation*, *16*(2), 223-250.
- Fairhall, A., Shea-Brown, E., & Barreiro, A. (2012). Information theoretic approaches to understanding circuit function. *Current Opinion in Neurobiology*, *22*(4), 653-659.
- Shadlen, M. N., & Newsome, W. T. (1998). The variable discharge of cortical neurons: implications for connectivity, computation, and information coding. *Journal of Neuroscience*, *18*(10), 3870-3896.
- Pillow, J. W., Shlens, J., Paninski, L., Sher, A., Litke, A. M., Chichilnisky, E. J., & Simoncelli, E. P. (2008). Spatio-temporal correlations and visual signalling in a complete neuronal population. *Nature*, *454*(7207), 995-999.
- Brown, E. N., Barbieri, R., Ventura, V., Kass, R. E., & Frank, L. M. (2002). The time-rescaling theorem and its application to neural spike train data analysis. *Neural Computation*, *14*(2), 325-346.

## 2.S1. Vectors and Functions (by Rich Pang)

<aside>
💡 vector, vector space, inner product, projection, inner product of functions

</aside>

## 2.S2. Convolutions and Linear Systems (by Rich Pang)

<aside>
💡 convolution

</aside>

- Convolution can be seen as an inner production and therefore as a projection operation.

## 2.S3. Change of Basis and PCA (by Rich Pang)

<aside>
💡 basis, principal component analysis (PCA)

</aside>

## 2.S4. Welcome to the Eigenworld! (by Rich Pang)

<aside>
💡 eigenvector, eigenvalue,

</aside>

- Knowing the eigenvectors and eigenvalues of a matrix `A` tells you how `A` acts on any vector multiplied by `A`.
- The eigenvectors form the most natural basis for `A`.
- The eigenvalues are invariant to the change of basis.
- Usage 1: Check the stability of recurrent connections in recurrent networks.
- Usage 2: Decorrelate bases and then earn decorrelated bases: principal components.
- Usage 3: Dynamic system theory. This is a general statement of Usage 1.
