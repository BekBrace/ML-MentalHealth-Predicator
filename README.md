# Mental Health Risk Predictor

This application uses machine learning to predict potential mental health risks based on lifestyle factors. It demonstrates the application of AI in healthcare while maintaining user privacy and providing actionable insights.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Project Development Order

When creating this project from scratch, follow this order to ensure proper dependency management:

1. Create project structure:
```
mental_health_predictor/
└── src/
```

2. Create `requirements.txt`:
   - Lists all project dependencies
   - Enables easy package installation
   - Must be created first to set up the development environment

3. Create `models.py`:
   - Defines database models and configurations
   - Sets up SQLAlchemy ORM
   - Other files depend on these data structures

4. Create `src/__init__.py`:
   - Empty file that makes src directory a Python package
   - Required for proper Python imports

5. Create `src/app.py`:
   - Contains FastAPI backend implementation
   - Depends on models.py for database operations
   - Implements ML model and API endpoints

6. Create `src/frontend.py`:
   - Contains Streamlit user interface
   - Depends on backend API being defined
   - Implements user interface that calls the API

7. Create `main.py`:
   - Application entry point
   - Runs the FastAPI server
   - Depends on app.py being properly set up

8. Create `README.md`:
   - Documentation for installation and usage
   - Written last as it describes the complete system

This order matters because:
- Dependencies must be installed first (requirements.txt)
- Database models define core data structures (models.py)
- Backend API needs database models (app.py)
- Frontend needs to know available API endpoints (frontend.py)
- Main entry point ties everything together (main.py)

## Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
cd mental_health_predictor
```

2. Create a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install fastapi==0.104.1
pip install uvicorn==0.24.0
pip install streamlit==1.28.2
pip install pandas==2.1.3
pip install scikit-learn==1.3.2
pip install numpy==1.26.2
pip install python-multipart==0.0.6
pip install sqlalchemy==2.0.23

```
FastAPI (0.104.1) – A modern, high-performance web framework for building APIs with Python, based on type hints and ASGI.

Uvicorn (0.24.0) – A lightning-fast ASGI server for running FastAPI and other ASGI-based applications, using asyncio for high performance.

Streamlit (1.28.2) – A powerful Python library for building interactive web apps for data science and machine learning with minimal effort.

Pandas (2.1.3) – A versatile data analysis and manipulation library, providing powerful DataFrame and Series structures for handling tabular data.

Scikit-learn (1.3.2) – A widely used machine learning library that offers simple and efficient tools for data mining, analysis, and predictive modeling.

NumPy (1.26.2) – A fundamental package for numerical computing in Python, supporting large multi-dimensional arrays, matrices, and mathematical functions.

Python-Multipart (0.0.6) – A lightweight library for handling multipart/form-data, often used for file uploads in FastAPI applications.

SQLAlchemy (2.0.23) – A powerful SQL toolkit and Object Relational Mapper (ORM) for Python, allowing seamless interaction with databases.
```
## Running the Application

The application consists of two components that need to be run separately:

1. Start the FastAPI backend server:
```bash
# From the project root directory
python main.py
```
The backend server will start at `http://localhost:8000`

2. In a new terminal, start the Streamlit frontend:
```bash
# From the project root directory
streamlit run src/frontend.py
```
The frontend will automatically open in your default web browser at `http://localhost:8501`

## Using the Application

1. Once both servers are running, you'll see the web interface in your browser
2. Use the sliders to input your lifestyle factors:
   - Sleep hours (0-12 hours)
   - Exercise hours per week (0-20 hours)
   - Stress level (1-10)
   - Social activity level (1-10)
   - Work hours per day (0-16 hours)
   - Screen time per day (0-16 hours)
3. Click "Predict Risk" to get your mental health risk assessment
4. View your prediction history in the right column

## Troubleshooting

1. If you see "Could not connect to the prediction service":
   - Make sure the FastAPI backend is running (python main.py)
   - Check that port 8000 is not being used by another application

2. If you see "ModuleNotFoundError":
   - Make sure you've installed all required packages
   - Verify you're in the virtual environment (if using one)

3. To stop the application:
   - Press Ctrl+C in both terminal windows
   - Or close the terminal windows

## Project Structure
```
mental_health_predictor/
├── src/                    # Source code directory
│   ├── __init__.py        # Makes src a Python package
│   ├── app.py             # FastAPI backend application
│   ├── frontend.py        # Streamlit frontend interface
│   └── models.py          # Database models
├── data/                  # Database and ML models
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Technology Stack
- Backend: FastAPI
- Frontend: Streamlit
- Database: SQLite
- ML: Scikit-learn
