# Import required SQLAlchemy components and datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create the base class for declarative models
Base = declarative_base()

# Create SQLite database engine
# Using SQLite for simplicity - stores data in a local file
engine = create_engine('sqlite:///health_predictions.db')

# Create a sessionmaker factory bound to our database
SessionLocal = sessionmaker(bind=engine)

class HealthData(Base):
    """
    Database model for storing health predictions and user inputs
    Includes various lifestyle factors and the resulting prediction
    """
    __tablename__ = "health_data"  # Name of the database table
    
    # Primary key for unique identification of each record
    id = Column(Integer, primary_key=True, index=True)
    
    # User input fields for lifestyle factors
    sleep_hours = Column(Float)        # Average daily sleep in hours
    exercise_hours = Column(Float)     # Weekly exercise hours
    stress_level = Column(Integer)     # Stress level on scale 1-10
    social_activity = Column(Integer)  # Social activity level on scale 1-10
    work_hours = Column(Float)         # Daily work hours
    screen_time = Column(Float)        # Daily screen time in hours
    
    # Model prediction output
    prediction = Column(String)        # Risk level prediction (Low/Medium/High)
    
    # Timestamp for tracking when the prediction was made
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create all defined tables in the database
Base.metadata.create_all(bind=engine)

def get_db():
    """
    Database session generator
    Yields a database session and ensures it's closed after use
    Used as a dependency in FastAPI endpoints
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
