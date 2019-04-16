from flask import Flask
import json
from flask_restful import Api, Resource, reqparse
import os

app = Flask(__name__)
api = Api(app)

json_file_directory = ''


class TICKET_lookup(Resource):
    def get(self, TICKET):
        if(os.path.exists(TICKET + '.json')):
            with open (TICKET + '.json', 'r') as json_file:
                TICKET_data = json.load(json_file)
            return TICKET_data, 200
        return "Ticket data not found", 404
    def delete(self, TICKET):
        if(os.path.exists(TICKET + '.json')):
            os.remove(TICKET + '.json')
            return "Ticket number " + TICKET + " data deleted", 200
        return "Ticket data not found", 404
class TICKET_create(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("TICKET")
        parser.add_argument("EMAIL")
        parser.add_argument("LOCATION")
        args = parser.parse_args()
        if(os.path.exists(args["TICKET"] + '.json')):
            return "Ticket data already exists", 400
        TICKET_data = {
            "TICKET": args["TICKET"],
            "EMAIL": args["EMAIL"],
            "LOCATION": args["LOCATION"]
        }
        with open (args["TICKET"] + '.json', 'w+') as json_file:
            json.dump(TICKET_data, json_file, indent=4)
        return TICKET_data, 201
class TICKET_closed(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("TICKET")
        parser.add_argument("EMAIL")
        parser.add_argument("LOCATION")
        args = parser.parse_args()

        return TICKET_data, 201
api.add_resource(TICKET_lookup, "/api/v0/ticket/<string:TICKET>")
api.add_resource(TICKET_create, "/api/v0/ticket/create_ticket")
api.add_resource(TICKET_create, "/api/v0/ticket/closed_ticket")
app.run(host='0.0.0.0', port=8080, debug=True)
