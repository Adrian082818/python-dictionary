import json

data = json.load(open("data/data.json"))

def translate(w):
    w = w.lower()
    if w in data:        
        return data[w]
    else:
        return "That word doesn't exist, Please double check it."

word = input("Enter word: ")

print(translate(word))