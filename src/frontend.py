# Import required libraries
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Configure the Streamlit page
st.set_page_config(
    page_title="Mental Health Risk Predictor",
    page_icon="🧠",
    layout="wide"  # Use wide layout for better visualization
)

# Main title and description
st.title("🧠 Mental Health Risk Predictor")
st.write("Enter your lifestyle factors to get a mental health risk assessment")

# Create two columns for better layout organization
col1, col2 = st.columns(2)

# Left column: Input form
with col1:
    st.subheader("Input Your Data")
    
    # Slider inputs for various lifestyle factors
    # Each slider has appropriate range and default values
    sleep_hours = st.slider(
        "Average Sleep Hours",
        0.0, 12.0, 7.0, 0.5,  # min, max, default, step
        help="How many hours do you sleep on average?"
    )
    
    exercise_hours = st.slider(
        "Weekly Exercise Hours",
        0.0, 20.0, 3.0, 0.5,
        help="How many hours do you exercise per week?"
    )
    
    stress_level = st.slider(
        "Stress Level (1-10)",
        1, 10, 5,
        help="Rate your stress level (1 = Very Low, 10 = Very High)"
    )
    
    social_activity = st.slider(
        "Social Activity Level (1-10)",
        1, 10, 5,
        help="Rate your social activity level (1 = Very Low, 10 = Very High)"
    )
    
    work_hours = st.slider(
        "Daily Work Hours",
        0.0, 16.0, 8.0, 0.5,
        help="How many hours do you work per day?"
    )
    
    screen_time = st.slider(
        "Daily Screen Time Hours",
        0.0, 16.0, 6.0, 0.5,
        help="How many hours do you spend on screens per day?"
    )

    # Prediction button
    if st.button("Predict Risk"):
        # Prepare data for API request
        data = {
            "sleep_hours": sleep_hours,
            "exercise_hours": exercise_hours,
            "stress_level": stress_level,
            "social_activity": social_activity,
            "work_hours": work_hours,
            "screen_time": screen_time
        }
        
        try:
            # Make POST request to backend API
            response = requests.post("http://localhost:8000/predict", json=data)
            
            if response.status_code == 200:
                # Display prediction result with appropriate styling
                prediction = response.json()["prediction"]
                st.success(f"Predicted Risk Level: {prediction}")
            else:
                # Handle API error
                st.error("Error making prediction. Please try again.")
        except requests.exceptions.ConnectionError:
            # Handle connection error (e.g., backend not running)
            st.error("Could not connect to the prediction service. Is the backend server running?")

# Right column: History display
with col2:
    st.subheader("Recent Predictions")
    try:
        # Fetch prediction history from backend
        response = requests.get("http://localhost:8000/history")
        if response.status_code == 200:
            history = response.json()
            if history:
                # Convert data to pandas DataFrame for better display
                df = pd.DataFrame(history)
                # Format timestamp for better readability
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M')
                
                # Display history table with selected columns
                st.dataframe(
                    df[['timestamp', 'sleep_hours', 'exercise_hours', 'stress_level', 
                        'social_activity', 'work_hours', 'screen_time', 'prediction']]
                )
            else:
                # Handle empty history
                st.info("No prediction history available yet.")
    except requests.exceptions.ConnectionError:
        # Handle connection error
        st.error("Could not fetch prediction history. Is the backend server running?")
