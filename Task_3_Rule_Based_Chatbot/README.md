# Task 3 – Rule-Based Interactive Chatbot

## Description
A Python-based interactive terminal chatbot that responds to user questions using predefined answers and keyword matching.

The chatbot uses regular expressions to identify user intents and loads frequently asked questions (FAQs) from an external JSON file. It can handle greetings, customer support questions, multiple intents, and unknown queries.

## Features
- Interactive terminal conversations.
- Greeting and thank-you responses.
- Keyword and regular-expression matching.
- Multiple intent detection in a single message.
- FAQ loading from an external JSON file.
- Built-in default FAQs if the JSON file is unavailable or invalid.
- Responses for business hours, products, shipping, returns, payments, and order status.
- Fallback responses for unknown questions.
- Exit commands such as `bye`, `exit`, and `quit`.

## Technologies Used
- Python 3
- JSON Module
- Regular Expressions (`re`)
- Dictionaries and Lists
- Functions and Loops
- String Handling
- pathlib

## Project Files
- `chatbot.py` – Main chatbot application.
- `sample_faq.json` – Stores FAQ questions, matching patterns, and responses.
- `README.md` – Project documentation.

## Installation
1. Install Python 3.
2. Download or clone this repository.
3. Open the terminal in the project folder.

No external Python packages are required.

## How to Run

Run the following command:

`python chatbot.py`

Make sure `sample_faq.json` is in the same folder as `chatbot.py`.

## Example Questions
- Hello!
- What are your business hours?
- How long does delivery take?
- What is your return policy?
- Which payment methods do you accept?
- Where is my order?

## Exit the Chatbot
Type any of these commands:
- `bye`
- `goodbye`
- `exit`
- `quit`
- `stop`

## Output
The chatbot displays suitable responses in the terminal based on the user's input. If it cannot identify a question, it provides a default fallback response.
