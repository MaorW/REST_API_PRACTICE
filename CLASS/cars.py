import json
from flask import Flask, request

app = Flask(__name__)

cars = [{'id': 1, 'make': 'audi', 'model': 'A7', 'year': 2022},
        {'id': 2, 'make': 'bmw', 'model': 'x6', 'year': 2021},
        {'id': 3, 'make': 'volvo', 'model': 's90', 'year': 2012},
        {'id': 4, 'make': 'mazda', 'model': '3', 'year': 2015},
        {'id': 5, 'make': 'skoda', 'model': 'Octatvia', 'year': 2014}]

# print(cars[1]) # {'id': 2, 'make': 'bmw', 'model': 'x6', 'year': 2021}

@app.route('/', methods=['GET'])
def home():
    return '<h1 style="color:red;"> I love Cars </h1> '


@app.route('/cars', methods=['GET'])
def getCars():
    return json.dumps(cars)


@app.route('/cars/<int:id>', methods=['GET'])
def getCar(id):
    return json.dumps( cars[id - 1] )


@app.route('/cars/<int:id>', methods=['DELETE'])
def deleteCar(id):
    for car in cars:
        if car['id'] == id:
            cars.remove(car)
    return json.dumps( cars )


@app.route('/cars', methods=['POST'])
def addCar():
      car = request.json
      cars.append(car)
      return "sir yes sir"


@app.route('/cars/<int:id>', methods=['PUT'])
def updateCar(id):
      newCar = request.json
      for car in cars:
            if car['id']==id:
                  cars.remove(car)
      cars.append(newCar)
      return 'updated',299

# app.run() # http://127.0.0.1:5000/cars -> Json
if "__name__"== "__main__":
    app.run()