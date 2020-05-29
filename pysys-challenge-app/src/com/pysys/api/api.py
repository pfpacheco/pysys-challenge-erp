""" This is the api.py file """
from flask import make_response, request
from flask_cors import cross_origin
from datetime import datetime
from json import loads

from com.pysys.db.app import app, db
from com.pysys.orm.person import Person


@app.route("/api/person/addPerson", methods=['POST'])
@cross_origin(origin='*')
def add_person():
    """ Responses a message from com """

    if request.data:
        person = loads(request.data).get("person")
    else:
        return make_response({"code": 500, "status": "error", "message": "Empty request is not allowed!"})

    message = {}
    person_db = Person()

    try:
        if person:
            person_db.name = person.get("name")
            person_db.email = person.get("email")
            person_db.registration_date = datetime.now()

            db.session.add(person_db)
            db.session.commit()

            message.update({"code": 200, "status": "ok", "message": "person number %s was successful inserted" % person_db.id})

        else:
            message.update({"code": 500, "status": "error", "message": "Empty request is not allowed!"})

    except Exception as e:
        message.update({"code": 500, "status": "error", "message": str(e)})

    return make_response(message)


@app.route("/api/person/deletePerson/<person_id>", methods=['GET'])
@cross_origin(origin='*')
def delete_person(person_id):
    """Responses a message from com """

    message = {}
    person_db = Person()

    if person_id:
        try:
            person_db.id = person_id
            db.session.delete(person_db)
            db.session.flush()

            message.update({"code": 200, "status": "ok", "message": "Person id number %s was successful deleted" % person_db.id})

        except Exception as e:
            message.update({"code": 500, "status": "error", "message": str(e)})

        finally:
            db.session.commit()

    else:
        message.update({"code": 500, "status": "error", "message": "Person id number is required!"})

    return make_response(message)


@app.route("/api/person/getPerson/<person_id>", methods=['GET'])
@cross_origin(origin='*')
def get_person(person_id):
    """Responses a message from com """

    message = {}
    person_db = Person()

    if person_id:
        try:
            person_db.id = person_id
            db.session.query(Person).filter_by(id=person_id).all()
            db.session.commit()

            message.update({"code": 200, "status": "ok", "message": "Person id number %s was successful deleted" % person_db.id})

        except Exception as e:
            message.update({"code": 500, "status": "error", "message": str(e)})
    else:
        message.update({"code": 500, "status": "error", "message": "Person id number is required!"})

    return make_response(message)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
