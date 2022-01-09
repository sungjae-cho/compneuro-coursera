# 3. Extracting Information from Neurons: Neural Decoding

- Neural decoding: To find mappings from spikes to stimuli.

## 3.1. Neural Decoding and Signal Detection Theory

<aside>
💡 neural decoding, signal detection theory(, likelihood-ratio test, Neyman-Pearson lemma)

</aside>

- **Detection theory** or **signal detection theory** is a means to measure the ability to differentiate between information-bearing patterns (called stimulus in living organisms, signal in machines) and random patterns that distract from the information (called noise). From Wikipedia.
- Britten, K. H., Shadlen, M. N., Newsome, W. T., & Movshon, J. A. (1992). The analysis of visual motion: a comparison of neuronal and psychophysical performance. *Journal of Neuroscience*, *12*(12), 4745-4765.
- Kiani, R., Hanks, T. D., & Shadlen, M. N. (2006). When is enough enough?. *Nature Neuroscience*, *9*(7), 861-863.

## 3.2. Population Coding and Bayesian Estimation

<aside>
💡 population coding, Bayesian inference, importance of correlation

</aside>

- **Population coding** is a method to represent signals by the joint activities of a number of neurons. In population coding, each neuron has a distribution of responses over some set of inputs, and the responses of many neurons may be combined to determine the value about the inputs.
- Jacobs, G. A., Miller, J. P., & Aldworth, Z. (2008). Computational mechanisms of mechanosensory processing in the cricket. *Journal of Experimental Biology*, *211*(11), 1819-1828.
- Theunissen, F. E., & Miller, J. P. (1991). Representation of sensory information in the cricket cercal sensory system. II. Information theoretic calculation of system accuracy and optimal tuning-curve widths of four primary interneurons. *Journal of Neurophysiology*, *66*(5), 1690-1703.
- [correlation] Shadlen, M. N., & Newsome, W. T. (1998). The variable discharge of cortical neurons: implications for connectivity, computation, and information coding. *Journal of neuroscience*, *18*(10), 3870-3896.

## 3.3. Reading Minds: Stimulus Reconstruction

<aside>
💡 stimulus reconstruction

</aside>

- Nishimoto, S., Vu, A. T., Naselaris, T., Benjamini, Y., Yu, B., & Gallant, J. L. (2011). Reconstructing visual experiences from brain activity evoked by natural movies. *Current Biology*, *21*(19), 1641-1646.

## 3.S1. Fred Rieke on Visual Processing in the Retina

- Rieke showed how to apply signal detection theory and Bayesian inference to visual processing in the retina.

## 3.S2. Gaussians in One Dimension (by Rich Pang)

<aside>
💡 Gaussian, central limit theorem

</aside>

- When not to use Gaussians
    - True distribution is bimodal.
    - True distribution is over small integers.
    - True distribution is over strictly positives.

## 3.S3. Probability distributions in 2D and Bayes' Rule (by Rich Pang)

<aside>
💡 multivariate Gaussian, chain rule, marginalization rule, Bayes rule

</aside>
