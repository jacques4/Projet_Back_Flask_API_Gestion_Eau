from pod.extension import db

from pod.models.utilisateur import Utilisateur
from pod.models.localite import Localite
from pod.models.marque import Marque

class Produit(db.Model):
    __tablename__='produits'
    id=db.Column(db.Integer,primary_key=True)
    quantite=db.Column(db.Float,nullable=True)
    prix=db.Column(db.Float,nullable=True)
    description=db.Column(db.String(300),nullable=True)
    date=db.Column(db.Date,nullable=False)
    id_marque=db.Column(db.Integer,db.ForeignKey('marques.id'),nullable=False)
    id_utilisateur=db.Column(db.Integer,db.ForeignKey('utilisateurs.id'),nullable=False)
    id_localite=db.Column(db.Integer,db.ForeignKey('localites.id'),nullable=False)



    def __init__(self,quantite,prix,description,date,id_utilisateur,id_localite,id_marque):
        self.quantite=quantite
        self.prix=prix
        self.description=description
        self.date=date
        self.id_localite=id_localite
        self.id_utilisateur=id_utilisateur
        self.id_marque=id_marque



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
         localite=Localite.query.get(self.id_localite)
         marque= Marque.query.get(self.id_marque)
         return{
            'id': self.id,
            'quantite': self.quantite,
            'prix': self.prix,
            'description': self.description,
            'date': self.date,
            'id_localite':self.id_localite,
            'id_marque':self.id_marque,
            'id_utilisateur': self.id_utilisateur,
            'localite':localite.format() if localite is not None else "The don't have product in this locality",
            'marque':marque.format() if marque is not None else "This product don't have marque",
            'utilisateur': utilisateur.format() if utilisateur is not None else "Product has not save by this user "
     
        }


