# Public Service Queue System

Terminal application that manages ticket queues at a public service desk, built on linked-list data structures implemented from scratch.

> **Course:** Data Structures and Algorithms · BSc in Data Science, ISCTE · Year 1, Semester 2

## Features
- Issue tickets for **normal** and **priority** service.
- Call the next person, balancing the priority and normal queues.
- Search for and remove tickets.
- Waiting time per person (HH:MM:SS) and service statistics.
- The same system runs on two interchangeable abstract data types:
  - singly linked list (`TADSimpleList`)
  - doubly linked list (`TADDoublyLinkedList`)

## Tech stack
Python · pytest

## How to run
```bash
pip install -r requirements.txt
python main.py
```

Run the tests:
```bash
python -m pytest tests
```

## Project structure
```
.
├── main.py
├── requirements.txt
├── pytest.ini
├── src/
│   ├── attendance_system.py       # Queue logic (issue, call, search, remove, statistics)
│   ├── tad_simple_list.py         # Singly linked list ADT
│   ├── tad_double_linked_list.py  # Doubly linked list ADT
│   ├── node.py                    # List node
│   ├── person.py                  # Person / ticket data
│   ├── system_terminal_ui.py      # Terminal interface
│   └── utils.py                   # Input helpers
└── tests/                         # pytest test suite
```

> The project skeleton and tests were provided by the course; the queue system and both list ADTs were implemented as part of the assignment.
