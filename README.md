# Insurance Premium Prediction

## Deployed Project
The project has been successfully deployed on AWS using a Docker image. 

## Overview
Insurance Premium Prediction is a comprehensive project designed to forecast insurance premiums by leveraging machine learning algorithms. It takes into account various factors such as age, BMI, number of children, gender, smoking status, and region to provide accurate predictions. This project utilizes historical data analysis and machine learning techniques to offer insights into future insurance premium trends.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yashdahekar/Insurance_Premium_Prediction
    cd Insurance_Premium_Prediction
    ```

2. **Set up the environment:**
    ```bash
    ./init_setup.sh
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```bash
    python application.py
    ```

5. **Access the application:**
    Open a web browser and go to `http://localhost:8080` to use the application.

## Technology Used
- **Python**: Core programming language
- **Flask**: Web application framework
- **pandas**: Data manipulation library
- **NumPy**: Numerical computing library
- **matplotlib**: Data visualization library
- **seaborn**: Data visualization library
- **scikit-learn**: Machine learning library
- **XGBoost**: Gradient boosting library

## Requirements
- Flask
- ipykernel
- scikit-learn
- matplotlib
- seaborn
- pandas 
- numpy
- xgboost

## Algorithms Used
The project employs various machine learning algorithms for insurance premium prediction:
- Linear Regression
- Lasso Regression
- Ridge Regression
- ElasticNet Regression
- Gradient Boosting Regressor
- Random Forest Regressor
- XGBoost Regressor

## Project Structure

- `Insurance_Premium_Prediction`: Main package containing project code.
  - `exception.py`: Defines custom exception classes.
  - `logger.py`: Configures logging for the project.
  - `components`: Package containing pipeline modules.
    - `data_ingestion.py`: Reads and preprocesses raw data.
    - `data_transformation.py`: Transforms data for modeling.
    - `model_trainer.py`: Trains machine learning models.
  - `pipelines`: Package containing pipeline modules.
    - `prediction_pipeline.py`: Makes predictions using trained models. 
    - `training_pipeline.py`: Trains machine learning models.. 
  - `utils`: Package containing utility functions.
    - `utils.py`: Contains utility functions for saving objects and evaluating models.
  - `artifacts`: Directory for storing trained models and processed data.
  - `notebooks`: Directory containing Jupyter notebooks for data exploration.
  - `templates`: Directory containing HTML templates for Flask application.
  - `static`: Directory containing static files (e.g., CSS, JavaScript) for Flask application.
  - `application.py`: Flask application for serving the prediction model.
  - `requirements.txt`: File containing project dependencies.
  - `setup.py`: File for packaging the project.
  - `init_setup.sh`: Shell script for initializing the environment.


## Next Steps
1. Explore the Jupyter notebooks in the `notebooks` directory for data exploration and analysis.
2. Train machine learning models using the provided scripts in the `pipelines` directory.
3. Serve the prediction model using the Flask application in `application.py`.
4. Utilize the web interface to make predictions on new data.

## Author
This project was created by vinayak. For any inquiries or feedback, please contact [jangirvinayak0001@gmail.com](mailto:jangirvinayak0001@gmail.com).