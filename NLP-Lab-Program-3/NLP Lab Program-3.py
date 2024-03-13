#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[15]:


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


# In[11]:


import nltk
from nltk import word_tokenize
# Define the words
words = ["kori", "maari", "korchille", "maar"]

# Define the morpheme boundaries and their meanings
morphemes = {
    "ko": "1s Subject Pronoun",
    "ri": "Do Verb Stem",
    "ma": "1s Subject Pronoun",
    "ar": "Hit Verb Stem",
    "chille": "2s Past Tense Auxiliary Verb",
}

# Define a function to split a word into its morphemes
def split_word(word):
    morpheme_list = []
    while len(word) > 0:
        for morpheme, meaning in morphemes.items():
            if word.endswith(morpheme):
                morpheme_list.append((morpheme, meaning))
                word = word[:len(word)-len(morpheme)]
                break
            else:
            # No morpheme found
                return None
    morpheme_list.reverse()
    return morpheme_list

# Identify the morphemes and their meanings for each word
for word in words:
    morpheme_list = split_word(word)
    if morpheme_list is None:
        print(f"Could not identify morphemes for {word}")
    else:
        print(f"Morphemes for {word}:")
for morpheme, meaning in morpheme_list:
    print(f"{morpheme}: {meaning}")


# In[17]:


class HindiWord:
    def __init__(self, word):
        self.word = word

    def get_features(self):
        features = {
            'root': self.word[:-2],
            'ending': self.word[-2:]
        }
        return features

def select_same_paradigm_words(words):
    paradigms = {}
    for word in words:
        word_obj = HindiWord(word)
        features = word_obj.get_features()
        root = features['root']
        if root not in paradigms:
            paradigms[root] = []
        paradigms[root].append(word)

    return paradigms

# Example usage:
if __name__ == "__main__":
    words = ['मनुष्य', 'पक्षी', 'शिशु', 'गुरु', 'नर']
    paradigms = select_same_paradigm_words(words)
    for root, paradigm_words in paradigms.items():
        print("Paradigm:", root)
        print("Words belonging to the same paradigm:", paradigm_words)


# In[19]:


class HindiWord:
    def __init__(self, root, gender, number, case):
        self.root = root
        self.gender = gender
        self.number = number
        self.case = case

    def generate_word(self):
        if self.number == 'singular':
            if self.gender == 'masculine':
                if self.case == 'direct':
                    return self.root
                elif self.case == 'oblique':
                    return self.root[:-1] + 'e'
            elif self.gender == 'feminine':
                if self.case == 'direct':
                    return self.root
                elif self.case == 'oblique':
                    return self.root[:-1] + 'e'
            elif self.gender == 'neuter':
                if self.case == 'direct':
                    return self.root
                elif self.case == 'oblique':
                    return self.root[:-1] + 'e'
        elif self.number == 'plural':
            if self.gender == 'masculine' or self.gender == 'feminine':
                return self.root[:-1] + 'e'

# Grouping the words based on their grammatical features
words = [
    HindiWord('मनुष्य', 'masculine', 'singular', 'direct'),
    HindiWord('पक्षी', 'masculine', 'singular', 'direct'),
    HindiWord('शिशु', 'neuter', 'singular', 'direct'),
    HindiWord('गुरु', 'masculine', 'singular', 'direct'),
    HindiWord('नर', 'masculine', 'singular', 'direct')
]

# Generate the paradigm table
print("Paradigm Table:")
print("{:<10} {:<10} {:<10} {:<10}".format("Root", "Gender", "Number", "Case"))
for word in words:
    generated_word = word.generate_word()
    print("{:<10} {:<10} {:<10} {:<10}".format(word.root, word.gender, word.number, word.case))
    print("{:<10} {:<10} {:<10} {:<10}".format(generated_word, word.gender, "plural", word.case))
    print()


# In[21]:


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


# In[ ]:




