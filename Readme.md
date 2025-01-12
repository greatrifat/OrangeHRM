# OrangeHRM Automation Testing

This repository contains automation testing scripts for the OrangeHRM web application using **Selenium**, **Python**, and **Unittest**. The project is structured into separate folders for data-driven tests and hardcoded tests.

## Project Structure

OrangeHRM/
│
├── DataDrivenSeleniumOhrmPy_unittest/
│   └── Contains scripts for data-driven testing using Excel files.
│
├── HardCodeSeleniumOhrmPy_unittest/
│   └── Contains scripts for hardcoded test cases.
│
├── Test_Results_DD/
│   └── Stores HTML reports for data-driven test results.
│
├── Test_Results_HC/
│   └── Stores HTML reports for hardcoded test results.
│
├── TestCase_Ohrm.xlsx
│   └── Excel file containing test cases for testing.
│
├── data.xlsx
│   └── Sample login data for data-driven tests.
│
└── README.md

## Features

- **Data-Driven Testing**: Automates login functionality using data from an Excel file.
- **Hardcoded Tests**: Validates login functionality with predefined inputs.
- **HTML Test Reports**: Generates comprehensive reports for test results.
- **Python Selenium Automation**:
  - Performs login with valid and invalid credentials.
  - Handles elements dynamically (e.g., login, logout, error messages).

## Prerequisites

Before running the tests, ensure you have the following installed:

- Python 3.10 or later
- Google Chrome browser
- ChromeDriver
- Required Python modules:
  - `selenium`
  - `openpyxl`
  - `HtmlTestRunner`

You can install the necessary Python modules using:
```bash 
pip install selenium openpyxl HtmlTestRunner
```

## Usage
Running Hardcoded Test Cases
1. Navigate to the HardCodeSeleniumOhrmPy_unittest folder.
2. Execute the test script:

```bash 
python test_script_name.py
```

## Viewing Test Reports
Test results are stored in **Test_Results_DD/** for data-driven tests and **Test_Results_HC/** for hardcoded tests.
Open the HTML files in a browser to view detailed reports.

## Contribution
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to create an issue or submit a pull request.