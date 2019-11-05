from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print ("hello world")
    return 'Hello, World!'

app.run ('localhost', 8080)