from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS
from flask_cors import cross_origin

from ..models.marque import Marque

marque_op = Blueprint("marque_op",__name__,url_prefix="/marques")


@marque_op.get('/')
@cross_origin()
def marque():
    marques=Marque.query.order_by(Marque.id).all()
    formated_marques=[et.format() for et in marques]
    if marques is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'marque': formated_marques,
        'total': len(Marque.query.all())
    })


@marque_op.get('/<int:id>')
@cross_origin()
def une_marque(id):
    marque=Marque.query.get(id)
    if marque is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_marque": marque.format()

            })

@marque_op.post('/')
@cross_origin()
def add_marque():
    body=request.get_json()
    new_nom=body.get('nom',None)
    
    marque = Marque(nom=new_nom)
    marque.insert()
    marques=Marque.query.order_by(Marque.id).all()
    marques_formatted=[p.format()  for p in marques]
    return jsonify({
        'success': True,
        'created': marque.id,
        'marques': marques_formatted,
        'total_marques': len(Marque.query.all())
    })


@marque_op.patch('/<int:id>')
def mod_marque(id):
    marque=Marque.query.get(id)

    body=request.get_json()
    marque.nom=body.get('nom',None)
    
    if  marque.nom is None :
        abort(400)
    else:    
       marque.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_marque": id,
                "New_marque": marque.format()
            })



@marque_op.delete('/<int:id>')
@cross_origin()
def sup_marque(id):
    marque=Marque.query.get(id)
    if marque is None:
        abort(404)
    else:
        marque.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Marque.query.count(),           
            })