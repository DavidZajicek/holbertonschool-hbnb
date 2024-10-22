
![HBNB BANNER](https://github.com/user-attachments/assets/26bfe7b6-cdf6-479a-90de-4d41d1bd740e)

# 🏨 Holberton AirBNB Clone

## Overview
HBnB is a platform designed to connect property owners with potential guests, facilitating short-term rentals and unique accommodation experiences. The application encompasses several key functionalities:

User Management: Allowing users to register, update their profiles, and operate as either guests or hosts. Place Management: Enabling hosts to list their properties with details such as description, price, and location. Review System: Facilitating guest feedback through ratings and comments on their stays. Amenity Management: Associating various amenities with listed properties to enhance guest experiences.

## Technical Architecture
The HBnB application is built on a three-layered architecture, ensuring modularity, scalability, and maintainability:

Presentation Layer: Handles user interactions through services and API endpoints, managing input/output and user interface elements. Business Logic Layer: Contains the core models (User, Place, Review, Amenity) and implements the rules governing the platform's functionality. Persistence Layer: Manages data storage and retrieval, interfacing with the database to perform CRUD operations.

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
To run the project, run the following command while in the root directory
`python run.py`

### Test
To test the project, run the following command while in the root directory
`python3 -m unittest discover app.tests`

-------------------------------------------------------------------------------------------------------------------------
### 🧑‍💻 Developed By:
* Chutima Puthachon
* Angela Enriquez Garcia
* David Zajicek
* Sonny Keo
