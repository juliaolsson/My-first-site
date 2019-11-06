from flask import Flask
app = Flask(__name__)

@app.route('/api/restart')
def restart():
    print ("restart")
    # lägg till kod som startar om filmen
    return 'restart'

@app.route('/api/ON')
def ON():
    print ("ON")
    # lägg till kod som startar filmen
    return "ON"

@app.route('/api/OFF')
def OFF():
    print ("OFF")
    # lägg till kod som avslutar filmen
    return "OFF"


@app.route('/')
def hello_world():
    print ("hello world")
    return app.send_static_file("index.html")

app.run ('172.20.10.3', 8080)