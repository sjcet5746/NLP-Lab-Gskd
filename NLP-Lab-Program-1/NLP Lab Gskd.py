#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Word Analyzer program-1
class MasculineNoun:
    def __init__(self, base_form):
        self.base_form = base_form
        self.forms = {
            'singular': {
                'nominative': base_form,
                'accusative': base_form,
                'dative': base_form,
                'genitive': base_form,
            },
            'plural': {
                'nominative': base_form + 's',
                'accusative': base_form + 's',
                'dative': base_form + 's',
                'genitive': base_form + 's',
            }
        }
        self.features = {
            'gender': 'masculine',
            'ending': 'A',
            'definiteness': ['definite', 'indefinite'],
            'number': ['singular', 'plural'],
            'case': ['nominative', 'accusative', 'dative', 'genitive'],
            'animacy': 'animate',
            # Add more features as needed
        }

    def print_forms(self):
        print("Base Form:", self.base_form)
        for number, forms in self.forms.items():
            for case, form in forms.items():
                print(f"{number.title()} {case.title()}: {form}")

    def print_features(self):
        print("Features:")
        for feature, value in self.features.items():
            print(f"{feature.capitalize()}: {value}")


# Example usage:
if __name__ == "__main__":
    masculine_noun = MasculineNoun("dia")
    masculine_noun.print_forms()
    print()
    masculine_noun.print_features()

#1.Word Analyzer program-2
A. The suffix "-en" typically attaches to verbs. The words in List A are adjectives.

B. When the suffix "-en" is attached to a word, the resulting word becomes a verb. For example, "soft" (adjective) becomes "soften" (verb) when the suffix "-en" is attached. 

Morphological properties of "soften" include:
- Infinitive form of the verb: "to soften"
- Present participle: "softening"
- Past tense: "softened"
- Present tense third person singular: "softens"
- Gerund: "softening"

These properties demonstrate the morphological transformation from an adjective to a verb with the attachment of the suffix "-en".
# In[6]:


#1.Word Analyzer program-3
class HindiVerb:
    def __init__(self, base_form):
        self.base_form = base_form
        self.conjugations = {
            'present_simple': {
                'singular': {
                    'first_person': base_form,
                    'second_person': base_form,
                    'third_person': base_form + 'ता/ती/ते है',
                },
                'plural': {
                    'first_person': base_form + 'ते हैं',
                    'second_person': base_form + 'ते हो',
                    'third_person': base_form + 'ते हैं',
                }
            },
            'past_simple': {
                'singular': {
                    'first_person': base_form + 'ा',
                    'second_person': base_form + 'ा',
                    'third_person': base_form + 'ा',
                },
                'plural': {
                    'first_person': base_form + 'े',
                    'second_person': base_form + 'े',
                    'third_person': base_form + 'े',
                }
            },
            # Add more tenses and aspects as needed
        }

    def conjugate(self):
        for tense, person in self.conjugations.items():
            print(f"{tense.replace('_', ' ').title()}:")
            for number, forms in person.items():
                print(f"{number.title()}:")
                for pronoun, form in forms.items():
                    print(f"{pronoun.replace('_', ' ').title()}: {form}")
            print()


# Example usage:
if __name__ == "__main__":
    hindi_verb = HindiVerb("खेल")
    hindi_verb.conjugate()

#1.Word Analyzer program-4
Yes, the words ending with 'er'/'or' in the provided lists do share a common feature. These endings typically denote a comparative form or an agent noun.

- List 1: Words like "taller", "shorter", "higher", "lower", and "smarter" all end with 'er' and indicate a comparison between two things or qualities. For example, "taller" compares the height of one thing to another, "smarter" compares intelligence, etc.

- List 2: Words like "mower", "teacher", "sailor", "caller", and "operator" all end with 'er' or 'or' and typically denote a person or thing that performs a specific action or function. For example, a "teacher" is someone who teaches, a "sailor" is someone who sails, etc.

So, the common feature among these words is that they either indicate a comparative form or an agent noun.
# In[7]:


#1.Word Analyzer program-5
class WordAnalyzer:
    def __init__(self, word):
        self.word = word

    def identify_root_and_suffix(self):
        suffixes = ['ed', 'er', 'ness', 'er', 'ment']
        for suffix in suffixes:
            if self.word.endswith(suffix):
                root = self.word[:-len(suffix)]
                print(f"Word: {self.word}")
                print(f"Root: {root}")
                print(f"Suffix: {suffix}")
                return
        print("Suffix not found in the word.")


# Example usage:
if __name__ == "__main__":
    words = ['kissed', 'stronger', 'goodness', 'teacher', 'achievement']
    for word in words:
        analyzer = WordAnalyzer(word)
        analyzer.identify_root_and_suffix()
        print()


# In[ ]:




