# 🤖 AgentHub: Hierarchical Multi-Agent System

A sophisticated AI agent system built with Google ADK that intelligently delegates tasks to specialized sub-agents for web search and code execution.

## 🌟 Features

- **Hierarchical Architecture**: Root agent delegates tasks to specialized sub-agents
- **Web Search Capability**: Real-time information retrieval using Google Search
- **Code Execution**: Safe Python code execution for calculations and data analysis
- **Intelligent Delegation**: LLM-powered task routing based on request type
- **Modular Design**: Easy to extend with additional specialized agents

## 🏗️ Architecture

```
AgentHub (Root Agent - Manager)
├── 🔍 Search Agent (Web Search Specialist)
│   ├── Uses Google Search API
│   └── Handles information retrieval
└── 💻 Code Agent (Computation Specialist)
    ├── Executes Python code safely
    └── Performs calculations & analysis
```

### Agent Roles

- **Root Agent**: Task coordinator that analyzes requests and delegates to specialists
- **Search Agent**: Web search specialist using Google Search tools
- **Code Agent**: Code execution specialist for mathematical and analytical tasks

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Cloud Project with Gemini API access
- Google Search API key (optional, for enhanced search)

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
   Create a `.env` file in the project root:
   ```env
   # Google Cloud credentials
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_LOCATION=us-central1

   # Optional: Enhanced search capabilities
   GOOGLE_SEARCH_API_KEY=your-search-api-key
   GOOGLE_SEARCH_CX=your-custom-search-engine-id
   ```

### Running the Agent

1. **Start the ADK development server**
   ```bash
   adk web
   ```

2. **Access the web interface**
   Open http://127.0.0.1:8000 in your browser

## 💡 Usage Examples

### Web Search Queries
```
"What is the current population of Tokyo?"
"Who won the Nobel Prize in Physics this year?"
"What are the latest developments in AI?"
```

### Code Execution Tasks
```
"Calculate 25 * 17 + 42"
"What is the square root of 144?"
"Generate a list of prime numbers up to 100"
"Calculate the factorial of 10"
```

### Combined Tasks
```
"What's Tokyo's population and what percentage is that of Japan's total?"
"Find the current price of Bitcoin and calculate its market cap"
```

## 📁 Project Structure

```
agenthub/
├── agent.py              # Main agent definitions and architecture
├── __init__.py          # Package initialization
├── __pycache__/         # Python cache files
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## 🔧 Configuration

### Agent Customization

Edit `agent.py` to modify agent behavior:

```python
# Change model version
model="gemini-2.0-flash"  # or "gemini-1.5-pro"

# Modify instructions
instruction="Your custom agent behavior here..."

# Add new tools
tools=[google_search, your_custom_tool]
```

### Adding New Agents

1. Create a new agent in `agent.py`:
```python
new_agent = Agent(
    model="gemini-2.0-flash",
    name="new_specialist",
    description="Specialist in [domain]",
    instruction="How to handle [domain] tasks...",
    tools=[relevant_tools]
)
```

2. Add it to the root agent's tools:
```python
tools=[
    AgentTool(agent=search_agent),
    AgentTool(agent=code_agent),
    AgentTool(agent=new_agent)  # Add your new agent
]
```

## 🧪 Testing

### Manual Testing
Use the ADK web interface at http://127.0.0.1:8000 to interact with your agents.

### Programmatic Testing
```python
from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

# Create runner and test
session_service = InMemorySessionService()
runner = Runner(agent=root_agent, app_name="agenthub", session_service=session_service)

# Test queries
test_queries = [
    "What is 15 + 27?",
    "What is the capital of France?",
    "Calculate the area of a circle with radius 5"
]

for query in test_queries:
    # Run test and check results
    pass
```

## 🔒 Security & Safety

- **Sandboxed Code Execution**: Code runs in isolated environment
- **API Key Management**: Secure credential handling via environment variables
- **Input Validation**: LLM instructions prevent harmful operations
- **Rate Limiting**: Built-in protection against API abuse

## 📊 Performance

- **Response Time**: Typically 2-5 seconds for simple queries
- **API Costs**: Pay-per-use based on Gemini API usage
- **Scalability**: Can handle multiple concurrent users
- **Caching**: Implement result caching for frequently asked questions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comprehensive comments and docstrings
- Write tests for new functionality
- Update documentation for API changes

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Google ADK](https://google.github.io/adk-docs/)
- Powered by [Google Gemini](https://ai.google.dev/)
- Inspired by hierarchical agent architectures

## 🆘 Troubleshooting

### Common Issues

**"429 RESOURCE_EXHAUSTED" Error**
- You've hit API rate limits
- Wait a few minutes and try again
- Consider upgrading your Gemini API quota

**"Tool execution failed"**
- Check your environment variables
- Verify API keys are valid
- Ensure network connectivity

**"Agent not responding"**
- Check ADK server logs
- Verify model configuration
- Test with simpler queries first

### Getting Help

- Check the [ADK Documentation](https://google.github.io/adk-docs/)
- Review [Gemini API Documentation](https://ai.google.dev/docs)
- Open an issue on GitHub

---

**AgentHub**: Where specialized AI agents work together to solve complex problems! 