import os
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.InsuracePrediction.exception import customexception
from src.InsuracePrediction.logger import logging


from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from src.InsuracePrediction.utils.utils import save_object
@dataclass
class DataTransformconfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocesser.pkl')

class DataTransform:
    def __init__(self):
         self.data_transformation_config = DataTransformconfig()
    
    def get_data_transformation(self):
        try:
            logging.info("Data transform started")

            categorical_cols = ['sex', 'smoker', 'region']
            numerical_cols = ['age', 'bmi', 'children']

            logging.info('Data pipeline started')
            # Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )
            # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder', OrdinalEncoder()),
                    ('scaler', StandardScaler())
                ]
            )
            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_cols),
                ('cat_pipeline', cat_pipeline, categorical_cols)
            ])
            return preprocessor

        except Exception as e:
            logging.info("Error occured in get_data_transformation")
            raise customexception(e,sys)


    # Method to initialize data transformation
    def initialize_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            

            logging.info('Read train and test data')
            logging.info(f'Train data DataFrame : \n {train_df.head().to_string()}')
            logging.info(f'Test data DataFrame : \n {test_df.head().to_string()}')

            preprocessing_obj = self.get_data_transformation()

            target_column_name = 'expenses'
            drop_column_name = [target_column_name]

            input_feature_train_df = train_df.drop(target_column_name,axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(target_column_name,axis=1)
            target_feature_test_df = test_df[target_column_name]

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            logging.info("Preprocessing pickle file saved")

            return (
                train_arr, 
                test_arr
            )


        except Exception as e:
            logging.info("Error occured in the initialize_data_transformation")
            raise customexception(e,sys)