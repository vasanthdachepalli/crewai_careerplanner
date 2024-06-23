# Import the necessary tool from crewai_tools
from crewai_tools import SerperDevTool

# Initialize SerperDevTool for use by agents
serper_tool = SerperDevTool()

# Import the predefined agents from the agents module
from agents import manager, goal_recommender, education_planner, fee_finder, writer, qualification_finder

# Function to get user feedback
def get_user_feedback(prompt):
    feedback = input(prompt)  # Prompt the user for feedback
    return feedback  # Return the user feedback

# Import the Task class from crewai
from crewai import Task

# Create a task for recommending career goals
recommend_goals_task = Task(
    description="Recommend career goals based on the user’s {interests} and confirm a goal with the user in feedback.",  # Task description
    expected_output='A selected career goal.',  # Expected output of the task
    tools=[serper_tool],  # Tools used by the task
    agent=goal_recommender,  # Agent responsible for the task
    human_input=True,  # Requires human input for feedback
)
# The recommend_goals_task involves recommending career goals to the user based on their interests.
# The Goal Recommender agent uses SerperDevTool to gather information and recommend suitable goals.
# The task requires user feedback to confirm the selected goal.

# Import custom tools
from tools import scrapespecial, file_search_tool

# Create a task for analyzing previous outputs and user feedback
analysistask = Task(
    description="Read the given file, learn the mistakes the agent did, what the changes user wants, provide the data to the next task.",  # Task description
    expected_output='Provide the previous outputs in txt file, feedbacks given in it to the next task.',  # Expected output of the task
    tools=[serper_tool, scrapespecial, file_search_tool],  # Tools used by the task
    human_input=False,  # Does not require human input
    async_execution=False,  # Execute synchronously
)
# The analysistask involves reading a file to analyze previous outputs and user feedback.
# It identifies mistakes made by agents and the changes requested by the user, then provides this data for subsequent tasks.
# The task uses multiple tools to gather and process the required information.

# Create a task for recommending education and universities
recommend_education_task = Task(
    description="Recommend the required education and universities in India based on the selected goal from the user's current education level ({current_education_level}), Confirm the university with the user., provide at least 10 universities.",  # Task description
    expected_output='A detailed recommendation of education and universities in India., choosed courses if choosed in feedback',  # Expected output of the task
    tools=[serper_tool, scrapespecial],  # Tools used by the task
    agent=education_planner,  # Agent responsible for the task
    context=[recommend_goals_task],  # Context from previous task
    human_input=True,  # Requires human input for feedback
    async_execution=False,  # Execute synchronously
)
# The recommend_education_task involves recommending appropriate educational paths and universities in India based on the selected career goal.
# The Education Planner agent uses SerperDevTool and a custom scraping tool to gather and provide recommendations.
# The task requires user feedback to confirm the selected universities and courses, if any.

# Create a task for finding tuition fees
find_fees_task = Task(
    description="Provide the tuition fee for the selected university in India and confirm any changes with the user.",  # Task description
    expected_output='Tuition fee for the selected university in India.',  # Expected output of the task
    tools=[serper_tool, scrapespecial],  # Tools used by the task
    context=[recommend_education_task],  # Context from previous task
    agent=fee_finder,  # Agent responsible for the task
    human_input=False,  # Does not require human input
    async_execution=False,  # Execute synchronously
)
# The find_fees_task involves providing the tuition fee for the selected university in India.
# The Fee Finder agent uses SerperDevTool and a custom scraping tool to gather and provide accurate tuition fee information.
# This task ensures the financial aspect of the selected educational path is clear to the user.

# Create a task for finding required qualifications
qualification_task = Task(
    description=(
        "Research and identify the required exams and qualifications needed to enter the selected university in India. "
        "Focus on providing detailed information about the entrance exams, minimum qualification criteria, and any other prerequisites."
    ),  # Task description
    expected_output=(
        "A comprehensive report detailing the required entrance exams, minimum qualification criteria, and any other prerequisites "
        "needed to enter the selected university. The report should be structured in clear, easy-to-understand language."
    ),  # Expected output of the task
    tools=[serper_tool, scrapespecial],  # Tools used by the task
    agent=qualification_finder,  # Agent responsible for the task
    async_execution=False,  # Execute synchronously
    context=[recommend_education_task],  # Context from previous task
)
# The qualification_task involves researching and identifying the necessary exams and qualifications for admission to the selected university.
# The Qualification Finder agent uses SerperDevTool and a custom scraping tool to gather and provide detailed and accurate information.
# This task ensures that the user understands the requirements for entering the chosen university.

# Create a task for compiling and formatting the final report
writer_task = Task(
    description="Compile and format the selected goal, university, courses if chosen, and its tuition fee, and the qualifications needed. The information will be provided by other agents.",  # Task description
    expected_output='A clear and structured presentation of the selected goal, university, and its tuition fee, qualifications needed.',  # Expected output of the task
    tools=[],  # No tools used by the task
    agent=writer,  # Agent responsible for the task
    context=[recommend_goals_task, recommend_education_task, find_fees_task, qualification_task],  # Context from previous tasks
    human_input=True,  # Requires human input for feedback
    output_file='final_report.md'  # Output file for the task
)
# The writer_task involves compiling and formatting the information provided by other agents into a clear and structured presentation.
# The Writer agent ensures the final report is well-organized and includes the selected goal, university, tuition fee, and required qualifications.
# This task requires user feedback to ensure the final report meets the user’s expectations.
