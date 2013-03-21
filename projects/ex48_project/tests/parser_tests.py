from nose.tools import *
from ex48 import parser
from ex48 import lexicon

def basic_peek_test():
	input_sentence = "Kill the bear"
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('verb', 'Kill'),
									('stop', 'the'),
									('noun', 'bear')])	
	assert_equal(parser.peek(scanned_sentence), 'verb')
	
def basic_match_test():	
	input_sentence = "Kill the bear"
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('verb', 'Kill'),
									('stop', 'the'),
									('noun', 'bear')])
	assert_equal(parser.match(scanned_sentence,'verb'),('verb', 'Kill'))
	assert_equal(parser.match(scanned_sentence,'stop'),('stop', 'the'))
	assert_equal(parser.match(scanned_sentence,'noun'),('noun', 'bear'))
	assert_equal(scanned_sentence, [])
	
def basic_skip_test():
	input_sentence = "Go north east south west"
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('verb', 'Go'),
									('direction', 'north'),
									('direction', 'east'),
									('direction', 'south'),
									('direction', 'west')])
	parser.skip(scanned_sentence, 'direction')
	assert_equal(scanned_sentence, [('verb', 'Go'),
									('direction', 'north'),
									('direction', 'east'),
									('direction', 'south'),
									('direction', 'west')])
	parser.skip(scanned_sentence, 'verb')
	assert_equal(scanned_sentence, [('direction', 'north'),
									('direction', 'east'),
									('direction', 'south'),
									('direction', 'west')])
	parser.skip(scanned_sentence, 'direction')
	assert_equal(scanned_sentence, [])
	
def basic_verb_test():
	input_sentence = "The in mame"
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('stop', 'The'),
									('stop', 'in'),
									('verb', 'mame')])
	assert_equal(parser.parse_verb(scanned_sentence), ('verb', 'mame'))
	input_sentence = "The in bear"
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('stop', 'The'),
									('stop', 'in'),
									('noun', 'bear')])
	#assert_equal(parser.parse_verb(scanned_sentence), ('verb', 'mame'))

def basic_object_test():
	
	input_sentence = "The in of bear"
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('stop', 'The'),
									('stop', 'in'),
									('stop', 'of'),
									('noun', 'bear')])
	assert_equal(parser.parse_object(scanned_sentence), ('noun', 'bear'))

	input_sentence = "The in of west"
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('stop', 'The'),
									('stop', 'in'),
									('stop', 'of'),
									('direction', 'west')])
	assert_equal(parser.parse_object(scanned_sentence), ('direction', 'west'))

def subject_test():
	class Test_Sentence(parser.Sentence):
		pass
	
	input_sentence = "In eat bear"
	test_subject = ('noun', 'Alan')
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('stop', 'In'),
									('verb', 'eat'),
									('noun', 'bear')])
	expected_sentence = Test_Sentence(test_subject, ('verb', 'eat'), ('noun', 'bear'))
	parsed_sentence = parser.parse_subject(scanned_sentence, test_subject)
	assert_equal(parsed_sentence.subject, expected_sentence.subject)
		
def sentence_test_subject():
	class Test_Sentence(parser.Sentence):
		pass
	
	# Start with a noun that is assumed to the be the subject
	
	input_sentence = "In Alan eat the bear"	
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('stop', 'In'),
									('noun', 'Alan'),
									('verb', 'eat'),
									('stop', 'the'),									
									('noun', 'bear')])
	expected_sentence = Test_Sentence(('noun', 'Alan'), ('verb', 'eat'), ('noun', 'bear'))
	parsed_sentence = parser.parse_sentence(scanned_sentence)
	assert_equal(parsed_sentence.subject, expected_sentence.subject)
	assert_equal(parsed_sentence.object, expected_sentence.object)
	assert_equal(parsed_sentence.verb, expected_sentence.verb)		

def sentence_test_no_subject():
	class Test_Sentence(parser.Sentence):
		pass
		
	# Start with a verb that so that the player is assumed to be the subject

	input_sentence = "In eat the bear"	
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('stop', 'In'),
									('verb', 'eat'),
									('stop', 'the'),									
									('noun', 'bear')])
	expected_sentence = Test_Sentence(('noun', 'player'), ('verb', 'eat'), ('noun', 'bear'))
	parsed_sentence = parser.parse_sentence(scanned_sentence)
	assert_equal(parsed_sentence.subject, expected_sentence.subject)
	assert_equal(parsed_sentence.object, expected_sentence.object)
	assert_equal(parsed_sentence.verb, expected_sentence.verb)		

def complete_sentence_test():
	class Test_Sentence(parser.Sentence):
		pass

	input_sentence = "Dance with the bear"	
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('verb', 'Dance'),
									('stop', 'with'),									
									('stop', 'the'),									
									('noun', 'bear')])
	expected_sentence = Test_Sentence(('noun', 'player'), ('verb', 'Dance'), ('noun', 'bear'))
	parsed_sentence = parser.parse_sentence(scanned_sentence)
	assert_equal(parsed_sentence.subject, expected_sentence.subject)
	assert_equal(parsed_sentence.object, expected_sentence.object)
	assert_equal(parsed_sentence.verb, expected_sentence.verb)		

def make_errors_test():
	class Test_Sentence(parser.Sentence):
		pass

	input_sentence = "Dance with the purple bear"	
	scanned_sentence = lexicon.scan(input_sentence)
	assert_equal(scanned_sentence, [('verb', 'Dance'),
									('stop', 'with'),									
									('stop', 'the'),
									('error', 'purple'),																		
									('noun', 'bear')])
	expected_sentence = Test_Sentence(('noun', 'player'), ('verb', 'Dance'), ('noun', 'bear'))
	
	# The next call should fail because it will be expecting a noun and insteal will see 'purple'
	
	assert_raises(1, parser.parse_sentence, scanned_sentence)
#	assert_equal(parsed_sentence.subject, expected_sentence.subject)
#	assert_equal(parsed_sentence.object, expected_sentence.object)
#	assert_equal(parsed_sentence.verb, expected_sentence.verb)		
