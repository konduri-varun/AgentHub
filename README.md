# 🤖 AgentHub: Multi-Agent Architecture Learning Repository

A comprehensive collection of multi-agent systems built with Google ADK, demonstrating different agent architectures and patterns for learning and experimentation.

## 📚 Learning Path

This repository contains **4 different agent architectures** organized in learning order:

### 1. **0_my_first_agent** - Hierarchical Multi-Agent System
**Pattern**: Root agent delegates to specialized sub-agents
- **Architecture**: Manager → Worker agents
- **Use Case**: Web search + code execution
- **Skills**: Agent delegation, tool usage

### 2. **1_BlogPipeline** - Sequential Agent Architecture
**Pattern**: Fixed pipeline with linear execution
- **Architecture**: Outline → Write → Edit
- **Use Case**: Blog post creation
- **Skills**: State management, sequential workflows

### 3. **2_ResearchSystem** - Parallel Agent Architecture
**Pattern**: Concurrent execution with aggregation
- **Architecture**: Parallel research → Aggregation
- **Use Case**: Multi-domain research
- **Skills**: Parallel processing, result synthesis

### 4. **3_StoryPipeline** - Loop Agent Architecture
**Pattern**: Iterative refinement with quality control
- **Architecture**: Write → Critique → Refine (loop)
- **Use Case**: Story writing with improvement cycles
- **Skills**: Loop control, iterative improvement

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/api-keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd agenthub
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install google-adk
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file and add your API key
   cp 0_my_first_agent/.env.example 0_my_first_agent/.env
   # Edit .env and add your GOOGLE_API_KEY
   ```

5. **Start the ADK web server**
   ```bash
   adk web
   ```

6. **Access the web interface**
   Open http://127.0.0.1:8000 in your browser

## 📁 Project Structure

```
AgentHub/
├── .gitignore                    # Git ignore rules
├── README.md                     # This comprehensive guide
├── 0_my_first_agent/            # Hierarchical agents
│   ├── agent.py                  # Agent definitions
│   ├── __init__.py              # Package init
│   ├── .env.example             # Environment template
│   ├── README.md                # Detailed documentation
│   └── requirements.txt         # Dependencies
├── 1_BlogPipeline/              # Sequential agents
│   ├── agent.py
│   ├── __init__.py
│   ├── .env.example
│   └── README.md
├── 2_ResearchSystem/            # Parallel agents
│   ├── agent.py
│   ├── __init__.py
│   ├── .env.example
│   └── README.md
└── 3_StoryPipeline/             # Loop agents
    ├── agent.py
    ├── __init__.py
    ├── .env.example
    └── README.md
```

## 🎯 Learning Objectives

By exploring these agents, you'll learn:

- **Agent Communication**: How agents pass data between each other
- **State Management**: Using `output_key` for workflow continuity
- **Workflow Patterns**: Sequential, parallel, and loop architectures
- **Tool Integration**: Google Search and custom function tools
- **Quality Control**: Iterative refinement and critique systems
- **Scalability**: Building complex systems from simple components

## 💡 Usage Examples

### Hierarchical Agent (0_my_first_agent)
```
"What is the current population of Tokyo?"
"Calculate 25 * 17 + 42"
"What's Tokyo's population and what percentage is that of Japan's total?"
```

### Sequential Agent (1_BlogPipeline)
```
"Write a blog post about the benefits of AI in healthcare"
"Create a blog about sustainable living tips"
```

### Parallel Agent (2_ResearchSystem)
```
"Run the daily executive briefing on Tech, Health, and Finance"
"What are the latest developments in AI, medical research, and fintech?"
```

### Loop Agent (3_StoryPipeline)
```
"Write a short story about a lighthouse keeper who discovers a mysterious map"
"Create a story about a robot learning to paint"
```

## 🔧 Configuration

### Environment Variables
Each agent folder contains a `.env.example` file. Copy it to `.env` and add your API key:

```bash
cp <agent_folder>/.env.example <agent_folder>/.env
```

### API Key Setup
1. Visit [Google AI Studio](https://aistudio.google.com/app/api-keys)
2. Create a new API key
3. Add it to your `.env` files: `GOOGLE_API_KEY=your_key_here`

## 🏗️ Architecture Patterns Explained

### Hierarchical (Manager-Worker)
- **Root Agent**: Analyzes requests and delegates
- **Worker Agents**: Specialized for specific tasks
- **Communication**: Via AgentTool wrappers

### Sequential (Assembly Line)
- **Fixed Order**: Agents run in predetermined sequence
- **State Passing**: Each agent receives previous output
- **Predictable**: Same workflow every time

### Parallel (Concurrent Teams)
- **Simultaneous**: Multiple agents work at once
- **Independent**: Tasks don't depend on each other
- **Aggregation**: Results combined at the end

### Loop (Iterative Refinement)
- **Quality Control**: Critique and improvement cycles
- **Exit Conditions**: Stops when quality met or max iterations
- **Self-Improvement**: Agents refine their own output

## 🧪 Testing & Experimentation

### Individual Agent Testing
```bash
# Test a specific agent
cd <agent_folder>
adk web
```

### Development Tips
- Start with simple prompts and gradually increase complexity
- Monitor the debug traces to understand agent communication
- Experiment with different prompt variations
- Check agent outputs in the web interface

## 🔒 Security & Best Practices

- ✅ **API Keys**: Never commit `.env` files (already in `.gitignore`)
- ✅ **Virtual Environment**: Always use venv for isolation
- ✅ **Rate Limits**: Built-in retry logic handles API limits
- ✅ **Error Handling**: Agents include error recovery mechanisms

## 📊 Performance Considerations

- **Sequential**: Slower but predictable and reliable
- **Parallel**: Faster for independent tasks, more complex setup
- **Loop**: Variable time based on quality requirements
- **Hierarchical**: Good balance of speed and complexity

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-agent-pattern`)
3. Add your agent in a new numbered folder
4. Update this README with your new pattern
5. Test thoroughly with different prompts
6. Submit a pull request

### Adding New Agent Patterns
- Follow the numbering convention (4_new_pattern)
- Include comprehensive README.md
- Add .env.example file
- Test with multiple use cases

## 📚 Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Multi-Agent Systems Guide](https://google.github.io/adk-docs/agents/multi-agent-systems/)

## 🆘 Troubleshooting

### Common Issues

**"No root_agent found"**
- Ensure `agent.py` contains a variable named `root_agent`
- Check folder structure matches ADK expectations

**"API Key Error"**
- Verify `.env` file exists and contains valid `GOOGLE_API_KEY`
- Check API key hasn't expired

**"Import Error"**
- Ensure `google-adk` is installed: `pip install google-adk`
- Activate virtual environment: `venv\Scripts\activate`

**"429 Rate Limited"**
- Wait a few minutes and retry
- Consider upgrading API quota if persistent

### Getting Help
- Check individual agent README.md files
- Review ADK documentation
- Test with simple prompts first

---

## 🔍 Detailed Agent Breakdown

### 0_my_first_agent: Hierarchical Architecture

**Core Concept**: Manager delegates to specialists
```python
# Root agent analyzes and routes requests
root_agent = Agent(
    name="AgentHub",
    instructions="Analyze the request and delegate to appropriate specialist",
    tools=[search_agent_tool, code_agent_tool]
)
```

**Key Components**:
- **Search Agent**: Handles web queries using Google Search API
- **Code Agent**: Executes Python code for calculations
- **Delegation Logic**: LLM determines which agent to use

**Learning Focus**: Agent communication, tool integration, task routing

### 1_BlogPipeline: Sequential Architecture

**Core Concept**: Linear workflow with state passing
```python
blog_pipeline = SequentialAgent(
    name="BlogPipeline",
    sub_agents=[
        Agent(name="OutlineAgent", instructions="Create blog outline", output_key="outline"),
        Agent(name="WriterAgent", instructions="Write blog post", output_key="draft"),
        Agent(name="EditorAgent", instructions="Edit and polish", output_key="final")
    ]
)
```

**Key Components**:
- **OutlineAgent**: Creates structure and topics
- **WriterAgent**: Generates content based on outline
- **EditorAgent**: Refines and improves the draft

**Learning Focus**: State management, sequential dependencies, workflow continuity

### 2_ResearchSystem: Parallel Architecture

**Core Concept**: Concurrent execution with aggregation
```python
research_system = ParallelAgent(
    name="ResearchSystem",
    sub_agents=[
        Agent(name="TechResearcher", instructions="Research tech news"),
        Agent(name="HealthResearcher", instructions="Research health news"),
        Agent(name="FinanceResearcher", instructions="Research finance news")
    ],
    aggregator=Agent(name="Aggregator", instructions="Synthesize findings")
)
```

**Key Components**:
- **Specialized Researchers**: Domain-specific information gathering
- **Aggregator**: Combines and synthesizes results
- **Concurrent Processing**: Multiple agents work simultaneously

**Learning Focus**: Parallel processing, result aggregation, concurrent workflows

### 3_StoryPipeline: Loop Architecture

**Core Concept**: Iterative refinement with quality control
```python
story_pipeline = LoopAgent(
    name="StoryPipeline",
    sub_agents=[
        Agent(name="Writer", instructions="Write story draft", output_key="draft"),
        Agent(name="Critic", instructions="Critique the story", output_key="critique"),
        Agent(name="Refiner", instructions="Improve based on critique", output_key="refined")
    ],
    exit_condition=FunctionTool(exit_loop_function)
)
```

**Key Components**:
- **Writer**: Creates initial story draft
- **Critic**: Evaluates quality and provides feedback
- **Refiner**: Improves story based on criticism
- **Exit Logic**: Determines when quality threshold is met

**Learning Focus**: Quality control, iterative improvement, exit conditions

## 🛠️ Technical Implementation Details

### Agent Communication Patterns

**State Passing**:
```python
# Agents pass data via output_key
agent1 = Agent(..., output_key="step1_result")
agent2 = Agent(..., input_from=["step1_result"])
```

**Tool Integration**:
```python
# Custom tools for agent interaction
search_tool = AgentTool(agent=search_agent)
code_tool = AgentTool(agent=code_agent)
```

### Error Handling & Resilience

**Built-in Features**:
- Automatic retry logic for API failures
- Graceful degradation when tools unavailable
- Timeout handling for long-running operations
- Error recovery and fallback mechanisms

### Performance Optimization

**Architecture Selection Guide**:
- **Use Sequential**: When steps depend on previous results
- **Use Parallel**: When tasks are independent
- **Use Loop**: When quality improvement is needed
- **Use Hierarchical**: When complex task routing required

## 🎓 Advanced Topics

### Custom Agent Development
1. Define clear agent roles and responsibilities
2. Design appropriate communication patterns
3. Implement proper error handling
4. Test with various input scenarios

### Scaling Multi-Agent Systems
- **Modularity**: Build reusable agent components
- **Composition**: Combine agents for complex workflows
- **Monitoring**: Track agent performance and interactions
- **Optimization**: Balance complexity with performance

### Real-World Applications
- **Content Creation**: Blog writing, article generation
- **Research Automation**: Multi-domain information gathering
- **Quality Assurance**: Automated review and improvement
- **Task Automation**: Complex workflow orchestration

---

**Happy Learning!** 🎓 Explore each agent architecture to understand the power of multi-agent systems!
