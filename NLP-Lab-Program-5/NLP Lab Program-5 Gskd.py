#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.util import ngrams
from nltk.probability import FreqDist
corpus = ["I like apples", "I like bananas", "I like oranges"]
sentence = "I like pears"
corpus_tokens = [nltk.word_tokenize(sentence) for sentence in corpus]
sentence_tokens = nltk.word_tokenize(sentence)
corpus_ngrams = [ngrams(tokens, 2) for tokens in corpus_tokens]
sentence_ngrams = list(ngrams(sentence_tokens, 2))
fdist = FreqDist([ngram for ngrams in corpus_ngrams for ngram in ngrams])
probabilities = []
for ngram in sentence_ngrams:
    count = fdist[ngram] + 1 # Add-One smoothing
    total_count = len(fdist) + len(sentence_ngrams) # Add-One smoothing
    probability = count / total_count
    probabilities.append(probability)
for ngram, probability in zip(sentence_ngrams, probabilities):
    print(f"Probability of {ngram}: {probability}")


# In[3]:


import nltk
# Define bigram counts and smoothing delta
bigram_counts = {
 ("eos", "John"): 0,
 ("John", "Read"): 0,
 ("Read", "Fountainhead"): 300,
 ("Fountainhead", "Mary"): 0,
 ("Mary", "a"): 0,
 ("a", "Different"): 0,
 ("Different", "Book"): 0,
 ("Book", "She"): 300,
 ("She", "By"): 0,
 ("By", "Dickens"): 0,
 ("Dickens", "(eos)"): 300,
 # Add more bigrams as needed
}
delta = 0.02 # Smoothing delta value
# Calculate total number of bigrams and vocabulary size
N = sum(bigram_counts.values())
V = len(set(bigram_counts.keys())) # Assuming unique bigrams are keys
def add_delta_smoothing(counts, delta, N, V):
    smoothed_counts = {ngram: count + delta for ngram, count in counts.items()}
    smoothed_probabilities = {ngram: (count + delta) / (N + delta * V) for ngram, count in
    smoothed_counts.items()}
    return smoothed_probabilities
# Apply Add-δ smoothing and print results
smoothed_probs = add_delta_smoothing(bigram_counts, delta, N, V)
for bigram, prob in smoothed_probs.items():
    print(f"Probability of '{bigram[1]}' after '{bigram[0]}': {prob:.4f}")


# In[4]:


from nltk.util import bigrams
from nltk.probability import FreqDist, LidstoneProbDist
# Given bigram count table
bigram_counts = {
 ('eos', 'John'): 0,
 ('eos', 'Read'): 300,
 # ... (complete the table with the provided counts)
}
# Sentence to find probability
sentence = ['Dickens', 'read', 'a', 'book']
# (a) Unsmoothed probability
unsmoothed_prob = 1.0
for bigram in bigrams(['eos'] + sentence):
    unsmoothed_prob *= bigram_counts.get(bigram, 0) / bigram_counts.get((bigram[0],), 1)
    print(f"(a) Unsmoothed Probability P(S): {unsmoothed_prob}")
# (b) Applying Add-One smoothing
add_one_prob = 1.0
N = sum(bigram_counts.values())
V = len(set(word for bigram in bigram_counts.keys() for word in bigram))
for bigram in bigrams(['eos'] + sentence):
    add_one_prob *= (bigram_counts.get(bigram, 0) + 1) / (bigram_counts.get((bigram[0],), 0) + V)
    print(f"(b) Add-One Smoothing Probability P(S): {add_one_prob}")
# (c) Applying Add-δ smoothing
delta = 0.02
add_delta_prob = 1.0
for bigram in bigrams(['eos'] + sentence):
    add_delta_prob *= LidstoneProbDist(FreqDist(bigram_counts), delta, bins=V).prob(bigram)
    print(f"(c) Add-δ Smoothing Probability P(S): {add_delta_prob}")


# In[ ]:




