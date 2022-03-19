from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print("hello!!!")
    return 'Hello AWS App Runner'

app.run(host='0.0.0.0', port=80)
