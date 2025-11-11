from google.adk.agents import Agent, SequentialAgent, ParallelAgent
from google.adk.tools import google_search

# Tech Researcher: Focuses on AI and ML trends
tech_researcher = Agent(
    name="TechResearcher",
    model="gemini-2.0-flash",
    instruction="""Research the latest AI/ML trends. Include 3 key developments,
the main companies involved, and the potential impact. Keep the report very concise (100 words).""",
    tools=[google_search],
    output_key="tech_research",
)

# Health Researcher: Focuses on medical breakthroughs
health_researcher = Agent(
    name="HealthResearcher",
    model="gemini-2.0-flash",
    instruction="""Research recent medical breakthroughs. Include 3 significant advances,
their practical applications, and estimated timelines. Keep the report concise (100 words).""",
    tools=[google_search],
    output_key="health_research",
)

# Finance Researcher: Focuses on fintech trends
finance_researcher = Agent(
    name="FinanceResearcher",
    model="gemini-2.0-flash",
    instruction="""Research current fintech trends. Include 3 key trends,
their market implications, and the future outlook. Keep the report concise (100 words).""",
    tools=[google_search],
    output_key="finance_research",
)

# Aggregator Agent: Combines all research findings
aggregator_agent = Agent(
    name="AggregatorAgent",
    model="gemini-2.0-flash",
    instruction="""Combine these three research findings into a single executive summary:

    **Technology Trends:**
    {tech_research}
    
    **Health Breakthroughs:**
    {health_research}
    
    **Finance Innovations:**
    {finance_research}
    
    Your summary should highlight common themes, surprising connections, and the most important key takeaways from all three reports. The final summary should be around 200 words.""",
    output_key="executive_summary",
)

# Parallel Agent: Runs all research agents simultaneously
parallel_research_team = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[tech_researcher, health_researcher, finance_researcher],
)

# Sequential Agent: Runs parallel research first, then aggregation
root_agent = SequentialAgent(
    name="2_ResearchSystem",
    sub_agents=[parallel_research_team, aggregator_agent],
)
