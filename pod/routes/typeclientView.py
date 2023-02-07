from flask import Blueprint,request ,jsonify,abort

from ..models.typeclient import TypeClient

typeclient_op = Blueprint("typeclient_op",__name__,url_prefix="/typeclients")


@typeclient_op.get('/')
def typeclient():
    typeclients=TypeClient.query.all()
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
def add_typeclient():
    body=request.get_json()
    new_nom=body.get('nom',None)
    new_libelle=body.get('libelle',None)
    
    typeclient = TypeClient(nom=new_nom,libelle=new_libelle)
    typeclient.insert()
    typeclients=TypeClient.query.all()
    typeclients_formatted=[p.format()  for p in typeclients]
    return jsonify({
        'success': True,
        'created': typeclient.id,
        'typeclients': typeclients_formatted,
        'total_typeclients': len(TypeClient.query.all())
    })

@typeclient_op.delete('/<int:id>')
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