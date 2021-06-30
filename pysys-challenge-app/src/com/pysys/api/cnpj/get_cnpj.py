""" This is the get_cnpj.py file """
import requests

from flask import make_response, request
from flask_cors import cross_origin

from com.pysys.db.app import app, db


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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
