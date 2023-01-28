from flask import Blueprint,request ,jsonify,abort
from flask_cors import CORS, cross_origin


from ..models.client import Client

client_op = Blueprint("client_op",__name__,url_prefix="/clients")


@client_op.get('/')
def clients():
    clients=Client.query.all()
    formatted_clients=[et.format() for et in clients]
    if clients is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'Clients': formatted_clients,
        'total': len(Client.query.all())
    })

@client_op.get('/<int:id>')
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
def add_client():
    body=request.get_json()
    new_nom=body.get('nom',None)
    new_prenom=body.get('prenom',None)
    new_email=body.get('email',None)
    new_tel=body.get('tel',None)
    new_adresse=body.get('adresse',None)
    client = Client(nom=new_nom,prenom=new_prenom,email=new_email,tel=new_tel,adresse=new_adresse)
    client.insert()
    clients=Client.query.all()
    clients_formatted=[p.format()  for p in clients]
    return jsonify({
        'success': True,
        'created': client.id,
        'clients': clients_formatted,
        'total_clients': len(Client.query.all())
    })

@client_op.delete('/<int:id>')
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

@client_op.put('/<int:id>')
def mod_client(id):
    client=Client.query.get(id)

    body=request.get_json()
    client.nom=body.get('nom',None)
    client.prenom=body.get('prenom',None)
    client.email=body.get('email',None)
    client.tel=body.get('tel',None)
    client.adresse=body.get('adresse',None)

    if  client.nom is None or client.prenom is None or  client.email is None or client.tel is None or client.adresse:
        abort(400)
    else:    
       client.update()
       return jsonify(
            {
                "Success": True,
                "Update_id_Client": id,
                "New_Client": client.format()
            })

