from fastapi import HTTPException
import joblib
import logging
from pydantic import BaseModel  # noqa: F401
import os
import io
from models import PredictionRequest, PredictionResponse  # ty:ignore[unresolved-import]
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

# Check if model exists before starting the app
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

try:
    with open(MODEL_PATH, "rb") as f:
        model = joblib.load(f)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise e



def predict_churn(input: PredictionRequest) -> PredictionResponse:
    # Convert Pydantic object to DataFrame
    data = pd.DataFrame([input.model_dump()])

    # Make prediction
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return PredictionResponse(
        #customerID=input.customerID,
        prediction="Yes" if prediction == 1 else "No",
        probability=probability
    )


def process_batch(file_bytes: bytes) -> pd.DataFrame:

    # read the csv file
    try:
        df = pd.read_csv(io.BytesIO(file_bytes))
        input_df = df.copy()

    # data preprocessing
        if 'TotalCharges' in input_df.columns:
            input_df['TotalCharges'] = pd.to_numeric(input_df['TotalCharges'], errors='coerce').fillna(0.0)

        if 'customerID' in input_df.columns:
            input_df = input_df.drop(columns=['customerID'])
        
        if 'Churn' in input_df.columns:
            input_df = input_df.drop(columns=['Churn'])

        return input_df
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {str(e)}")
    

def predict_batch(input_df: pd.DataFrame, threshold: float = 0.35) -> pd.DataFrame:
    try:
        # Get predicted probabilities for the positive class ("Yes")
        probabilities = model.predict_proba(input_df)[:, 1]

        # Apply custom threshold instead of model.predict()
        predictions = ["Yes" if prob >= threshold else "No" for prob in probabilities]

        new_predictions = model.predict(input_df)

        # Combine into results
        results_df = input_df.copy()
        results_df['prediction'] = predictions
        results_df['new_prediction'] = new_predictions
        results_df['probability'] = probabilities

        return results_df


    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during batch prediction: {str(e)}")
    

