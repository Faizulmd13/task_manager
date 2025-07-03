import json

def load_tasks(file_path):
    if not file_path.exists() or file_path.read_text().strip() == "":
        file_path.write_text("[]")

    try:
        task_list = json.loads(file_path.read_text())
    except json.JSONDecodeError:
        task_list = []
        file_path.write_text("[]")

    return task_list

def save_tasks(task_list, file_path):
    tasks = json.dumps(task_list, indent=4)
    file_path.write_text(tasks)