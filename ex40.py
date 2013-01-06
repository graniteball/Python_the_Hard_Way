class Song(object):
	
	def __init__(self,lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
		
happy_bday = Song(["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stip right there"])
	
bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells"])
	
bjw_lyrics = ["There's a fog upon LA",
		"and my friends have lost their way",
		"they'll be over soon they said",
		"now they've lost themselves instead."]

blue_jay_way = Song(bjw_lyrics)	
	
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

blue_jay_way.sing_me_a_song()

