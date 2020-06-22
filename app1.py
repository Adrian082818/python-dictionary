import json

data = json.load(open("data/data.json"))

def translate(w):
    return data[w]

word = input("Enter word: ")

print(translate(word))