#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import os
import json

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class HelloWorld(Resource):
    # for Health Check
    def get(self):
        return {'hello': 'world'}


class Calc(Resource):
    # REST Service Main
    def post(self):
        args = parser.parse_args()
        try:
            dic = json.loads(args.json)
            if self.auth(dic['username'],dic['password']):
                ans = float(dic['a']) * float(dic['b'])
                return {'ans': ans }
            else:
                return {'error': '401'}
        except:
            abort(500, message="internal server error")

    # for Authentication
    def auth(self,u,p):
        if u == "takara" and p == "hogehoge":
            return True
        else:
            return False



if __name__ == '__main__':
    parser.add_argument('json')
    api.add_resource(HelloWorld, '/')
    api.add_resource(Calc, '/calc')
    bx_port = os.getenv("PORT")
    listen_port = int(bx_port if bx_port else 5000)
    app.run(host='0.0.0.0', port=listen_port, debug=True)

