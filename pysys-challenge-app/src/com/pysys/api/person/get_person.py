""" This is the get_person.py file """
from flask import make_response, request
from flask_cors import cross_origin

from com.pysys.db.app import app, db
from com.pysys.orm.person import Person


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
    app.run(host="127.0.0.1", port=5003)
