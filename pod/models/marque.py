from pod.extension import db

class Marque(db.Model):
    __tablename__='marques'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(300),nullable=False)


    def __init__(self, nom):
        self.nom=nom
    

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
            'nom': self.nom
        }