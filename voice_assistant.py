import requests
import speech_recognition as sr
import pyttsx3

# 1. Define the Actions (Functions to be triggered by the commands)
def open_browser():
    print("Opening browser...")  # Replace with actual implementation

def play_music():
    print("Playing music...")

def shutdown_computer():
    print("Shutting down...")

def tell_joke():
    print("Why don't scientists trust atoms? Because they make up everything.")

# 2. Initialize Text-to-Speech Engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 3. Interpret the Command using Ollama
def interpret_command(command_text):
    prompt = f"""
You are a helpful AI voice assistant. Your job is to interpret a user's spoken command and convert it to a known action keyword.

The user said: "{command_text}"

Respond with one of these exact keywords:
- open_browser
- play_music
- shutdown_computer
- tell_joke

If you are unsure, respond with: unknown_command
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return response.json()["response"].strip().lower()

# 4. Handle the Command and Execute the Appropriate Function
def handle_command(command_text):
    action = interpret_command(command_text)
    print(f"AI interpreted action: {action}")

    actions = {
        "open_browser": open_browser,
        "play_music": play_music,
        "shutdown_computer": shutdown_computer,
        "tell_joke": tell_joke
    }

    if action in actions:
        actions[action]()
        speak(f"Executing {action}")
    else:
        print("Sorry, I didn't understand that command.")
        speak("Sorry, I didn't understand that command.")

# 5. Listen to the User's Voice Command
def listen_to_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        handle_command(command)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        speak("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech service; {e}")
        speak("Sorry, there was an error with the speech service.")

# Main loop to keep listening for commands
if __name__ == "__main__":
    while True:
        listen_to_command()