from flask import Blueprint,request ,jsonify,abort
from datetime import timedelta
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token , jwt_required

from ..models.utilisateur import Utilisateur


login_op = Blueprint("login_op",__name__,url_prefix="/login")


@login_op.post('/')
def login():
    if request.is_json:
        login = request.json['login']
        mdp = request.json['mdp']
    else:
        login = request.form['login']
        mdp = request.form['mdp']

    test = Utilisateur.query.filter_by(login=login).first()
    if test != None and check_password_hash(test.mdp, mdp) and test.status == True :
        access_token = create_access_token(identity=login)
        return jsonify(message='Login Successful', user=test.format() , access_token=access_token,status=True)
    else:
        return jsonify(message='Bad login or Password',status=False)


@login_op.get('/dashboard')
@jwt_required()
def dashboard():
    return True
  
