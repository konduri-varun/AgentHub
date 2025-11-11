# BlogPipeline - Sequential Agent Architecture

## Overview
A sequential multi-agent system that creates blog posts through a three-stage pipeline: outline creation, writing, and editing.

## Architecture Pattern
**Sequential Execution** - Agents run in a fixed order, with each agent building on the output of the previous one.

```
User Input → OutlineAgent → WriterAgent → EditorAgent → Final Blog Post
```

## Agents

### 1. OutlineAgent
- **Purpose**: Creates a structured blog outline
- **Output**: `blog_outline`
- **Creates**:
  - Catchy headline
  - Introduction hook
  - 3-5 main sections with bullet points
  - Concluding thought

### 2. WriterAgent
- **Purpose**: Writes a complete blog post based on the outline
- **Input**: `{blog_outline}`
- **Output**: `blog_draft`
- **Produces**: 200-300 word blog post with engaging tone

### 3. EditorAgent
- **Purpose**: Polishes and refines the draft
- **Input**: `{blog_draft}`
- **Output**: `final_blog`
- **Improvements**: Grammar, flow, sentence structure, clarity

## Usage

### Start the ADK Web Server
```bash
adk web
```

### Access the Web UI
Open http://127.0.0.1:8000 in your browser

### Example Prompts
- "Write a blog post about the benefits of AI in healthcare"
- "Create a blog about sustainable living tips"
- "Write a blog post explaining quantum computing for beginners"

## Key Features
- ✅ **Deterministic Order**: Agents always run in the same sequence
- ✅ **State Management**: Each agent passes its output to the next via `output_key`
- ✅ **Quality Pipeline**: Multi-stage refinement ensures high-quality output

## When to Use Sequential Agents
- Order of operations matters
- Each step builds on the previous one
- You need a predictable, linear workflow
- Quality control through multiple stages

## Files
- `agent.py` - Main agent definitions
- `__init__.py` - Package initialization
- `.env` - Environment variables (API keys)
- `README.md` - This file
