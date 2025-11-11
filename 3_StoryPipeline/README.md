# StoryPipeline - Loop Agent Architecture

## Overview
A loop-based multi-agent system that iteratively refines short stories through cycles of writing, critique, and revision until quality standards are met.

## Architecture Pattern
**Iterative Refinement Loop** - Initial draft followed by repeated critique-and-improve cycles.

```
User Prompt
    ↓
InitialWriterAgent (First Draft)
    ↓
    ┌─────────────────────┐
    │  Refinement Loop    │
    │  (max 2 iterations) │
    │                     │
    │  CriticAgent        │
    │       ↓             │
    │  RefinerAgent       │
    │  (Improve or Exit)  │
    └─────────────────────┘
    ↓
Final Story
```

## Agents

### 1. InitialWriterAgent
- **Purpose**: Creates the first draft of a short story
- **Output**: `current_story`
- **Specifications**: 100-150 words, story text only

### 2. CriticAgent (Loop)
- **Purpose**: Reviews and evaluates the story
- **Input**: `{current_story}`
- **Output**: `critique`
- **Evaluates**:
  - Plot quality
  - Character development
  - Pacing
- **Responses**:
  - "APPROVED" if story is complete
  - 2-3 specific improvement suggestions otherwise

### 3. RefinerAgent (Loop)
- **Purpose**: Improves story based on critique or exits loop
- **Inputs**: `{current_story}`, `{critique}`
- **Output**: `current_story` (updated)
- **Tools**: `exit_loop` function
- **Behavior**:
  - Calls `exit_loop()` if critique is "APPROVED"
  - Rewrites story incorporating feedback otherwise

## Loop Control

### Exit Condition
The loop terminates when:
1. CriticAgent returns "APPROVED" (RefinerAgent calls `exit_loop()`)
2. Maximum iterations (2) are reached

### Exit Function
```python
def exit_loop():
    """Signals loop termination when story is approved"""
    return {"status": "approved", "message": "Story approved. Exiting refinement loop."}
```

## Usage

### Start the ADK Web Server
```bash
adk web
```

### Access the Web UI
Open http://127.0.0.1:8000 in your browser

### Example Prompts
- "Write a short story about a lighthouse keeper who discovers a mysterious, glowing map"
- "Create a story about a robot learning to paint"
- "Write a tale about a time traveler stuck in a library"

## Key Features
- ✅ **Iterative Improvement**: Story gets better with each cycle
- ✅ **Quality Control**: Critic provides constructive feedback
- ✅ **Automatic Exit**: Loop stops when quality is achieved
- ✅ **Safety Limit**: Max iterations prevents infinite loops
- ✅ **State Persistence**: Story evolves through refinement cycles

## Loop Mechanics
1. **Initial Draft**: First version created
2. **Critique**: Story evaluated for quality
3. **Decision Point**: 
   - If approved → exit loop
   - If needs work → refine and repeat
4. **Refinement**: Story rewritten with improvements
5. **Repeat**: Back to critique (up to max iterations)

## When to Use Loop Agents
- Iterative improvement is needed
- Quality refinement matters
- Output needs multiple review cycles
- You want automated quality control

## Files
- `agent.py` - Main agent definitions
- `__init__.py` - Package initialization
- `.env` - Environment variables (API keys)
- `README.md` - This file
