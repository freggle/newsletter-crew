import os
import requests

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
            print(f"Chunk sent successfully! Response status: {response.status_code}")
        
        print("Newsletter sent to Discord successfully!")
    except Exception as e:
        print(f"Error sending to Discord: {e}")

if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1428719787172958269/lqJvy4kfMjte89wMcpqr6alLD7eZYa0Kq5zazIRL67k2LxdwZigSvYBlIdjveT53zb5l"
    send_to_discord(webhook_url)



