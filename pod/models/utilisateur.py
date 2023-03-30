from pod.extension import db

from pod.models.profile import Profile
from pod.models.localite import Localite
from pod.models.personne import Personne


class Utilisateur(db.Model):
    __tablename__='utilisateurs'
    id=db.Column(db.Integer,primary_key=True)
    matricule=db.Column(db.String(300),nullable=True)
    login=db.Column(db.String(300),nullable=True)
    mdp=db.Column(db.String(300),nullable=True)
    status=db.Column(db.Boolean,nullable=True)
    id_profile=db.Column(db.Integer,db.ForeignKey('profiles.id'),nullable=False)
    id_localite=db.Column(db.Integer,db.ForeignKey('localites.id'),nullable=False)
    id_personne=db.Column(db.Integer,db.ForeignKey('personnes.id'),nullable=True)
    id_utilisateur=db.Column(db.Integer,db.ForeignKey('utilisateurs.id'),nullable=True)



    def __init__(self, matricule,login,mdp,status,id_profile,id_localite,id_personne,id_utilisateur):
        self.matricule=matricule
        self.login=login
        self.mdp=mdp
        self.status=status
        self.id_profile=id_profile
        self.id_localite=id_localite
        self.id_personne=id_personne
        self.id_utilisateur=id_utilisateur

    def insert(self):
        db.session.add(self)
        db.session.commit()
   

    def delete(self):
        db.session.delete(self)
        db.session.commit()
     

    def update(self):
         db.session.commit()
         

    def format(self):
        profile = Profile.query.get(self.id_profile)
        localite= Localite.query.get(self.id_localite)
        personne= Personne.query.get(self.id_personne)
        utilisateur = Utilisateur.query.get(self.id_utilisateur)
    
        return{
            'id': self.id,
            'matricule':self.matricule,
            'login':self.login,
            'mdp':self.mdp,
            'status':self.status,
            'id_profile': self.id_profile,
            'id_utilisateur': self.id_utilisateur,
            'id_localite': self.id_localite,
            'id_personne':self.id_personne,
            'localite': localite.format() if localite is not None else "User has no Localite",
            'personne': personne.format() if personne is not None else "Nothing",
            'profile': profile.format() if profile is not None else "User has no profile",
            'utilisateurs': utilisateur.format() if utilisateur is not None else "User hasn't save by a user",
        }







