from flask import Flask , flash, request, redirect, url_for,send_file, send_from_directory, safe_join, abort

from flask_cors import CORS, cross_origin

from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from arima import arima

app = Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)



@app.route('/test', methods=['GET'])
def home():
    return "this is our first appi "

@cross_origin()
@app.route('/algo1', methods=['POST' , 'GET'])
def algo1Handler():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save(secure_filename(f.filename))
        arima(f.filename)

        return send_file("sent.xlsx",as_attachment=True)


@cross_origin()
@app.route('/algo2',methods=['POST','GET'])
def algo2Handler():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save(secure_filename(f.filename))
        arima(f.filename)

        return send_file("sent.xlsx", as_attachment=True)


@cross_origin()
@app.route('/algo3',methods=['POST','GET'])
def algo3Handler():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save(secure_filename(f.filename))
        arima(f.filename)

        return send_file("sent.xlsx", as_attachment=True)


app.run()