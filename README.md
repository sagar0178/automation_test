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
   cd automation_test
 
2. **Create a virtual environment**

`python -m venv venv`

3. **Activate the virtual environmen**t

   _**Windows (PowerShell)**_

`venv\Scripts\Activate.ps1`

   _**Mac/Linux**_

`source venv/bin/activate`

4. **Install dependencies**

`pip install -r requirements.txt`

5. **Run Tests**

`pytest`

   OR

`python -m pytest`

