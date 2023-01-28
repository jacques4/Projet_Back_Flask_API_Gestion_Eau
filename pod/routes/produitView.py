from flask import Blueprint,request ,jsonify,abort

from ..models.produits import Produit

produits_op = Blueprint("produits_op",__name__,url_prefix="/produits")


@produits_op.get('/')
def produits():
    produits=Produit.query.all()
    formated_produits=[et.format() for et in produits]
    if produits is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'produits': formated_produits,
        'total': len(Produit.query.all())
    })