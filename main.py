import os
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from utils.trello_task import add_tasks_to_trello
from utils.slack_notifier import send_slack_notification

# Load environment variables
load_dotenv()

# Hugging Face API key setup
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Function to load meeting notes
def load_meeting_notes(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to generate tasks from meeting transcript
def generate_tasks(meeting_transcript):
    # Define the question
    question = "Extract actionable tasks from this meeting: " + meeting_transcript
    
    # Define the prompt template
    template = """Question: {question} Answer: Let's think step by step. Give the brief answer in 3-4 words. Also remember to only give the lists nothing more than that."""

    prompt = PromptTemplate.from_template(template)
    
    # Set up Hugging Face endpoint with the model repo
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    )
    
    # Create LLMChain and invoke it with the meeting notes as input
    llm_chain = prompt | llm
    response = llm_chain.invoke({"question": question})
    
    return response

def main():
    # Step 1: Load meeting notes
    meeting_notes = load_meeting_notes("meeting-notes.txt")

    # Step 2: Generate tasks from meeting transcript
    tasks = generate_tasks(meeting_notes)

    print(tasks)
    
    add_tasks_to_trello(tasks)

    send_slack_notification(tasks)

if __name__ == "__main__":
    main()
