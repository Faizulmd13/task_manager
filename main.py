import argparse
import json
from pathlib import Path
import task_ops
import storage


parser = argparse.ArgumentParser(description="CLI Task Manager")

subparsers = parser.add_subparsers(dest="command", help="Available commands")

add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("title", help="Title of the task")
add_parser.add_argument("--due", help="Add a due date to the task")
add_parser.add_argument("--priority", help="Set task priority")

list_parser = subparsers.add_parser("list", help="List tasks")
list_parser.add_argument("--completed", action="store_true", help="Show only completed tasks")

done_parser = subparsers.add_parser("done", help="Mark task as done")
done_parser.add_argument("task_id", type=int, help="ID of the task to mark as done")

delete_parser = subparsers.add_parser("delete", help="Delete the task")
delete_parser.add_argument("task_id", type=int, help="ID of the task to be deleted")

args = parser.parse_args()

if not args.command:
    parser.print_help()
    exit()

file_path = Path("tasks.json")

tasks = storage.load_tasks(file_path)

if args.command == "add":
    tasks = task_ops.add_task(tasks, args.title, args.due, args.priority)
    storage.save_tasks(tasks, file_path)
    print("Task added: ", args.title)
elif args.command == "list":
    task_ops.list_tasks(tasks, args.completed)
elif args.command == "done":
    tasks = task_ops.mark_done(tasks, args.task_id)
    storage.save_tasks(tasks, file_path)
    print(f"Marked task {args.task_id} as completed")
elif args.command == "delete":
    tasks = task_ops.delete_task(tasks, args.task_id)
    storage.save_tasks(tasks, file_path)
    print(f"Task {args.task_id} is deleted")
else:
    print("Invalid Command")