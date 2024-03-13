#!/usr/bin/env python
# coding: utf-8

# In[5]:


import nltk
from nltk.util import trigrams
from nltk.probability import ConditionalFreqDist, ConditionalProbDist, MLEProbDist
corpus = [
 "Can I sit near you",
 "You can sit",
 "Sit near him",
 "I can sit you"
]
tokenized_corpus = [nltk.word_tokenize(sentence) for sentence in corpus]
trigram_list = list(trigrams(word for sentence in tokenized_corpus for word in sentence))
cfd = ConditionalFreqDist()
for trigram in trigram_list:
    condition = (trigram[0], trigram[1])
    cfd[condition][trigram[2]] += 1
    cpd = ConditionalProbDist(cfd, MLEProbDist)
    trigram_probabilities = {}
    for condition in cpd.conditions():
        trigram_probabilities[condition] = {}
    for word in cpd[condition].samples():
        trigram_probabilities[condition][word] = cpd[condition].prob(word)
        for condition in trigram_probabilities:
            for word in trigram_probabilities[condition]:
                print(f"Probability of '{word}' given the condition {condition}:{trigram_probabilities[condition][word]}")


# In[4]:


import nltk
from nltk.util import trigrams
from nltk.probability import ConditionalFreqDist, ConditionalProbDist, MLEProbDist
corpus = [
 "Can I sit near you",
 "You can sit",
 "Sit near him",
 "I can sit you"
]
tokenized_corpus = [nltk.word_tokenize(sentence) for sentence in corpus]
trigram_list = list(trigrams(word for sentence in tokenized_corpus for word in sentence))
cfd = ConditionalFreqDist()
for trigram in trigram_list:
    condition = (trigram[0], trigram[1])
    cfd[condition][trigram[2]] += 1
cpd = ConditionalProbDist(cfd, MLEProbDist)
trigram_probabilities = {}
for condition in cpd.conditions():
    trigram_probabilities[condition] = {}
    for word in cpd[condition].samples():
        trigram_probabilities[condition][word] = cpd[condition].prob(word)
for condition in trigram_probabilities:
    for word in trigram_probabilities[condition]:
        print(f"Probability of '{word}' given the condition {condition}:{trigram_probabilities[condition][word]}")


# In[6]:


import nltk
words = ["quote", "patient", "patent", "impatient"]
n = 3 # Change this value to adjust the n-gram size
def generate_ngrams(word):
    return [word[i:i+n] for i in range(len(word)-n+1)]
word_ngrams = {word: generate_ngrams(word) for word in words}
def jaccard_similarity(ngram1, ngram2):
    intersection = len(set(ngram1) & set(ngram2))
    union = len(set(ngram1) | set(ngram2))
    return intersection / union if union else 0
# Calculate similarity between each pair of words
similarities = { }
for i in range(len(words)):
    for j in range(i+1, len(words)):
        word1, word2 = words[i], words[j]
        ngram1, ngram2 = word_ngrams[word1], word_ngrams[word2]
        similarities[(word1, word2)] = jaccard_similarity(ngram1, ngram2)
# Print the n-grams and their similarities
for word1, word2 in similarities:
    print(f"Words: {word1} and {word2}")
    print(f"N-grams: {word_ngrams[word1]} & {word_ngrams[word2]}")
    print(f"Similarity: {similarities[(word1, word2)]:.4f}\n")


# In[12]:


import nltk
# Define corpus text (a large sample of text)
corpus_text = nltk.corpus.gutenberg.raw("C:/Users/Public/Gskd/gskd.txt")
words = ["qotient", "quotent", "quotient"] # Include all potential spellings
tokens = nltk.word_tokenize(corpus_text.lower())
fdist = nltk.FreqDist(tokens)
total_words = len(tokens)
probabilities = {word: (fdist[word] + 1) / (total_words + len(fdist.keys())) for word in words}
for word, prob in probabilities.items():
    print(f"- {word}: {prob:.4f}")
most_likely_word = max(probabilities, key=probabilities.get)
print("\nMost Likely Correct Spelling:")
print(most_likely_word)


# In[ ]:




