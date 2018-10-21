from flask import Flask, request, redirect, render_template
import cgi
import os
#import jinja2

#template_dir = os.path.join(os.path.dirname(__file__) ,'templates')
#jinja.env = jinja2.Evironment (loader = jinja2.FileSystemLoader(template_dir), autoescape=True

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_user_signup_form():
    return render_template('Homepage.html')

def username():
    if username == '': 
        username_error = 'Username must been 3 or more 20'
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Username is Invaild'
    else:
        if '' in username:
            username_error = 'Username is Invaild'
            username = ''  

@app.route("/", methods=['POST'])
def signup_complete():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # THIS CREATES EMPTY STRINGS FOR THE ERROR MESSAGES

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    #template = jinja_env.get_tempplate('welcome.html')
    # THESE ARE FUNCTIONS FOR THE VALIDATIONS
    
    if username == '':
        username_error = 'Username must been 3 or more 20'
        username = ''
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Username is Invaild'
        username = ''
    else:
        if '' in username:
            username_error = 'Username is Invaild'
            username = ''
     
    if password == '':
        password_error = 'Password must match'
        password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Password is Invaild'
        password = ''
    else:
        if '' in password:
            password_error = 'Password is Invaild'
            password = ''

    if password  != verify:
        verify_error = 'Confirm password cannot be empty'
        verify = ''
    
    if len(email) == 0:
        email_error = ''
        email = ''
    elif len(email) < 3 or len(email) > 20:
        email_error = 'Email is Invaild'
        email = ''
    
    if not username_error and not password_error and not verify_error and not email_error:
        return 'Welcome' + username 
    else:
        return render_template('Homepage.html',username=username, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route('/index.html' , methods=['GET'])
def welcome():
    username = request.args.get('username')
    #template = jinja_env.get_template('welcome.html')
    return render_template(username=username)

#if __name__ == '__main__':
app.run()