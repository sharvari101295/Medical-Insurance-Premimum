
from flask import Flask,jsonify,request,render_template
from project_app.utils import MedicalInsurance

import config

app = Flask(__name__)


@app.route("/")  
def hello_flask():
    return " Welcome to Medical Insurance Premium Prediction Project "
    
@app.route('/test')
def student():

    return render_template("index.html")
        
        
@app.route('/result', methods = ['POST', 'GET'])

def get_insurance_charges():

    if request.method == 'POST':

        result = request.form

        age  = result['age']
        sex  = result['sex']
        bmi  = result['bmi']
        children = result['children']
        smoker = result['smoker']
        region = result['region']

        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_ins.get_predict_charges()

        return render_template("result.html", charges = charges)
    

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)  # server start
