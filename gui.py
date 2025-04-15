import tkinter as tk
from voice_input import listen_command
from ai_engine import interpret_command
from task_executor import execute_task

def run_gui():
    root = tk.Tk()
    root.title("Voice AI Assistant")
    root.geometry("400x300")

    output = tk.StringVar()

    label = tk.Label(root, text="Say a command", font=("Arial", 14))
    label.pack(pady=10)

    response_label = tk.Label(root, textvariable=output, wraplength=350, font=("Arial", 10))
    response_label.pack(pady=10)

    def handle_voice():
        command = listen_command()
        if not command:
            output.set("Didn't catch that. Try again.")
            return
        response = interpret_command(command)
        output.set(f"You said: {command}\nAI: {response}")
        execute_task(response)

    btn = tk.Button(root, text="Listen", command=handle_voice, font=("Arial", 12))
    btn.pack(pady=20)

    root.mainloop()