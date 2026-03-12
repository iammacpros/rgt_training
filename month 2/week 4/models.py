from pydantic import BaseModel, Field, field_validator
from typing import Literal

class PredictionRequest(BaseModel):
   # customerID: str = Field(..., description="Unique customer identifier")
    gender: Literal["Male", "Female"] = Field(..., description="Customer gender")
    SeniorCitizen: int = Field(..., ge=0, le=1, description="0 = No, 1 = Yes")
    Partner: Literal["Yes", "No"] = Field(..., description="Partner status")
    Dependents: Literal["Yes", "No"] = Field(..., description="Dependents status")
    tenure: int = Field(..., ge=0, description="Number of months the customer has stayed")
    PhoneService: Literal["Yes", "No"] = Field(..., description="Has phone service")
    MultipleLines: Literal["Yes", "No", "No phone service"] = Field(..., description="Multiple phone lines")
    InternetService: Literal["DSL", "Fiber optic", "No"] = Field(..., description="Type of internet service")
    OnlineSecurity: Literal["Yes", "No", "No internet service"] = Field(..., description="Online security subscription")
    OnlineBackup: Literal["Yes", "No", "No internet service"] = Field(..., description="Online backup subscription")
    DeviceProtection: Literal["Yes", "No", "No internet service"] = Field(..., description="Device protection subscription")
    TechSupport: Literal["Yes", "No", "No internet service"] = Field(..., description="Tech support subscription")
    StreamingTV: Literal["Yes", "No", "No internet service"] = Field(..., description="Streaming TV subscription")
    StreamingMovies: Literal["Yes", "No", "No internet service"] = Field(..., description="Streaming Movies subscription")
    Contract: Literal["Month-to-month", "One year", "Two year"] = Field(..., description="Contract type")
    PaperlessBilling: Literal["Yes", "No"] = Field(..., description="Paperless billing preference")
    PaymentMethod: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ] = Field(..., description="Payment method")
    MonthlyCharges: float = Field(..., ge=0, description="Monthly charges in USD")
    TotalCharges: float = Field(..., ge=0, description="Total charges in USD")
    
    @field_validator("TotalCharges", mode="before")
    def convert_total_charges(cls, v):
        """
        Convert TotalCharges to float if it's a string
        and handle empty or whitespace strings.
        """
        if isinstance(v, str):
            v = v.strip()
            if v == "":
                return 0.0
            try:
                return float(v)
            except ValueError:
                raise ValueError("TotalCharges must be a number")
        return v

class PredictionResponse(BaseModel):
   # customerID: str = Field(..., description="Unique customer identifier")
    prediction: Literal["Yes", "No"] = Field(..., description="Prediction result")
    probability: float = Field(..., ge=0, le=1, description="Probability of churn")