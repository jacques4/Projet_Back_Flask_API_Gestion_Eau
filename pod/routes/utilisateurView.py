from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS, cross_origin
from werkzeug.security import check_password_hash,generate_password_hash

from ..models.utilisateur import Utilisateur
from ..models.personne import Personne
from ..models.profile import Profile

utilisateur_op = Blueprint("utilisateur_op",__name__,url_prefix="/utilisateurs")


@utilisateur_op.get('/')
@cross_origin()
def utilisateurs():
    utilisateurs=Utilisateur.query.order_by(Utilisateur.id).all()
    formated_utilisateurs=[et.format() for et in utilisateurs]
    if utilisateurs is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'utilisateurs': formated_utilisateurs,
        'total': len(Utilisateur.query.all()),
    })


@utilisateur_op.get('/<int:id>')
@cross_origin()
def un_utilisateur(id):
    utilisateur=Utilisateur.query.get(id)
    if utilisateur is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_utilisateur": utilisateur.format()

            })

@utilisateur_op.post('/')
@cross_origin()
def add_utilisateur():
    body=request.get_json()
    new_matricule=body.get('matricule',None)
    new_login=body.get('login',None)
    new_mdp=body.get('mdp',None)
    new_status=body.get('status',None)
    new_id_profile=body.get('id_profile',None)
    new_id_localite = body.get('id_localite',None)
    new_id_personne = body.get('id_personne',None)
    new_id_utilisateur = body.get('id_utilisateur',None)

    utilisateur = Utilisateur(matricule=new_matricule,login=new_login,mdp=generate_password_hash(new_mdp) ,status=new_status,id_profile=new_id_profile,id_personne=new_id_personne,id_localite=new_id_localite,id_utilisateur=new_id_utilisateur)
    utilisateur.insert()
    utilisateurs=Utilisateur.query.order_by(Utilisateur.id).all()
    utilisateurs_formatted=[p.format()  for p in utilisateurs]
    return jsonify({
        'success': True,
        'created': utilisateur.id,
        'utilisateurs': utilisateurs_formatted,
        'total_utilisateurs': len(Utilisateur.query.all())
    })


@utilisateur_op.patch('/<int:id>')
@cross_origin()
def mod_utilisateur(id):
    utilisateur=Utilisateur.query.get(id)

    body=request.get_json()
    utilisateur.matricule=body.get('matricule',None)
    utilisateur.login=body.get('login',None)
    utilisateur.status=body.get('status',None)
    utilisateur.id_profile=body.get('id_profile',None)
    utilisateur.id_personne=body.get('id_personne',None)
    utilisateur.id_localite=body.get('id_localite',None)
    

    if utilisateur.matricule is None or utilisateur.login is None or  utilisateur.status is None or utilisateur.id_profile is None or utilisateur.id_personne is None or utilisateur.id_localite is None :
        abort(400)
    else:    
       utilisateur.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_utilisateur": id,
                "New_utilisateur": utilisateur.format()
            })

@utilisateur_op.delete('/<int:id>')
@cross_origin()
def sup_utilisateur(id):
    utilisateur=Utilisateur.query.get(id)
    if utilisateur is None:
        abort(404)
    else:
        utilisateur.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Utilisateur.query.count(),
            
            })