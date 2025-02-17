# Mental Health Risk Predictor - Project Documentation

## Project Overview
This project is a machine learning-based web application that predicts mental health risks based on lifestyle factors. It combines modern web technologies with machine learning to provide useful health insights.

## Project Structure
```
mental_health_predictor/
├── src/                    # Source code directory
│   ├── __init__.py        # Makes src a Python package
│   ├── app.py             # FastAPI backend application
│   ├── frontend.py        # Streamlit frontend interface
│   └── models.py          # Database models and configuration
├── data/                  # Directory for database and ML models
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Technology Stack
1. **Backend Framework**: FastAPI
   - Modern, fast Python web framework
   - Automatic API documentation
   - Built-in data validation
   - Async support

2. **Frontend Framework**: Streamlit
   - Python-based web interface
   - Built-in data visualization
   - Interactive widgets
   - Real-time updates

3. **Database**: SQLite with SQLAlchemy
   - Lightweight database
   - No separate server needed
   - Easy to set up and maintain
   - Robust ORM with SQLAlchemy

4. **Machine Learning**: Scikit-learn
   - Random Forest Classifier
   - Prediction based on lifestyle factors
   - Easy to update and maintain

## Component Details

### 1. Database Model (models.py)
- Defines the database schema using SQLAlchemy ORM
- Stores user inputs and predictions
- Manages database connections
- Includes timestamp for tracking prediction history

### 2. Backend API (app.py)
- Handles HTTP requests using FastAPI
- Processes user input data
- Manages ML model predictions
- Stores results in database
- Provides endpoints:
  - POST /predict: Make new predictions
  - GET /history: Retrieve prediction history

### 3. Frontend Interface (frontend.py)
- User-friendly interface using Streamlit
- Input collection through sliders
- Real-time prediction display
- Historical data visualization
- Error handling and user feedback

### 4. Main Application (main.py)
- Application entry point
- Server configuration
- Development server setup

## Key Features
1. **Risk Prediction**
   - Sleep pattern analysis
   - Exercise habit evaluation
   - Stress level assessment
   - Social activity measurement
   - Work-life balance analysis
   - Screen time impact

2. **Data Visualization**
   - Historical prediction tracking
   - Trend analysis
   - Real-time updates

3. **User Experience**
   - Intuitive slider inputs
   - Immediate feedback
   - Clear risk assessment
   - Historical data access

## Running the Application

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the backend server:
```bash
python main.py
```

3. Launch the frontend interface:
```bash
streamlit run src/frontend.py
```

## Future Improvements
1. User authentication
2. More detailed risk analysis
3. Personalized recommendations
4. Data export functionality
5. Advanced visualization options
6. Model retraining capability
