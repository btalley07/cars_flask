from flask import Blueprint, request,jsonify
from cars_inventory.helpers import token_required
from cars_inventory.models import db, User, Character, cars_schema, cars_schemas

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return { 'some': 'value'}


# Create Marvel Endpoint
@api.route('/cars',methods = ['POST'])
@token_required
def create_car(current_user_token):
    name = request.json['name']
    description = request.json['description']
    make = request.json['make']
    model = request.json['model']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    car = Cars(name,description,make,model,user = user_token)

    db.session.add(car)
    db.session.commit()

    response = cars_schema.dump(car)
    return jsonify(response)


 # Retrieve all characters endpoint
@api.route('/cars', methods = ['GET'])
@token_required
def get_car(current_user_token):
    owner = current_user_token.token
    car = Cars.query.filter_by(user = owner).all()
    response = cars_schemas.dump(car)
    return jsonify(response)

# Retrieve one characters endpoint
@api.route('/car/<id>', methods =['GET'])
@token_required
def get_car(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        car = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({'message': "Valid Token Required"}), 401

# UPDATE characters ENDPOINT
@api.route('/car/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token,id):
    car = Car.query.get(id) 
    name = request.json['name']
    description = request.json['description']
    make = request.json['make']
    model = request.json['model']
    
    user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# DELETE character ENDPOINT
@api.route('/car/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)