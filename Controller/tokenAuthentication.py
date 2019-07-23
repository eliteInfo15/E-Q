import jwt
from flask import jsonify,request
from app import app
from functools import wraps

def token_required(f):
        @wraps(f)

        def decorated(*args, **kwargs):

            if "token" not in request.form:
                return jsonify({'status': 'token missing'}), 403
            try:
                token = request.form["token"]
                jwt.decode(token, app.config['SECRET_KEY'])
            except:
                return jsonify({'status': 'token is invalid'}), 403
            return f(*args, **kwargs)

        return decorated
