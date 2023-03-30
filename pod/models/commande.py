from pod.extension import db

from pod.models.utilisateur import Utilisateur
from pod.models.client import Client
from pod.models.produits import Produit



class Commande(db.Model):
    __tablename__='commandes'
    id=db.Column(db.Integer,primary_key=True)
    quantite=db.Column(db.Float,nullable=True)
    prix=db.Column(db.Float,nullable=True)
    date=db.Column(db.Date,nullable=False)
    status=db.Column(db.Boolean,nullable=True)
    id_utilisateur=db.Column(db.Integer,db.ForeignKey('utilisateurs.id'),nullable=False)
    id_client=db.Column(db.Integer,db.ForeignKey('clients.id'),nullable=False)
    id_produit=db.Column(db.Integer,db.ForeignKey('produits.id'),nullable=False)
    


    def __init__(self, quantite,prix,date,status,id_utilisateur,id_client,id_produit):
        self.quantite=quantite
        self.date=date
        self.prix=prix
        self.status=status
        self.id_utilisateur=id_utilisateur
        self.id_client=id_client
        self.id_produit=id_produit


    def insert(self):
        db.session.add(self)
        db.session.commit()
   

    def delete(self):
        db.session.delete(self)
        db.session.commit()
     

    def update(self):
         db.session.commit()
         

    def format(self):
        utilisateur=Utilisateur.query.get(self.id_utilisateur)
        client=Client.query.get(self.id_client)
        produit=Produit.query.get(self.id_produit)
        return{
            'id': self.id,
            'quantite': self.quantite,
            'date': self.date,
            'prix':self.prix,
            'status':self.status,
            'id_utilisateur': self.id_utilisateur,
            'id_client': self.id_client,
            'id_produit': self.id_produit,
            'utilisateur': utilisateur.format() if utilisateur is not None else "Command has not save by this user ",
            'client': client.format() if client is not None else "Command has not command by this client",
            'produit': produit.format() if produit is not None else "Command has not command by this product",

            
        }


