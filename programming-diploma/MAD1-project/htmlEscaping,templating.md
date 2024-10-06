# Learning HTMLescaping and dealing with untrusted data from the user

from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

- In this example we can see user is giving some data in the url itself which means that this data in unsafe
- like the user can even pass script tag in the url to make use of the script tag so that he can manipulate the actions of the website in his browser
- therefore escape method is used
- and the <name> is stored as variable which takes the value that is passed by the user after the / in the url 

# Using variables in return statement

- we can even convert the variables in the url into certain data type before using it, more about these converters in the docs of the flask framework 

# Jinja2 Template engine

-
