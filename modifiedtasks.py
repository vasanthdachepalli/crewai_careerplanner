
#this file is exact copy of task.py ,with little change to prompts too work in a  different way
from crewai_tools import SerperDevTool,FileReadTool

serper_tool = SerperDevTool()

file_search_tool = FileReadTool(file_path='perviousdata.txt')
from agents import manager ,education_planner,fee_finder,writer,qualification_finder,analysiser

def get_user_feedback(prompt):
    feedback = input(prompt)
    return feedback

from crewai import Task



    
data_analysis_task = Task(
    description="Read the given file,and collect the all info pervious selected unviersty and goal and remaining data ",
    expected_output='provide the what goal selected to all other agents .',
    tools=[file_search_tool],
    agent=analysiser,
)
from tools import scrapespecial
recommend_education_task1 = Task(
    description="Recommend the required education and universities in India based on the selected goal from the user's current education level ({current_education_level}). Confirm the university with the user.,provide at least 10 unviersitys,didnot give the unviersity from the pervious data",
    expected_output='A detailed recommendation of education and universities in India.,choosed courses if choosed in feedback',
    tools=[serper_tool,scrapespecial],
    agent=education_planner,
    context=[data_analysis_task],
    human_input=True
)


find_fees_task1 = Task(
    description="Provide the tuition fee for the selected university in India and confirm any changes with the user.",
    expected_output=' tuition fee for the selected university in India.',
    tools=[serper_tool,scrapespecial],
    context= [recommend_education_task1],
    agent=fee_finder,
    human_input=False
)


qualification_task1 = Task(
    description=(
        "Research and identify the required exams and qualifications needed to enter the selected university in India. "
        "Focus on providing detailed information about the entrance exams, minimum qualification criteria, and any other prerequisites."
    ),
    expected_output=(
        "A comprehensive report detailing the required entrance exams, minimum qualification criteria, and any other prerequisites "
        "needed to enter the selected university. The report should be structured in clear, easy-to-understand language."
    ),
    tools=[serper_tool, scrapespecial],
    agent=qualification_finder,
    async_execution=False,
    context= [recommend_education_task1]
   
)

writer_task1= Task(
    description="Compile and format the selected goal, university ,courses if choosed, and its tuition fee,and the qualifications need. The information will be provided by other agents.",
    expected_output='A clear and structured presentation of the selected goal, university, and its tuition fee,qualifications need.',
    tools=[],
    agent=writer,
    context = [recommend_education_task1,find_fees_task1,qualification_task1],
    human_input=True,
    output_file='final_report.md'  
)
