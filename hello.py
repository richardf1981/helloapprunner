from flask import Flask
import json
import requests

app = Flask(__name__)

def my_reg():
    try:
        result = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document')
        if result.status_code == 200:
            my_obj = json.loads(result.content)
            if my_obj and my_obj.get("region"):
                return "<br><br> I'm at " + my_obj.get("region")
    except:
        return ''
    

@app.route('/')
def index():
    return 'Hello AWS App Runner' + my_reg()

if __name__ == "__main__":
    print("hello!!!")
    app.run(host='0.0.0.0', port=80)
