import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def add_tasks_to_trello(tasks):
    TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
    TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')
    TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')

    # URL for creating a new list
    url = "https://api.trello.com/1/lists"

    tasks_to_add = get_tasks_from_input(tasks)

    for task in tasks_to_add:
        # Define the new card details
        query = {
            'name': task,
            'idBoard': TRELLO_BOARD_ID,
            'key': TRELLO_API_KEY,
            'token': TRELLO_TOKEN
        }

        # Send POST request to create a new card
        response = requests.post(url, params=query)

        # Check the response
        if response.status_code == 200:
            print(f"Task '{task}' added successfully!")
            print(json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": ")))
        else:
            print(f"Failed to add task '{task}': {response.text}")

def get_tasks_from_input(task_input):

    formatted_tasks = [task.strip() for task in task_input.strip().split('\n') if task.strip()]
    return formatted_tasks
