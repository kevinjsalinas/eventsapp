from flask import request, make_response, session
from flask_restful import Resource
from config import app, db, api
from models import Attendee

from sqlalchemy.exc import IntegrityError


# @app.before_request
# def check_if_logged_in():
#     open_access_list = [
#         'signup',
#         'login',
#         'check_session'
#     ]

#     if (request.endpoint) not in open_access_list and (not session.get('attendee_id')):
#         response = make_response({'error': 'Unauthorized'}, 401)
#         return response


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
            
        response = make_response({'error': 'Unauthorized'}, 401)

        return response

api.add_resource(Login, '/login', endpoint='login')

class CheckSession(Resource):
    
    def get(self):

        if session.get('attendee_id'):

            attendee = Attendee.query.filter_by(id=session['attendee_id']).first()

            attendee_dict = attendee.to_dict()

            response = make_response(attendee_dict, 200)

            return response
        
        response = make_response( {'error': '401 Unauthorized'}, 401)

        return response

api.add_resource(CheckSession, '/check_session', endpoint='check_session')

class Logout(Resource):

    def delete(self):
        
        session['attendee_id'] = None
        
        response = make_response( {}, 204)

        return response

api.add_resource(Logout, '/logout', endpoint='logout')


class Signup(Resource):

    def post(self):
        data = request.get_json()

        new_attendee = Attendee(email=data['email'])

        new_attendee.password_hash = data.get('password')

        try:

            db.session.add(new_attendee)
            db.session.commit()

            session['attendee_id'] = new_attendee.id
            
            new_attendee_dict = new_attendee.to_dict()

            response = make_response(new_attendee_dict, 201)

        except IntegrityError:

            db.session.rollback()

            response = make_response( {'error': 'email already exists' }, 422)

        return response

api.add_resource(Signup, '/signup', endpoint='signup')








if __name__ == '__main__':
    app.run(port=5555, debug=True)