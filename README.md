# Fedora Rawhide Compose CLI Tool
This tool allows users to interact with Fedora Rawhide composes (the rolling development snapshots of Fedora). You can:

- List Rawhide Composes from a specific number of days in the past.<br>
- Compare Two Composes to see which packages were added, removed, or changed.<br>
When comparing two composes, the tool categorizes packages into three groups:<br>

1. <b>Added:</b> Packages present in the newer compose but not in the older one.<br>
2. <b>Removed:</b> Packages in the older compose but not in the newer one.<br>
3. <b>Changed:</b> Packages that have different versions in the two composes.<br>

This tool helps developers and Fedora maintainers track changes between Rawhide snapshots, making debugging issues or analysing package transitions easier.

# Table of Contents
[Files Included](#files-included)<br>
[Installation](#installation)<br>
[Usage](#usage)<br>
[Examples](#examples)<br>

## Files Included
- `__init__.py`: This file marks the directory as a Python package and imports necessary modules from different files. The following components are imported:
  - **CLI** from *cli_script.py*
  - **FedoraComposeManager** from *fedora_compose_manager.py*
  - **parse** from *nevra_parser.py*
  - **BASE_URL** and **ARCHITECTURE** from *config.py*
- `cli_script.py`: This is the entry point for the CLI tool. It defines the command-line interface and the functionality for different commands such as ***list*** and ***diff*** (compare).
  It uses the **argparse** library to parse command-line arguments and routes them to the appropriate methods.

  **Functions:**<br>
  - **list_composes(days):** Lists composes from the past X days.<br>
  - **compare_composes(old_date, new_date):** Compares two composes and outputs added, removed, and changed packages.<br>

-  `

## Installation
Follow these steps to install...

## Usage
To use the project...

## Examples
Here are some usage examples...
    
