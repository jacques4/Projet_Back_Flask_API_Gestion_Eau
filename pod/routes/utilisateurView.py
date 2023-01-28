from flask import Blueprint,request ,jsonify,abort

from ..models.utilisateur import Utilisateur

utilisateur_op = Blueprint("utilisateur_op",__name__,url_prefix="/utilisateurs")


@utilisateur_op.get('/')
def utilisateurs():
    utilisateurs=Utilisateur.query.all()
    formated_utilisateurs=[et.format() for et in utilisateurs]
    if utilisateurs is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'utilisateurs': formated_utilisateurs,
        'total': len(Utilisateur.query.all())
    })


@utilisateur_op.get('/<int:id>')
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
def add_utilisateur():
    body=request.get_json()
    new_matricule=body.get('matricule',None)
    new_nom=body.get('nom',None)
    new_prenom=body.get('prenom',None)
    new_email=body.get('email',None)
    new_tel=body.get('tel',None)
    new_login=body.get('login',None)
    new_mdp=body.get('mdp',None)
    new_status=body.get('status',None)
    new_adresse=body.get('adresse',None)
    new_id_profile=body.get('id_profile',None)

    utilisateur = Utilisateur(matricule=new_matricule,nom=new_nom,prenom=new_prenom,email=new_email,tel=new_tel,login=new_login,mdp=new_mdp,status=new_status,adresse=new_adresse,id_profile=new_id_profile)
    utilisateur.insert()
    utilisateurs=Utilisateur.query.all()
    utilisateurs_formatted=[p.format()  for p in utilisateurs]
    return jsonify({
        'success': True,
        'created': utilisateur.id,
        'utilisateurs': utilisateurs_formatted,
        'total_utilisateurs': len(Utilisateur.query.all())
    })

@utilisateur_op.delete('/<int:id>')
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