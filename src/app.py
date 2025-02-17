# Import necessary libraries and modules
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import joblib
import numpy as np
from models import get_db, HealthData

# Initialize FastAPI application with title
app = FastAPI(title="Mental Health Risk Predictor")

class HealthDataInput(BaseModel):
    """
    Pydantic model for validating input data
    Defines the structure and types of the input data expected from users
    """
    sleep_hours: float      # Daily sleep hours (0-12)
    exercise_hours: float   # Weekly exercise hours (0-20)
    stress_level: int       # Stress level (1-10)
    social_activity: int    # Social activity level (1-10)
    work_hours: float       # Daily work hours (0-16)
    screen_time: float      # Daily screen time hours (0-16)

# Function to create a dummy ML model for demonstration
def create_dummy_model():
    """
    Creates and trains a dummy Random Forest model
    In production, this should be replaced with a properly trained model
    """
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Generate dummy training data
    X = np.random.rand(100, 6)
    y = np.random.choice(['Low Risk', 'Medium Risk', 'High Risk'], size=100)
    model.fit(X, y)
    return model

# Initialize the machine learning model
model = create_dummy_model()

@app.post("/predict")
def predict_health_risk(data: HealthDataInput, db: Session = Depends(get_db)):
    """
    Endpoint for making predictions
    Takes user input data, makes a prediction, and stores results in database
    
    Args:
        data: Validated input data from user
        db: Database session (automatically injected by FastAPI)
    
    Returns:
        dict: Prediction result
    """
    try:
        # Convert input data to numpy array for prediction
        input_data = np.array([[
            data.sleep_hours,
            data.exercise_hours,
            data.stress_level,
            data.social_activity,
            data.work_hours,
            data.screen_time
        ]])
        
        # Use model to make prediction
        prediction = model.predict(input_data)[0]
        
        # Create and save record to database
        db_record = HealthData(
            sleep_hours=data.sleep_hours,
            exercise_hours=data.exercise_hours,
            stress_level=data.stress_level,
            social_activity=data.social_activity,
            work_hours=data.work_hours,
            screen_time=data.screen_time,
            prediction=prediction
        )
        db.add(db_record)
        db.commit()
        
        return {"prediction": prediction}
    except Exception as e:
        # Handle any errors that occur during prediction
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
def get_prediction_history(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve prediction history
    Returns the 10 most recent predictions from the database
    
    Args:
        db: Database session (automatically injected by FastAPI)
    
    Returns:
        list: List of previous predictions
    """
    records = db.query(HealthData).order_by(HealthData.timestamp.desc()).limit(10).all()
    return records
