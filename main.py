from flask import Flask, request, redirect, render_template
import cgi
#import os
#import jinja2

#template_dir = os.path.join(os.path.dirname(__file__) ,'templates')
#jinja.env = jinja2.Evironment (loader = jinja2.FileSystemLoader(template_dir), autoescape=True

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_user_signup_form():
     return render_template('signup.html')

"""def username():
    if username == '': 
        username_error = 'Username must been 3 or more 20'
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Username is Invaild'
    else:
         if '' in username:
            username_error = 'Username is Invaild'
            username = ''"""

@app.route('/signup', methods=['POST'])
def signup_complete():
    #if request.method == 'POST':
    username = request.form ['username']
    password = request.form ['password']
    verify = request.form ['verify']
    email = request.form ['email']

    # THIS CREATES EMPTY STRINGS FOR THE ERROR MESSAGES

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    #template = jinja_env.get_template('welcome.html')
    # THESE ARE FUNCTIONS FOR THE VALIDATIONS
    
    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error = 'Username must been 3 or more 20'
    

    if len(password) < 3 or len(username) > 20 or " " in password:
        password_error = 'Password is Invaild'
        password = ''

    if password  != verify:
        verify_error = 'Confirm password cannot be empty'
        verify = ''
    
    if len(email) > 1:
        email_error = ''
        email = ''
    
        if len(email) < 3 or len(email) > 20:
            email_error = 'Email is Invaild'
            email = ''
    
    if username_error or password_error or verify_error or email_error:
        return render_template('signup.html', username=username, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
    else:
        return render_template('welcome.html', username=username)

"""@app.route('/welcome', methods=['GET'])
def welcome():
    username = request.args.get('username')
    #template = jinja_env.get_template('welcome.html')
    return render_template("/welcome.html", username=username)"""

#if __name__ == '__main__':
app.run()