# 0x03. Unittests and Integration Tests

## Project Description

This project focuses on understanding and implementing unit testing and integration testing in Python using the `unittest` framework.  
It includes testing patterns such as mocking, parameterization, and decorators.  

The project aims to:
- Differentiate between unit tests and integration tests.
- Practice mocking external calls using `unittest.mock`.
- Parameterize tests for multiple inputs using `parameterized`.
- Test function logic without making actual HTTP calls.
- Test caching decorators.

---

## Files

| File                | Description                                                                                   |
|---------------------|-----------------------------------------------------------------------------------------------|
| `utils.py`         | Contains the functions `access_nested_map`, `get_json`, and the `memoize` decorator.         |
| `test_utils.py`    | Contains unit tests for `utils.py` using the `unittest` framework and `parameterized`.       |
| `fixtures.py`      | Contains fixtures for testing (if applicable).                                              |
| `README.md`        | Project description and instructions.                                                        |

---

## Requirements

- Python 3.7+
- `parameterized` library
- `requests` library
- `unittest` standard library

Install requirements with:

```bash
pip install parameterized requests
