from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS, cross_origin

from ..models.personne import Personne

personne_op = Blueprint("personne_op",__name__,url_prefix="/personnes")


@personne_op.get('/')
@cross_origin()
def personnes():
    personnes=Personne.query.all()
    formated_personnes=[et.format() for et in personnes]
    if personnes is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'personne': formated_personnes,
        'total': len(Personne.query.all()),
    })


@personne_op.get('/<int:id>')
@cross_origin()
def une_personne(id):
    personne=Personne.query.get(id)
    if personne is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_personne": personne.format()

            })

@personne_op.post('/')
@cross_origin()
def add_personne():
    body=request.get_json()
    new_nom=body.get('nom',None)
    new_prenom=body.get('prenom',None)
    new_email=body.get('email',None)
    new_tel=body.get('tel',None)
    new_adresse=body.get('adresse',None)

    personne = Personne(nom=new_nom,prenom=new_prenom,email=new_email,tel=new_tel,adresse=new_adresse)
    personne.insert()
    personnes=Personne.query.all()
    personnes_formatted=[p.format()  for p in personnes]
    return jsonify({
        'success': True,
        'created': personne.id,
        'personnes': personnes_formatted,
        'total_personnes': len(Personne.query.all())
    })


@personne_op.patch('/<int:id>')
@cross_origin()
def mod_personne(id):
    personne=Personne.query.get(id)

    body=request.get_json()
    personne.nom=body.get('nom',None)
    personne.prenom=body.get('prenom',None)
    personne.email=body.get('email',None)
    personne.tel=body.get('tel',None)
    personne.adresse=body.get('adresse',None)
    

    if  personne.nom is None or personne.prenom is None or  personne.email is None or personne.tel is None or personne.adresse is None :
        abort(400)
    else:    
       personne.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_personne": id,
                "New_personne": personne.format()
            })


@personne_op.delete('/<int:id>')
@cross_origin()
def sup_personne(id):
    personne=Personne.query.get(id)
    if personne is None:
        abort(404)
    else:
        personne.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Personne.query.count(),
            
            })