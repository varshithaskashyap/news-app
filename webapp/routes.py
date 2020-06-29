from flask import render_template, request
from flask import Flask
from webapp import app



@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.errorhandler(404)
def not_found(error):
    return "<h1>PAGE NOT FOUND</h1>"

if __name__ == "__main__":
    app.run(debug=True)
