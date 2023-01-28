from pod.extension import db


class Produit(db.Model):
    __tablename__='produits'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(300),nullable=False)
    quantite=db.Column(db.Float,nullable=True)
    description=db.Column(db.String(300),nullable=True)
    date=db.Column(db.Date,nullable=False)
    id_utilisateur=db.Column(db.Integer,db.ForeignKey('utilisateurs.id'),nullable=False)



    def __init__(self, nom,quantite,description,date,id_utilisateur):
        self.nom=nom
        self.quantite=quantite
        self.description=description
        self.date=date
        self.id_utilisateur



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
            'Id de utilisateur': self.id_utilisateur
            
        }


