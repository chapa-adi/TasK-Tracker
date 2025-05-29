# TasK-Tracker
A simple CLI project that tracks user's current standings on tasks(to-do,done and in progress).

The commands that the program can accept are: 
add, update, list, list done, list to-do, mark-done, mark-in-progress, list done, list in-progress

Syntax specific to commands
  task-cli.py add "Description"    ----- Adds a new Task with unique ID and given description

  task-cli.py update ID "Description" ------  Changes task's descrption of the task with ID also stores the time when the task was updated

  task-cli.py list   ----------------- lists all tasks

  task-cli.py list to-do ------------ lists tasks that is to be done

  task-cli.py mark-done ID ----------- marks task with ID as done and changes the updated time as well

  task-cli.py mark-in-progress ID  -------- marks task with ID as in-progress and changes the updated time as well

  task-cli.py list done   --------- lists all the done task

  task-cli.py list in-progress -------- lists all the in-progress task


Some example:
  task-cli.py add "First"
  task-cli.py add "Second"
  task-cli.py add "Third"
  task-cli.py update 1 "Changed"
  task-cli.py list
  task-cli.py list to-do
  task-cli.py mark-done 3
  task-cli.py mark-in-progress 2
  task-cli.py list done
  task-cli.py list in-progress
