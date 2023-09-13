from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

api = Blueprint('api', __name__)#define routes separately from main app

#database model(person)
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@api.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    new_person = Person(name=data['name'])
    db.session.add(new_person)
    db.session.commit()

    return jsonify({'message': 'Person created successfully', 'person_id': new_person.id})

@api.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify({'id': person.id, 'name': person.name})

@api.route('/api/<int:person_id>', methods=['PUT', 'PATCH'])
def update_person(person_id):
    data = request.get_json()
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    person.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Person updated successfully', 'person_id': person.id})

@api.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})


app.register_blueprint(api)

if __name__ == "__main__":
    db.create_all()
    app.run(port=5001)


