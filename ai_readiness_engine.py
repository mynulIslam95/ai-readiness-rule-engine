"""
Generative AI & Agentic AI Access Decision Engine

Use Case:
This project demonstrates conditional decision logic by evaluating a learner’s
readiness to start working with Generative AI, Agentic AI and multi-agent systems.
The program analyzes core prerequisites such as Python skills, API knowledge,
prompt engineering ability, ML fundamentals and project experience.

Based on these inputs, the system classifies the learner into one of four levels:
Agentic AI Ready, Generative AI Ready, Foundation Level or Beginner Level.
A follow-up recommendation suggests the next logical learning direction.
"""

print("=== Generative AI & Agentic AI Access Decision Engine ===")

name = input("Enter your name: ")

python_skill = int(input("Python skill (1-10): "))
api_skill = int(input("API knowledge (1-10): "))
prompt_skill = int(input("Prompt engineering skill (1-10): "))
ml_basics = input("Do you understand ML basics? (yes/no): ").lower()
projects = input("Have you built any coding projects? (yes/no): ").lower()
math_interest = input("Interested in AI math concepts? (yes/no): ").lower()

# Decision logic using conditional statements

if python_skill >= 8 and api_skill >= 7 and prompt_skill >= 7 and ml_basics == "yes" and projects == "yes":
    level = "Agentic AI Ready"
    message = "You are ready to build AI agents, tool-calling systems and autonomous workflows."

elif python_skill >= 6 and api_skill >= 5 and prompt_skill >= 6 and ml_basics == "yes":
    level = "Generative AI Ready"
    message = "You can start building GenAI apps such as chatbots, RAG systems and AI assistants."

elif python_skill >= 4 and prompt_skill >= 4:
    level = "Foundation Level"
    message = "You should strengthen Python, APIs and ML basics before building GenAI systems."

else:
    level = "Beginner Level"
    message = "Focus on Python fundamentals, coding practice and understanding AI basics first."

# Nested condition example
if level == "Agentic AI Ready":
    if math_interest == "yes":
        recommendation = "Recommended: Start building multi-agent systems, LLM orchestration and advanced AI workflows."
    else:
        recommendation = "Recommended: Focus on practical AI applications and automation tools."
else:
    recommendation = "Recommended: Improve Python and API skills through small projects."

print("\n=== AI Learning Decision Report ===")
print("Name:", name)
print("Access Level:", level)
print("Explanation:", message)
print("Next Step:", recommendation)