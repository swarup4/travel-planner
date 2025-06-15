from crewai import Crew, Process

def create_travel_crew(tasks):
    return Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
        verbose=True,
        process=Process.sequential
    )