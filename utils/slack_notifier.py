import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_notification(tasks):
    client = WebClient(token=os.getenv("SLACK_TOKEN"))

    message = "New tasks added to Trello:\n" + "\n"+"Please Check it"
    
    try:
        response = client.chat_postMessage(
            channel=os.getenv("SLACK_CHANNEL_ID"),  # Ensure this is set to the tasks channel ID
            text=message
        )
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")
