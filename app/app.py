from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask with DevOps Pipeline!"

@app.route('/error')
def error():
    raise Exception("Test Bugsnag Error")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
