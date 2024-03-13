#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
nltk.download()


# In[5]:


import nltk 
spanish_lemmatizer = nltk.stem.WordNetLemmatizer() 
# Singular forms 
dia = "día"
dia_lemma = spanish_lemmatizer.lemmatize(dia, "n") 
dia_plural = "días" 
dia_plural_lemma = spanish_lemmatizer.lemmatize(dia_plural, "n") 
 
# Gender 
gender = "masculine" 
 
# Number 
number = "singular" 
number_plural = "plural" 
 
# Part of speech 
pos = "noun" 
 
# Syntactic features 
features = { 
    "Gender": gender, 
    "Number": number 
} 
features_plural = { 
    "Gender": gender, 
    "Number": number_plural 
}
# Print results 
print(f"Singular form: {dia}, lemma: {dia_lemma}, features: {features}") 
print(f"Plural form: {dia_plural}, lemma: {dia_plural_lemma}, features: {features_plural}") 


# In[12]:


import nltk 
list_a = ['Red', 'Mad', 'Soft', 'Wide', 'Sharp'] 
tagged_list_a = nltk.pos_tag(list_a) 
print(tagged_list_a)


# In[15]:


import nltk 
from nltk.stem import WordNetLemmatizer 
wnl = WordNetLemmatizer() 
word = 'madden' 
lemma = wnl.lemmatize(word, 'v') 
print(f"Word: {word}") 
print(f"Lemma: {lemma}") 
print(f"Suffix: {word[len(lemma):]}") 


# In[22]:


import nltk 
from nltk.stem import WordNetLemmatizer 
 
# Initialize the WordNetLemmatizer 
wnl = WordNetLemmatizer() 
 
# Define the verb 
verb = "run" 
 
# Define the tenses and aspects 
tenses_aspects = ["infinitive", "present", "past", "present_continuous", "past_continuous", "present_perfect", "past_perfect", "present_perfect_continuous", "past_perfect_continuous"] 
 
# Define the persons 
persons = ["first_singular", "second_singular", "third_singular", "first_plural", "second_plural", "third_plural"] 
 
# Loop through all combinations and print the result 
for tense_aspect in tenses_aspects: 
    for person in persons: 
        if tense_aspect == "infinitive": 
            if person == "third_singular": 
                result = wnl.lemmatize(verb, "v") 
            else: 
                result = verb 
        elif tense_aspect == "present": 
            if person == "third_singular": 
                result = verb + "s" 
            else: 
                result = verb 
        elif tense_aspect == "past": 
            if verb[-1] == "e": 
                result = verb + "d" 
            elif verb[-2:] == "y": 
                result = verb[:-1] + "ied" 
            else: 
                result = verb + "ed" 
        elif tense_aspect == "present_continuous": 
            result = "am/is/are " + verb + "ing" 
        elif tense_aspect == "past_continuous": 
            result = "was/were " + verb + "ing" 
        elif tense_aspect == "present_perfect": 
            result = "have/has " + verb + "ed" 
        elif tense_aspect == "past_perfect": 
            result = "had " + verb + "ed" 
        elif tense_aspect == "present_perfect_continuous": 
            result = "have/has been " + verb + "ing" 
        elif tense_aspect == "past_perfect_continuous": 
            result = "had been " + verb + "ing" 
 
        # Add the person to the result 
    if person == "first_singular": 
        result += " (I)" 
    elif person == "second_singular": 
        result += " (you)" 
    elif person == "third_singular": 
        result += " (he/she/it)" 
    elif person == "first_plural": 
        result += " (we)" 
    elif person == "second_plural": 
        result += " (you all)" 
    elif person == "third_plural": 
        result += " (they)" 
        
        # Print the result 
print(tense_aspect.capitalize() + " " + person.capitalize() + ": " + result)


# In[23]:


import nltk 
 
# Define the three lists of words 
list1 = ['taller', 'shorter', 'higher', 'lower', 'smarter'] 
list2 = ['mower', 'teacher', 'sailor', 'caller', 'operator'] 
list3 = ['never', 'cover', 'finger', 'river'] 
 
# Use the NLTK POS tagger to get the POS tags of the words 
pos_tags_list1 = nltk.pos_tag(list1) 
pos_tags_list2 = nltk.pos_tag(list2) 
pos_tags_list3 = nltk.pos_tag(list3) 
 
# Filter out the words that end with 'er' or 'or' 
er_words = [word for word, pos in pos_tags_list1 if word[-2:] == 'er'] 
or_words = [word for word, pos in pos_tags_list2 if word[-2:] == 'or'] 
 
# Check if the filtered words have a common POS tag 
er_pos_tags = set(pos for word, pos in pos_tags_list1 if word[-2:] == 'er') 
or_pos_tags = set(pos for word, pos in pos_tags_list2 if word[-2:] == 'or') 
 
if len(er_pos_tags) == 1 and len(or_pos_tags) == 1 and er_pos_tags == or_pos_tags: 
    print("The words ending with 'er'/'or' have a common feature of indicating the agent or doer of an action or the one who performs a specific role or function.") 
else: 
    print("The words ending with 'er'/'or' do not have a common feature.")


# In[24]:


import nltk 
from nltk.stem import SnowballStemmer 
 
# Create a Snowball stemmer for English 
stemmer = SnowballStemmer('english') 
 
# Define the list of words 
words = ['kissed', 'stronger', 'goodness', 'teacher', 'achievement'] 
 
# Iterate over the words and identify their root and suffix 
for word in words: 
    root = stemmer.stem(word) 
    suffix = word[len(root):] 
    print(f"{word}: root='{root}', suffix='{suffix}'")


# In[ ]:




