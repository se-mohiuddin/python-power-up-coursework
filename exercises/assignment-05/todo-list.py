'''
Task-2: Managing a ToDo List

1. Create a Python class named Task.
2. Define the following methods within the Task class:
	set_task_detail(self, task_name, priority)
	mark_as_complete(self) 
	display_task_info(self)

3. Create an object of the Task class.
4. Use the set_task_details method to set the task_name, and task’s priority.
5. Use the mark_as_complete method to mark the task as completed.
6. Finally, use the display_task_info method to print the toDo List.
'''
class Task:
    def set_task_detail(self, task_name, priority):
        self.task_name=task_name
        self.priority=priority
    def mark_as_complete(self):
        self.status="Completed"
        
    def display_task_info(self):
        print("Task Name: ", self.task_name)
        print("Task Priority: ", self.priority)
        print("Task status: ",self.status)
        print("-----------------------------")

task1=Task()
task1.set_task_detail("cooking", 2)
task1.mark_as_complete()
task1.display_task_info()
