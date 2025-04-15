from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Air Quality Web</h1><p>Application is running!</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
