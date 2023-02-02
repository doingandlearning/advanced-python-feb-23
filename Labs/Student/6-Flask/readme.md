

## Exercise 1: Create a Hello World

- Create a basic Flask application that returns "Hello, World!" when you access the root URL.

## Exercise 2: Routing and Request Handling

This exercise will cover how to use Flask to handle different types of HTTP requests and route them to the appropriate handlers.

- Create a new endpoint that handles GET requests to the path "/greet/<name>", where "name" is a variable passed in the URL. This endpoint should return a greeting message with the provided name.

- Create a new endpoint that handles POST requests to the path "/greet", which takes a JSON object containing a "name" field and returns a greeting message with the provided name.

## Exercise 3: Creating a RESTful API

In this exercise, you'll use flask_restful to create a more structured, restful API.

- Convert the existing application to use Flask_RESTful instead of Flask's built-in routing.
- Create a new resource for managing "users", which supports GET, POST, PUT, and DELETE operations.

Start with this code and work on each verb individually:

```python
users = {}
nextId = 1


class UserList(Resource):
    def get(self):
		pass

    def post(self):
        pass

    def patch(self, id):
        pass

    def delete(self, id):
        pass
```

## Exercise 4: Add an authentication middleware

Add a function that will run before every request. It should check for the existence of an authentication header and test the value against a hard-coded one.

Note: In production we should have secret data like this stored in environment variables outside of source control.

## Optional Exercise 5: 

Create a proxy to Geolocate by IP address.

Here's the URL: 
https://ipgeolocation.abstractapi.com/v1/?api_key=40f78db40af64d159e2a83ebd1ba5bdb&127.0.0.1