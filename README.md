# Directory tree
Directory tree is a command line script that provides a way to organize files in hierarchical directories. The script allows users to create, move, and delete directories.
Directory tree takes a file that contains commands as input, parse commands from file and executes the commands. It implements custom directory tree data structure that imitates os direcotry tree and application that is responsible for management and representation of directory tree.

## Coding challenge
This repository contains a backend coding challenge that demonstrates my knowledge of OOP, ability to organize file structure, and understanding of tests.

### Project setup
1. To install project, clone the repository:
```
git clone https://github.com/biletboh/directory-tree.git
```
2. Install [poetry].
3. Install project dependencies with `poetry install`.
4. Activate virtual environment with `poetry shell`.

### Usage
To use the utility, call `python run.py` with `-f` flag to point to the files with commands.
```
python run.py -f tests/data/input.txt
```
The project contains `input.txt` with commands. Try it to check how the script works.
### Testing
Tests cover most of the package business logic. To run automated tests, call:
```
pytest
```
