from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import os

from newsletter_crew.crew import NewsletterCrew
from newsletter_crew.main import send_to_discord

app = FastAPI(
    title="Newsletter Crew API",
    description="API for generating AI-focused newsletters using CrewAI",
    version="1.0.0"
)

class NewsletterRequest(BaseModel):
    topic: str = "Artificial Intelligence"
    webhook_url: Optional[str] = None

class NewsletterResponse(BaseModel):
    content: str
    generated_at: str

@app.post("/generate", response_model=NewsletterResponse)
async def generate_newsletter(request: NewsletterRequest):
    """Generate a newsletter based on the provided topic"""
    try:
        # Initialize inputs
        inputs = {
            'topic': request.topic,
            'current_year': str(datetime.now().year)
        }
        
        # Create and run the crew
        crew_instance = NewsletterCrew().crew()
        crew_instance.kickoff(inputs=inputs)
        
        # Read the generated newsletter
        with open('newsletter.md', 'r') as f:
            content = f.read()
        
        # Send to Discord if webhook URL is provided
        if request.webhook_url:
            send_to_discord(request.webhook_url)
        
        return NewsletterResponse(
            content=content,
            generated_at=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
