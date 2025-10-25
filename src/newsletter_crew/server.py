import os
import uvicorn
from newsletter_crew.api import app

def run_server():
    """Run the FastAPI server"""
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        "newsletter_crew.api:app",
        host="0.0.0.0",
        port=port,
        reload=False  # Disable reload in production
    )

if __name__ == "__main__":
    run_server()
