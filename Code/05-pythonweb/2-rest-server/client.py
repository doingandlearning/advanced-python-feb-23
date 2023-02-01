import requests

baseAddress = "http://127.0.0.1:5000/api/v1/products"


# Helper function, to display the fields for a single product.
def displayProduct(product):
    pstr = "{} {} {} {}".format(product['id'], product['description'], product['price'], product['unitsInStock'])
    print(pstr)
    
# Helper function, to display a collection of products.
def displayAllProducts(products):
    for product in products:
        displayProduct(product)

# This method shows how to make a GET request to the server, to get all products.       
def demoGetAllProducts():
    response = requests.get(baseAddress)
    print(response, baseAddress)
    if response.status_code != 200:
        print("Oops, couldn't get all products")
    else:
        displayAllProducts(response.json())

# This method shows how to make a GET request to the server, to get a single product with a specified id.       
def demoGetOneProduct(id):
    address = baseAddress + "/" + str(id)
    response = requests.get(address)
    if response.status_code != 200:
        print("Oops, couldn't get product " + str(id))
    else:
        displayProduct(response.json())

# This method shows how to make a POST request to the server, to insert a new product.              
def demoInsertProduct():
    product = { "description": "Socks", "price": 3.50, "unitsInStock": 2 }
    response = requests.post(baseAddress, json=product)
    if response.status_code != 201:
        print("Oops, couldn't insert product")
    else:
        displayProduct(response.json())

# This method shows how to make a PUT request to the server, to update an existing product.             
def demoUpdateProduct(id):
    
    # First get a product.
    address = baseAddress + "/" + str(id)
    product = requests.get(address).json()

    # Double its price.
    product['price'] *= 2
    
    # Send it back to the server, to save.
    response = requests.put(address, json=product)
    if response.status_code != 200:
        print("Oops, couldn't update product")
    else:
        displayProduct(response.json())

# This method shows how to make a DELETE request to the server, to delete an existing product.                      
def demoDeleteProduct(id):
    address = baseAddress + "/" + str(id)
    response = requests.delete(address)
    if response.status_code != 204:
        print("Oops, couldn't delete product")
    else:
        print("Product deleted")
        
# Client code.
demoGetAllProducts()
demoGetOneProduct(1)
demoInsertProduct()
# demoUpdateProduct(1)
demoDeleteProduct(2)