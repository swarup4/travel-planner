from crewai import Task

def get_location_task(agent, from_city, destination_city, other_city, date_from, date_to, interest):
    return Task(
        description=f"""
            Collect travel logistics and city-specific insights from {from_city} to {destination_city} 
            between {date_from} and {date_to}, focusing on {interest}.
            I want to cover other city also along with {destination_city}. Add other city option in my travel plan. 
            Other City: {other_city}
        """,
        agent=agent,
        expected_output="A detailed markdown report with relevant travel data.",
        output_file="output/City_report.md"
    )

def get_guide_task(agent, destination_city, interest):
    return Task(
        description=f"""
            Provide detailed recommendations for places to visit, eat, and explore in {destination_city}, 
            specifically aligned to interest: {interest}.
        """,
        agent=agent,
        expected_output="A markdown itinerary including attractions, food, and activities.",
        output_file = "output/Guide_report.md"
    )

def get_planner_task(agent, context):
    return Task(
        description=f"""
            Use gathered city logistics and interest data to construct a detailed travel plan itinerary.
        """,
        agent=agent,
        expected_output="""
            A structured markdown travel itinerary.
        """,
        context=context,
        output_file="output/Travel_plan.md"
    )