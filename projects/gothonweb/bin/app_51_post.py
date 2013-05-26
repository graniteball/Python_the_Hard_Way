import web

urls = (
	'/hello','Index','/','Index','/testing','Index'
)

# app is an object to instantiate the web server
app = web.application(urls, globals())

# render is a web.template.render object
# it knows how to get templates from the 'templates/' directory
render = web.template.render('templates/', base="layout")

# Create the Index class that is used for the root URL
class Index(object):
	# Define what to do when there is a HTTP Get
	def GET(self):
		return render.hello_form()
	
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s " % (form.greet, form.name)
		return render.index(greeting = greeting)
		
if __name__ == "__main__":
	app.run()