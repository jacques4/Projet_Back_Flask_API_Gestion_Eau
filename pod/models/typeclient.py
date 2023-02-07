from pod.extension import db

class TypeClient(db.Model):
    __tablename__='typeclients'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(300),nullable=False)
    libelle=db.Column(db.String(300),nullable=True)


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