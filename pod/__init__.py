from flask import Flask
from pod.extension import db
from pod.models.utilisateur import Utilisateur

from pod.routes.clientView import client_op
from pod.routes.commandeView import commande_op
from pod.routes.produitView import produits_op
from pod.routes.utilisateurView import utilisateur_op
from pod.routes.profileView import profile_op
from pod.routes.localiteView import localite_op
from pod.routes.typeclientView import typeclient_op
from pod.routes.loginView import login_op
from pod.routes.personneView import personne_op

from .import models
from flask_migrate import Migrate
from pod.extension import db
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager

JWT=JWTManager()

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*"}})
    #cors = CORS(app, support_credentials=True)
    app.config.from_object('config')
    migrate = Migrate(app , db)

    db.init_app(app)
    JWT.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(client_op)
    app.register_blueprint(commande_op)
    app.register_blueprint(produits_op)
    app.register_blueprint(utilisateur_op)
    app.register_blueprint(profile_op)
    app.register_blueprint(localite_op)
    app.register_blueprint(typeclient_op)
    app.register_blueprint(login_op)
    app.register_blueprint(personne_op)

    return app


@JWT.user_identity_loader
def user_identity_lookup(login):
    return login

@JWT.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Utilisateur.query.filter_by(login=identity).one_or_none()


