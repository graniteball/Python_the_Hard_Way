import random # import lib to generate random numbers
from urllib import urlopen # import lib to open a URL and get resulting text
import sys #this is so that we can use argv to get passed in arguments

WORD_URL = "http://learncodethehardway.org/words.txt" # set a constant to Zed's URL
WORDS = [] # initialize words list

PHRASES = { # this is a dictionary of questions and answers
    "class ###(###):":
      "Make a class named ### that is-a ###.",
    "class ###(object):\n\tdef __init__(self, ***)" :
      "class ### has-a __init__ that takes self and *** parameters.",
    "class ###(object):\n\tdef ***(self, @@@)":
      "class ### has-a function named *** that takes self and @@@ parameters.",
    "*** = ###()":
      "Set *** to an instance of class ###.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first?
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website	
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip()) # this gives a nice list of works with the '/n' stripped off
	
def convert(snippet, phrase): # i.e., key, value
	# analysis of next line
		# count the nunber of times that "###" appears in the snippet
		# randomly grab that number of words from the list of words and return as a list
		# loop through the list and capitalize each word
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("###"))]
	# analysis of next line
		# count the nunber of times that "***" appears in the snippet
		# randomly grab that number of words from the list of words and return as a list
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0,snippet.count("@@@")): # for every time "@@@" appears in the snippet...
		param_count = random.randint(1,3) # generate a random param count of 1, 2, or 3 
		param_names.append(', '.join(random.sample(WORDS, param_count))) # make a random list of 1, 2, or 3 param names
		
	for sentence in snippet, phrase:
#		result = sentence[:]
		result = sentence
		
		# fake class names
		for word in class_names:
			result = result.replace("###", word, 1)
			
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
	return results
	
#keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys() # make a list just the keys from the Q&A database
		random.shuffle(snippets) # shuffle the list of keys in to a random order

		for snippet in snippets: # go through the list of questions
			phrase = PHRASES[snippet] # snippet is the key that gets the value phrase from the ditionary PHRASES
			# snippet is the key, phrase if the value
			question, answer = convert(snippet, phrase) 
			if PHRASE_FIRST:
				question, answer = answer, question # cool, you can flip then all in one line
			
			print question
		
			raw_input("> ")
			print "ANSWER:  %s\n" % answer
		
except EOFError:
	print "\nBye"
			