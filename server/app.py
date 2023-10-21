#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

api = Api(app)

class Plants(Resource):
    def get(self):
        plants = Plant.query.all()

        plants_to_pass=[]
        for plant in plants:
            plants_dict={
                "id":plant.id,
                "name":plant.name,
                "image":plant.image,
                "price":plant.price
            
            }
            plants_to_pass.append(plants_dict)
        response= make_response(jsonify(plants_to_pass), 200)

        return response
    
    def post(self):
        name= request.form.get("name")
        # print(name)
        image= request.form.get("image")
        price= request.form.get("price")

        plant=Plant(name=name, image=image, price=price)
        db.session.add(plant)
        db.session.commit()

        plants_dict={
                "id":plant.id,
                "name":plant.name,
                "image":plant.image,
                "price":plant.price
            
            }
        return make_response(jsonify(plants_dict), 201)

api.add_resource(Plants, "/plants")

class PlantByID(Resource):
    def get(self, id):
        plant=Plant.query.get(id)
        response =None
        if not plant:
            response = make_response("plant does not exist", 200)
            return response
        plants_dict={
                "id":plant.id,
                "name":plant.name,
                "image":plant.image,
                "price":plant.price
            
            }
        response=make_response(jsonify(plants_dict), 200)
        return response
    

    
api.add_resource(PlantByID, "/plants/<int:id>")   
   



if __name__ == '__main__':
    app.run(port=5555, debug=True)
