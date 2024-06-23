import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


# Set the API keys and model selection as environment variables

os.environ["SERPER_API_KEY"] = os.getenv('SERPER')
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI')
os.environ["OPENAI_MODEL_NAME"]=os.getenv('MODEL')
# Import the predefined tasks
from tasks import recommend_goals_task, find_fees_task, recommend_education_task, writer_task, qualification_task, analysistask

# Create a list of tasks to be executed
task1 = [recommend_goals_task, recommend_education_task, find_fees_task, qualification_task, writer_task]

# Function to handle task completion and optionally repeat tasks based on user feedback
def handle_task_completion(task):
    b = ''
    des = ''
    a = 0  # Initialize the counter variable

    for i in task:
        for j in i:
            a = a + 1
            if a == 6:
                b = j
            if a == 2:
                des = j
    
    # Check if the task description matches the special task that should not be repeated
    if des == 'Provide the tuition fee for the selected university in India and confirm any changes with the user.':
        return

    feedback = input('Do you want the task to be repeated? Say yes if you want to repeat, enter anything to skip: ')

    if feedback != 'yes':
        with open('task_repeation.md', 'w') as file:
            content = file.write('no data')
        return

    with open('task_repeation.md', 'r') as file:
        context = file.read()

    if context == 'no data':
        with open('task_repeation.md', 'w') as file:
            content = file.write('')

    for i in range(len(crew.tasks)):
        cc = 0
        for j in crew.tasks[i]:
            for c in j:
                if c == des:
                    cc = 1
            if cc == 1:
                break
        if cc == 1:
            crew.tasks.insert(i, crew.tasks[i])
            crew.tasks.insert(i + 1, analysistask)
            break

    with open('task_repeation.md', 'a') as file:
        context = file.write('The output you got before:\n' + b)

    message = input('What is the feedback (what you want to change from the previous output)?\n')
    with open('task_repeation.md', 'a') as file:
        context = file.write('\nFeedback on previous output: ' + message + '\n')

# Explanation:
# The handle_task_completion function checks if a task needs to be repeated based on user feedback.
# It reads and updates a markdown file to track task repetitions and user feedback.
# If the user wants to repeat a task, it adds the task and the analysistask to the task list.

# Duplicate function for handling a different set of tasks
def handle_task_completion1(task):
    b = ''
    des = ''
    a = 0  # Initialize the counter variable

    for i in task:
        for j in i:
            a = a + 1
            if a == 6:
                b = j
            if a == 2:
                des = j
    
    # Check if the task description matches the special task that should not be repeated
    if des == 'Provide the tuition fee for the selected university in India and confirm any changes with the user.':
        return

    feedback = input('Do you want the task to be repeated? Say yes if you want to repeat, enter anything to skip: ')

    if feedback != 'yes':
        with open('task_repeation.md', 'w') as file:
            content = file.write('no data')
        return

    with open('task_repeation.md', 'r') as file:
        context = file.read()

    if context == 'no data':
        with open('task_repeation.md', 'w') as file:
            content = file.write('')

    for i in range(len(crew2.tasks)):
        cc = 0
        for j in crew2.tasks[i]:
            for c in j:
                if c == des:
                    cc = 1
            if cc == 1:
                break
        if cc == 1:
            crew2.tasks.insert(i, crew2.tasks[i])
            crew2.tasks.insert(i + 1, analysistask)
            break

    with open('task_repeation.md', 'a') as file:
        context = file.write('The output you got before:\n' + b)

    message = input('What is the feedback (what you want to change from the previous output)?\n')
    with open('task_repeation.md', 'a') as file:
        context = file.write('\nFeedback on previous output: ' + message + '\n')

# Explanation:
# The handle_task_completion1 function is similar to handle_task_completion but is used for a different set of tasks.
# It follows the same logic to determine if a task needs to be repeated and tracks user feedback.

# Import necessary classes and agents from crewai and agents modules
from crewai import Crew, Process
from agents import manager, goal_recommender, education_planner, fee_finder, writer, qualification_finder, analysiser, analysist2

# Initialize the first crew with a set of agents and tasks for new or existing users who want to change all data
crew = Crew(
    agents=[goal_recommender, education_planner, fee_finder, writer, qualification_finder, analysist2],
    tasks=task1,
    process=Process.hierarchical,  # Use hierarchical process for task execution
    manager_agent=manager,  # Set the manager agent
    task_callback=handle_task_completion  # Set the task completion handler
)

# Explanation:
# This crew configuration is for new users or existing users who want to change all their data.
# The crew includes agents for goal recommendation, education planning, fee finding, writing, and qualification finding.
# Tasks are executed in a hierarchical process, managed by the manager agent, with handle_task_completion handling task completion.

# Import modified tasks for existing users
from modifiedtasks import recommend_education_task1, find_fees_task1, qualification_task1, writer_task1, data_analysis_task

# Initialize the second crew with a different set of agents and tasks for already existing users
crew2 = Crew(
    agents=[analysiser, education_planner, fee_finder, writer, qualification_finder],
    tasks=[data_analysis_task, recommend_education_task1, find_fees_task1, qualification_task1, writer_task1],
    process=Process.hierarchical,  # Use hierarchical process for task execution
    manager_agent=manager,  # Set the manager agent
    task_callback=handle_task_completion1  # Set the task completion handler
)

# Explanation:
# This crew configuration is for existing users who want to change specific data.
# The crew includes agents for data analysis, education planning, fee finding, writing, and qualification finding.
# Tasks are executed in a hierarchical process, managed by the manager agent, with handle_task_completion1 handling task completion.

# Import MongoDB client from pymongo
from pymongo import MongoClient

# Function to check if a user name exists in the database
def check_name_exists(name):
    query = {'name': name}  # Query to find the user by name
    result = collection.find_one(query)  # Execute the query
    return result is not None  # Return True if the user exists, else False

# Initialize MongoDB client and select the database and collection
client = MongoClient('mongodb://localhost:27017/')
db = client['users_crewai'] 
collection = db['userdata']

# Create a unique index on the 'name' field to ensure no duplicate user names
collection.create_index([('name', 1)], unique=True)

# Explanation:
# The check_name_exists function queries the MongoDB collection to check if a user name already exists.
# MongoDB client is initialized and connected to the 'users_crewai' database and 'userdata' collection.
# A unique index is created on the 'name' field to prevent duplicate user names.

# Prompt the user to check if they are an existing user
usertype = input('Are you an existing user? If yes, write your username, if no, type no: ')

# If the user is not an existing user or chooses to start as a new user
if not check_name_exists(usertype) or usertype == 'no':
    interests = input('Enter your interest: ')
    education_level = input('Enter your current education level (e.g., high school, bachelors, masters): ')
    budget = input('Enter your annual budget: ')
    result = crew.kickoff(inputs={'current_education_level': education_level, 'interests': interests, 'budget': budget})

    print(result)

    a = 1
    name = input('Enter the username you like: ')
    while a == 1:
        if check_name_exists(name):
            name = input('The name already exists, try a new name or attach some numbers to your name: ')
        else:
            with open('final_report.md', 'r') as file:
                content = file.read()
                document = {
                    'name': name,
                    'data': content,
                    'interest': interests,
                    'current_education_level': education_level,
                    'budget': budget
                }
                result = collection.insert_one(document)
                print("Your data is successfully stored in our database.")
                a = 0

# Explanation:
# If the user is new or chooses to start afresh, they are prompted to enter their interests, education level, and budget.
# The crew.kickoff method is called with the user's inputs to start the task execution.
# The user's name is checked for uniqueness before storing their data in the MongoDB collection.

# If the user is an existing user
else:
    typee = input('Enter 1 if you want to change the goal itself (all things will be changed in this option), enter 2 if you want to change the university only: ')
    if typee == '1':
        interests = input('Enter your interest: ')
        education_level = input('Enter your current education level (e.g., high school, bachelors, masters): ')
        budget = input('Enter your annual budget: ')
        result = crew.kickoff(inputs={'current_education_level': education_level, 'interests': interests, 'budget': budget})
        with open('final_report.md', 'r') as file:
            content = file.read()
            query = {'name': usertype}
            update = {
                '$set': {
                    'data': content,
                    'interest': interests,
                    'current_education_level': education_level,
                    'budget': budget
                }
            }
            result = collection.update_one(query, update)
    else:
        datas = collection.find({'name': usertype})
        with open('perviousdata.txt', 'w') as file:
            content = file.write(datas[0]['data'])
        education_level = input('Enter your current education level (e.g., high school, bachelors, masters): ')
        budget = input('Enter your annual budget: ')
        result = crew2.kickoff(inputs={'current_education_level': education_level, 'budget': budget})
        with open('final_report.md', 'r') as file:
            content = file.read()
            query = {'name': usertype}
            update = {
                '$set': {
                    'data': content,
                    'current_education_level': education_level,
                    'budget': budget
                }
            }
            result = collection.update_one(query, update)

# Explanation:
# If the user is an existing user, they can choose to change their goal or university.
# If the user chooses to change their goal, they are prompted for new inputs, and the crew.kickoff method is called.
# The user's data is updated in the MongoDB collection.
# If the user chooses to change their university, the existing data is loaded, and the crew2.kickoff method is called with new inputs.
