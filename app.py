from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Render! This is an update again, this is dev'
