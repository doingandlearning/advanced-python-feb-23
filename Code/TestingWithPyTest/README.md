## Overview

This Flask application contains the basic user management functionality (register, login, logout) to demonstrate how to test a Flask project using [pytest](https://docs.pytest.org/en/stable/).

For details on how to test a Flask app using pytest, check out my blog post on [TestDriven.io](https://testdriven.io/):

* [https://testdriven.io/blog/flask-pytest/](https://testdriven.io/blog/flask-pytest/)

![Testing Flask Applications with Pytest](project/static/img/flask_pytest_social.png?raw=true "Testing Flask Applications with Pytest")

## Motivation

After reading [Python Testing with pytest](https://pragprog.com/titles/bopytest/python-testing-with-pytest/) by Brian Okken, I was convinced that I should learn about pytest and then figure out how to use it to test Flask applications.

## Installation Instructions

### Installation

Pull down the source code from this GitLab repository:

```sh
$ git clone git@gitlab.com:patkennedy79/flask_user_management_example.git
```

Create a new virtual environment:

```sh
$ cd flask_user_management_example
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages specified in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

### Database Initialization

This Flask application needs a SQLite database to store data.  The database should be initialized using:

```
(venv) $ flask init_db
```

### Running the Flask Application

Run development server to serve the Flask application:

```sh
(venv) $ flask --app app --debug run
```

Navigate to 'http://127.0.0.1:5000' in your favorite web browser to view the website!

## Key Python Modules Used

* **Flask**: micro-framework for web application development which includes the following dependencies:
  * click: package for creating command-line interfaces (CLI)
  * itsdangerous: cryptographically sign data 
  * Jinja2: templating engine
  * MarkupSafe: escapes characters so text is safe to use in HTML and XML
  * Werkzeug: set of utilities for creating a Python application that can talk to a WSGI server
* **pytest**: framework for testing Python projects
* **Flask-SQLAlchemy** - ORM (Object Relational Mapper) for Flask
* **Flask-Login** - support for user management (login/logout) in Flask
* **Flask-WTF** - simplifies forms in Flask
* **flake8** - static analysis tool

This application is written using Python 3.10.

## Testing

To run all the tests:

```sh
(venv) $ python -m pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ python -m pytest --cov-report term-missing --cov=project
```
