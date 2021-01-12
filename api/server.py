from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from algo import  algo1


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/test', methods=['GET'])
def home():
    return "this is our first appi "

@app.route('/algo1', methods=['POST' , 'GET'])
def algo1Handler():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save(secure_filename(f.filename))
        algo1(f.filename)
        return 'file uploaded successfully'


@app.route('/algo2',methods=['POST','GET'])
def algo2():
    return 'this endpoint will handle the first algo2 '


@app.route('/algo3',methods=['POST','GET'])
def algo3():
    return 'this endpoint will handle the first algo3 '
app.run()