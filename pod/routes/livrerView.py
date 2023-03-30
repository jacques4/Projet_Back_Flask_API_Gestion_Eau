from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS, cross_origin

from ..models.livrer import Livrer
from ..models.commande import Commande

livrer_op = Blueprint("livrer_op",__name__,url_prefix="/livrers")

@livrer_op.get('/')
@cross_origin()
def livrers():
    livrers=Livrer.query.order_by(Livrer.id).all()
    formated_livrers=[et.format() for et in livrers]
    if livrers is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'Livrer': formated_livrers,
        'total': len(Livrer.query.all())
    })

@livrer_op.get('/<int:id>')
@cross_origin()
def un_livrer(id):
    livrer=Livrer.query.get(id)
    if livrer is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_livrer": livrer.format()

            })


@livrer_op.post('/')
@cross_origin()
def add_livrer():
    body=request.get_json()
    new_quantite=body.get('quantite',None)
    new_date=body.get('date',None)
    new_status=body.get('status',None)
    new_id_utilisateur=body.get('id_utilisateur',None)
    new_id_commande=body.get('id_commande',None)

    commande = Commande.query.get(new_id_commande)

    if(commande.quantite < new_quantite):
        return jsonify({
        'success': False
         })


    livrer = Livrer(quantite=new_quantite,date=new_date,status=new_status,id_utilisateur=new_id_utilisateur,id_commande=new_id_commande)
    livrer.insert()
    commande.quantite -=livrer.quantite
    commande.update()
    livrers=Livrer.query.order_by(Livrer.id).all()
    livrers_formatted=[p.format()  for p in livrers]
    return jsonify({
        'success': True,
        'created': livrer.id,
        'livrers': livrers_formatted,
        'total_livrers': len(Livrer.query.all())
    })


@livrer_op.patch('/<int:id>')
@cross_origin()
def mod_livrer(id):
    livrer=Livrer.query.get(id)

    body=request.get_json()

    livrer.quantite=body.get('quantite',None)
    livrer.status=body.get('status',None)
    livrer.date=body.get('date',None)
    livrer.id_commande=body.get('id_commande',None)
   
    if livrer.quantite is None or  livrer.status is None or livrer.date is None or livrer.id_commande is None :
        abort(400)
    else:    
       livrer.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_livrer": id,
                "New_livrer": livrer.format()
            })


@livrer_op.delete('/<int:id>')
@cross_origin()
def sup_livrer(id):
    livrer=Livrer.query.get(id)
    if livrer is None:
        abort(404)
    else:
        livrer.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Livrer.query.count(),
            
            })
