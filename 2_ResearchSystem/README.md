# ResearchSystem - Parallel Agent Architecture

## Overview
A parallel multi-agent system that conducts concurrent research across multiple domains (Technology, Health, Finance) and aggregates findings into a comprehensive executive summary.

## Architecture Pattern
**Parallel Execution + Aggregation** - Independent research agents run simultaneously, followed by a sequential aggregation step.

```
User Request
    ↓
[TechResearcher || HealthResearcher || FinanceResearcher] (Parallel)
    ↓
AggregatorAgent
    ↓
Executive Summary
```

## Agents

### Parallel Research Team

#### 1. TechResearcher
- **Purpose**: Research latest AI/ML trends
- **Tools**: Google Search
- **Output**: `tech_research`
- **Focuses on**:
  - 3 key developments
  - Main companies involved
  - Potential impact

#### 2. HealthResearcher
- **Purpose**: Research medical breakthroughs
- **Tools**: Google Search
- **Output**: `health_research`
- **Focuses on**:
  - 3 significant advances
  - Practical applications
  - Estimated timelines

#### 3. FinanceResearcher
- **Purpose**: Research fintech trends
- **Tools**: Google Search
- **Output**: `finance_research`
- **Focuses on**:
  - 3 key trends
  - Market implications
  - Future outlook

### 4. AggregatorAgent
- **Purpose**: Synthesizes all research into executive summary
- **Inputs**: `{tech_research}`, `{health_research}`, `{finance_research}`
- **Output**: `executive_summary`
- **Highlights**: Common themes, surprising connections, key takeaways

## Usage

### Start the ADK Web Server
```bash
adk web
```

### Access the Web UI
Open http://127.0.0.1:8000 in your browser

### Example Prompts
- "Run the daily executive briefing on Tech, Health, and Finance"
- "What are the latest developments in AI, medical research, and fintech?"
- "Give me a comprehensive update on technology, healthcare, and finance trends"

## Key Features
- ✅ **Concurrent Execution**: All research agents run simultaneously for speed
- ✅ **Domain Expertise**: Each agent specializes in one area
- ✅ **Comprehensive Coverage**: Multi-domain research in parallel
- ✅ **Intelligent Synthesis**: Aggregator finds connections across domains
- ✅ **Google Search Integration**: Real-time information retrieval

## Performance Benefits
- **3x Faster**: Parallel execution vs sequential
- **Independent Tasks**: No dependencies between research agents
- **Scalable**: Easy to add more research domains

## When to Use Parallel Agents
- Tasks are independent of each other
- Speed matters
- You need concurrent execution
- Each agent specializes in a different domain

## Files
- `agent.py` - Main agent definitions
- `__init__.py` - Package initialization
- `.env` - Environment variables (API keys)
- `README.md` - This file
