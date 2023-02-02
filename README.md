# FASTAPI_learning

API endpoint is the point of entry in a communication channel when two systems are interacting.
It refers to touch points of the communication between an API and a server.
For instance, in localhost/hello, /hello is the endpoint

Methods used in the practice code for the endpoint are:
GET: Asks the endpoint to get something and return it.
POST: Sends information to the endpoint like creating something new or adding information to the database
PUT: Updates information or modify
DELETE: Deletes information

The advantages of using FASTAPI are Data Validation, Auto Documentation, Auto Completion and Code Suggestion.
The variable defined in the `working.py` resets everytime the server restarts. So if we add any items, we cannot get the added item after restarting of server.

```shell
    @app.get("/get-item/{item_id}/{name}")
    def get_item(item_id: int, name: str):
        return inventory[item_id]
    # In item_id, if we pass anything except int, FASTAPI automatically returns an error
```
There are two parameters i.e path parameters and query parameters. Path parameters are required to be provided with some value while Query parameters can be made optional.
Query parameter is written after the `?` sign and for passing second query, we use `&` like in `facebook.com/home?redirect=/bibek&msg=sucess`
In `@app.get("/get-item/{item_id}/{name}")`, `item_id` and `name` are path parameters.

When we add the information in any database, we don't send them in query and path parameters, we send them in request body.

```shell
    @app.post("/create-item/{item_id}")
    def create_item(item_id: int, item: Item):
    # Here the datatype of item is our custom class, so it tells FASTAPI that this is for the request body not the query parameter
```

`inventory[item_id].update(item)` takes this called item and updates the item which is already present in inventory[item_id]. If item doesn't contain anything, it will not be changed. Only the above can be used if inventory[item_id] returns a python dictionary not object instance.

Status codes is returned everytime we call the HTTTP endpoint. For instance: 200-OK, 202-CREATED, 404:NOT FOUND, etc.
