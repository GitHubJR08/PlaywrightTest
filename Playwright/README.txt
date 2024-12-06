Test Automation with Playwright in Python
Description
This project implements end-to-end (E2E) tests for the Qubika Sports Club management system. It uses Playwright for UI tests and requests to interact with the API.

Requirements
Python 3.13.0

Installation
pip install
playwright install

IDE
PyCharm 2024.2.4

Solution
The project was created individually by me with the help of materials from the internet, using as a guide a YouTube channel called JoanMedia, and prior knowledge of the framework. Playwright was installed, and Python and PyCharm were already installed on the machine. Then, I proceeded to create a script called sync.py, which contains the solution for exercise number 2 of the technical test provided by Qubika.

Improvements
The creation of the user via the API was researched, and a solution for creating the user was found, but it was not executed successfully. Therefore, to log in, it was detected that the string parameter can be used for both email and password, and after logging in, the remaining tests can be performed.

Instructions for Running Tests
Install PyCharm, then open the project in this Python IDE.
Make sure both Python and Playwright are installed on the computer.
In the PyCharm terminal, run: python sync.py
The project will proceed with its execution.