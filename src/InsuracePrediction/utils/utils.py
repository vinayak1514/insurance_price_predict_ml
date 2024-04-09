import pickle
from src.InsuracePrediction.logger import logging


def save_object(file_path, obj):
    """
    Save Python object to a file using pickle.
    """
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
        logging.info(f"Object saved to {file_path}")
    except Exception as e:
        logging.error(f"Error occurred while saving object to {file_path}: {e}")

def evaluate_model(X_train, y_train, X_test, y_test, models):
    """
    Evaluate multiple models on the given training and testing data.
    """
    model_report = {}
    for name, model in models.items():
        try:
            model.fit(X_train, y_train)
            score = model.score(X_test, y_test)
            model_report[name] = score
            logging.info(f"Model: {name}, Score: {score}")
        except Exception as e:
            logging.error(f"Error occurred while evaluating model {name}: {e}")
    return model_report

def load_object(file_path):
    """
    Load Python object from a file using pickle.
    """
    try:
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
        logging.info(f"Object loaded from {file_path}")
        return obj
    except Exception as e:
        logging.error(f"Error occurred while loading object from {file_path}: {e}")
        raise e