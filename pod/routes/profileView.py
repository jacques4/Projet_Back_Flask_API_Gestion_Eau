from flask import Blueprint,request ,jsonify,abort

from ..models.profile import Profile

profile_op = Blueprint("profile_op",__name__,url_prefix="/profiles")


@profile_op.get('/')
def profile():
    profiles=Profile.query.all()
    formated_profiles=[et.format() for et in profiles]
    if profiles is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'profile': formated_profiles,
        'total': len(Profile.query.all())
    })

@profile_op.get('/<int:id>')
def un_profile(id):
    profile=Profile.query.get(id)
    if profile is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_profile": profile.format()

            })

@profile_op.post('/')
def add_profile():
    body=request.get_json()
    new_nom=body.get('nom',None)
    new_libelle=body.get('libelle',None)
    
    profile = Profile(nom=new_nom,libelle=new_libelle)
    profile.insert()
    profiles=Profile.query.all()
    profiles_formatted=[p.format()  for p in profiles]
    return jsonify({
        'success': True,
        'created': profile.id,
        'profiles': profiles_formatted,
        'total_clients': len(Profile.query.all())
    })

@profile_op.delete('/<int:id>')
def sup_profile(id):
    profile=Profile.query.get(id)
    if profile is None:
        abort(404)
    else:
        profile.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Profile.query.count(),
            
            })