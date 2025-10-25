from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class NewsletterCrew():
    """Newsletter crew for creating AI-focused newsletters"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],  # type: ignore[index]
            verbose=True
        )

    @agent
    def reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer'],  # type: ignore[index]
            verbose=True
        )

    @task
    def research_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_news_task']  # type: ignore[index]
        )

    @task
    def research_paper_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_paper_task']  # type: ignore[index]
        )

    @task
    def write_newsletter_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_newsletter_task']  # type: ignore[index]
        )

    @task
    def review_newsletter_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_newsletter_task'],  # type: ignore[index]
            output_file='newsletter.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Newsletter crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )