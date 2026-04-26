# SpaceX_API_Testing
This project is an automated API testing framework built with Python and pytest. It uses the requests library to validate the open-source SpaceX API endpoints (like launches, rockets, and crew data) and automatically generates detailed HTML test reports.

# SpaceX API Testing Suite

A comprehensive automated testing suite built with Python and `pytest` to validate the [SpaceX REST API (v4)](https://github.com/r-spacex/SpaceX-API).

## Overview

This project is designed to automate API tests for the public SpaceX API. It verifies the availability, status codes, and data payload integrity of various endpoints, ensuring the API is behaving as expected. The suite uses the Python `requests` library to make HTTP requests and leverages `pytest-html` to generate detailed, self-contained HTML reports for easy viewing of test results.

## Tested Endpoints

The test suite covers the following endpoints from the SpaceX API v4:
- `/launches` - Retrieves all SpaceX launches.
- `/rockets` - Retrieves all SpaceX rockets.
- `/crew` - Retrieves all SpaceX crew members.
- `/launchpads` - Retrieves all SpaceX launchpads.
- `/capsules` - Retrieves all SpaceX capsules.
- `/payloads` - Retrieves all SpaceX payloads.

It also includes negative testing scenarios, such as verifying the correct HTTP 404 response for invalid endpoints.

## Project Structure

```text
spacex_testing/
├── tests/
│   └── test_spacex.py  # Contains all the API test case functions
├── conftest.py         # Pytest configuration and shared fixtures
├── pytest.ini          # Pytest execution settings (e.g., report generation flags)
└── README.md           # Project documentation
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd spacex_testing
   ```

2. Install the required dependencies:
   ```bash
   pip install pytest requests pytest-html
   ```

## Running the Tests

To run the complete test suite, simply execute the following command in the project root directory:

```bash
pytest
```

Thanks to the configurations defined in `pytest.ini`, running the `pytest` command will automatically:
- Discover and execute all tests located in the `tests/` directory.
- Generate a self-contained HTML test report named `report.html` in the root directory.

### Viewing the Test Report

After the test execution finishes, a file named `report.html` will be created. You can open this file in any web browser to view a detailed, visual breakdown of your test run (passed, failed, skipped, etc.).

## Technologies Used

- **[Python](https://www.python.org/)**: The core programming language.
- **[pytest](https://pytest.org/)**: The testing framework.
- **[Requests](https://requests.readthedocs.io/)**: For making HTTP requests to the API.
- **[pytest-html](https://pypi.org/project/pytest-html/)**: Plugin for generating HTML test reports.

## Contributing

Feel free to fork this repository, add more test coverage for other SpaceX API endpoints, or improve existing tests, and submit a pull request!
