from pod.extension import db


class Commande(db.Model):
    __tablename__='commandes'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(300),nullable=False)
    quantite=db.Column(db.Float,nullable=True)
    description=db.Column(db.String(300),nullable=True)
    date=db.Column(db.Date,nullable=False)
    status=db.Column(db.Boolean,nullable=True)
    id_utilisateur=db.Column(db.Integer,db.ForeignKey('utilisateurs.id'),nullable=False)
    id_client=db.Column(db.Integer,db.ForeignKey('clients.id'),nullable=False)


    def __init__(self, nom,quantite,description,date,status,id_utilisateur,id_client):
        self.nom=nom
        self.quantite=quantite
        self.description=description
        self.date=date
        self.status=status
        self.id_utilisateur
        self.id_client


    def insert(self):
        db.session.add(self)
        db.session.commit()
   

    def delete(self):
        db.session.delete(self)
        db.session.commit()
     

    def update(self):
         db.session.commit()
         

    def format(self):
            return{
            'id': self.id,
            'nom': self.nom,
            'quantite': self.quantite,
            'description': self.description,
            'date': self.date,
            'status':self.status,
            'Id de utilisateur': self.id_utilisateur,
            'Id du client': self.id_client
            
        }


