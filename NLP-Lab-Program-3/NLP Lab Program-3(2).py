#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
# Define the list of words
words = ['मनुष्य', 'पक्षी', 'शिशु', 'गुरु', 'नर']

# Define the morphological patterns for the paradigm
paradigm_pattern = r'(.*?)$'

# Create an empty dictionary to store the paradigm groups
paradigm_groups = {}
	
# Iterate through each word
for word in words:
    # Extract the morphological pattern of the word
    morphological_pattern = nltk.regexp_tokenize(word, paradigm_pattern)[0]

    # If the pattern is not in the paradigm groups dictionary, add it with the current word as the value
    if morphological_pattern not in paradigm_groups:
        paradigm_groups[morphological_pattern] = [word]
    else:
        # If the pattern is already in the paradigm groups dictionary, append the current word to the existing value
        paradigm_groups[morphological_pattern].append(word)

# Print the paradigm groups
for pattern, group in paradigm_groups.items():
    print(f'Words in paradigm with pattern "{pattern}": {", ".join(group)}')


# In[2]:


import nltk
from nltk import word_tokenize
from tabulate import tabulate

# Define the words
words = ["मनुष्य", "पक्षी", "शिशु", "गुरु", "नर"]

# Define the morphological categories
categories = {
    "Person": ["1s", "2s", "3s", "1p", "2p", "3p"],
    "Gender": ["Masc", "Fem", "Neut"],
    "Number": ["Sg", "Pl"]
}

# Define the inflection rules for each word
inflections = {
    "मनुष्य": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg", "Pl"]
    },
    "पक्षी": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg", "Pl"]
    },
    "शिशु": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg"]
    },
    "गुरु": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc"],
        "Number": ["Sg"]
    },
    "नर": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc"],
        "Number": ["Sg"]
    }
}

# Construct the paradigm table for each word
for word in words:
    table = []
    for person in categories["Person"]:
        for gender in categories["Gender"]:
            for number in categories["Number"]:
                inflected_word = inflections[word]["Person"][categories["Person"].index(person)]
                inflected_word += " " + inflections[word]["Gender"][categories["Gender"].index(gender)]
                inflected_word += " " + inflections[word]["Number"][categories["Number"].index(number)]
                table.append((person, gender, number, inflected_word))
    print(f"Paradigm table for {word}:")
    print(tabulate(table, headers=["Person", "Gender", "Number", "Inflected Word"], tablefmt="pipe"))
    print()


# In[3]:


class BengaliWord:
    def __init__(self, word):
        self.word = word

    def identify_morphemes(self):
        morphemes = {
            'kori': [('ko', '(I)'), ('ri', 'do')],
            'maari': [('ma', '(I)'), ('ari', 'hit')],
            'korchille': [('kor', '(You)'), ('chil', 'were'), ('le', 'doing')],
            'maar': [('ma', '(You)'), ('ar', 'hit')]
        }

        if self.word in morphemes:
            print(f"Word: {self.word}")
            print("Morphemes:")
            for morpheme, meaning in morphemes[self.word]:
                print(f"{morpheme} - {meaning}")
        else:
            print("Word not found in the dictionary.")


# Example usage:
if __name__ == "__main__":
    bengali_words = ['kori', 'maari', 'korchille', 'maar']
    for word in bengali_words:
        analyzer = BengaliWord(word)
        analyzer.identify_morphemes()
        print()


# In[5]:


import nltk
from nltk import word_tokenize
# Define the words
words = ["मनुष्य", "पक्षी", "शिशु", "गुरु", "नर"]
 
# Define the morphological categories
categories = {
    "Person": ["1s", "2s", "3s", "1p", "2p", "3p"],
    "Gender": ["Masc", "Fem", "Neut"],
    "Number": ["Sg", "Pl"]
}
# Define the inflection rules for each word
inflections = {
    "मनुष्य": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg", "Pl"]
    },
    "पक्षी": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg", "Pl"]
    },
    "शिशु": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg"]
    },
    "गुरु": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc"],
        "Number": ["Sg"]
    },
    "नर": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc"],
        "Number": ["Sg"]
    }
}

# Construct the paradigm table for each word
from tabulate import tabulate
for word in words:
    table = []
    for person in categories["Person"]:
        for gender in categories["Gender"]:
            for number in categories["Number"]:
                inflected_word = inflections[word]["Person"][categories["Person"].index(person)]
            inflected_word += " " +inflections[word]["Gender"][categories["Gender"].index(gender)]
        inflected_word += " " + inflections[word]["Number"][categories["Number"].index(number)]
    table.append((person, gender, number, inflected_word))
    print(f"Paradigm table for {word}:")
    print(tabulate(table, headers=["Person", "Gender", "Number", "Inflected Word"], tablefmt="pipe"))


# In[6]:


import nltk
from nltk import word_tokenize
from tabulate import tabulate

# Define the words
words = ["मनुष्य", "पक्षी", "शिशु", "गुरु", "नर"]

# Define the morphological categories
categories = {
    "Person": ["1s", "2s", "3s", "1p", "2p", "3p"],
    "Gender": ["Masc", "Fem", "Neut"],
    "Number": ["Sg", "Pl"]
}

# Define the inflection rules for each word
inflections = {
    "मनुष्य": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg", "Pl"]
    },
    "पक्षी": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg", "Pl"]
    },
    "शिशु": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc", "Fem", "Neut"],
        "Number": ["Sg"]
    },
    "गुरु": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc"],
        "Number": ["Sg"]
    },
    "नर": {
        "Person": ["मैं", "तुम", "वह", "हम", "तुम्हारे", "वे"],
        "Gender": ["Masc"],
        "Number": ["Sg"]
    }
}

# Construct the paradigm table for each word
for word in words:
    table = []
    for person in categories["Person"]:
        for gender in categories["Gender"]:
            for number in categories["Number"]:
                person_index = categories["Person"].index(person)
                gender_index = categories["Gender"].index(gender)
                number_index = categories["Number"].index(number)
                if person_index < len(inflections[word]["Person"]) and \
                   gender_index < len(inflections[word]["Gender"]) and \
                   number_index < len(inflections[word]["Number"]):
                    inflected_word = inflections[word]["Person"][person_index]
                    inflected_word += " " + inflections[word]["Gender"][gender_index]
                    inflected_word += " " + inflections[word]["Number"][number_index]
                    table.append((person, gender, number, inflected_word))
    print(f"Paradigm table for {word}:")
    print(tabulate(table, headers=["Person", "Gender", "Number", "Inflected Word"], tablefmt="pipe"))
    print()


# In[ ]:




