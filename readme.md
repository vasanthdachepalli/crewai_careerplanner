# CrewAI Project

This project leverages CrewAI to create and manage a team of AI agents that recommend career goals, education, universities, tuition fees, and qualifications, and compile this information into a structured report. The project also integrates user feedback to refine and repeat tasks as needed.

## Table of Contents

- [Setup](#setup)
- [Agents](#agents)
- [Tasks](#tasks)
- [Crews](#crews)
- [MongoDB Integration](#mongodb-integration)
- [User Interaction](#user-interaction)
- [Execution](#execution)

## Setup

### Environment Variables

First, set up the required API keys and model selection by initializing the following environment variables:

```python
import os

os.environ["SERPER_API_KEY"] = "your-serper-api-key"
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

Required Libraries
Ensure you have the required libraries installed:
pip install crewai crewai_tools pymongo

Agents
Importing and Initializing Agents
The project defines several agents, each with a specific role and goal. Here are the details of each agent:

Senior Manager: Supervises and ensures tasks are completed efficiently and correctly.
Goal Recommender: Recommends career goals based on user’s current education level and interests.
Education Planner: Recommends required education and universities in India based on the selected goal.
Fee Finder: Provides tuition fees for selected universities in India.
Qualification Finder: Identifies required exams and qualifications for university admissions.
Writer: Compiles and formats the selected goal, university, tuition fee, and qualifications into a clear presentation.
File Reader (Analysis): Reads and analyzes a given text file to provide data to other agents


Tasks
Defining Tasks
Each task is designed to achieve specific objectives and utilize relevant agents and tools.

Recommend Career Goals: Recommends career goals based on the user’s interests and confirms a goal with user feedback.

Read and Analyze File: Reads the given file, learns the mistakes the agent did, and what changes the user wants, then provides the data to the next task.

Recommend Education: Recommends the required education and universities in India based on the selected goal from the user's current education level.
Find Tuition Fees: Provides the tuition fee for the selected university in India and confirms any changes with the user.
Find Required Qualifications: Identifies the required exams and qualifications needed to enter the selected university in India.
Compile and Format Report: Compiles and formats the selected goal, university, courses, and its tuition fee, and the qualifications needed.


Crews
Creating and Initializing Crews
Two types of crews are defined: one for new users or users wanting to change all data, and another for existing users wanting to change specific data.

Crew for New or Changing All Data Users:

Agents: Goal Recommender, Education Planner, Fee Finder, Writer, Qualification Finder, Analysis
Process: Hierarchical
Manager: Senior Manager
Task Completion Callback: handle_task_completion
Crew for Existing Users:

Agents: Analysis, Education Planner, Fee Finder, Writer, Qualification Finder
Process: Hierarchical
Manager: Senior Manager
Task Completion Callback: handle_task_completion1



Additional Instructions:

here we are using perviousdata.txt file like a memory to stroe,the data of pervious iterations ,for a existing user

task_repeation.md,acts like a stroage when we need to repeat only one task
#   c r e w a i _ c a r e e r p l a n n e r  
 