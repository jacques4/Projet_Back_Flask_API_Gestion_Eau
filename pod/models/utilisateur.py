from pod.extension import db


class Utilisateur(db.Model):
    __tablename__='utilisateurs'
    id=db.Column(db.Integer,primary_key=True)
    matricule=db.Column(db.String(300),nullable=True)
    nom=db.Column(db.String(300),nullable=False)
    prenom=db.Column(db.String(300),nullable=True)
    email=db.Column(db.String(300),nullable=True)
    tel=db.Column(db.String(300),nullable=False)
    login=db.Column(db.String(300),nullable=True)
    mdp=db.Column(db.String(300),nullable=True)
    status=db.Column(db.Boolean,nullable=True)
    adresse=db.Column(db.String(200),nullable=True)
    id_profile=db.Column(db.Integer,db.ForeignKey('profiles.id'),nullable=False)



    def __init__(self, matricule,nom,prenom,email,tel,login,mdp,status,adresse,id_profile):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.email=email
        self.tel=tel
        self.login=login
        self.mdp=mdp
        self.status=status
        self.adresse=adresse
        self.id_profile=id_profile

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
            'matricule':self.matricule,
            'nom': self.nom,
            'prenom': self.prenom,
            'email': self.email,
            'tel': self.tel,
            'login':self.login,
            'mdp':self.mdp,
            'status':self.status,
            'adresse': self.adresse,
            'profile': self.id_profile,

        }







