#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter

# Corpus
corpus = [
    "I like ice cream.",
    "I like cake."
]

# Tokenize the corpus into words
words = [word for sentence in corpus for word in sentence.split()]

# Count the occurrences of each word in the corpus
word_counts = Counter(words)

# Vocabulary size
V = len(set(words))

# Total number of words in the corpus
N = len(words)

# Calculate the probability of each word with add-one smoothing
word_probabilities = {}
for word, count in word_counts.items():
    word_probabilities[word] = (count + 1) / (N + V)

# Calculate the probability of the word "chocolate"
# Assume it is unseen in the corpus
chocolate_probability = 1 / (N + V)

# Print the probability of each word and the probability of "chocolate"
print("Word Probabilities with Add-One Smoothing:")
for word, probability in word_probabilities.items():
    print(f"{word}: {probability}")

print(f"\nProbability of 'chocolate': {chocolate_probability}")


# In[2]:


# Given bigram count table
bigram_counts = {
    '(eos)': {'John': 0, 'Read': 300, 'Fountainhead': 0, 'Mary': 0, 'a': 300, 'Different': 0, 'Book': 0, 'She': 300, 'By': 0, 'Dickens': 0},
    'John': {'Read': 300, 'Fountainhead': 0, 'Mary': 0, 'a': 0, 'Different': 0, 'Book': 0, 'She': 0, 'By': 0, 'Dickens': 0},
    'Read': {'Fountainhead': 0, 'Mary': 300, 'a': 600, 'Different': 0, 'Book': 0, 'She': 0, 'By': 0, 'Dickens': 0},
    'Fountainhead': {'Mary': 0, 'a': 0, 'Different': 0, 'Book': 0, 'She': 0, 'By': 0, 'Dickens': 0},
    'Mary': {'a': 0, 'Different': 0, 'Book': 0, 'She': 0, 'By': 0, 'Dickens': 0},
    'a': {'Different': 300, 'Book': 300, 'She': 0, 'By': 0, 'Dickens': 0},
    'Different': {'Book': 300, 'She': 0, 'By': 0, 'Dickens': 0},
    'Book': {'She': 0, 'By': 300, 'Dickens': 0},
    'She': {'By': 0, 'Dickens': 0},
    'By': {'Dickens': 0},
    'Dickens': {}
}

# Parameters
delta = 0.02
N = 5100  # Total count of bigrams
V = 11    # Vocabulary size

# Apply Add-δ smoothing and calculate probabilities
bigram_probabilities = {}
for word, next_words in bigram_counts.items():
    bigram_probabilities[word] = {}
    total_count = sum(next_words.values()) + (V * delta)
    for next_word, count in next_words.items():
        bigram_probabilities[word][next_word] = (count + delta) / total_count

# Print the probabilities
print("Bigram Probabilities with Add-δ Smoothing:")
for word, next_words in bigram_probabilities.items():
    for next_word, probability in next_words.items():
        print(f"Probability of '{next_word}' given '{word}': {probability:.6f}")


# In[3]:


#(a)
# Unsmoothed probabilities
unsmoothed_probabilities = {
    'Dickens': 300 / 5100,
    'read': 300 / 5100,
    'a': 600 / 5100,
    'book': 300 / 5100
}

# Calculate the probability of the sentence using unsmoothed probabilities
sentence_probability_unsmoothed = 1
for word in "Dickens read a book".split():
    sentence_probability_unsmoothed *= unsmoothed_probabilities.get(word, 0)

print(f"Probability of the sentence using unsmoothed probabilities: {sentence_probability_unsmoothed}")


# In[4]:


#(b)
# Add-One smoothing
add_one_probabilities = {
    'Dickens': (300 + 1) / (5100 + 11),
    'read': (300 + 1) / (5100 + 11),
    'a': (600 + 1) / (5100 + 11),
    'book': (300 + 1) / (5100 + 11)
}

# Calculate the probability of the sentence using Add-One smoothing
sentence_probability_add_one = 1
for word in "Dickens read a book".split():
    sentence_probability_add_one *= add_one_probabilities.get(word, 1 / (5100 + 11))

print(f"Probability of the sentence using Add-One smoothing: {sentence_probability_add_one}")


# In[5]:


#(c)
# Add-δ smoothing with δ = 0.02
delta = 0.02
add_delta_probabilities = {
    'Dickens': (300 + delta) / (5100 + 11 * delta),
    'read': (300 + delta) / (5100 + 11 * delta),
    'a': (600 + delta) / (5100 + 11 * delta),
    'book': (300 + delta) / (5100 + 11 * delta)
}

# Calculate the probability of the sentence using Add-δ smoothing
sentence_probability_add_delta = 1
for word in "Dickens read a book".split():
    sentence_probability_add_delta *= add_delta_probabilities.get(word, delta / (5100 + 11 * delta))

print(f"Probability of the sentence using Add-δ smoothing: {sentence_probability_add_delta}")


# In[ ]:




