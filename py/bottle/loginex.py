from bottle import run, get, post, request, route, template, error, redirect, debug
from Tkinter import * 
import time
import requests

@get('/login') # or @route('/login')
def login():
    return template('''
        <form action="/login/check" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form> ''')

@route('/')
@post('/login/check') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username=="username" and password=="password":
	root = Tk()
	Label(root, text="Login Success", bg="green", fg="white").pack()
	mainloop()
        time.sleep( 1 )
	values = "python"
	debug(True)

	redirect('https://www.google.com/?')
	req = requests.get('http://localhost:8080/login')
	print req.headers
	print req.text
        return "<p>Your login information was correct.</p>"
    else:
	root = Tk()
	Label(root, text="Login Failed", bg="red", fg="white").pack()
	mainloop()
#	return error
	debug(True)
	return error404(error)
#	redirect("/login")
#        return template('''<p>Login failed.</p> <form action="/login" method="get">
#            Username: <input name="username" type="text" />
#            Password: <input name="password" type="password" />
#            <input value="Login" type="submit" />
#            </form>  ''')

@error(404)
def error404(error):
    root = Tk()
    Label(root, text="Check username or pwd", bg="red", fg="white").pack()
    mainloop()
    redirect('/login')

run(host='localhost', port=8080, reloader=True)
