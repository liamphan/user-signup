from flask import Flask, request, redirect, render_template, url_for
import cgi
import os
# Import regular expressions module
import re

app = Flask(__name__)
app.config['DEBUG'] = True

# Validation functions for required fields.
# How can I collapse these functions into one?

# def val_username(username):
#     username, username_error = username, ""

#     if username == "":
#         username_error = "Please enter a valid username."
#     elif len(username) < 3 or len(username) > 20:
#         username_error = "Username must be between 3 and 20 characters long."
#         username = ""
#     elif " " in username:
#         username_error = "Your username cannot contain any spaces."
#         username = ""
#     return username, username_error

# def val_password(password):
#     password, password_error = password, ""

#     if password == "":
#         password_error = "Please enter a valid password."
#     elif len(password) < 3 or len(password) > 20:
#         password_error = "Password must be between 3 and 20 characters long."
#     elif " " in password:
#         password_error = "Your password cannot contain any spaces."
#     return password, password_error

# def val_verify(verify):
#     verify, verify_error = verify, ""

#     password = request.form['password']
#     if password != "":
#         if verify == "" or verify != password:
#             verify_error = "Passwords do not match. Please try again."
#             verify = ""
#     return verify, verify_error

# def val_email(email):
#     email, email_error = email, ""

#     if email != "":
#         if len(email) < 3 or len(email) > 20:
#             email_error = "Email must be between 3 and 20 characters long."
#             email = ""
#         elif " " in email:
#             email_error = "Your email cannot contain any spaces."
#             email = ""
#         elif email.count("@") != 1 or email.count(".") != 1:
#             email_error = "Not a valid email address."
#     return email, email_error

# Initial application route
@app.route("/")
def index():
    return render_template('index.html', title = "Sign Up")

# Signup validation requirements
@app.route("/signup", methods=['POST'])
def signup():

    # username, username_error = val_username(request.form["username"])
    # password, password_error = val_password(request.form["password"])
    # verify, verify_error = val_verify(request.form["verify"])
    # email, email_error = val_email(request.form["email"])

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    # Collapsed above functions into one sign up function.

    # Validate Username
    if username == "":
        username_error = "Please enter a valid username."
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters long."
        username = ""
    elif " " in username:
        username_error = "Your username cannot contain any spaces."
        username = ""

    # Validate Password
    if password == "":
        password_error = "Please enter a valid password."
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters long."
    elif " " in password:
        password_error = "Your password cannot contain any spaces."

    # Verify Passwords
    if verify == "" or verify != password:
        verify_error = "Passwords do not match. Please try again."
        verify = ""

    # Validate Email
    if email != "":
        # Used regex for further validating email.
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                email_error = "Not a valid email address."

        # if len(email) < 3 or len(email) > 20:
        #     email_error = "Email must be between 3 and 20 characters long."
        #     email = ""
        # elif " " in email:
        #     email_error = "Your email cannot contain any spaces."
        #     email = ""
        # elif email.count("@") != 1 or email.count(".") != 1:
        #     email_error = "Not a valid email address."

    # Welcome and success confirmation page!
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template(
            'index.html',
            username = username,
            username_error = username_error,
            password_error = password_error,
            verify_error = verify_error,
            email = email,
            email_error = email_error
            )

app.run()
