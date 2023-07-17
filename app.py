from flask import Flask
from datetime import datetime

app = Flask(__name__)

start_time = datetime.now()  # gets the current time when the application starts

@app.route('/')
def hello_world():
    return f'Hello Render! This app was started at {start_time}.'