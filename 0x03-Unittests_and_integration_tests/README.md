# 0x03. Unittests and Integration Tests

## Project Overview

This project focuses on writing **unit tests** and **integration tests** in Python using the `unittest` framework.  
It demonstrates testing patterns such as **mocking**, **parameterization**, and **memoization**.

The goal is to ensure that functions and methods work correctly in isolation and when integrated with other parts of the system.

---

## Files

- **`utils.py`**  
  Contains utility functions:
  - `access_nested_map`: Accesses nested dictionaries.
  - `get_json`: Retrieves JSON payload from a URL.
  - `memoize`: Decorator to cache method results.

- **`test_utils.py`**  
  Contains unit tests for functions in `utils.py`:
  - Tests `access_nested_map` with normal and edge cases.
  - Tests `get_json` without making real HTTP calls using `unittest.mock.patch`.
  - Tests `memoize` to ensure caching behavior.

---

## Requirements

- Python 3.7+  
- `requests` library  
- `parameterized` library  
- `unittest` module (built-in)  

---

## Installation

Clone the repository and install dependencies:

```bash
git clone <repository_url>
cd 0x03-Unittests_and_integration_tests
pip install -r requirements.txt
