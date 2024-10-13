
![HBNB BANNER](https://github.com/user-attachments/assets/26bfe7b6-cdf6-479a-90de-4d41d1bd740e)

# Holberton AirBNB Clone

## Structure

### app
This directory contains the core Flask application and instance, which is created and served within the __init__.py script

### persistence
This directory contains the current in-memeory persistence layer that will be replaced with a database layer in the future

### services
This directory contoains our services that run HBnB
#### HBnBFacade
This class handles communication between the Presentation, Business Logic, and Persistence Layers.

### run.py
This is the root file that will serve as the entry point for our AirBNB Clone

### config.py
This file contains environment-specific setting definitions

### requirements.txt
To install the requirements to run this project run the following command
`pip install -r requirements.txt`

### Run
To run and test the project, run the following command while in the root directory
`python run.py`
