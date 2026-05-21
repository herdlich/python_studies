# Auth System + Log Parser

A simple Python authentication system with logging support and a separate log parser utility.

## Features

### main.py
- User registration
- User login
- JSON file storage
- Logging user activity
- Error handling

### parser.py
- View all logs
- Search logs by level
- Search logs by date
- Search logs by username

---

## Technologies Used

- Python
- JSON
- logging
- pathlib

---

## Log Levels

The application uses:
- INFO
- WARNING
- ERROR
- CRITICAL

---

## File Structure

project/  
&nbsp;|  
├── main.py  
├── parser.py  
├── users.json  
└── logs/  
&emsp;&emsp;└── app.log

---

## How to Run

Run authentication system:

```bash
python main.py
```
---

## Run log parser:

```bash
python parser.py
```

---

## Example log
```bash
[21/05/2026 18:20:15]root - INFO: User "admin" has been successfully registered
```