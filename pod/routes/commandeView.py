from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS, cross_origin
from datetime import datetime

from ..models.commande import Commande
from ..models.produits import Produit

commande_op = Blueprint("commande_op",__name__,url_prefix="/commandes")

@commande_op.get('/')
@cross_origin()
def commandes():
    commandes=Commande.query.order_by(Commande.id).all()
    formated_commandes=[et.format() for et in commandes]
    if commandes is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'Commande': formated_commandes,
        'total': len(Commande.query.all())
    })


@commande_op.get('/<int:id>')
@cross_origin()
def une_commande(id):
   commande=Commande.query.get(id)
   if commande is None:
        abort(404)
   else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_commande": commande.format()

            })

@commande_op.post('/')
@cross_origin()
def add_commande():
    body=request.get_json()
    new_quantite=body.get('quantite',None)
    new_status=body.get('status',None)
    new_id_utilisateur=body.get('id_utilisateur',None)
    new_id_client=body.get('id_client',None)
    new_id_produit=body.get('id_produit',None)

    produit = Produit.query.get(new_id_produit)

    if(produit.quantite < new_quantite):
        return jsonify({
        'success': False
         })

    commande = Commande(quantite=new_quantite,date=datetime.now(),status=new_status,id_utilisateur=new_id_utilisateur,id_client=new_id_client,id_produit=new_id_produit,prix=produit.quantite*new_quantite)
    commande.insert()
    
    produit.quantite -=commande.quantite
    produit.update()
    commandes=Commande.query.order_by(Commande.id).all()
    commandes_formatted=[p.format()  for p in commandes]
    return jsonify({
        'success': True,
        'created': commande.id,
        'commandes': commandes_formatted,
        'total_commandes': len(Commande.query.all())
    })

@commande_op.patch('/<int:id>')
@cross_origin()
def mod_commande(id):
    commande=Commande.query.get(id)

    body=request.get_json()
    body=request.get_json()
    commande.quantite=body.get('quantite',None)
    commande.status=body.get('status',None)
    commande.id_client=body.get('id_client',None)
    commande.id_produit=body.get('id_produit',None)
    

    if commande.quantite is None or  commande.status is None or commande.date is None or commande.id_client is None or commande.id_produit is None :
        abort(400)
    else:    
       commande.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_commande": id,
                "New_commande": commande.format()
            })

@commande_op.delete('/<int:id>')
@cross_origin()
def sup_utilisateur(id):
    commande=Commande.query.get(id)
    if commande is None:
        abort(404)
    else:
        commande.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Commande.query.count(),
            
            })