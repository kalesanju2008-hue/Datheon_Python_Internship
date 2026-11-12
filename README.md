# Datheon Python Internship

This repository contains four Python projects developed as part of my Python Internship at Datheon. These projects demonstrate practical Python programming concepts, problem-solving skills, data handling, and automation techniques.

## Projects Overview

### Task 1 – Hangman Game
An interactive word guessing game where players try to guess a hidden word one letter at a time within a limited number of attempts.

**Key Features:**
- Random word selection
- Letter-by-letter guessing
- Tracks correct and incorrect guesses
- Displays remaining attempts
- Win and lose messages

### Task 2 – Stock Portfolio Tracker
A Python application that helps users manage stock investments by recording stock names, quantities, and purchase prices.

**Key Features:**
- Add stock details
- Track quantities and prices
- Calculate total investment
- Fetch current stock prices using the optional yfinance library
- Calculate profit and loss
- Generate portfolio summaries in CSV format

### Task 3 – Rule-Based Chatbot
A Python chatbot that interacts with users by providing predefined answers using keyword matching and stored FAQs.

**Key Features:**
- Interactive conversations
- Predefined responses
- Keyword and pattern-based matching
- JSON-based FAQ storage
- Handles unknown questions

### Task 4 – Automated File Organizer & Cleanup Utility
A Python utility that organizes files into category folders based on their file extensions.

**Key Features:**
- Scans files in a directory
- Identifies file extensions
- Creates category folders automatically
- Organizes documents, images, videos, audio, archives, and code files
- Prevents overwriting files with duplicate names
- Maintains an activity log

## Technologies Used

- Python
- CSV and JSON
- Random Module
- OS and Shutil Modules
- Pathlib Module
- Regular Expressions
- File Handling
- Functions, Loops, and Conditional Statements

## Repository Structure

```text
Datheon_Python_Internship/
│
├── Task_1_Hangman/
│   ├── hangman.py
│   └── README.md
│
├── Task_2_Stock_Portfolio_Tracker/
│   ├── portfolio.py
│   ├── portfolio_summary.csv
│   └── README.md
│
├── Task_3_Rule_Based_Chatbot/
│   ├── Chatbot.py
│   ├── sample_faq.json
│   └── README.md
│
├── Task_4_File_Organizer/
│   ├── organizer.py
│   └── README.md
│
└── README.md
```

## Installation and Setup

### 1. Install Python
Download and install Python from the official website:

https://www.python.org/downloads/

### 2. Clone the Repository

```bash
git clone https://github.com/kalesanju2008-hue/Datheon_Python_Internship.git
```

### 3. Open the Project Folder

```bash
cd Datheon_Python_Internship
```

### 4. Run Individual Projects

Open the required task folder and execute its Python file.

Example:

```bash
cd Task_1_Hangman
python hangman.py
```

Repeat this process for the other projects using their respective Python filenames.

### Optional Dependency

Task 2 can use the `yfinance` library to fetch live stock prices.

Install it using:

```bash
python -m pip install yfinance
```

The tracker also supports manual price entry if the library or live price fetching is unavailable.

## Project Architecture

Each task is maintained in a separate folder with its own Python source code and README file.

- **Input Layer:** Accepts user input and required data.
- **Processing Layer:** Uses Python functions, conditions, loops, and modules to perform the required operations.
- **Output Layer:** Displays results or saves information in CSV, JSON, or log files where applicable.

This modular structure makes each project easier to understand, run, and maintain.

## Learning Outcomes

Through these projects, I gained practical experience in:

- Python programming fundamentals
- Functions and modular programming
- File handling and data storage
- CSV and JSON operations
- Input validation and error handling
- Basic automation
- Problem-solving and logical thinking

## Author

**Sanjana Kale**

Python Internship Project – Datheon
