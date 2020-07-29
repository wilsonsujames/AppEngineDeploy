from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/write')
def writefile():
    with open('/tmp/123.txt', 'w') as f:
        f.write("hello")

    return 'write success!'

@app.route('/read')
def readfile():
    with open('/tmp/123.txt', 'w') as f:
        contents =f.read()
    return contents




if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)    