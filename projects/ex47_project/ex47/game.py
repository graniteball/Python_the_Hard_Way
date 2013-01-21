class Room(object):
	
	# Init function to set name and descriptions to passed in value and initialize the path dict
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	# Function to look up the direction in the paths dict
	def go(self, direction):
		return self.paths.get(direction, None)
		
	# Function to add the passed in path to the paths dict
	def add_paths(self, paths):
		self.paths.update(paths)