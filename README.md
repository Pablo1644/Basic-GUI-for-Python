# Test Checker GUI Application

This application is a simple GUI for checking test answers. Users can navigate through multiple-choice questions and submit their answers. The application then calculates the user's score based on their inputs.

## Features

- **Question Navigation:** Users can navigate between questions using "next" and "previous" buttons.
- **Answer Submission:** Users can submit their answers for each question.
- **Score Calculation:** The application calculates the user's score and displays it in a message box.

## Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)
- `base.py` file containing the following variables:
  - `questions`: List of questions.
  - `anwsers`: List of correct answers.
  - `nr`: Total number of questions.
  - `possible_signs`: Function to check if the answer is valid (a, b, c, or d).

## Installation

1. Clone the repository or download the source code.
2. Ensure you have `base.py` with the required variables and functions.
3. Place an image named `bg.png` in the same directory as your script for the background.

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing your script.
3. Run the script using Python:

   ```bash
   python your_script_name.py
