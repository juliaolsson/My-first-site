import subprocess
from flask import Flask
from omxplayer.player import OMXPlayer
from pathlib import Path

app = Flask(__name__)


class omxPlayer:
    player = None

    def __init__(self):
        path = Path('../julia4.mp4')
        self.player = OMXPlayer(path)

omx = omxPlayer()


@app.route('/api/restart')
def restart():
    print ("restart")
    path = Path('../movie.mp4')
    omx.player.load(path)
    return 'restart'

@app.route('/api/ON')
def ON():
    print ("ON")
    path = Path('../julia4.mp4')
    omx.player = OMXPlayer(path)
    return "ON"

@app.route('/api/OFF')
def OFF():
    print ("OFF")
    omx.player.stop()
    return "OFF"


@app.route('/')
def index():
    print ("hello world. Loading index.html")
    return app.send_static_file("index.html")


app.run ('172.20.10.8', 8081)
