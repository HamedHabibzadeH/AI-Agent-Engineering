# AI Agent Engineering — 16-Week Learning Journey

**A structured, hands-on, and project-based journey toward AI Agent Engineering.**

[GitHub Repository](https://github.com/HamedHabibzadeH/AI-Agent-Engineering)

## About the Project

This repository documents an experimental 16-week learning program focused on AI Agent Engineering.

The goal is to develop a systematic learning path that combines theoretical foundations, software engineering principles, and practical AI agent development.

Rather than relying on disconnected tutorials, this program follows a progressive roadmap where each stage builds on the previous one.

The project is currently in its **experimental and development phase**. I am implementing the exercises, evaluating the learning sequence, documenting challenges, and improving the material throughout the journey.

The long-term objective is to transform this experience into a comprehensive, well-organized educational resource that other learners and developers can use.

## Learning Approach

The program follows five principles:

1. **Fundamentals first:** Understand the concepts before relying on frameworks.
2. **Learning by building:** Apply concepts through practical programming exercises.
3. **Software engineering practices:** Emphasize modularity, maintainability, testing, and version control.
4. **Progressive complexity:** Move from simple Python agents toward more advanced AI systems.
5. **Continuous improvement:** Document progress, identify weaknesses, and refine the curriculum.

**Planned duration:** 16 weeks  
**Estimated commitment:** 20 hours per week  
**Total planned effort:** Approximately 320 hours

## 16-Week Roadmap

| Week | Main Focus                                     |
| ---- | ---------------------------------------------- |
| 01   | Python Software Engineering, OOP, Git, Testing |
| 02   | LLM Fundamentals and Prompt Engineering        |
| 03   | Tool Calling and Agent Loops                   |
| 04   | RAG, Embeddings, and Memory                    |
| 05   | OpenAI Agents SDK                              |
| 06   | Multi-Agent Systems                            |
| 07   | LangGraph                                      |
| 08   | MCP, Evaluation, and Human-in-the-Loop         |
| 09   | FastAPI and Backend Development                |
| 10   | PostgreSQL and Vector Search                   |
| 11   | Docker, Deployment, and CI/CD                  |
| 12   | Security, Testing, and Observability           |
| 13   | Capstone Project: Planning and Architecture    |
| 14   | Capstone Project: Implementation               |
| 15   | Capstone Project: Evaluation and Refinement    |
| 16   | Capstone Project: Deployment and Portfolio     |

For the detailed learning plan, see [ROADMAP.md](ROADMAP.md).

## Current Progress

**Current phase:** Week 01 — Python Software Engineering

### Completed

- [x] Created the initial project structure
- [x] Developed a modular Python SimpleAgent
- [x] Implemented calculator tools
- [x] Applied object-oriented programming concepts
- [x] Implemented inheritance and polymorphism
- [x] Introduced a shared BaseTool interface
- [x] Implemented Dependency Injection and a Tool Registry
- [x] Added tool descriptions and operation history
- [x] Verified independent agent histories

### Upcoming

- [ ] Python Type Hints
- [ ] Structured unit testing with pytest
- [ ] Additional software engineering improvements
- [ ] Introduction to LLM fundamentals

For ongoing updates, see [PROGRESS.md](PROGRESS.md).

## First Practical Project: SimpleAgent

The first project is a lightweight Python agent designed to demonstrate fundamental software engineering concepts.

### Features

- Modular Python architecture
- Class-based tools
- Dynamic tool registration
- Basic mathematical operations
- Tool descriptions
- Error handling
- Execution history
- Independent agent state

This is a **rule-based educational agent**, not yet an LLM-powered autonomous agent. LLM integration and more advanced agent capabilities are planned for later stages.

### Project Structure

```text
AI-Agent-Engineering/
├── README.md
├── ROADMAP.md
├── PROGRESS.md
└── week-01-python-engineering/
    └── simple_agent/
        ├── main.py
        ├── core/
        │   ├── __init__.py
        │   └── agent.py
        └── tools/
            ├── __init__.py
            ├── base_tool.py
            └── calculator.py
```

### Running the Project

Clone the repository:

```bash
git clone https://github.com/HamedHabibzadeH/AI-Agent-Engineering.git
cd AI-Agent-Engineering/week-01-python-engineering/simple_agent
```

Run the interactive agent:

```bash
python main.py
```

The project currently uses Python's standard library for its core functionality.

## Long-Term Vision

By the end of this experimental journey, the aim is to create:

- A structured AI Agent Engineering curriculum
- Practical exercises and documented examples
- Reusable project templates
- A progressively developed portfolio
- A comprehensive capstone project
- Learning materials that can help other developers follow a similar path

The curriculum and repository will evolve based on practical implementation, testing, and feedback.

## Follow the Journey

I plan to share development milestones, technical lessons, project updates, and challenges on LinkedIn.

Feedback, suggestions, and constructive technical discussions are welcome.

**GitHub:** https://github.com/HamedHabibzadeH

---

**Project status:** Experimental / Work in Progress

**Maintained by:** Hamed Habibzadeh

_Learn. Build. Test. Improve. Share._
