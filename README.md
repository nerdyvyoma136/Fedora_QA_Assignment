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
  - `list [days]` → Lists composes from the past `days` (default: 7).  
  - `diff <old_date> <new_date>` → Compares two composes by date (YYYYMMDD format).

  **Functions:**<br>
  - **list_composes(days):** Lists composes from the past X days.<br>
  - **compare_composes(old_date, new_date):** Compares two composes and outputs added, removed, and changed packages.<br>

-  `config.py`: This file contains configuration information:<br>
    - **BASE_URL:** The URL base for Fedora Rawhide composes.
    - **ARCHITECTURE:** The default architecture used for Fedora packages, is set to x86_64 in this case.

- `nevra_parser.py`: Contains a function called parse to parse NEVRA (Name, Environment, Version, Release, Architecture) format.
  - **parse(nevra)**:  
    - Extracts the package name from a NEVRA-formatted string.  
    - Extracts the version by handling delimiters properly.
   
- `fedora_compose_manager.py`: Contains three different functions, as below:
    - **List Recent Composes** *`list_composes(days=7)`*: Fetches unique Fedora Rawhide compose dates from the past specified days (default: 7 days).  
    - **Fetch RPM Packages** *`fetch_rpms(compose_date)`*: Retrieves the list of RPMs available in a specific compose.  
    - **Compare Composes** *`compare_composes(old_date, new_date)`*: Identifies added, removed, and changed packages between two specified composes.
 
- `utils.py`: provides essential utility functions for fetching HTML content, extracting Fedora Rawhide compose dates, and retrieving timestamps from package metadata.<br>
It is used by other modules in the Fedora Rawhide Compose Diff Tool.<br>
  - **`fetch_html(url)`**  
    - Fetches HTML content from a specified URL.  
    - Handles request errors and returns `None` if fetching fails.  

  - **`extract_compose_dates(html)`**  
    - Extracts Fedora Rawhide compose dates (`YYYYMMDD`) from the provided HTML.  
    - Returns a sorted list of dates in descending order.  

  - **`extract_timestamp(pkg_name)`**  
    - Extracts a timestamp (`YYYYMMDD`) from a package name using regex.  
    - If no timestamp is found, defaults to the current system date.
   
- `main.py`: Main execution file which initializes and runs the command-line interface (CLI) by invoking the `CLI.run()` method from `cli_script.py`.
  
## Prerequisites 
- Python 3.6 or above to be installed.
- Access to Fedora Rawhide composes.

## Installation
```bash
git clone https://github.com/nerdyvyoma136/Fedora_QA_Assignment.git
cd Fedora_QA_Assignment
```

## Usage
This tool can be executed through the terminal with two primary commands:<br>

**List Composes**: Lists Fedora Rawhide composes from the past X days.
```bash
python main.py list <days>
```
**Compare Two Composes (Diff)**: Compares two Fedora Rawhide composes and outputs added, removed, and changed packages.
```bash
python main.py diff <old_date> <new_date>
```

## Examples
1. List Fedora Rawhide composes from the last 7 days:
```bash
python main.py list 7
```
**Output**:
```bash
20250213
20250212
20250211
20250210
20250209
20250208
20250207
```
2. Compare the composes from 2024-02-07 and 2024-02-13:
```bash
python main.py diff 20240207 20240213
```
**Output**:
```bash
=== REMOVED PACKAGES ===
[20250213] phpunit10 REMOVED (0:10.5.44-1)
[20250213] astromenace REMOVED (0:1.4.2-12)
[20250213] kdepim-runtime REMOVED (1:24.12.1-2)
[20250213] python-twilio REMOVED (0:9.4.4-1)
[20250213] ceph REMOVED (2:19.2.0-10)
[20250213] dragon REMOVED (0:24.12.1-2)
[20250213] extra-cmake-modules REMOVED (0:6.10.0-2)
[20250213] python3.10 REMOVED (0:3.10.16-4)
[20250213] ocaml-ppx-js-style REMOVED (0:0.17.0-5)
[20250213] plasma-thunderbolt REMOVED (0:6.2.90-2)
.
.
.
[20250213] kscreen REMOVED (1:6.2.90-2)

=== ADDED PACKAGES ===
[20250213] calindori ADDED (0:24.12.2-1)
[20250213] kdialog ADDED (0:24.12.2-1)
[20250213] nautilus ADDED (0:47.2-3)
[20250213] filelight ADDED (1:24.12.2-1)
[20250213] libkscreen ADDED (0:6.3.0-1)
.
.
.
[20250207] fedora-appstream-metadata ADDED (0:20250207-1)

=== CHANGED PACKAGES ===
```

