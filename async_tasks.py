import asyncio

class AsyncTasks:
    """
    A class to manage asynchronous tasks in a Discord bot.

    This class allows starting, freezing, and unfreezing asynchronous tasks.

    Attributes
    ----------
    declared_functions : list
        A list of functions declared to run as tasks.
    running_tasks : list of asyncio.Task
        A list of currently running tasks.
    variables : dict
        A dictionary of variables to be passed to the tasks.
    """
    def __init__(self, variables: dict):
        """
        Initialize the AsyncTasks instance.

        Parameters
        ----------
        variables : dict
            A dictionary of variables to be passed to the tasks.
        """
        self.declared_functions = []
        self.running_tasks: list[asyncio.Task] = []
        self.variables = variables

    def run_tasks(self, functions: list):
        """
        Start the tasks for each function in the provided list.

        The given functions are started as asynchronous tasks, and references are stored
        for potential later cancellation or restart.

        Parameters
        ----------
        functions : list
            A list of asynchronous functions that accept a single dict argument.
        """
        for function in functions:
            task = asyncio.create_task(function(self.variables))
            self.running_tasks.append(task)
            self.declared_functions.append(function)
            print(f"Task {function.__name__} has been started.")

    def freeze_tasks(self):
        """
        Freeze (cancel) all currently running tasks.

        Each task in the running tasks list is cancelled and then removed from the list.
        """
        # Iterujemy po kopii listy, aby móc usuwać elementy na bieżąco.
        for task in self.running_tasks.copy():
            task.cancel()
            self.running_tasks.remove(task)
            print(f"Task {task} has been frozen.")

    def unfreeze_tasks(self):
        """
        Unfreeze tasks by restarting all declared functions.

        New tasks are created for each function in the declared functions list and added
        to the running tasks list.
        """
        for function in self.declared_functions:
            task = asyncio.create_task(function(self.variables))
            self.running_tasks.append(task)
            print(f"Task {function.__name__} has been unfrozen.")