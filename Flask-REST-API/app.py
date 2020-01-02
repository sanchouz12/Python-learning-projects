from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from dotenv import load_dotenv
import os

from security import authenticate, identity

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
api = Api(app)

# /auth
# returns token, if everything is ok
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    @jwt_required()
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
