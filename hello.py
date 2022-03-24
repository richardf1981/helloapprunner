from flask import Flask
import json
import requests

app = Flask(__name__)

def my_reg():
    try:
        result = requests.get('http://169.254.169.254/latest/meta-data/placement/availability-zone')
        if result.status_code == 200:
            return "<br><br> I'm in " + result.content
    except:
        return ''
    

@app.route('/')
def index():
    'a
    return 'Hello AWS App Runner - version 1' + my_reg()

if __name__ == "__main__":
    print("hello!!!")
    app.run(host='0.0.0.0', port=80)
