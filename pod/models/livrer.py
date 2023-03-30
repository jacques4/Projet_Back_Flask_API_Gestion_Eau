from pod.extension import db


from pod.models.utilisateur import Utilisateur
from pod.models.commande import Commande

class Livrer(db.Model):
    __tablename__='livrers'
    id=db.Column(db.Integer,primary_key=True)
    quantite=db.Column(db.Float,nullable=True)
    date=db.Column(db.Date,nullable=False)
    status=db.Column(db.Boolean,nullable=True)
    id_utilisateur=db.Column(db.Integer,db.ForeignKey('utilisateurs.id'),nullable=False)
    id_commande=db.Column(db.Integer,db.ForeignKey('commandes.id'),nullable=False)



    def __init__(self, quantite,date,status,id_utilisateur,id_commande):
        self.quantite=quantite
        self.date=date
        self.status=status
        self.id_utilisateur=id_utilisateur
        self.id_commande=id_commande


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
        commande=Commande.query.get(self.id_commande)
        return{
            'id': self.id,
            'quantite': self.quantite,
            'date': self.date,
            'status':self.status,
            'id_utilisateur': self.id_utilisateur,
            'id_commande': self.id_commande,
            'utilisateur': utilisateur.format() if utilisateur is not None else "Command has not deliver by this user ",
            'commande': commande.format() if commande is not None else "Command is null",

            
        }