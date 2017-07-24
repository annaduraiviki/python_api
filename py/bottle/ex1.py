from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/hello/home/redirect/')
def home2():
    return template('/hello/home2')

@route('/hello/home2')
def index2():
    return template('<b>In home 2 </b>!')

@route('/')
@route('/hello/home/<name>')
def home(name="viki"):
    return template('<b>this is  {{name}}</b>!', name=name)

run(host='localhost', port=8080)


