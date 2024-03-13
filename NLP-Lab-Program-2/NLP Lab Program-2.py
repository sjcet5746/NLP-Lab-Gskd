#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn

def generate_word(root, category, number=None, gender=None, person=None, tense=None):
    stemmer = PorterStemmer()
    stem = stemmer.stem(root)

    # Noun singular/plural
    if category == 'noun':
        if number == 'singular':
            return root
        elif number == 'plural':
            plural = stem + 'ren' if stem.endswith(('s', 'x', 'ch')) else stem + 's'
            return plural

    # Verb conjugation (limited to present tense)
    elif category == 'verb':
        if tense == 'simple-present':
            if person == 'first':
                return root
            elif person == 'third':
                if gender == 'male':
                    return stem + 's'
                else:
                    return root

# Example usage
if __name__ == "__main__":
    # Generate words with the specified features
    words = [
        ('boy', 'noun', 'singular'),
        ('child', 'noun', 'plural'),
        ('play', 'verb', 'singular', 'male', 'first', 'simple-present'),
        ('play', 'verb', 'singular', 'male', 'third', 'simple-present') 
    ]

    for word_info in words:
        generated_word = generate_word(*word_info)
        print(generated_word)


# In[10]:


import nltk
# Generate word
word = nltk.corpus.wordnet.morphy('boy', nltk.corpus.wordnet.NOUN)
print(word)


# In[12]:


import nltk
# Generate word
word = nltk.corpus.wordnet.morphy('child', nltk.corpus.wordnet.NOUN)
word_plural = nltk.PluralizePluralize.pluralize(word)
print(word_plural)


# In[13]:


import nltk
# Generate word
word = nltk.corpus.wordnet.morphy('play', nltk.corpus.wordnet.VERB)
word_inflected = nltk.conjugate.conjugate(word, tense='present', number='singular', person='1st', gender='male')
print(word_inflected)


# In[14]:


import nltk
# Generate word
word = nltk.corpus.wordnet.morphy('play', nltk.corpus.wordnet.VERB)
word_inflected = nltk.conjugate.conjugate(word, tense='present', number='singular', person='3rd', gender='male')
print(word_inflected)


# In[17]:


def generate_words(features):
    for feature in features:
        root = feature['root']
        category = feature['category']
        gender = feature.get('gender', None)
        number = feature['number']
        case = feature.get('case', None)
        person = feature.get('person', None)
        tense = feature.get('tense', None)
        
        if category == 'noun':
            if gender == 'female' and number == 'singular' and case == 'direct':
                word = root
            elif gender == 'male' and number == 'singular' and case == 'oblique':
                word = root + 'e'
        elif category == 'verb':
            if gender == 'female' and number == 'plural' and person == 'third' and tense == 'present-perfect':
                word = root + 'ी हैं'
            elif gender == 'female' and number == 'singular' and person == 'first' and tense == 'simple-future':
                word = root + 'ूंगा'
                
        print(f"Root: {root}, Category: {category}, Gender: {gender}, Number: {number}, Case: {case}, Person: {person}, Tense: {tense}, Word: {word}")

# Example usage:
features = [
    {'root': 'पुस्तक', 'category': 'noun', 'gender': 'female', 'number': 'singular', 'case': 'direct'},
    {'root': 'बाग', 'category': 'noun', 'gender': 'male', 'number': 'singular', 'case': 'oblique'},
    {'root': 'खेल', 'category': 'verb', 'gender': 'female', 'number': 'plural', 'person': 'third', 'tense': 'present-perfect'},
    {'root': 'पढ़', 'category': 'verb', 'gender': 'female', 'number': 'singular', 'person': 'first', 'tense': 'simple-future'}
]

generate_words(features)


# In[ ]:




