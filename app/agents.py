from crewai import Agent
from config import get_llm
from tools import search_tool

llm = get_llm()

def get_guide_agent():
    return Agent(
        role="City local guide expert",
        goal="Provide recommendations for activities and food in the destination city.",
        backstory="Local expert passionate about hidden gems and tourist favorites.",
        tools=[search_tool],
        verbose=True,
        max_iter=5,
        llm=llm,
        allow_delegation=False
    )

def get_location_agent():
    return Agent(
        role="Travel Trip Expert",
        goal="Handle logistics and city language info.",
        backstory="Seasoned traveler with strong knowledge of various destinations.",
        tools=[search_tool],
        verbose=True,
        max_iter=5,
        llm=llm,
        allow_delegation=False
    )

def get_planner_agent():
    return Agent(
        role="Travel Planning Expert",
        goal="Compile all info into a seamless itinerary.",
        backstory="Organizational wizard and professional guide who crafts plans.",
        tools=[search_tool],
        verbose=True,
        max_iter=5,
        llm=llm,
        allow_delegation=False
    )