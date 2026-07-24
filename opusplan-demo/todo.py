#!/usr/bin/env python3
"""A small command-line to-do app: add tasks, list them, mark them done.

Tasks are stored in tasks.json next to this script.
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(SCRIPT_DIR, "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: could not read {TASKS_FILE} ({e}). Starting with an empty list.")
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    text = input("Task description: ").strip()
    if not text:
        print("Task text can't be empty. Nothing added.")
        return
    next_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": next_id, "text": text, "done": False})
    save_tasks(tasks)
    print(f"Added task {next_id}: {text}")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['text']}")


def mark_done(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    list_tasks(tasks)
    raw = input("Enter the id of the task to mark done: ").strip()
    if not raw.isdigit():
        print("Please enter a numeric id.")
        return
    task_id = int(raw)
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Marked task {task_id} done.")
            return
    print(f"No task found with id {task_id}.")


MENU = """
1) Add task
2) List tasks
3) Mark task done
4) Quit
"""


def main():
    tasks = load_tasks()
    print("To-do app. Tasks are saved to", TASKS_FILE)
    while True:
        print(MENU)
        try:
            choice = input("Choose an option (1-4): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
