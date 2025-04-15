import ollama
from task_executor import execute_task

def interpret_command(command):
    command = command.lower()

    # Check for simple executable tasks first
    task_response = execute_task(command)
    if task_response != "Command not recognized":
        return task_response

    # Otherwise, query the local AI model for an answer
    try:
        response = ollama.chat(model="tinyllama", messages=[
            {"role": "user", "content": command}
        ])
        return response["message"]["content"]
    except Exception as e:
        return f"An error occurred: {str(e)}"