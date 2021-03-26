import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" #Set url to WORD_URL
WORDS = [] #Set WORDS to an empty list

PHRASES = { #Dictionary full of phrases (Key: Values)
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english": #If the length of argument variables = 2 and the first argument is English
    PHRASE_FIRST = True #Thus Phrase_First becomes True
else: #Else False
    PHRASE_FIRST = False #Thus Phrase_First becomes False

# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #For every word in WORD_URL reach each line 
    WORDS.append(word.strip().decode("utf-8")) #Append the stripped word to Words

def convert(snippet, phrase): #questions, answer is snippet key and phrase value
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))] #Capitalize the words that have been Shuffle WORDS and return a list of WORDS depending on the amount of snippets with %%%
    other_names = random.sample(WORDS, snippet.count("***"))  #Shuffle WORDS list with the amount of *** in snippet
    results = [] # Empty lists
    param_names = [] # Empty lists

    for i in range(0, snippet.count("@@@")): # For i in the rane within the 0 and amount of snippets with @@@
        param_count = random.randint(1,3) # The param_count is picking a  random integer between 1 and 3
        param_names.append(', '.join(random.sample(WORDS, param_count))) # Pick random words depending on the amount of param_count and join them with a comma
    
    for sentence in snippet, phrase: #For both sentence in snippet and phrase
        result = sentence[:] #Result becomes the combination of both snippet and phrase combined
        

        # fake class names
        for word in class_names: #For each in class_names
            result = result.replace("%%%", word, 1) # Replace %%% with word when it encounters the first %%%

        # fake other names
        for word in other_names: # Replace *** with word when it encounters the first ***
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names: #Replace @@@ with word when it encounters the first @@@
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try: #Try to run this code
    while True: #Infinite Loop till False
        snippets = list(PHRASES.keys()) #Set snippets to a list of keys in the PHRASES dictionary 
        random.shuffle(snippets) #Randomly shuffle the snippets (List of keys in the phrases)

        for snippet in snippets: #For each key in snippets do this
            phrase = PHRASES[snippet] #For each key (snippet), set phrase to the value
            question, answer = convert(snippet, phrase) #Set results of snippet and phrase in convert function
            if PHRASE_FIRST: 
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER:  %s\n\n" % answer)
except EOFError:
    print("\nBye")