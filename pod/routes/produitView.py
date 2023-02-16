from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS, cross_origin

from ..models.produits import Produit

produits_op = Blueprint("produits_op",__name__,url_prefix="/produits")


@produits_op.get('/')
@cross_origin()
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

@produits_op.get('/<int:id>')
@cross_origin()
def un_produit(id):
    produit=Produit.query.get(id)
    if produit is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_produit": produit.format()

            })

@produits_op.post('/')
@cross_origin()
def add_produit():
    body=request.get_json()
    new_nom=body.get('nom',None)
    new_quantite=body.get('quantite',None)
    new_prix=body.get('prix',None)
    new_description=body.get('description',None)
    new_date=body.get('date',None)
    new_id_utilisateur=body.get('id_utilisateur',None)

    produit = Produit(nom=new_nom,quantite=new_quantite,prix=new_prix,description=new_description,date=new_date,id_utilisateur=new_id_utilisateur)
    produit.insert()
    produits=Produit.query.all()
    produits_formatted=[p.format()  for p in produits]
    return jsonify({
        'success': True,
        'created': produit.id,
        'produits': produits_formatted,
        'total_produits': len(Produit.query.all())
    })


@produits_op.patch('/<int:id>')
@cross_origin()
def mod_produit(id):
    produit=Produit.query.get(id)

    body=request.get_json()
    produit.nom=body.get('nom',None)
    produit.quantite=body.get('quantite',None)
    produit.prix=body.get('prix',None)
    produit.description=body.get('description',None)
    produit.date=body.get('date',None)
    

    if produit.nom is None or produit.quantite is None or  produit.prix is None or produit.description is None or produit.date is None :
        abort(400)
    else:    
       produit.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_produit": id,
                "New_produit": produit.format()
            })

@produits_op.delete('/<int:id>')
@cross_origin()
def sup_produit(id):
    produit=Produit.query.get(id)
    if produit is None:
        abort(404)
    else:
        produit.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Produit.query.count(),
            
            })