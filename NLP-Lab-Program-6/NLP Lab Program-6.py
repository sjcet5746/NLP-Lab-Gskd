#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

class MarkovModel:
    def __init__(self, transition_matrix, emission_matrix):
        self.transition_matrix = transition_matrix
        self.emission_matrix = emission_matrix

    def generate_sequence(self, initial_state, length):
        current_state = initial_state
        sequence = []
        for _ in range(length):
            sequence.append(current_state)
            current_state = np.random.choice(len(self.transition_matrix), p=self.transition_matrix[current_state])
        return sequence

class HiddenMarkovModel:
    def __init__(self, transition_matrix, emission_matrix):
        self.transition_matrix = transition_matrix
        self.emission_matrix = emission_matrix

    def generate_sequence(self, initial_state, length):
        current_state = initial_state
        sequence = []
        for _ in range(length):
            observed_state = np.random.choice(len(self.emission_matrix[current_state]), p=self.emission_matrix[current_state])
            sequence.append(observed_state)
            current_state = np.random.choice(len(self.transition_matrix), p=self.transition_matrix[current_state])
        return sequence

# Example usage
transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])  # Example transition matrix
emission_matrix = np.array([[0.9, 0.1], [0.2, 0.8]])  # Example emission matrix

# Markov Model
markov_model = MarkovModel(transition_matrix, emission_matrix)
markov_sequence = markov_model.generate_sequence(initial_state=0, length=10)
print("Markov Model Sequence:", markov_sequence)

# Hidden Markov Model
hidden_markov_model = HiddenMarkovModel(transition_matrix, emission_matrix)
hidden_markov_sequence = hidden_markov_model.generate_sequence(initial_state=0, length=10)
print("Hidden Markov Model Sequence:", hidden_markov_sequence)


# In[3]:


import numpy as np

class HMM_POS_Tagging:
    def __init__(self, states, observations, transition_probabilities, emission_probabilities):
        self.states = states
        self.observations = observations
        self.transition_probabilities = transition_probabilities
        self.emission_probabilities = emission_probabilities

    def viterbi_algorithm(self, sequence):
        T = len(sequence)  # Length of the input sequence
        N = len(self.states)  # Number of POS tags

        # Initialize dynamic programming table
        dp = np.zeros((N, T))
        backpointer = np.zeros((N, T), dtype=int)

        # Initialize the first column of dp table
        for i, state in enumerate(self.states):
            dp[i, 0] = self.emission_probabilities[state].get(sequence[0], 0) * 1  # Initial probability * transition probability

        # Fill in the dp table
        for t in range(1, T):
            for i, state in enumerate(self.states):
                max_prob = 0
                max_index = 0
                for j, prev_state in enumerate(self.states):
                    prob = dp[j, t-1] * self.transition_probabilities[prev_state].get(state, 0) * self.emission_probabilities[state].get(sequence[t], 0)
                    if prob > max_prob:
                        max_prob = prob
                        max_index = j
                dp[i, t] = max_prob
                backpointer[i, t] = max_index

        # Backtrace to find the best path
        best_path = [np.argmax(dp[:, T-1])]
        for t in range(T-1, 0, -1):
            best_path.insert(0, backpointer[best_path[0], t])

        return [self.states[i] for i in best_path]

# Example usage
states = ['Noun', 'Verb', 'Adjective']
observations = ['the', 'cat', 'sat']
transition_probabilities = {
    'Noun': {'Noun': 0.5, 'Verb': 0.2, 'Adjective': 0.3},
    'Verb': {'Noun': 0.3, 'Verb': 0.4, 'Adjective': 0.3},
    'Adjective': {'Noun': 0.2, 'Verb': 0.3, 'Adjective': 0.5}
}
emission_probabilities = {
    'Noun': {'the': 0.6, 'cat': 0.2, 'sat': 0.2},
    'Verb': {'the': 0.1, 'cat': 0.7, 'sat': 0.2},
    'Adjective': {'the': 0.2, 'cat': 0.3, 'sat': 0.5}
}

hmm = HMM_POS_Tagging(states, observations, transition_probabilities, emission_probabilities)
sequence = ['the', 'cat', 'sat']
predicted_tags = hmm.viterbi_algorithm(sequence)
print("Predicted POS Tags:", predicted_tags)


# In[4]:


import numpy as np

class HMM_POS_Tagging:
    def __init__(self, transition_matrix, emission_matrix, initial_probabilities):
        self.transition_matrix = transition_matrix
        self.emission_matrix = emission_matrix
        self.initial_probabilities = initial_probabilities

    def viterbi_decode(self, sequence):
        T = len(sequence)
        N = len(self.transition_matrix)

        # Initialize Viterbi matrix and backpointers
        V = np.zeros((N, T))
        backpointers = np.zeros((N, T), dtype=int)

        # Initialize Viterbi matrix with initial probabilities
        V[:, 0] = self.initial_probabilities * self.emission_matrix[:, sequence[0]]

        # Iterate over each word in the sequence
        for t in range(1, T):
            for s in range(N):
                # Calculate the probability of the best path to state s at time t
                V[s, t] = np.max(V[:, t - 1] * self.transition_matrix[:, s]) * self.emission_matrix[s, sequence[t]]
                # Store the index of the previous state in the best path
                backpointers[s, t] = np.argmax(V[:, t - 1] * self.transition_matrix[:, s])

        # Backtrack to find the best path
        best_path = [np.argmax(V[:, T - 1])]
        for t in range(T - 1, 0, -1):
            best_path.append(backpointers[best_path[-1], t])
        best_path.reverse()

        return best_path

# Example usage
transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])  # Example transition matrix
emission_matrix = np.array([[0.9, 0.1], [0.2, 0.8]])  # Example emission matrix
initial_probabilities = np.array([0.5, 0.5])  # Example initial probabilities

hmm_pos_tagger = HMM_POS_Tagging(transition_matrix, emission_matrix, initial_probabilities)
sequence = [0, 1]  # Example sequence of word indices (e.g., [0, 1] corresponds to ['the', 'cat'])

best_path = hmm_pos_tagger.viterbi_decode(sequence)
print("Best path (POS tags):", best_path)


# In[10]:


import numpy as np
from collections import Counter

class HMM_POS:
    def __init__(self, states, transition_probs, emission_probs):
        self.states = states
        self.transition_probs = transition_probs
        self.emission_probs = emission_probs

    def train(self, corpus):
        # Count occurrences of state transitions and emissions in the corpus
        transition_counts = {state: Counter() for state in self.states}
        emission_counts = {state: Counter() for state in self.states}

        for sentence in corpus:
            previous_state = None
            for observation, state in sentence:
                if previous_state is not None:
                    transition_counts[previous_state][state] += 1
                emission_counts[state][observation] += 1
                previous_state = state

        # Estimate transition and emission probabilities from counts
        self.transition_probs = {state: {next_state: count / sum(transition_counts[state].values())
                                         for next_state, count in counts.items()}
                                  for state, counts in transition_counts.items()}
        self.emission_probs = {state: {observation: count / sum(emission_counts[state].values())
                                       for observation, count in counts.items()}
                                for state, counts in emission_counts.items()}

# Example corpus
corpus = [
    [('The', 'DET'), ('quick', 'ADJ'), ('brown', 'ADJ'), ('fox', 'NOUN'), ('jumps', 'VERB'), ('over', 'ADP'), ('the', 'DET'), ('lazy', 'ADJ'), ('dog', 'NOUN')],
    [('The', 'DET'), ('lazy', 'ADJ'), ('dog', 'NOUN'), ('is', 'VERB'), ('sleeping', 'VERB')],
    [('The', 'DET'), ('cat', 'NOUN'), ('chases', 'VERB'), ('the', 'DET'), ('mouse', 'NOUN')]
]

# Initialize HMM
states = {'DET', 'NOUN', 'ADJ', 'VERB', 'ADP'}
transition_probs = {state: {next_state: 0.2 for next_state in states} for state in states}
emission_probs = {state: {'word': 0.2 for word in ['word']} for state in states}

hmm = HMM_POS(states, transition_probs, emission_probs)

# Train HMM on corpus
hmm.train(corpus)

# Print transition and emission probabilities
print("Transition Probabilities:")
for state, probs in hmm.transition_probs.items():
    print(f"{state}: {probs}")

print("\nEmission Probabilities:")
for state, probs in hmm.emission_probs.items():
    print(f"{state}: {probs}")


# In[ ]:




