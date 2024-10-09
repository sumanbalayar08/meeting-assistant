# Meeting Assistant

## Overview

The Meeting Assistant automates the extraction of actionable tasks from meeting notes and integrates with Trello and Slack for task management and notifications.

## Features

- Extracts tasks from meeting transcripts using Hugging Face models.
- Adds tasks to a specified Trello board and list.
- Sends notifications to a designated Slack channel.

## Prerequisites

- Python 3.x
- Environment variables for Trello and Slack API keys, and Hugging Face token.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>

2. Create Virtual Environment
   ```bash
   python3 -m venv env
   source env/bin/activate

3. Install the Dependencies
   ```bash
   pip install -r requirements.txt

4. Run the Program
   ```bash
   python3 main.py   