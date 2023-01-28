from flask import Flask
from pod.extension import db

from pod.routes.clientView import client_op
from pod.routes.commandeView import commande_op
from pod.routes.produitView import produits_op
from pod.routes.utilisateurView import utilisateur_op
from pod.routes.profileView import profile_op
from .import models
from flask_cors import CORS, cross_origin


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object('config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(client_op)
    app.register_blueprint(commande_op)
    app.register_blueprint(produits_op)
    app.register_blueprint(utilisateur_op)
    app.register_blueprint(profile_op)

    return app

