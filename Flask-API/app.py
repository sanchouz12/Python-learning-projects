from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "First_store",
        "items":
        [
            {
                "name": "Item1",
                "price": 12.00
            },
            {
                "name": "Item2",
                "price": 20.00
            }
        ]
    },
    {
        "name": "Second_store",
        "items":
        [
            {
                "name": "Item1",
                "price": 5.00
            }
        ]
    }
]


# homepage of app
@app.route("/")
def home():
    return "Hello from Flask!"


@app.route("/store", methods = ["POST"])
def create_store():
    data = request.get_json()
    new_store = {
        "name": data["name"],
        "items": []
    }

    stores.append(new_store)

    return jsonify(new_store)


# GET by default
@app.route("/store/<string:name>")
def return_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)

    return jsonify({"message": "Store not found"})


@app.route("/store")
def return_all_stores():
    return jsonify({"stores": stores})


@app.route("/store/<string:name>/item", methods = ["POST"])
def create_item(name):
    data = request.get_json()
    new_item = {
        "name": data["name"],
        "price": data["price"]
    }

    for store in stores:
        if store["name"] == name:
            store["items"].append(new_item)

            return jsonify(new_item)

    return jsonify({"message": "Store not found, cannot add item"})


@app.route("/store/<string:name>/item")
def return_all_items(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})

    return jsonify({"message": "Store not found, cannot show all items"})


app.run(port = 5000)
