from flask import Flask,render_template
import os


template_dir = os.path.abspath('./public')


app = Flask(__name__,template_folder=template_dir)


@app.route('/',methods=[ "GET",'POST'])
def index():



    return render_template('index.html')







@app.route('/FandQ',methods=[ "GET",'POST'])
def FandQ():
    print('FandQ')

    return render_template('FandQ.html')    




if __name__ == "__main__":
    app.run(debug=True,threaded=True,port=5566)    