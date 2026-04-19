from task import TaskManager

def test_add_task():
    tm = TaskManager()
    result = tm.add_task("Study CI/CD")
    assert result == "Task added"
    assert len(tm.get_tasks()) == 1

def test_empty_task():
    tm = TaskManager()
    assert tm.add_task("") == "Task cannot be empty"

def test_complete_task():
    tm = TaskManager()
    tm.add_task("Test task")
    result = tm.complete_task(0)
    assert result == "Task completed"
    assert tm.get_tasks()[0]["completed"] == True

def test_delete_task():
    tm = TaskManager()
    tm.add_task("Delete me")
    result = tm.delete_task(0)
    assert result == "Task deleted"
    assert len(tm.get_tasks()) == 0

def test_invalid_index():
    tm = TaskManager()
    assert tm.complete_task(5) == "Invalid index"