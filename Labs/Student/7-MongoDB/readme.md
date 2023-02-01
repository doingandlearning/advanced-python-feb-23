# MongoDB

## Overview

In this lab, you'll write a script that will carry out a series of operations on a database. 

If time permits, you'll link this database to a web server.

Source folders
Student folder​: Labs\Student\7-FunctionalProg
Solution folder: Labs\Solutions\7-FunctionalProg

## Roadmap

There are 7 exercises with the last one being available if time permits.

- 1) Create a MongoClient object and connect to the database
- 2) Insert 10 documents to a "products" collection
- 3) Find all documents in the "products" collection and prints them to the console
- 4) Update the price of all products that have a quantity of less than 10 to be 10% more expensive.
- 5) Deletes all products that have a price greater than £50.
- 6) Prints the number of products remaining in the collection to the console
- 7) (if time permits) - link this database to a webserver


## Exercise 1: Create a MongoClient object and connect to the database

Get the connection string for your database, either locally or from MongoDB Atlas. 

Connect to the database and capture a handle to the database and another handle to a collection called `products`.


## Exercise 2 - Insert 10 documents to a "products" collection

Insert 10 products into the database. They should be in the format:

```
{
	"name": string,
	"price": number,
	"quantity": number
}
```

## Exercise 3 - Find all documents in the "products" collection and prints them to the console

Find all of the documents in the products collection and print them to the console.


## Exercise 4 - Update the price of products 

- Find all of the products that have a quantity of less than 10
- Increase the price of these products by 10%


## Exercise 5 - Deletes products

- Find all the products that have a price of £50
- Delete these

## Exercise 6 - Prints the number of products remaining in the collection to the console

- Find all of the remaining products in the collection
- Print the number of products

## Exercise 7 (if time permits) - link this database to a webserver

- Set up a webserver (using Flask or HTTP)
- Setup the following routes:
	- GET /api/products - get all products
	- POST /api/products - create new product
	- GET /api/products/<id> - get product by id
	- PATCH /api/products/<id> - update a product
	- DELETE /api/products/<id> - delete product