from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello AWS App Runner'

if __name__ == "__main__":
    print("hello!!!")
    app.run(host='0.0.0.0', port=80)
