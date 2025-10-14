# Python 201 - Procedural Programming

## Repository Overview
This repository contains my coursework for [Python 201 - Procedural Programming](https://codingnomads.com/course/python-programming-201), the second course in the [Python Web Development Career Track](https://codingnomads.com/career-track/python-web-development-learn-python-bootcamp) by [CodingNomads](https://codingnomads.com/). This was an 80-hour course, designed to help learners deepen their understanding of Python through procedural programming concepts, debugging, and API integration. This included multiple projects and labs, including SQLAlchemy, API integration, and debugging approaches. 

---

## Table of Contents
- [Repository Overview](#repository-overview)
- [Table of Contents](#table-of-contents)
- [Concepts Covered](#concepts-covered)
- [Prerequisites](#prerequisites)
- [Exercises & Labs](#exercises--labs)
- [Projects](#projects)
- [API Capstone Project](#api-capstone-project)
- [To Clone This Repository](#to-clone-this-repository)
  
---

## Concepts Covered 
The following Python skills were acquired when completing this course:
- Functions: arguments, return values, and scope 
- Advanced data types: tuples, lists, sets, and dictionaries
- File input/output and managing paths effectively
- Building modules and packages 
- Dependency management, using virtual environments 
- Debugging programs using IDE features, Python PDB, web-pdb and pudb modules  
- Database integration, with SQLAlchemy
- REST API integration, with the Python `requests` package 

---

## Prerequisites
The [CodingNomads Python 101 course](https://github.com/franpanteli/CodingNomads-python-101) was a prerequisite for this. Other prerequisites included a Python version above 3.0 to be installed, for the completion of its pdb debugger and virtual environment sections.

---

## Exercises & Labs
One directory was created for each module in the course, from modules two to ten. Each of these directories includes two further directories, for content and practice. Course content was presented in the form of videos and webpages. Notes were made on each of these, in a .py file per video and webpage. These notes are included in each module’s `webpage_and_video_notes` directory. Labs (module exercises) were next completed. My solutions for these were annotated with comments and are published in each module’s lab folder. Links to each set of my module notes and exercise solutions are presented below. These are also found in the repository [resources](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/resources) folder. 
- [02 More Data Types](labs/resources/02_more-datatypes)
  - [02_webpage_and_video_notes](labs/resources/02_more-datatypes/02_webpage_and_video_notes)
  - [02_labs](labs/resources/02_more-datatypes/02_labs)
- [03 File Input/Output](labs/resources/03_file-input-output)
  - [03_webpage_and_video_notes](labs/resources/03_file-input-output/03_webpage_and_video_notes)
  - [03_labs](labs/resources/03_file-input-output/03_labs)
- [04 Functions and Scopes](labs/resources/04_functions-and-scopes)
  - [04_webpage_and_video_notes](labs/resources/04_functions-and-scopes/04_webpage_and_video_notes)
  - [04_labs](labs/resources/04_functions-and-scopes/04_labs)
- [05 Virtual Environments and Packages](labs/resources/05_venvs-and-packages)
  - [05_webpage_and_video_notes](labs/resources/05_venvs-and-packages/05_webpage_and_video_notes)
  - [05_labs](labs/resources/05_venvs-and-packages/05_labs)
- [06 Advanced Python Concepts](labs/resources/06_advanced-python-concepts)
  - [06_webpage_and_video_notes](labs/resources/06_advanced-python-concepts/06_webpage_and_video_notes)
  - [06_labs](labs/resources/06_advanced-python-concepts/06_labs)
- [07 APIs and Databases](labs/resources/07_APIs_and_Databases)
  - [07_webpage_and_video_notes](labs/resources/07_APIs_and_Databases/07_webpage_and_video_notes)
  - [07_labs](labs/resources/07_APIs_and_Databases/07_labs)
- [08 Debugging](labs/resources/08_debugging)
  - [08_webpage_and_video_notes](labs/resources/08_debugging/08_webpage_and_video_notes)
  - [08_labs](labs/resources/08_debugging/08_labs)
- [09 Integrating APIs](labs/resources/09_Integrating_APIs)
- [10 Next Steps](labs/resources/10_Next_Steps)

---

## Projects

- **[Crash Blossoms CLI](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/Crash_Blossoms_CLI)**: Expands a title-case function into a command-line interface programme that generates “Crash Blossoms” style headlines. Users can input text, and the programme capitalises it according to headline conventions, repeatedly prompting for new input. This project revisits function creation and user input handling while demonstrating practical string manipulation.  
    **Files:**  
    - [crashblossoms.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/Crash_Blossoms_CLI/crashblossoms.py)  
    - [Python_Project_Crash_Blosssoms_video_notes.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/Crash_Blossoms_CLI/Python_Project_Crash_Blosssoms_video_notes.py)  

- **[Python REST API Tutorial (Automation Tools)](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/Python_REST_API_Tutorial_(Automation_Tools))**: Integrates multiple APIs to automatically fetch data and generate a simple HTML page. The project demonstrates fetching dog images and quotes, parsing JSON responses, and dynamically generating HTML content. It also teaches creating virtual environments and using Python’s requests module safely.  
    **Files:**  
    - [website.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/Python_REST_API_Tutorial_(Automation_Tools)/website.py)  
    - [(task)-barking-shibes.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/Python_REST_API_Tutorial_(Automation_Tools)/(task)-barking-shibes.py)  

- **[Rock Paper Scissors Game](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/Rock_Paper_Scissors_Game)**: Implements a complete command-line rock-paper-scissors game. Users input a number to represent their hand, while the computer generates a random choice. The programme compares the selections, prints both hands, and announces the winner. This project reinforces understanding of game logic and decision-making in Python.  
    **Files:**  
    - [Rock_Paper_Scissors_Game.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/Rock_Paper_Scissors_Game/Rock_Paper_Scissors_Game.py)  

- **[File Counter](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/file_counter)**: Analyses file types on the desktop over time, creating a SQL-like summary of file counts and types. The main script counts files, moves frequent file types into organised folders, and appends timestamped summaries to a database file. The companion Data_Analysis.py script reads these summaries, calculates statistics, and identifies trends such as the most common file type or the busiest day.  
    **Files:**  
    - [file_counter.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/file_counter/after_module_07/file_counter.py)  
    - [Data_Analysis.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/file_counter/Data_Analysis.py)  
    - [Desktop file summary.sql](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/file_counter/after_module_07/Desktop%20file%20summary.sql)  

- **[Making the Enumerate Function](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/making_the_enumerate_function.py)**: Recreates Python’s built-in enumerate() function to demonstrate iteration with indices. The project contains several scripts showing alternative ways to iterate over lists, including using range(), for loops, and a custom enumerate function. It emphasises understanding of tuples, indexing, and iteration logic.  
    **Files:**  
    - [my_enumerate.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/making_the_enumerate_function.py/my_enumerate.py)  
    - [for_loops.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/making_the_enumerate_function.py/for_loops.py)  
    - [range_length.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/making_the_enumerate_function.py/range_length.py)  

- **[Dungeons and Dragons Game 4.0 with APIs](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/dungeons_and_dragon_game_4.0_with_APIs)**: A Dungeons and Dragons-inspired command-line game enhanced by API integration. The game incorporates external data to enrich gameplay, including generating characters and scenarios dynamically. This project combines advanced procedural programming with practical API usage.  
    **Files:** *(links to specific files within this project can be added if needed)*  

- **[API Name Game](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/api-name-game.py)**: A command-line interface game that fetches names or other content from an API and interacts with the user. Demonstrates how external data can be manipulated and used within a Python programme to create dynamic and interactive experiences.  
    **Files:** [api-name-game.py](https://github.com/franpanteli/CodingNomads-python-201/blob/main/labs/projects/api-name-game.py)  

---

## API Capstone Project

---

## To Clone This Repository
```bash
git clone https://github.com/franpanteli/CodingNomads-python-201.git
