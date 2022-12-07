# build a new api using flask and python
# this apu must have 5 functions
# the functions are:
# getFood
# deleteFood   recives id
# updateFood   recives id
# addFood
# getFoodByID  recives id
from flask import Flask, request
import json

app = Flask(__name__)

foods = [{"id": 1, "name": "Pasta", "Region": "Italy"},
    {"id": 2, "name": "Hamburger", "Region": "Germany"},
    {"id": 3, "name": "Homos", "Region": "Egypt"},
    {"id": 4, "name": "Sushi", "Region": "Japan"}]


@app.route('/foods', methods=['GET'])
def getFoods():
    return json.dumps(foods)


@app.route('/foods/<int:id>', methods=['DELETE'])
def deleteFood(id):
    for item in foods:
        if item['id'] == id:
            foods.remove(item)
    return json.dumps( foods )


@app.route('/foods/<int:id>', methods=['PUT'])
def updateFood(id):
    newFood = request.json
    for item in foods:
        if item['id'] == id:
            foods.remove(item)
    foods.append(newFood)
    return json.dumps(foods)


@app.route('/foods', methods=['POST'])
def addFood():
    newFood = request.json
    foods.append(newFood)
    return json.dumps(foods)


@app.route('/foods/<int:id>', methods=['GET'])
def getFoodByID(id):
    newFood = list()
    for food in foods:
        if food['id'] == id:
            newFood = food
    return json.dumps(newFood)


app.run()
