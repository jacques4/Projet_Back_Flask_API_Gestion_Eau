from pod.extension import db

from pod.models.typeclient import TypeClient
from pod.models.utilisateur import Utilisateur

class Client(db.Model):
    __tablename__='clients'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(300),nullable=False)
    prenom=db.Column(db.String(300),nullable=True)
    email=db.Column(db.String(300),nullable=True)
    tel=db.Column(db.String(200),nullable=False)
    adresse=db.Column(db.String(300),nullable=True)
    longi=db.Column(db.Float,nullable=True)
    lat=db.Column(db.Float,nullable=True)
    date=db.Column(db.Date,nullable=False)
    nif=db.Column(db.String(300),nullable=False)
    numrccm=db.Column(db.String(300),nullable=False)
    id_utilisateur=db.Column(db.Integer,db.ForeignKey('utilisateurs.id'),nullable=False)
    id_typeclient=db.Column(db.Integer,db.ForeignKey('typeclients.id'),nullable=False)


    def __init__(self, nom,prenom,email,tel,adresse,id_utilisateur,longi,lat,id_typeclient,date,nif,numrccm):
        self.nom=nom
        self.prenom=prenom
        self.email=email
        self.tel=tel
        self.adresse=adresse
        self.nif=nif
        self.longi=longi
        self.lat=lat
        self.date=date
        self.numrccm=numrccm
        self.id_utilisateur=id_utilisateur
        self.id_typeclient=id_typeclient

 
    def insert(self):
        db.session.add(self)
        db.session.commit()
   

    def delete(self):
        db.session.delete(self)
        db.session.commit()
     

    def update(self):
         db.session.commit()
         

    def format(self):
        typeclient=TypeClient.query.get(self.id_typeclient)
        utilisateur=Utilisateur.query.get(self.id_utilisateur)
        return{
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'email': self.email,
            'tel': self.tel,
            'adresse': self.adresse,
            'nif':self.nif,
            'longi':self.longi,
            'lat':self.lat,
            'date':self.date,
            'numrccm':self.numrccm,
            'id_utilisateur': self.id_utilisateur,
            'id_typeclient': self.id_typeclient,
            'utilisateur': utilisateur.format() if utilisateur is not None else "Client has not  save by this user ",
            'typeclient': typeclient.format() if typeclient is not None else "Client has not  typeclient "

        }