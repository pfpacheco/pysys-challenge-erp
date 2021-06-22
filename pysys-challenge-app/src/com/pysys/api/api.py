""" This is the api.py file """
import requests

from flask import make_response, request
from flask_cors import cross_origin
from datetime import datetime
from json import loads

from com.pysys.db.app import app, db
from com.pysys.orm.person import Person


@app.route('/api/external/getCnpj/<cnpj>', methods=['GET'])
@cross_origin(origin='*')
def get_cnpj(cnpj):
    """ Responses a message from com """

    if cnpj != '':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        base_url = "https://www.receitaws.com.br/v1/cnpj/" + cnpj
        res = requests.get(url=base_url, headers=headers)
        response = make_response(res.json(), 200)
        res.close()
    else:
        message = \
            {
                "error": "Could not retrieve information about the CNPJ: %s" % cnpj
            }
        response = make_response(message, 500)
    return response


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

            message.update(
                {
                    "code": 200,
                    "status": "ok",
                    "message": "Person id number %s was successful deleted" % person_db.id
                }
            )

        except Exception as e:
            message.update(
                {
                    "code": 500,
                    "status": "error",
                    "message": str(e)
                }
            )

        finally:
            db.session.commit()

    else:
        message.update(
            {
                "code": 500,
                "status": "error",
                "message": "Person id number is required!"
            }
        )

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

            message.update(
                {
                    "code": 200,
                    "status": "ok",
                    "message": "Person id number %s was successful deleted" % person_db.id
                }
            )

        except Exception as e:
            message.update(
                {
                    "code": 500,
                    "status": "error",
                    "message": str(e)
                }
            )
    else:
        message.update(
            {
                "code": 500,
                "status": "error",
                "message": "Person id number is required!"
            }
        )

    return make_response(message)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
