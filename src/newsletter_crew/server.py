import uvicorn
from newsletter_crew.api import app

def run_server():
    """Run the FastAPI server"""
    uvicorn.run(
        "newsletter_crew.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    run_server()
