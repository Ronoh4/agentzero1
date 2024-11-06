from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os

# Set environmental var variables
nvidia_api_key = os.environ.get["NVIDIA_API_KEY"]


# Initialize NVIDIA Client using LLM
nvidia_llm = LLM(
    model="meta/llama-3.1-8b-instruct",
    api_key=os.environ["NVIDIA_API_KEY"],
    api_base="https://integrate.api.nvidia.com/v1/",
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024
)

@CrewBase
class ClothingStoreCrew:
    @agent
    def origin_agent(self) -> Agent:
        return Agent(
            llm=nvidia_llm,
            config=self.agents_config['origin_agent'],
            verbose=False
        )

    @agent
    def trends_agent(self) -> Agent:
        return Agent(
            llm=nvidia_llm,
            config=self.agents_config['trends_agent'],
            verbose=False
        )

    @agent
    def reporting_agent(self) -> Agent:
        return Agent(
            llm=nvidia_llm,
            config=self.agents_config['reporting_agent'],
            verbose=False
        )
    
    @agent
    def quality_agent(self) -> Agent:
        return Agent(
            llm=nvidia_llm,
            config=self.agents_config['quality_agent'],
            verbose=True
        )

    @task
    def origin_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['origin_research_task'],
        )

    @task
    def trends_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['trends_research_task'],
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task'], 
        )
    
    @task
    def quality_task(self) -> Task:
        return Task(
            config=self.tasks_config['quality_task'],
            delegations=True  
        )
    
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Define the order in which tasks will run
            verbose=True,
        )
