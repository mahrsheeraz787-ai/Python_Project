import json
import os
Tasks_File = "tasks.json"
def load_tasks():
    if not os.path.exists(Tasks_File):
        return []
    try:
        with open(Tasks_File, "r") as f:
            return json.load(f)
    except(json.JSONDecodeError, ValueError):
         print("Warning: tasks file was empty or corrupted. Starting fresh.")
         return []
    def save_tasks(tasks):
        with open(Tasks_File, "w") as f:
            json.dump(tasks,f, indent=2)
    def add_tasks(tasks):
        task_text = input("Enter the new task: ").strip()
        if not task_text:
            print("Task cannot be empty. \n")
            return
        tasks.append({"task": task_text, "done": False})
        save_tasks(tasks)
        print(f'Added: "{task_text}"\n')
    def view_tasks(tasks):
        if not tasks:
            print("No tasks yet. Add one!\n")
            return
            print("\nYour Tasks:")