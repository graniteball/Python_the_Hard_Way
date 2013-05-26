import web

urls = (
	'/hello','Index','/','Index','/testing','Index'
)

# app is an object to instantiate the web server
app = web.application(urls, globals())

# render is a web.template.render object
# it knows how to get templates from the 'templates/' directory
render = web.template.render('templates/')

# Create the Index class that is used for the root URL
class Index(object):
	# Define what to do when there is a HTTP Get
	def GET(self):
		form = web.input(name="Nobody", greet=None)
		if form.greet:
			greeting = "Hello, %s %s" % (form.name, form.greet)
			return render.index(greeting = greeting)
		else:
			return "ERROR: greet is required."
		
if __name__ == "__main__":
	app.run()