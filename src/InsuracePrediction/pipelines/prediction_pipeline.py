import os
import sys
import pandas as pd

from src.InsuracePrediction.exception import customexception
from src.InsuracePrediction.logger import logging
from src.InsuracePrediction.utils.utils import load_object


class InsurancePremiumPredictor:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            # Define paths for preprocessor and model files
            preprocessor_path = os.path.join("artifacts", "preprocesser.pkl")
            model_path = os.path.join("artifacts","insurance_model.pkl")
            
            # Load preprocessor and model objects
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)
            
            # Log column names before transformation
            logging.info("Column names before transformation: %s", features.columns)
            
            # Transform features using preprocessor
            scaled_data = preprocessor.transform(features)
            
            # Make predictions using the model
            pred = model.predict(scaled_data)
            
            return pred
            
        except Exception as e:
            # Raise custom exception if an error occurs
            raise customexception(e, sys)
    
    
class CustomData:
    def __init__(self, age: float, bmi: float, children: float, sex: str, smoker: str, region: str):
        # Initialize data attributes
        self.age = age
        self.bmi = bmi
        self.children = children
        self.sex = sex
        self.smoker = smoker
        self.region = region
                
    def get_data_as_dataframe(self):
        try:
            # Create a dictionary with custom data
            custom_data_input_dict = {
                'age': [self.age],
                'bmi': [self.bmi],
                'children': [self.children],
                'sex': [self.sex],
                'smoker': [self.smoker],
                'region': [self.region]
            }
            # Create a DataFrame from the dictionary
            df = pd.DataFrame(custom_data_input_dict)
            
            # Log that DataFrame is gathered
            logging.info('Dataframe Gathered')
            
            return df
        except Exception as e:
            # Log an exception if an error occurs
            logging.info('Exception Occurred in prediction pipeline')
            raise customexception(e, sys)