from logger import task_logger

task=[]
def add_task(task_name:str):
    task_logger.debug("DEBUG : Entering function add_task()")
    if not task_name:
        task_logger.warning("Attempted to add empty task")
        return "Task name cannot be empty"
    task.append(task_name)
    task_logger.info(f"INFO :Task added :{task_name}")
def display_task():
    task_logger.debug("DEBUG : I'm entering the function diplay_task()")
    if not task:
        task_logger.warning("WARNING : No task found here")
        print(task)
        return 
    task_logger.info("INFO : Displaying tasks")
    print([i for i in task])
def remove_task(index:int):
    task_logger.debug(f"DEBUG : Attempting to remove task at {index}")
    try:
        removed=task.pop(index)
        task_logger.info(f"INFO : Task at {index} has been removed")
        return removed
    except IndexError as e:
        task_logger.error(f"ERROR : Failed to remove task at {index}- {e}")
        return "Index not found"
