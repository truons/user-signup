from flask import Flask, request, redirect
import cgi




app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)
