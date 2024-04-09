from src.InsuracePrediction.pipelines.prediction_pipeline import CustomData,InsurancePremiumPredictor
from flask import Flask, request, render_template

# Creating Flask application instance
app = Flask(__name__)

# Route for home page
@app.route('/')
def home_page():
    return render_template("index.html")

# Route for predicting insurance premium
@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        # Extracting form data
        data = CustomData(
            age=float(request.form.get('age')),
            bmi=float(request.form.get('bmi')),
            children=float(request.form.get('children')),
            sex=request.form.get('sex'),
            smoker=request.form.get('smoker'),
            region=request.form.get('region')
        )
        
        # Converting form data to dataframe
        final_data = data.get_data_as_dataframe()
        
        # Predicting insurance premium
        predictor = InsurancePremiumPredictor()
        pred = predictor.predict(final_data)
        result = round(pred[0], 2)
        
        # Displaying prediction result
        return render_template("result.html", final_result=result)

if __name__ == '__main__':
    # Running Flask app
    app.run(host="0.0.0.0",  port=8080)