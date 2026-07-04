import json
import os
from datetime import datetime

STORAGE_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        with open(STORAGE_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("\n[!] Error reading data file. Starting with an empty list.")
        return []

def save_tasks(tasks):
    try:
        with open(STORAGE_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"\n[!] Critical Error saving data: {e}")

def add_task(title):
    if not title.strip():
        print("\n[!] Task title cannot be empty.")
        return
        
    tasks = load_tasks()
    next_id = max([task["id"] for task in tasks], default=0) + 1
    
    new_task = {
        "id": next_id,
        "title": title.strip(),
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\n[+] Success: Task '{title}' added successfully (ID: {next_id}).")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\n--- No tasks found. Your queue is clear! ---")
        return

    print("\n" + "=" * 45)
    print(f"{'ID':<5} {'Status':<8} {'Task Description':<20}")
    print("=" * 45)
    
    for task in tasks:
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{task['id']:<5} {status:<8} {task['title']:<20}")
    print("=" * 45)

def mark_completed(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print(f"\n[-] Task {task_id} is already marked as completed.")
                return
            task["completed"] = True
            save_tasks(tasks)
            print(f"\n[X] Success: Task {task_id} marked as completed.")
            return
    print(f"\n[!] Error: Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    initial_length = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(tasks) < initial_length:
        save_tasks(tasks)
        print(f"\n[-] Success: Task {task_id} has been removed.")
    else:
        print(f"\n[!] Error: Task with ID {task_id} not found.")

def main():
    while True:
        print("\n::: TO-DO ENGINE PROTOCOL :::")
        print("1. View Current Tasks")
        print("2. Add New Task")
        print("3. Complete Task (By ID)")
        print("4. Delete Task (By ID)")
        print("5. Exit Application")
        
        choice = input("\nEnter operation index (1-5): ").strip()
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            title = input("Enter task description: ")
            add_task(title)
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                mark_completed(task_id)
            except ValueError:
                print("\n[!] Input Error: Please enter a valid numerical ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to purge: "))
                delete_task(task_id)
            except ValueError:
                print("\n[!] Input Error: Please enter a valid numerical ID.")
        elif choice == "5":
            print("\nShutting down To-Do Engine. Progress saved.")
            break
        else:
            print("\n[!] Invalid Selection. Pick an option between 1 and 5.")

if __name__ == "__main__":
    main()
