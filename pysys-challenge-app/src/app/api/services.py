""" This is the services.py file """
import requests

from flask import make_response
from flask_cors import cross_origin
from datetime import datetime

from src.app.pysys_app import app, db
from src.app.models.models import Person
from src.app.models.enums.group_enum import GroupEnum


@app.route('/api/external/getCnpj/<cnpj>', methods=['GET'])
@cross_origin(origin='*')
def get_cnpj_data(cnpj):
    """ Responses a message from app """

    if cnpj != '':
        headers = {
            'Access-Control-Allow-Origin': '*'
        }
        base_url = "https://www.receitaws.com.br/v1/cnpj/" + cnpj
        res = requests.get(url=base_url, headers=headers)
        response = make_response(res.json(), 200)
        res.close()
    else:
        message = {'error': 'Could not retrieve information about the CNPJ: %s' % cnpj}
        response = make_response(message, 500)
    return response


@app.route("/api/services/addPerson", methods=['POST'])
@cross_origin(origin='*')
def add_person(request):
    """ Responses a message from app """

    person = request.args.get('data')
    message = {}

    try:
        if person:

            person_db = Person()
            person_db.name = person.name
            person_db.email = person.email
            person_db.group = GroupEnum.VENDOR
            person_db.registration_date = datetime.now()

        session = db.session
        session.add(person_db)
        session.commit()
        session.close()

        message.update({'code': 200, 'status': 'ok', 'error': ''})

    except Exception as e:
        message.update({'code': 500, 'error': str(e)})

    return make_response(message, message.code)
