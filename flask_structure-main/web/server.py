from flask import Flask,render_template



app = Flask(__name__)


@app.route('/',methods=[ "GET",'POST'])
def index():



    return render_template('index.html')







@app.route('/FandQ',methods=[ "GET",'POST'])
def dashboard():
    print('FandQ')

    return render_template('FandQ.html')    




if __name__ == "__main__":
    app.run(debug=True,threaded=True,port=5566)    