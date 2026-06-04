# Task Manager CLI

A simple command-line task manager written in Python.

## Features

- Add new tasks
- View all tasks
- Delete tasks by ID
- Search tasks by title or description
- Change task status
- Filter tasks by priority
- Filter tasks by status
- Save tasks to a JSON file
- Log actions to a log file

## Data Storage

Tasks are saved in:

    task.json

Logs are saved in:

    logs/app.log

## Priority Levels

When creating a task, choose one of the following priorities:

    1. Low
    2. Medium
    3. High

## Status Options

Available task statuses:

    1. todo
    2. in_progress
    3. done

## How to Run

Make sure you have Python installed.

Run the program with:

    python main.py

## Menu

    1. Add task
    2. Read task
    3. Delete task
    4. Search task
    5. Change status
    6. Filter priority
    7. Filter status
    8. Exit

## Requirements

- Python 3.10 or newer
- No external libraries required