from datetime import datetime

def task_id_generator(task_list):
    if not task_list:
        return 1
    return max(task["id"] for task in task_list) + 1

def parse_due_date(due_str):
    try:
        due_date = datetime.strptime(due_str, "%Y-%m-%d")
        return due_date.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format")
    
def validate_priorities(priority):
    valid_prioirities = ["low", "medium", "high"]
    if priority and priority.lower() not in valid_prioirities:
        raise ValueError("Priority must be one of: low, medium, high")
    return priority.lower()
