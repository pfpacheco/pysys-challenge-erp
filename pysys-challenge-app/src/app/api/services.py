import requests
from flask import Request, Response, make_response
from flask_cors import cross_origin

from src.app.pysys_app import app


@app.route(
    "/api/external/searchCnpj",
    methods=["POST", "GET"]
)
@cross_origin()
def search_for_cnpj(request: Request, response: Response):

    url = "https://www.receitaws.com.br/v1/cnpj/"

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json"
    }

    cnpj = request.args.get("cnpj")

    if cnpj is not None and cnpj != "":
        res = requests.get(url=url + cnpj, params=headers)
        response = make_response(res.json(), 200)
        res.close()
    else:
        message = {"cnpj": cnpj, "error": "The request does not produced any result"}
        response = make_response(message, 400)
    return response

