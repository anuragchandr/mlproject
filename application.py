import pickle

from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import PredictPipeline, CustomData


application = Flask(__name__)

app = application
@app.route('/', )
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # 1. Get the data from the form
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=int(request.form.get('reading_score')),
                writing_score=int(request.form.get('writing_score'))
            )
            # 2. Convert the data to a DataFrame
            data_df = data.get_data_as_dataframe()
            # 3. Create an instance of the PredictPipeline and make a prediction
            predict_pipeline = PredictPipeline()    
            result = predict_pipeline.predict(data_df)
            # 4. Render the result on the home page
            return render_template('home.html', results=result[0])
        

        except Exception as e:
            print(e)
            return "An error occurred during prediction."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)