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

@produits_op.get('/<int:id>')
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

@produits_op.delete('/<int:id>')
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