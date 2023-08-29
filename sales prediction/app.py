import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
import pickle

app = Flask(__name__) #Initialize the flask App



dtrs = pickle.load(open('C:/Users/user/PycharmProjects/sales prediction/model/dtrs.pkl','rb'))
@app.route('/')

@app.route('/index')
def index():
	return render_template('index1.html')

#@app.route('/future')
#def future():
#	return render_template('future.html')    

@app.route('/login')
def login():


	return render_template('login1.html')
@app.route('/upload',methods=["POST"])
def upload():
	if request.method == 'POST':
		login_name = request.form.get("text1")
		login_pass = request.form.get("pass")
		print(login_pass, login_name)
		if login_name == "ahmed@123" and login_pass == "ahmed123":
			return render_template('upload1.html')
		if login_name == "junaid@123" and login_pass == "junaid123":
			return render_template('upload1.html')
@app.route('/upload1',methods=["POST"])
def upload1():
	if request.method == 'POST':
		login_name = request.form.get("text1")
		login_pass = request.form.get("pass")
		print(login_pass, login_name)
		if login_name == "ahmed@123" and login_pass == "ahmed123":
			return render_template('upload1.html')
		if login_name == "junaid@123" and login_pass == "junaid123":
			return render_template('upload1.html')

@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)

@app.route('/result')
def result():
    return render_template('result1.html')
    
@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [x for x in request.form.values()]
	print(int_feature)
	int_feature = [float(i) for i in int_feature]
	final_features = [np.array(int_feature)]
	prediction = dtrs.predict(final_features)
	output =format(float(prediction[0]))
	print(output)
	result =float(output) * float(output) * float(output)
	return render_template('result1.html', prediction_text= int(result))

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')


if __name__ == "__main__":
    app.run(debug=True)
