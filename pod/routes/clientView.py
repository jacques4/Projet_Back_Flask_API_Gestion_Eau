from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token, create_refresh_token , jwt_required ,current_user
from datetime import datetime

from ..models.client import Client

client_op = Blueprint("client_op",__name__,url_prefix="/clients")


@client_op.get('/')
@cross_origin()
def clients():
    clients=Client.query.order_by(Client.id).all()
    formatted_clients=[et.format() for et in clients]
    if clients is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'Clients': formatted_clients,
        'total': len(Client.query.all()),
 
    })

@client_op.get('/<int:id>')
@jwt_required()
@cross_origin()
def un_client(id):
    client=Client.query.get(id)
    if client is None:
        abort(404)
    else:
        return jsonify({

                "Success": True,
                "selected": id,
                "Selected_client": client.format()

            })

@client_op.post('/')
@cross_origin()
def add_client():
    body=request.get_json()
    new_nom=body.get('nom',None)
    new_prenom=body.get('prenom',None)
    new_email=body.get('email',None)
    new_tel=body.get('tel',None)
    new_longi=body.get('longi',None)
    new_lat=body.get('lat',None)
    new_adresse=body.get('adresse',None)
    new_nif=body.get('nif',None)
    new_numrccm=body.get('numrccm',None)
    new_id_typeclient=body.get('id_typeclient',None)
    new_id_utilisateur=body.get('id_utilisateur',None)
    client = Client(nom=new_nom,prenom=new_prenom,email=new_email,tel=new_tel,adresse=new_adresse,id_typeclient=new_id_typeclient,id_utilisateur=new_id_utilisateur,longi=new_longi,lat=new_lat, numrccm=new_numrccm,nif=new_nif,date=datetime.now())
    client.insert()
    clients=Client.query.order_by(Client.id).all()
    clients_formatted=[p.format()  for p in clients]
    return jsonify({
        'success': True,
        'created': client.id,
        'clients': clients_formatted,
        'total_clients': len(Client.query.all())
    })

@client_op.patch('/<int:id>')
@cross_origin()
def mod_client(id):
    client=Client.query.get(id)

    body=request.get_json()
    client.nom=body.get('nom',None)
    client.prenom=body.get('prenom',None)
    client.email=body.get('email',None)
    client.tel=body.get('tel',None)
    client.adresse=body.get('adresse',None)
    client.id_typeclient=body.get('id_typeclient',None)
    client.nif=body.get('nif',None)
    client.numrccm=body.get('numrccm',None)
    
    if client.nom is None or client.prenom is None or  client.email is None or client.tel is None or client.adresse is None or client.id_typeclient is None or client.nif is None or client.numrccm is None :
        abort(400)
    else:    
       client.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_client": id,
                "New_client": client.format()
            })



@client_op.delete('/<int:id>')
@cross_origin()
def sup_client(id):
    client=Client.query.get(id)
    if client is None:
        abort(404)
    else:
        client.delete()
        return jsonify(
            {
                "delete_id": id,
                "Success": True,
                "Total": Client.query.count(),
            
            })


