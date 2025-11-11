from google.adk.agents import Agent, SequentialAgent

# Outline Agent: Creates the initial blog post outline
outline_agent = Agent(
    name="OutlineAgent",
    model="gemini-2.0-flash",
    instruction="""Create a blog outline for the given topic with:
    1. A catchy headline
    2. An introduction hook
    3. 3-5 main sections with 2-3 bullet points for each
    4. A concluding thought""",
    output_key="blog_outline",
)

# Writer Agent: Writes the full blog post based on the outline
writer_agent = Agent(
    name="WriterAgent",
    model="gemini-2.0-flash",
    instruction="""Following this outline strictly: {blog_outline}
    Write a brief, 200 to 300-word blog post with an engaging and informative tone.""",
    output_key="blog_draft",
)

# Editor Agent: Edits and polishes the draft
editor_agent = Agent(
    name="EditorAgent",
    model="gemini-2.0-flash",
    instruction="""Edit this draft: {blog_draft}
    Your task is to polish the text by fixing any grammatical errors, improving the flow and sentence structure, and enhancing overall clarity.""",
    output_key="final_blog",
)

# Sequential Agent: Runs agents in order (Outline -> Write -> Edit)
root_agent = SequentialAgent(
    name="1_BlogPipeline",
    sub_agents=[outline_agent, writer_agent, editor_agent],
)
