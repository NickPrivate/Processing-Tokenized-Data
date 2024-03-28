## Requirements:
- Python 3

## Install Python here:
######
- https://www.python.org/downloads/

## Dependencies:
- ```pip install tabulate```
- ```pip install nltk```
#
### Run program on Unix:
cd to where the file is located then type
- ```python3 main.py```

### Run program on Windows:
cd to where the file is located then type
- ```python main.py```

## Overview
main.py initializes the script by importing the modules used to tokenize the data. Each module contains a function that handles the data. This modular approach allows for easier integration and expansion.

## Functionality:
- file_reader.py
  - Responsible for reading input data. It ensures that data is correctly loaded into the program for processing.
- preprocessor.py
  - Preprocesses the input data by performing tasks such as removing comments, making it ready for tokenization.
- tokenizer.py
  - Analyzes the preprocessed data to identify and extract tokens. This module is central to the program's purpose, converting raw text into a structured format for further analysis, sending the tokenized data to be processed by the output formatter.
- output_formatter.py
  - Formats the tokenized data into a table for easy readability.

## Test Cases
Included is a test case that it automatically called upon running the script. The output is a formatted table with the Lexeme, Token, and Count.

## Contributors:
- Ryan Haddadi
- Nicholas Goulart
- Anthony LaPan
