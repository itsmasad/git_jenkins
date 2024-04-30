import pytest

def test_solution(setUp):
    driver = setUp
    driver.get("https://www.google.com")
    str_value = "This is a demo code"
    n_value = 1
    assert n_value == 1
    # Add more assertions or tests as needed


