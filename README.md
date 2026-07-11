# Contact Book CLI
This project is a simple command-line contact manager written in Python.

## What does this project do?
This project lets users manage their personal contacts directly from the terminal, without needing a database or external app. Contacts are saved locally in a JSON file, so they persist between sessions.

## Features
Add, list, search, and delete contacts
Each contact is assigned a unique ID automatically
Shows an error message if the name or phone field is left empty
Search matches partial names (not just exact matches)
Contacts are automatically saved to a local JSON file

## How to run
Download the ZIP file and extract it.
Open a terminal (cmd) and navigate to the project folder:
cd contact-book-cli
python main.py
Follow the on-screen menu to add, list, search, or delete contacts.

## What I learned
I learned how to read and write data to a JSON file, and how to handle missing or corrupted files without crashing the program (using try/except). I also practiced writing separate functions for each feature (add, list, search, delete) and validating user input, such as checking for empty fields and invalid IDs.