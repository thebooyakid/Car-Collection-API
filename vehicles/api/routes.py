from flask import Blueprint, request, jsonify
from vehicles.helpers import token_required, JSONEncoder
from models import db, User, Car, car_schema, cars_schema


api = Blueprint('api',__name__,url_prefix='/api')

@api.route('/getdata')
def getdata():
    return{'some': 'value'}

@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    price = request.json['price']
    mpg = request.json['mpg']
    color = request.json['color']
    weight = request.json['weight']
    upgrades = request.json['upgrades']
    condition = request.json['condition']
    user_token = current_user_token.token

    print(f"TEST: {current_user_token.token}")

    car = Car(make,model,year,price,mpg,color,weight,upgrades,condition,user_token = user_token)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        car = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401
    
@api.route('/cars/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token,id):
    car = Car.query.get(id) #get car instance
    car.make = request.json['make']
    car.model = request.json['model']
    car.year = request.json['year']
    car.price = request.json['price']
    car.mpg = request.json['mpg']
    car.color = request.json['color']
    car.weight = request.json['weight']
    car.upgrades = request.json['upgrades']
    car.condition = request.json['condition']
    car.user_token = current_user_token.token
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

