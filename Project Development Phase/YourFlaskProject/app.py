import numpy as np
import pandas as pd
from flask import Flask,request,jsonify,render_template
import pickle
#flaskapp
app=Flask(__name__)
#loading the saved model
m=pickle.load(open('fbcrypto.pkl','rb'))
#Routing html pages
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/Bitcoin',methods=['POST','GET'])
def prediction():
    return render_template('predict.html')

future=m.make_future_dataframe(periods=365)
forecast=m.predict(future)
print(forecast)

@app.route('/predict',methods=['POST'])
def y_predict():
    if request.method=="POST":
        ds=request.form["Date"]
        print(ds)
        next_day=ds
        print(next_day)
        prediction=forecast[forecast['ds']==next_day]['yhat'].item()
        prediction=round(prediction,2)
        print(prediction)
        return render_template('predict.html',prediction_text="Bitcpin Price on selected date is $ {} Cents".format(prediction))
    return render_template("predict.html")

if __name__=="__main__":
    app.run(debug=False)