from pathlib import Path

ROOT = Path(__file__).resolve().parent

ROADMAP = '''# AI Agent Engineering — Master Roadmap

**Duration:** 16 weeks | **Study time:** 20 hours/week (320 hours)

**Goal:** Build, evaluate, deploy and document reliable AI agent systems and develop a job-ready portfolio. This roadmap is the stable reference; troubleshooting and side questions do not change the sequence. Change it only by explicit decision.

## Weekly learning rhythm
- Concepts and architecture: 4 hours
- Guided implementation: 4 hours
- Independent exercises: 4 hours
- Project work: 4 hours
- Testing, review and documentation: 4 hours

## Weekly syllabus and deliverables

| Week | Topic | Practical deliverable |
|---|---|---|
| 01 | Python Software Engineering: modules, packages, OOP, type hints, exceptions, venv, Git, HTTP/REST, intro to async | Modular SimpleAgent with calculator tools, help, history, basic tests and documentation |
| 02 | LLM foundations: tokens, context, prompting, structured outputs | Small structured-output LLM application |
| 03 | Function calling, tool use and agent loop | Tool-using agent with validation and error handling |
| 04 | Memory, embeddings and RAG | Retrieval pipeline with a small document collection |
| 05 | OpenAI Agents SDK | Intelligent Research Agent (Project 1) |
| 06 | Multi-agent architecture | Design and prototype collaborating agents |
| 07 | LangGraph: state, workflows and checkpointing | Stateful multi-step agent workflow |
| 08 | MCP, evaluation and human-in-the-loop | Tool integration and evaluation harness |
| 09 | FastAPI and backend engineering | HTTP API for an agent service |
| 10 | PostgreSQL, vector search and persistent memory | Persistent agent data and retrieval |
| 11 | Docker, deployment and CI/CD | Containerized service with basic automation |
| 12 | Security, testing and observability | Tested, observable Multi-Agent Software Engineering Assistant (Project 2) |
| 13 | Final project architecture and requirements | Industrial AI Monitoring Agent design and acceptance criteria |
| 14 | Core implementation and agent integration | Working industrial monitoring agent prototype |
| 15 | Testing, optimization and deployment | Evaluated and deployed final project |
| 16 | Documentation, GitHub portfolio and interview preparation | Public portfolio, project walkthroughs and interview preparation |

## Portfolio projects
1. **Intelligent Research Agent** — Weeks 3–5.
2. **Multi-Agent Software Engineering Assistant** — Weeks 6–12.
3. **Industrial AI Monitoring Agent** — Weeks 13–16; use simulated sensor data, diagnostics and human approval for sensitive actions.

## Learning rules
- Teach concepts, implement small increments, assign exercises, then review code.
- Troubleshooting does not skip or reorder the syllabus.
- Track actual progress in `PROGRESS.md` (not here).
- Prefer Python, OpenAI SDK, LangGraph, MCP, FastAPI, PostgreSQL, Docker, Git and pytest; use other frameworks only when justified.
- Reassess schedule if needed, but preserve the master plan unless explicitly changed.
'''

PROGRESS = '''# AI Agent Engineering — Progress Tracker

**Last reviewed:** 2026-10-27  
**Current position:** Week 01 — Lesson 1, final practice  
**Next action:** Implement and review calculation history, then continue to Week 01 Lesson 2 (OOP).

## Status legend
- [x] Completed and verified
- [ ] Not yet completed or not yet verified

## Week 01 — Python Software Engineering

### Lesson 1: Modules, packages and tool registry
- [x] Create the `week-01-python-engineering/simple_agent` project structure.
- [x] Implement `main.py`, `core/agent.py`, and `tools/calculator.py`.
- [x] Add calculator tools including `power`.
- [x] Implement tool descriptions / `help` command.
- [x] Run the agent and resolve the `None` output issue.
- [x] Initialize Git and push commits to GitHub.
- [ ] Implement `history` for successful calculations.
- [ ] Review history implementation and edge cases.

### Remaining Week 01 topics
- [ ] Lesson 2: OOP and professional agent class design.
- [ ] Type hints and exception design.
- [ ] Virtual environments, dependencies and secrets.
- [ ] REST/HTTP and introductory async.
- [ ] Basic testing, documentation and Week 01 review.

## Weeks 02–16
- [ ] Week 02 — LLM foundations
- [ ] Week 03 — Tool calling and agent loop
- [ ] Week 04 — Memory, embeddings and RAG
- [ ] Week 05 — OpenAI Agents SDK
- [ ] Week 06 — Multi-agent architecture
- [ ] Week 07 — LangGraph
- [ ] Week 08 — MCP and evaluation
- [ ] Week 09 — FastAPI
- [ ] Week 10 — PostgreSQL and vector search
- [ ] Week 11 — Docker and deployment
- [ ] Week 12 — Security, testing and observability
- [ ] Week 13 — Final project design
- [ ] Week 14 — Final project implementation
- [ ] Week 15 — Final project evaluation and deployment
- [ ] Week 16 — Portfolio and interview preparation

## Session handoff
**Resume instruction:** Continue from the first unchecked task in Week 01. Do not change the sequence in `ROADMAP.md` for debugging or side discussions.

**When finishing a session:** Update the completed checkboxes, the current position, the next action and the review date; commit `PROGRESS.md` to GitHub.
'''

for name, content in [('ROADMAP.md', ROADMAP), ('PROGRESS.md', PROGRESS)]:
    path = ROOT / name
    try:
        with path.open('x', encoding='utf-8') as f:
            f.write(content)
        print(f'Created: {path}')
    except FileExistsError:
        print(f'Skipped (already exists): {path}')
