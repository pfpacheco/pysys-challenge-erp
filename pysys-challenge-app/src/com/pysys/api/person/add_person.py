""" This is the add_person.py file """
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
        return make_response(
            {
                "code": 500,
                "status": "error",
                "message": "Empty request is not allowed!"
            }
        )

    message = {}
    person_db = Person()

    try:
        if person:
            person_db.name = person.get("name")
            person_db.email = person.get("email")
            person_db.registration_date = datetime.now()

            db.session.add(person_db)
            db.session.commit()

            message.update(
                {
                    "code": 200,
                    "status": "ok",
                    "message": "person number %s was successful inserted - %s" % (person_db.id, person_db.__repr__())
                }
            )

        else:
            message.update(
                {
                    "code": 500,
                    "status": "error", "message": "Empty request is not allowed!"
                }
            )

    except Exception as e:
        message.update(
            {
                "code": 500,
                "status": "error",
                "message": "Error adding a new person: %s" % str(e.__cause__)
            }
        )

    return make_response(message)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
