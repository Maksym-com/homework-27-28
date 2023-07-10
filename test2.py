import googletrans

translator = googletrans.Translator()

with open('file.txt', 'r') as file:
    info = file.readlines()

for t in info:
    print(t)

for i in info:
    inf = translator.translate(i, src='en', dest='pl')
    print(inf.text)
