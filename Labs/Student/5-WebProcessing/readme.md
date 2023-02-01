# Python Web Processing

## Overview 

In this lab, you'll add some routes to parse some routes and carry out some work.

## Roadmap


- 1) Add a get route at "/hello"
- 2) Add a get route at "/hello/<name>"
- 3) Add a get route at "/fib"
- 4) Add a 404 page
- 5) Create a client file that will fetch from `/fib` and print the result.

## Exercise 1: Add a get route at "/hello"

- At a `do_GET` function to the handler class
- Check that the path is "/hello"
- Set the status code to 200
- Set the content type to text/html
- Set the response to Hello world!
- Send the response.

## Exercise 2: Add a get route at "/hello/<name>"

- If you haven't used an if statement in the handler, then add one in now
- Add an elif to check if the path starts with "/hello/"
- Split the path and extract the name
- Set the status code to 200
- Set the content type to text/html
- Set the response to Hello <name>!
- Send the response.

## Exercise 3: Add a get route at "/fib"

- Import the fib function
- Instantiate it before the start of the handler class
- Add another elif to test for "/fib"
- Send back the result with the correct status and content type.

## Exercise 4: Add a 404 page

- Handler any other path by sending back a status of 404 and a helpful message

## Exercise 5: Create a client file that will fetch from `/fib` and print the result.

- Import requests 
- Use this to fetch from the /fib route on your server
- Print the result to the console