# Selenium Automation Framework with Pytest

This project is an automated UI testing framework built with Selenium WebDriver and pytest.
It uses environment variables to configure the browser and wait times,
making it easy to switch settings without changing code.
---

## Features

- Supports browser configuration via `.env` file
- Uses Pytest fixtures for clean setup and teardown of WebDriver
- Implements the Page Object Model (POM) design pattern for maintainability
- Includes example login tests
- Easily extendable to support more browsers and test cases

---

## Getting Started

### Prerequisites

- Python 3.7+
- Chrome browser installed (or other browsers with further setup)
- Basic familiarity with command line and Python

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/sagar0178/automation_test.git
 
2. **open the Terminal and ron**

    `python -m pytest`

3. Dependency updates-Freeze requirements.txt before commit operation use following command for this

    `pip freeze > requirements.txt`

4. whenever you took a pull, and want to install the dependencies from requirements.txt, use following command

    `pip install -r requirements.txt`
