from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
import urllib.parse
import requests
import json

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

endpoint = 'https://api.hubapi.com/contacts/v1/contact/?hapikey=408ab40e-3b08-428e-8849-e619a40f9f75'
headers = {}
headers["Content-Type"]="application/json"

@app.route("/dataentry", methods=["POST","GET"])
def submitData():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        name   = post_data.get('name'),
        company  = post_data.get('company')
        email = post_data.get('email')
        firstname = name[0]
        print(firstname)
        print(company)
        print(email)
        data = json.dumps({
            "properties" : [
                {
                "property": "firstname",
                "value": firstname
                },
                {
                    "property": "company",
                    "value": company
                },
                {
                    "property": "email",
                    "value": email
                }
            ]
        })
        print (data)
        r = requests.post(url=endpoint,data=data,headers=headers)
        print(r.text)
        response_object['message'] ='Data added!'
        return jsonify(response_object)

if __name__ == '__main__':    
    app.run(debug=True)