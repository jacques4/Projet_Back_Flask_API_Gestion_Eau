from pod.extension import db
from pod.models import utilisateur

class Profile(db.Model):
    __tablename__='profiles'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(300),nullable=False)
    libelle=db.Column(db.String(300),nullable=True)
    utilisateurs=db.relationship('Utilisateur',backref='profiles',lazy=True)



    def __init__(self, nom,libelle):
        self.nom=nom
        self.libelle=libelle
    

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
            'libelle': self.libelle
        
            
        }



