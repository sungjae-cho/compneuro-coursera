# 6. Computing with Networks

## 6.1. Modeling Connections Between Neurons

<aside>
💡 [excitatory/inhibitory] synapse, glutamate, GABA, synaptic filter

</aside>

- The strength of a synapse is determined by the numbers of releasing vesicles by the pre-synapse and opening ion channels by the post-synapse.
- The difference between excitatory and inhibitory synapses arises since their neurotransmitters are different. For this reason, their synapses toward a single neuron can be derived from the Hodgkin-Huxley model.
- The **synaptic filter** transforms a pre-synaptic spike to post-synaptic potential as times goes.

## 6.2. Introduction to Network Models

<aside>
💡 spiking neuron, firing-rate neuron, steady state

</aside>

- The firing rate neuron can be derived from a spiking neuron in the steady state such that `dV/dt=0`.

## 6.3. The Fascinating World of Recurrent Networks

<aside>
💡 recurrent network, stability analysis (of recurrence connectivity), amplification, short-term memory, working memory, gain modulation, oscillation

</aside>

- The eigenvalues of the matrix of recurrent connections tell us the activity of recurrent neurons. By the eigenvalues, the activity of recurrent neurons in the phase plane is well classified: convergence (stable fixed point), divergence (stable fixed point), converging oscillation (stable fixed point), diverging oscillation (unstable limit cycle), and pure oscillation (stable limit cycle).
- The roles of recurrent connections in recurrent networks
    - To amplify the activity of recurrent neurons (divergence)
    - To keep the activity of recurrent neurons: short-term memory, working memory (convergence)
    - To modulate the gain from inputs (convergence)
    - To induce the periodic activity of recurrent neurons (oscillation)
