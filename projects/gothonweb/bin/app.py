import web

# This tells the program to look for the class 'Index' to see what to display for 
# the root of the web page
urls = (
	'/(.*)','Index'
)

# app is an object to instantiate the web server
app = web.application(urls, globals())

# render is a web.template.render object
# it knows how to get templates from the 'templates/' directory
render = web.template.render('templates/')

# Create the Index class that is used for the root URL
class Index(object):
	# Define what to do when there is a HTTP Get
	def GET(self, greeting):
		# Use my render object to render the greeting for the root of the web page
		# Everytning after the '/' is the greeting
		print 'Greeting is %r' % greeting
		return render.index(greeting)
		
if __name__ == "__main__":
	app.run()