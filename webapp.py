from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return "<h1> hello</h1>"
	if __name__=='_main__':
		app.run()
