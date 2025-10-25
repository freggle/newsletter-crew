# NewsletterCrew Crew

Welcome to the NewsletterCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/newsletter_crew/config/agents.yaml` to define your agents
- Modify `src/newsletter_crew/config/tasks.yaml` to define your tasks
- Modify `src/newsletter_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/newsletter_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

### Local Development

You can run the project in two ways:

1. Using Docker (recommended):
```bash
# Build and start the container
docker-compose up --build
```

2. Direct Python execution:
```bash
# Install dependencies
pip install -e .

# Run the API server
python -m newsletter_crew.server
```

The API will be available at http://localhost:8000

### API Endpoints

1. `POST /generate`
   - Generates a newsletter based on the provided topic
   - Request body:
     ```json
     {
       "topic": "Artificial Intelligence",
       "webhook_url": "optional-discord-webhook-url"
     }
     ```
   - Response:
     ```json
     {
       "content": "Generated newsletter content...",
       "generated_at": "2025-10-25T12:00:00"
     }
     ```

2. `GET /health`
   - Health check endpoint
   - Returns: `{"status": "healthy"}`

### Deployment on Railway

1. Install the Railway CLI:
```bash
# On macOS
brew install railway

# Other platforms
curl -fsSL https://railway.app/install.sh | sh
```

2. Login to Railway:
```bash
railway login
```

3. Create a new project:
```bash
railway init
```

4. Deploy the application:
```bash
railway up
```

This command initializes the newsletter-crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The newsletter-crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the NewsletterCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
