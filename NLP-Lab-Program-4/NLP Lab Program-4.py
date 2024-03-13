#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict

# Given corpus
corpus = [
    "(eos) Can I sit near you (eos)",
    "(eos) You can sit (eos)",
    "(eos) Sit near him (eos)",
    "(eos) I can sit you (eos)"
]

# Function to tokenize text into words
def tokenize(text):
    return text.split()

# Function to calculate trigram probabilities
def calculate_trigram_probabilities(corpus):
    trigram_counts = defaultdict(int)
    bigram_counts = defaultdict(int)

    for sentence in corpus:
        words = tokenize(sentence)
        for i in range(len(words) - 2):
            trigram = tuple(words[i:i+3])
            bigram = tuple(words[i:i+2])
            trigram_counts[trigram] += 1
            bigram_counts[bigram] += 1

    trigram_probabilities = {}
    for trigram, count in trigram_counts.items():
        bigram = trigram[:2]
        trigram_probabilities[trigram] = count / bigram_counts[bigram]

    return trigram_probabilities

# Calculate trigram probabilities
trigram_probabilities = calculate_trigram_probabilities(corpus)

# Print trigram probabilities
print("Trigram Probabilities:")
for trigram, probability in trigram_probabilities.items():
    print(f"{trigram}: {probability}")


# In[2]:


def generate_ngrams(word, n):
    ngrams = []
    for i in range(len(word) - n + 1):
        ngrams.append(word[i:i+n])
    return ngrams

# Given words
words = ['quote', 'patient', 'patent', 'impatien']

# Generate and print character-based N-grams for each word
for word in words:
    print(f"Word: {word}")
    for n in range(1, len(word) + 1):
        ngrams = generate_ngrams(word, n)
        print(f"{n}-grams: {ngrams}")
    print()


# In[3]:


from collections import Counter

# Given words
words = ['qotient', 'quotent', 'quotient']

# Corpus of words
corpus = ['quotient'] * 1000  # Assume 'quotient' occurs 1000 times in the corpus

# Calculate the frequency of each word in the corpus
word_counts = Counter(corpus)

# Calculate the total number of words in the corpus
total_words = sum(word_counts.values())

# Calculate the probability of occurrence of each word
word_probabilities = {}
for word in words:
    word_probabilities[word] = word_counts[word] / total_words

# Print the probabilities of occurrence of each word
for word, probability in word_probabilities.items():
    print(f"Probability of {word}: {probability}")

# Identify the correct spelling based on the highest probability
correct_spelling = max(word_probabilities, key=word_probabilities.get)
print(f"\nCorrect Spelling: {correct_spelling}")


# In[ ]:




