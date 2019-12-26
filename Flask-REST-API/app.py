import random

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, item_id):
        # bad request
        try:
            int(item_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        item = next(filter(lambda x: str(x["id"]) == item_id, items), None)

        return {"item": item}, 200 if item else 404

    def post(self, item_id):
        try:
            int(item_id)
        except ValueError:
            return {"message": "Bad id format"}, 400

        if next(filter(lambda x: str(x["id"]) == item_id, items), None):
            return {"message": "Item with id '{}' already exists".format(item_id)}, 400

        data = request.get_json()

        item = {
            "id": item_id,
            "name": data["name"],
            "price": data["price"],
            "description": data["description"]
        }
        items.append(item)
        return {"item": item}, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:item_id>")
api.add_resource(ItemList, "/items")

app.run(port = 5000, debug = True)
