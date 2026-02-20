# Python Piscine

This repository consists of a series of intensive projects designed to introduce *Python programming* and *Object-Oriented Programming (OOP)*. The curriculum is organized into 11 modules (00 to 10), featuring exercises that progress from foundational logic to advanced implementation.

## Project Progress

| Module | Status | Score | Topic |
| :--- | :---: | :---: | :--- |
| **Module 00** | ✅ | 100/100 | Fundamentals & Standard I/O |
| **Module 01** | ✅ | 100/100 | Object-Oriented Programming |
| **Module 02** | ❌ | -- | Error Handling & Exceptions |
| **Module 03** | ❌ | -- | System Interaction & Data Structures |
| **Module 04** | ❌ | -- | File I/O & Streams |
| **Module 05** | ❌ | -- | Stream Processing |

## Module 00: Fundamentals
7 Exercises - Focuses on the core syntax and essential building blocks of the language:  
* *Function Definition:* definition, arguments, and return values.  
* *Data Types:* Manipulation of strings and integers.  
* *Standard I/O:* Utilizing built-in functions like `print()` and `input()` for user interaction.  

## Module 01: Object-Oriented Programming
6 Exercises - An introduction to the OOP paradigm. This module covers the creation and management of *classes and subclasses*, enabling the development of complex, modular, and reusable software architectures.  

## Module 02: Error Handling and Exceptions
6 Exercises - Dedicated to writing robust, crash-resistant code. Key topics include:  
* *Control Flow:* Implementing `try`, `except`, and `finally` blocks.
* *Exception Hierarchy:* Understanding how Python categorizes errors.  
* *Custom Logic:* Learning how to `raise` and define custom exceptions for specific use cases.  

## Module 03: System Interaction and Data Structures
7 Exercises - Focuses on environment interaction and efficient data management:  
* *The `sys` Library:* Using `sys.argv` to process command-line arguments.
* *Advanced Structures:* Working with *tuples*, *sets*, and *unions*.
* *Dictionary Mapping:* Managing key-value pairs and getter/setter logic.
* *Memory Efficiency:* An introduction to memory-efficient data iteration. 

## Module 04: File I/O and Streams
5 Exercises - Covers of file system operations and stream management:  
* *File Operations:* Practical experience opening, reading, writing, and closing files.  
* *Standard Streams:* Utilizing `stdin`, `stdout`, and `stderr` via the `sys` library for advanced input/output control.  

## Module 05 - Data Streams
3 Exercises - Covers method overriding and subtype polymorphism

## Module 06 - Import system
1 Exercise with 4 parts - Focuses on how to use python's import system.
* *`__init__.py`:* Practical use of importing python packages
* *Different import methods*: Covers different methods for importing packages, functions and files
* *Circular dependency Curse*: Understanding and avoiding circular imports


## Repository Structure

```

├── Module_00/
│   ├── main.py
│   ├── ex0/ ft_hello_garden.py
│   ├── ex1/ ft_plot_area.py
│   ├── ex2/ ft_harvest_total.py
│   ├── ex3/ ft_plant_age.py
│   ├── ex4/ ft_water_reminder.py
│   ├── ex5/ ft_count_harvest_iterative.py, ft_count_harvest_recursive.py
│   ├── ex6/ ft_garden_summary.py
│   └── ex7/ ft_seed_inventory.py

├── Module_01/
│   ├── ex0/ ft_garden_intro.py
│   ├── ex1/ ft_garden_data.py
│   ├── ex2/ ft_plant_growth.py
│   ├── ex3/ ft_plant_factory.py
│   ├── ex4/ ft_garden_security.py
│   ├── ex5/ ft_plant_types.py
│   └── ex6/ ft_garden_analytics.py
├── Module_02/
│   ├── ex0/ ft_first_exception.py
│   ├── ex1/ ft_different_errors.py
│   ├── ex2/ ft_custom_errors.py
│   ├── ex3/ ft_finally_block.py
│   ├── ex4/ ft_raise_errors.py
│   └── ex5/ ft_garden_management.py
├── Module_03/
│   ├── data_quest_tools/
│   ├── ex0/ ft_command_quest.py
│   ├── ex1/ ft_score_analytics.py
│   ├── ex2/ ft_coordinate_system.py
│   ├── ex3/ ft_achievement_tracker.py
│   ├── ex4/ ft_inventory_system.py
│   ├── ex5/ ft_data_stream.py
│   └── ex6/ ft_analytics_dashboard.py
├── Module_04/
│   ├── data-generator-tools/
│   ├── ex0/ ft_ancient_text.py
│   ├── ex1/ ft_archive_creation.py
│   ├── ex2/ ft_stream_management.py
│   ├── ex3/ ft_vault_security.py
│   └── ex4/ ft_crisis_response.py
└── Module_05/
    ├── main.py
    ├── ex0/ stream_processor.py
    └── ex1/ data_stream.py