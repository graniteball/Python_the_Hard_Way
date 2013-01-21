# scan function
def scan(input_string):
	input_words = input_string.split()
	lexicon_list = []
	for token in input_words:
		# check to see if the token is a direction
		if token.lower() in direction_lexicon:
			token_type = ('direction', token)
		# check to see if the token is a verb
		elif token.lower() in verb_lexicon:
			token_type = ('verb', token)
		# check to see if the token is a stop
		elif token.lower() in stop_lexicon:
			token_type = ('stop', token)
		# check to see if the token is a noun
		elif token.lower() in noun_lexicon:
			token_type = ('noun', token)
		else:
		# at this point, it has to either be a number of an error
			try:
				token_type = ('number', int(token))
			except ValueError:
				token_type = ('error', token)
							
		# add the new token definition to the list
		lexicon_list.append(token_type)
	return(lexicon_list)

direction_lexicon = ('north', 'east', 'south', 'west')
verb_lexicon = ('go', 'kill', 'eat', 'mame')
stop_lexicon = ('the', 'in', 'of')
noun_lexicon = ('bear', 'princess')
