#!/usr/bin/env python
import sys
import warnings
import os
import requests
from datetime import datetime

from newsletter_crew.crew import NewsletterCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def send_to_discord(webhook_url):
    """Send newsletter content to Discord webhook"""
    try:
        # Read the newsletter content
        with open('newsletter.md', 'r') as f:
            content = f.read()
        
        # Remove the @ symbol from the webhook URL if present
        webhook_url = webhook_url.replace('@', '')
        
        # Split content into chunks of 2000 characters (Discord's limit)
        chunks = [content[i:i+2000] for i in range(0, len(content), 2000)]
        
        # Send each chunk
        for chunk in chunks:
            payload = {"content": chunk}
            response = requests.post(webhook_url, json=payload)
            response.raise_for_status()
        
        print("Newsletter sent to Discord successfully!")
    except Exception as e:
        print(f"Error sending to Discord: {e}")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Artificial Intelligence',
        'current_year': str(datetime.now().year)
    }
    
    try:
        # Run the crew
        NewsletterCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    # First run the crew
    run()
    
    # Then send to Discord if webhook is configured
    webhook_url = os.getenv('webhook')
    if webhook_url:
        send_to_discord(webhook_url)