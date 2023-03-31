from flask import Flask, request, render_template

from prediction_value.predValue import Prediction
from flask import Response

application = Flask(__name__)
app = application

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predictPrice():
    try:
        if request.form is not None:
            form_data = request.form
            loadvalObj= Prediction(form_data)
            y_pred = loadvalObj.predictValue()

            return render_template('prediction.html',value=y_pred)
    
    except Exception as e:
        return Response("Error occured %s" %e)




if __name__ == '__main__':
    # app.run(host='127.0.0.1',port=8080,debug=True)   # for local run
    app.run(host='0.0.0.0',port=8080)  # for deployment run