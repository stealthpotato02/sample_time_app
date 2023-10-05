from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def latest_time():
    time_now=datetime.now()
    current_time=time_now.strftime("%H:%M:%S")
    return current_time


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
