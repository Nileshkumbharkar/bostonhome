from flask import Flask,render_template,request
from utils import Boston

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('user.html')

@app.route('/predict_charges',methods = ['post'])
def open():
    CRIM  = float(request.form.get('CRIM'))
    ZN         =float(request.form.get('ZN')) 
    INDUS    =    float(request.form.get('INDUS'))
    CHAS       = float(request.form.get('CHAS'))
    NOX        = float(request.form.get('NOX'))
    RM          =float(request.form.get('RM'))
    AGE         =float(request.form.get('AGE'))
    DIS        =  float(request.form.get('DIS'))
    RAD        =  float(request.form.get('RAD'))
    TAX       = float(request.form.get('TAX'))
    PTRATIO   = float(request.form.get('PTRATIO'))
    B          =float(request.form.get('B'))
    LSTAT      = float(request.form.get('LSTAT'))
    s = Boston(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT)
    n=s.predict()
    return '''<html>
    <head></head>
    <center>
    <body style="background-color:rgb(176, 230, 222);">
    <p style="font-size:50px ; ">
    
        <label>result : %(n)s </label>
        <br>            
    </body>
    </center>
</html>
''' % locals()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)