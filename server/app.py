from flask import request, make_response, session
from flask_restful import Resource
from config import app, db, api
from models import Attendee


class Login(Resource):

    def post(self):

        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        attendee = Attendee.query.filter_by(email=email).first()

        if attendee:

            if attendee.authenticate(password):

                session['attendee_id'] = attendee.id

                attendee_dict = attendee.to_dict()

                response = make_response(attendee_dict, 200)

                return response
            
        response = make_response({'error': 'Unauthorized'})

        return response

api.add_resource(Login, '/login')

class CheckSession(Resource):
    
    def get(self):

        if session.get('attendee_id'):

            attendee = Attendee.query.filter_by(id=session['attendee_id']).first()

            attendee_dict = attendee.to_dict()

            response = make_response(attendee_dict, 200)

            return response
        
        response = make_response( {'error': '401 Unauthorized'}, 401)

        return response

api.add_resource(CheckSession, '/check_session')


class Signup(Resource):

    pass

api.add_resource(Signup, '/signup')








if __name__ == '__main__':
    app.run(port=5555, debug=True)