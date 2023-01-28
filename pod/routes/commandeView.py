from flask import Blueprint,request ,jsonify,abort

from ..models.commande import Commande

commande_op = Blueprint("commande_op",__name__,url_prefix="/commandes")

@commande_op.get('/')
def commandes():
    commandes=Commande.query.all()
    formated_commandes=[et.format() for et in commandes]
    if commandes is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'Commande': formated_commandes,
        'total': len(Commande.query.all())
    })