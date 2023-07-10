import googletrans
import os

TRANSLATOR = googletrans.Translator()

# word = 'Hello'

# translate1 = TRANSLATOR.translate(word, dest='pl')
# print(translate1.text)

# translate2 = TRANSLATOR.translate(word, dest='fr')
# print(translate2.text)

# translate3 = TRANSLATOR.translate(word, dest='es')
# print(translate3.text)

# words = ["Cherries", "Watermelon", "Carrots"]

# translates = TRANSLATOR.translate(words, dest='pl')
# print(translates.text)

with open('C:\\Users\\HP\\Python_0\\test\\Homework.xlsx', 'r') as file:
    translate1 = TRANSLATOR.translate(file, dest='pl')
    print(translate1.text)
