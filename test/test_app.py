import pytest
from app import app  # Assuming your app is in a file named `app.py`

# from datetime import datetime

"""
We use pytest.fixture to set up the client.
This creates a test client for Flask,
which simulates requests to your application.
"""


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Test the home route
def test_home(client):
    """Test the home route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, Flask!"  # output check


# Test the hello_there route with a valid name
def test_hello_there_with_name(client):
    """Test the hello_there route with a valid name"""
    name = "John"
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert b"Hello There, John!" in response.data  # different version as above


# Test the hello_there route with an invalid name
# (contains numbers or special characters)
def test_hello_there_with_invalid_name(client):
    """Test the hello_there route with an invalid name"""
    name = "John123!"
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert b"Hello There, Friend!" in response.data


# Test the hello_there route without a name (using the default "Friend")
def test_hello_there_no_name(client):
    """Test the hello_there route without a name"""
    response = client.get("/hello/")
    assert response.status_code == 200
    assert b"Hello There, Friend!" in response.data


# Test the hello_template route with a query parameter
def test_hello_template_with_name(client):
    """Test the hello_template route with a name query parameter"""
    response = client.get("/hello_template/?names=Alice")
    assert response.status_code == 200
    # assert b"Hello, Alice!" in response.data
    assert (
        b"<h1>Hello, Alice!</h1>" in response.data
    )  # Check for the h1 tag instead of plain text
    assert (
        b"Today's date and time is:" in response.data
    )  # Also check for the date and time part


# Test the hello_template route
# without a query parameter (should default to "Friend")


def test_hello_template_no_name(client):
    """Test the hello_template route without a name query parameter"""
    response = client.get("/hello_template/")
    assert response.status_code == 200
    # assert b"Hello, Friend!" in response.data
    assert (
        b"<h1>Hello, Friend!</h1>" in response.data
    )  # Check for the h1 tag instead of plain text
    assert (
        b"Today's date and time is:" in response.data
    )  # Also check for the date and time part
