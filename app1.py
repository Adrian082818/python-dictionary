import json #importing libraries
from difflib import get_close_matches

data = json.load(open("data/data.json")) #loading data in python into a python datatype

def translate(w):
    w = w.lower()
    if w in data:        
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else: 
            return "We didn't understand your entry."
    else:
        return "That word doesn't exist, Please double check it."

word = input("Enter word: ") #user input 

print(translate(word))