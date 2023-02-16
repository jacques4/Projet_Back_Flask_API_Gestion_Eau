from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS
from flask_cors import cross_origin

from ..models.localite import Localite

localite_op = Blueprint("localite_op",__name__,url_prefix="/localites")


@localite_op.get('/')
@cross_origin()
def localite():
    localites=Localite.query.all()
    formated_localites=[et.format() for et in localites]
    if localites is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'localite': formated_localites,
        'total': len(Localite.query.all())
    })


@localite_op.get('/<int:id>')
@cross_origin()
def une_localite(id):
    localite=Localite.query.get(id)
    if localite is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_localite": localite.format()

            })

@localite_op.post('/')
@cross_origin()
def add_localite():
    body=request.get_json()
    new_nom=body.get('nom',None)
    new_libelle=body.get('libelle',None)
    
    localite = Localite(nom=new_nom,libelle=new_libelle)
    localite.insert()
    localites=Localite.query.all()
    localites_formatted=[p.format()  for p in localites]
    return jsonify({
        'success': True,
        'created': localite.id,
        'localites': localites_formatted,
        'total_localites': len(Localite.query.all())
    })


@localite_op.patch('/<int:id>')
def mod_localite(id):
    localite=Localite.query.get(id)

    body=request.get_json()
    localite.nom=body.get('nom',None)
    localite.libelle=body.get('libelle',None)
    

    if  localite.nom is None or localite.libelle is None :
        abort(400)
    else:    
       localite.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_localite": id,
                "New_localite": localite.format()
            })



@localite_op.delete('/<int:id>')
@cross_origin()
def sup_localite(id):
    localite=Localite.query.get(id)
    if localite is None:
        abort(404)
    else:
        localite.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Localite.query.count(),           
            })