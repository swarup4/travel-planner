from agents import get_guide_agent, get_location_agent, get_planner_agent
from tasks import get_location_task, get_guide_task, get_planner_task
from service import create_travel_crew


from_city = "Bangalore"
destination_city = "Phuket"
date_from = "1st June 2025"
date_to = "7th June 2025"
interest = "Sight Seeing and good local food"
other_city = "Koh Samui, Krabi"


# Load Agents
guide_agent = get_guide_agent()
location_agent = get_location_agent()
planner_agent = get_planner_agent()

# Create Tasks
location_task = get_location_task(location_agent, from_city, destination_city, other_city, date_from, date_to, interest)
guide_task = get_guide_task(guide_agent, destination_city, interest)
planner_task = get_planner_task(planner_agent, [location_task, guide_task])

# Assemble and run the crew
crew = create_travel_crew([location_task, guide_task, planner_task])
result = crew.kickoff()
