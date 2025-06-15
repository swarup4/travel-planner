from crewai import Agent, Task, Crew, Process
from crewai import LLM
# from tools import search_tool

# Tools
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

# Tasks
from datetime import datetime


# Initialize Ollama for the LLM
llm = LLM(
    model="ollama/llama3.2:latest",
    base_url="http://localhost:11434"
)
flightInfo = []

from_city = "Bangalore"
destination_city = ["Phuket", "Bangkok"]
date_from = "1st June 2025"


@tool
def flight_search(from_city: str, destination_cities: list, date_from: str):
    """
    Compares flight options across multiple destinations from a given source.
    Extracts basic flight details from unstructured search text.
    Converts price to INR.
    """
    search = DuckDuckGoSearchResults(num_results=10, verbose=True)
    results = []

    for city in destination_cities:
        query = f"Flight from {from_city} to {city} on {date_from}"
        flight_info = search.run(query)
        results.append((city, flight_info))
        flightInfo.append((city, flight_info))

    summary = "### Flight Comparison Summary\n"
    for city, info in results:
        summary += f"#### {from_city} → {city}\n{info}\n\n"

    best_city = results[0][0]  # Simulated
    summary += f"---\n** Recommended Destination Based on Cheapest Match:** `{best_city}`"
    return summary


# Flight booking agent 
flight_book_agent = Agent(
    role="Flight booking expert",
    goal="Searches multiple destinations and finds the best and cheapest flight.",
    backstory="Experienced travel agent who compares destinations and picks the most efficient option.",
    tools=[flight_search],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False
)

# Flight booking task
flight_booking_task = Task(
    description=f"""
    Compare flights from {from_city} to each of the following destinations on {date_from}: 
    {", ".join(destination_city)}.

    Return:
    - Cheapest & best flight (based on relevance)
    - Summary of results in markdown
    """,
    agent=flight_book_agent,
    inputs={
        "from_city": from_city,
        "destination_cities": destination_city,
        "date_from": date_from
    },
    expected_output="Detailed markdown report of flight options and recommendation",
    output_file="output/Flight_Info.md"
)

# Create crew and run the task
crew = Crew(
    agents=[flight_book_agent],
    tasks=[flight_booking_task],
    process=Process.sequential,
    full_output=True,
    share_crew=False,
    verbose=True
)

result = crew.kickoff()


print(flightInfo)