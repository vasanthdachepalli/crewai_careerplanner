# Import necessary tools from crewai_tools and custom tools from the tools module
from crewai_tools import SerperDevTool, FileReadTool
from tools import scrapespecial

# Initialize SerperDevTool for use by agents
serper_tool = SerperDevTool()

# Import the Agent class from crewai
from crewai import Agent

# Create a Senior Manager agent
manager = Agent(
    role='Senior Manager',  # Role of the agent
    goal='Supervise and ensure tasks are completed according to instructions',  # Goal of the agent
    verbose=True,  # Enable verbose mode for detailed output
    memory=True,  # Enable memory to retain information across tasks
    backstory="With extensive experience in project management, you ensure that every task is completed efficiently and correctly.",  # Background story of the agent
    allow_delegation=True  # Allow this agent to delegate tasks to other agents
)
# The Senior Manager agent oversees all tasks, ensuring they are completed accurately and efficiently. 
# This agent has the ability to delegate tasks to other agents to optimize workflow.

# Create a Goal Recommender agent
goal_recommender = Agent(
    role='Goal Recommender',  # Role of the agent
    goal='Recommend career goals based on user’s current education level and interests',  # Goal of the agent
    verbose=True,  # Enable verbose mode for detailed output
    memory=True,  # Enable memory to retain information across tasks
    backstory="An expert in career counseling, you provide personalized goal recommendations.",  # Background story of the agent
    tools=[serper_tool],  # Assign SerperDevTool to this agent
    allow_delegation=False  # Do not allow this agent to delegate tasks
)
# The Goal Recommender agent uses the SerperDevTool to gather information and recommend career goals tailored 
# to the user’s education level and interests. This agent specializes in career counseling and does not delegate tasks.

# Initialize a FileReadTool for reading a specific file
file_search_tool1 = FileReadTool(file_path='perviousdata.txt')

# Create a File Reader agent
analysiser = Agent(
    role='File reader',  # Role of the agent
    goal='Read the given txt file, provide the data to all agents',  # Goal of the agent
    verbose=True,  # Enable verbose mode for detailed output
    memory=True,  # Enable memory to retain information across tasks
    backstory="An expert in analysis.",  # Background story of the agent
    tools=[file_search_tool1],  # Assign FileReadTool to this agent
    allow_delegation=False  # Do not allow this agent to delegate tasks
)
# The File Reader agent reads data from a specified text file using the FileReadTool. 
# It processes the data and makes it available to other agents for their respective tasks.

# Import the custom file search tool
from tools import file_search_tool

# Create another File Reader agent
analysist2 = Agent(
    role='file reader',  # Role of the agent
    goal='read the given file, provide the info of outputs it got before to next task',  # Goal of the agent
    memory=True,  # Enable memory to retain information across tasks
    backstory="An expert in analysis.",  # Background story of the agent
    tools=[file_search_tool],  # Assign custom file search tool to this agent
    allow_delegation=False  # Do not allow this agent to delegate tasks
)
# This second File Reader agent also reads data from a given file using a custom file search tool. 
# It focuses on providing previously obtained output data to subsequent tasks, ensuring continuity and coherence.

# Create an Education Planner agent
education_planner = Agent(
    role='Education Planner',  # Role of the agent
    goal='Recommend the required education and universities in India based on the selected goal',  # Goal of the agent
    verbose=True,  # Enable verbose mode for detailed output
    memory=True,  # Enable memory to retain information across tasks
    backstory="With extensive knowledge in educational planning, you provide detailed recommendations for required education and potential universities in India.",  # Background story of the agent
    tools=[serper_tool, scrapespecial],  # Assign SerperDevTool and a custom scraping tool to this agent
    allow_delegation=False  # Do not allow this agent to delegate tasks
)
# The Education Planner agent uses the SerperDevTool and a custom scraping tool to recommend appropriate educational paths 
# and universities in India based on the user’s selected career goal. This agent does not delegate tasks.

# Create a Fee Finder agent
fee_finder = Agent(
    role='Fee Finder',  # Role of the agent
    goal='Provide the tuition fee for the selected universities in India',  # Goal of the agent
    verbose=True,  # Enable verbose mode for detailed output
    memory=True,  # Enable memory to retain information across tasks
    backstory="An expert in university financials, you provide detailed and accurate tuition fee information for universities in India.",  # Background story of the agent
    tools=[serper_tool, scrapespecial],  # Assign SerperDevTool and a custom scraping tool to this agent
    allow_delegation=False  # Do not allow this agent to delegate tasks
)
# The Fee Finder agent uses the SerperDevTool and a custom scraping tool to gather and provide accurate tuition fee information 
# for selected universities in India. This agent focuses on financial details and does not delegate tasks.

# Create a Qualification Finder agent
qualification_finder = Agent(
    role='Qualification Finder',  # Role of the agent
    goal='Find the required exams and qualifications needed to enter the selected universities in India',  # Goal of the agent
    verbose=True,  # Enable verbose mode for detailed output
    memory=True,  # Enable memory to retain information across tasks
    backstory="An expert in university admissions, you provide detailed and accurate information about the exams and qualifications required to enter universities in India.",  # Background story of the agent
    tools=[serper_tool, scrapespecial],  # Assign SerperDevTool and a custom scraping tool to this agent
    allow_delegation=False  # Do not allow this agent to delegate tasks
)
# The Qualification Finder agent uses the SerperDevTool and a custom scraping tool to identify the necessary exams and qualifications 
# for admission into selected universities in India. This agent specializes in admissions requirements and does not delegate tasks.

# Create a Writer agent
writer = Agent(
    role='Writer',  # Role of the agent
    goal='Format and present the selected goal, university, and its tuition fee in a clear and structured manner.',  # Goal of the agent
    verbose=True,  # Enable verbose mode for detailed output
    memory=True,  # Enable memory to retain information across tasks
    backstory="An expert in formatting and presentation, you compile and format the information provided by other agents.",  # Background story of the agent
    tools=[],  # No tools assigned to this agent
    allow_delegation=False  # Do not allow this agent to delegate tasks
)
# The Writer agent compiles and formats the information gathered by other agents into a clear and structured presentation. 
# This agent focuses on the final presentation of data and does not delegate tasks.
