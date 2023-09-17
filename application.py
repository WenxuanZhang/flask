from flask import Flask,render_template
import pandas as pd
import os

application = Flask(__name__)
data_path = os.getcwd()+'/data'
data_file = data_path + '/name.csv'
data = pd.read_csv(data_file)

name = data['name'][1]

@application.route('/')
def hello_world():
	return render_template('index.html',name = name)

