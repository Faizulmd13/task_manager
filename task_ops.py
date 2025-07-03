from datetime import datetime
import utils

def add_task(task_list, title, due=None, priority=None):
    task_id = utils.task_id_generator(task_list)

    formatted_due = None
    if due:
        formatted_due = utils.parse_due_date(due)

    Priority = None
    if priority:
        Priority = utils.validate_priorities(priority)
    new_task = {
        "id": task_id,
        "title": title,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "due_date": formatted_due,
        "priority": Priority
    }

    task_list.append(new_task)
    return task_list

def list_tasks(task_list, show_completed=False):
    for task in task_list:
        is_done = task["completed"]

        if show_completed and not is_done:
            continue
        
        x = "x" if is_done else ""
        id = task["id"]
        title = task["title"]
        due = task["due_date"] if task["due_date"] else "N/A"
        priority = task["priority"] if task["priority"] else "N/A"

        print(f"{id}. [{x}] {title} (Due: {due}) - Priority: {priority}")

def mark_done(task_list, task_id):
    for task in task_list:
        if task["id"] == task_id:
            task["completed"] = True
            break
    return task_list

def delete_task(task_list, task_id):
    for i, task in enumerate(task_list):
        if task["id"] == task_id:
            del task_list[i]
            break
    return task_list
