# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

from statistics import mean

sentence = input()
for char in ',.;:?!-':
    if char in sentence:
        sentence = sentence.replace(char, '')


lengths = (len(word) for word in sentence.split())
print(mean(lengths))
