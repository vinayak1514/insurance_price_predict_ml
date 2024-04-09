import os 
import sys
import pandas as pd 
from dataclasses import dataclass

from src.InsuracePrediction.utils.utils import save_object,evaluate_model
from src.InsuracePrediction.logger import logging
from src.InsuracePrediction.exception import customexception

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from xgboost import XGBRegressor


# Configuration class for model trainer
@dataclass
class InsuranceModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','insurance_model.pkl')

class InsuranceModelTrainer:
    def __init__(self):
        self.model_trainer_config = InsuranceModelTrainerConfig()


    def initate_model_training(self,train_array,test_array):
        try:
            logging.info('splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            # Dictionary containing different regression models
            models = {
                'Linear Regression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Random Forest': RandomForestRegressor(),
                'XGBoost': XGBRegressor()
            }

            # Evaluating models and obtaining model report
            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)

            # Printing model report
            logging.info(f'Model Report : {model_report}')

            # Printing model report
            logging.info(f'Model Report : {model_report}')

            # Finding the best model based on model report
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]
            best_model = models[best_model_name]

            # Saving the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        except Exception as e:
            raise customexception(e,sys)