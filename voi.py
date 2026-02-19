import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

# Task storage
tasks = []

def add_task(task):
    tasks.append(task)
    speak(f"Task '{task}' added.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        speak(f"Task '{task}' removed.")
    else:
        speak("Task not found.")

def list_tasks():
    if not tasks:
        speak("Your task list is empty.")
    else:
        speak("Your tasks are:")
        for i, task in enumerate(tasks, 1):
            speak(f"Task {i}: {task}")
   
def main():
    speak("Voice task manager started. Waiting for your command.")

    while True:
        command = listen()

        if "add task" in command:
            task = command.replace("add task", "").strip()
            if task:
                add_task(task)
            else:
                speak("Please say the task after add task.")

        elif "remove task" in command:
            task = command.replace("remove task", "").strip()
            if task:
                remove_task(task)
            else:
                speak("Please say the task after remove task.")

        elif "list tasks" in command:
            list_tasks()

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
