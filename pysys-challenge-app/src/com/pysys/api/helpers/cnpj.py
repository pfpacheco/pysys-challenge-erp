""" This is the helper for CNPJ operations """
from flask import make_response, request
from flask_cors import cross_origin
from com.pysys.db.app import app


@app.route('/api/external/getCnpj/<cnpj>', methods=['GET'])
@cross_origin(origin='*')
def get_cnpj(cnpj):
    """ Responses a message from com """

    if cnpj != '':
        headers = {
            'Access-Control-Allow-Origin': '*'
        }
        base_url = "https://www.receitaws.com.br/v1/cnpj/" + cnpj
        res = request.get(url=base_url, headers=headers)
        response = make_response(res.json(), 200)
        res.close()
    else:
        message = {'error': 'Could not retrieve information about the CNPJ: %s' % cnpj}
        response = make_response(message, 500)
    return response
