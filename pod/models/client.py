from pod.extension import db


class Client(db.Model):
    __tablename__='clients'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(300),nullable=False)
    prenom=db.Column(db.String(300),nullable=True)
    email=db.Column(db.String(300),nullable=True)
    tel=db.Column(db.String(200),nullable=False)
    adresse=db.Column(db.String(300),nullable=True)


    def __init__(self, nom,prenom,email,tel,adresse):
        self.nom=nom
        self.prenom=prenom
        self.email=email
        self.tel=tel
        self.adresse=adresse

 
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
            'prenom': self.prenom,
            'email': self.email,
            'tel': self.tel,
            'adresse': self.adresse
        }