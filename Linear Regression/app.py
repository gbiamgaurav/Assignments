
# importing the necessary dependencies
from distutils.log import debug
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)  # initializing a flask app

@app.route('/', methods=['GET']) # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()

def index():
    if request.method == 'POST':
        try:

            # reading the inputs given by the user
            CRIM = float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            INDUS = float(request.form['INDUS'])
            CHAS = float(request.form['CHAS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            AGE = float(request.form['AGE'])
            DIS = float(request.form['DIS'])
            RAD = float(request.form['RAD'])
            TAX = float(request.form['TAX'])
            PTRATIO = float(request.form['PTRATIO'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])
           
            data = {'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': NOX,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT}


            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))

            # Predictions using the loaded model file

            prediction = loaded_model.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
            print('Prediction is', prediction)

            return render_template('results.html', prediction)
        except Exception as e:
            print("The Exception message is: ",e)
            return 'something is wrong'

    else:
        return render_template('index.html') 


if __name__ == "__main__":

    #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app       







     