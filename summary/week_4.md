# 4. Information Theory & Neural Coding (Adrienne Fairhall)

## 4.1. Information and Entropy

<aside>
💡 entropy, information, information in a spike train, mutual information,

</aside>

- Entropy is average information of a random variable. Entropy measures variability. (The base 2 is used for logarithm when dealing with information.)
- Information can quantify the degree of surprise.
- Mutual information (MI) quantifies how independent response (R) and stimulus (S) are.
- The average noise entropy is the average of entropy of R given every possible S. Every S indicates noise.
- Response is perfectly predicted by stimulus: `MI(R,S)=1`.
- Response is unrelated to stimulus: `MI(R,S)=0`.
- Fairhall, A., Shea-Brown, E., & Barreiro, A. (2012). Information theoretic approaches to understanding circuit function. *Current Opinion in Neurobiology*, *22*(4), 653-659.

## 4.2. Calculating Information in Spike Trains

<aside>
💡 information in spikes patterns, information in single spikes

</aside>

- Two types of information for spikes
    - Information in spikes patterns: the words of spike train
    - Information in single spikes: the firing rate (word size 1)
- Word: Fixed-length binary spike train.
- Mutual information is the difference between the total response entropy and the mean noise entropy.
- Experimental steps to obtain the mutual information of S and R.
    - Take one stimulus `S` and repeat many times to obtain `P(R|S)`.
    - Compute variability due to noise: noise entropy `H(R|S)`.
    - Repeat for all `S` and compute the mean noise entropy `sum_{S}( P(S) H(R|S) )`.
    - Compute the total entropy `H(R)`.
    - `MI(S,R) = H(R) - sum_{S}( P(S) H(R|S) )`
- [example 1] van Steveninck, R. R. D. R., Lewen, G. D., Strong, S. P., Koberle, R., & Bialek, W. (1997). Reproducibility and variability in neural spike trains. *Science*, *275*(5307), 1805-1808.
- [example 2] Reinagel, P., & Reid, R. C. (2000). Temporal coding of visual information in the thalamus. *Journal of Neuroscience*, *20*(14), 5392-5400.
- Brenner, N., Bialek, W., & Van Steveninck, R. D. R. (2000). Adaptive rescaling maximizes information transmission. *Neuron*, *26*(3), 695-702.

## 4.3. Coding Principles

<aside>
💡 efficient coding, feature adaptation, redundancy reduction, sparse coding

</aside>

- Coding principles for stimuli in the nature
    1. Efficient coding
    2. Feature adaptation
    3. Redundancy reduction
    4. Sparse coding
- **Efficient coding**: Barlow hypothesized that the spikes in the sensory system formed a neural code for efficiently representing sensory information. By efficient Barlow meant that the code minimized the number of spikes needed to transmit a given signal.
- **Redundancy reduction** means that the neural system should be optimized to perform as independently as possible. However, correlations can help error correction, robust coding and discrimination.
- [efficient coding] Barlow, H. B. (1961). Possible principles underlying the transformation of sensory messages. *Sensory Communication*, *1*(01).
- [efficient coding] Attneave, F. (1954). Some informational aspects of visual perception. *Psychological Review*, *61*(3), 183.
- [efficient coding] Laughlin, S. (1981). A simple coding procedure enhances a neuron's information capacity. *Zeitschrift für Naturforschung C*, *36*(9-10), 910-912.
- [feature adaptation] Fairhall, A. L., Lewen, G. D., Bialek, W., & van Steveninck, R. R. D. R. (2001). Efficiency and ambiguity in an adaptive neural code. *Nature*, *412*(6849), 787-792.
    - For fly neuron H1, determine the input/output relations through the stimulus presentation.
- [feature adaptation] Maravall, M., Petersen, R. S., Fairhall, A. L., Arabzadeh, E., & Diamond, M. E. (2007). Shifts in coding properties and maintenance of information transmission during adaptation in barrel cortex. *PLoS biology*, *5*(2), e19.
    - Extracellular in vivo recordings of responses to whisker motion in rat S1 barrel cortex in the anesthetized rat.
- [feature adaptation] Laughlin, S. (1981). A simple coding procedure enhances a neuron's information capacity. *Zeitschrift für Naturforschung C*, *36*(9-10), 910-912.
- [feature adaptation] Atick, J. J., & Redlich, A. N. (1991). Predicting ganglion and simple cell receptive field organizations. *International Journal of Neural Systems*, *1*(04), 305-315.
- [feature adaptation] Brenner, N., Bialek, W., & Van Steveninck, R. D. R. (2000). Adaptive rescaling maximizes information transmission. *Neuron*, *26*(3), 695-702.
- [feature adaptation] Atick, J. J., & Redlich, A. N. (1990). Towards a theory of early visual processing. *Neural Computation*, *2*(3), 308-320.
- [feature adaptation] Atick, J. J. (1992). Could information theory provide an ecological theory of sensory processing?. *Network: Computation in Neural Systems*, *3*(2), 213-251.
- [feature adaptation] Sharpee, T., Rust, N. C., & Bialek, W. (2004). Analyzing neural responses to natural signals: maximally informative dimensions. *Neural Computation*, *16*(2), 223-250.
- [sparse coding] Olshausen, B. A., & Field, D. J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural images. *Nature*, *381*(6583), 607-609.
- [sparse coding] Bell, A. J., & Sejnowski, T. J. (1995). An information-maximization approach to blind separation and blind deconvolution. *Neural Computation*, *7*(6), 1129-1159.

## 4.S1. What's up with entropy? (by Rich Pang)

<aside>
💡 entropy

</aside>

- Entropy is for quantifying uncertainty.
- Entropy for discrete and continuous distributions

## 4.S2. Information theory? That's crazy! (by Rich Pang)

<aside>
💡 information, mutual information

</aside>
