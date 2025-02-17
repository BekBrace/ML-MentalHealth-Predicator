# Import the ASGI server
import uvicorn

# Entry point of the application
if __name__ == "__main__":
    # Run the FastAPI application using uvicorn
    # host="0.0.0.0" makes the server accessible from other machines
    # port=8000 is the default port for the API
    # reload=True enables auto-reload on code changes (development mode)
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)
