from src.InsuracePrediction.components.data_ingestion import DataIngestion
from src.InsuracePrediction.components.data_transformation import DataTransform
from src.InsuracePrediction.components.model_trainer import InsuranceModelTrainer
from src.InsuracePrediction.exception import customexception
from src.InsuracePrediction.logger import logging



# Initialize DataIngestion object
obj = DataIngestion()

# Perform data ingestion and get paths to train and test data
train_data_path, test_data_path = obj.initiate_data_ingestion()

# Initialize DataTransformation object
data_transformation = DataTransformat()

# Initialize data transformation and get transformed train and test arrays
train_arr, test_arr = data_transformation.initialize_data_transformation(train_data_path, test_data_path)

# Initialize InsuranceModelTrainer object
model_trainer_obj = InsuranceModelTrainer()

# Initiate model training with transformed train and test arrays
model_trainer_obj.initate_model_training(train_arr, test_arr)