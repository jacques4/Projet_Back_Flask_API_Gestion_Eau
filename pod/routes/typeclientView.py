from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS, cross_origin

from ..models.typeclient import TypeClient

typeclient_op = Blueprint("typeclient_op",__name__,url_prefix="/typeclients")


@typeclient_op.get('/')
@cross_origin()
def typeclient():
    typeclients=TypeClient.query.order_by(TypeClient.id).all()
    formated_typeclients=[et.format() for et in typeclients]
    if typeclients is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'typeclient': formated_typeclients,
        'total': len(TypeClient.query.all())
    })

@typeclient_op.get('/<int:id>')
@cross_origin()
def un_typeclient(id):
    typeclient=TypeClient.query.get(id)
    if typeclient is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_typeclient": typeclient.format()

            })

@typeclient_op.post('/')
@cross_origin()
def add_typeclient():
    body=request.get_json()
    new_nom=body.get('nom',None)
    new_libelle=body.get('libelle',None)
    
    typeclient = TypeClient(nom=new_nom,libelle=new_libelle)
    typeclient.insert()
    typeclients=TypeClient.query.order_by(TypeClient.id).all()
    typeclients_formatted=[p.format()  for p in typeclients]
    return jsonify({
        'success': True,
        'created': typeclient.id,
        'typeclients': typeclients_formatted,
        'total_typeclients': len(TypeClient.query.all())
    })


@typeclient_op.patch('/<int:id>')
@cross_origin()
def mod_typeclient(id):
    typeclient=TypeClient.query.get(id)

    body=request.get_json()
    typeclient.nom=body.get('nom',None)
    typeclient.libelle=body.get('libelle',None)
    

    if  typeclient.nom is None or typeclient.libelle is None :
        abort(400)
    else:    
       typeclient.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_typeclient": id,
                "New_typeclient": typeclient.format()
            })


@typeclient_op.delete('/<int:id>')
@cross_origin()
def sup_typeclient(id):
    typeclient=TypeClient.query.get(id)
    if typeclient is None:
        abort(404)
    else:
        typeclient.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": TypeClient.query.count(),
            
            })