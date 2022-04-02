#Importation des modules
from datetime import datetime
from datetime import timedelta
from datetime import date

#1. Classe Personne
class Personne:
    #2. Constructeur
    def __init__(self,nom,prenom):
        self.__nom = nom
        self.__prenom = prenom
    #3. Les accesseurs et les mutateurs
    def get_nom(self):
        return self.__nom
    def get_pre(self):
        return self.__pre
    def set_nom(self,nom):
        self.__nom = nom
    def set_prenom(self,pre):
        self.__prenom = pre
    #4. Méthode __str__
    def __str__(self):
        return f"Le nom est : {self.__nom} et le prénom est : {self.__prenom}"

#5. Classe Adherent
class Adherent(Personne):
    #6. Constructeur
    def __init__(self,nom,prenom,codeAdherent,dateAdhesion = date.today()):
        #7. Constructeur paramétré qui initialise le nom et le prénom
        super().__init__(nom,prenom)
        self.__CodeAdherent = codeAdherent
        self.__dateAdhension = dateAdhesion
    def get_codeAdherent(self):
        return self.__CodeAdherent
    def set_codeAdherent(self,code):
        self.__CodeAdherent = code
    #8. Méthode __str__
    def __str__(self):
        return "{}\nLe code de l'adhérent est : {} et La date d'adhésion est : {}".format(Personne.__str__(self),self.__CodeAdherent,self.__dateAdhension)

#9. Classe Auteur
class Auteur(Personne):
    #10. Constructeur
    def __init__(self, nom, prenom,codeAuteur):
        super().__init__(nom,prenom)
        self.__codeAuteur = codeAuteur
    #11. Les accesseurs et les mutateurs
    def get_codeauteur(self):
        return self.__codeAuteur
    def set_codeauteur(self,code):
        self.__codeAuteur = code
    #12. Méthode __str__
    def __str__(self):
        return "{}\nLe code d'Auteur est : {}".format(Personne.__str__(self),self.__codeAuteur)

#13. Classe Livre
class Livre:
    #14. Constructeur
    def __init__(self,codelivre,titrelivre,auteurlivre,totexemplaires,exemplairesdisponibles):
        self.__codeLivre=codelivre
        self.__titreLivre=titrelivre
        self.__auteurLivre=auteurlivre
        self.__totalExemplaires=totexemplaires
        self.__exemplairesDispo=exemplairesdisponibles
    def get_codeLivre(self):
        return self.__codeLivre
    def set_codeLivre(self,codelivre):
        self.__codeLivre = codelivre
    def get_titreLivre(self):
        return self.__titreLivre
    def set_titreLivre(self,titrelivre):
        self.__titreLivre = titrelivre
    def get_Auteur(self):
        return self.__auteurLivre
    def set_Auteur(self,Auteur):
        self.__auteurLivre = Auteur
    def get_total(self):
        return self.__totalExemplaires
    def set_total (self,total):
        self.__totalExemplaires = total
    def get_disponible (self):
        return self.__exemplairesDispo
    def set_disponible (self,dispo):
        self.__exemplairesDispo = dispo
    #15. Méthode livreDisponsible
    def livreDisponsible(self):
        if self.__exemplairesDispo > 0:
            print("Cet livre est disponible pour l'emprunt")
        else:
            print("Cet livre n'est pas disponible pour l'emprunt")
    def __str__(self):
        return f"Le titre de livre : {self.__titreLivre}, et son code est : {self.__codeLivre}"

#16. Classe Emprunt
class Emprunt:
    #17. Constructeur
    def __init__(self,codeEmprunt=1235,livreemprunte="",emprunteur="",dateEmprunt=date(2021,11,10),dateretourprevue=date(2021,2,3),dateretoureffective=None):
        self.__codeEmprunt=codeEmprunt
        self.__livreEmprunte=livreemprunte
        self.__emprunteur=emprunteur
        self.__dateEmprunt=dateEmprunt
        self.__dateRetourPrevue=dateretourprevue
        self.__dateRetourEffective=dateretoureffective
    def set_livre(self,livv):
        self.__livreEmprunte = livv
    def set_emprunteur(self,emp):
        self.__emprunteur = emp
    def get_livre(self):
        return self.__livreEmprunte
    def get_emprunteur(self):
        return self.__emprunteur
    def get_codeEmprunt(self):
        return self.__codeEmprunt
    def get_dateEmprunt(self):
        return self.__dateEmprunt
    def set_dateEmprunt(self,dat):
        self.__dateEmprunt = dat
    def get_dateRetourPrevue(self):
        return self.__dateRetourPrevue
    def set_dateRetourPrevue(self,datp):
        self.__dateRetourPrevue = datp
    def get_dateRetourEffective(self):
        return self.__dateRetourEffective
    def set_dateRetourEffective(self,datE):
        self.__dateRetourEffective = datE
    #18. Méthode etatEmprunt
    def etatEmprunt(self):
        if self.__dateRetourEffective == None and self.__dateRetourPrevue >= date.today():
            return "en cours"
        if self.__dateRetourEffective != None:
            return "rendu"
        if self.__dateRetourEffective == None and self.__dateRetourPrevue < date.today():
            return "non rendu"

#19. Classe Biblio
class Biblio:
    emprunt = Emprunt()
    def __init__(self,Livre,Adherent,Emprunt):
        self.ListeLivres = Livre
        self.ListeAdherents = Adherent
        self.ListeEmprunts = Emprunt
    #20. Méthode ajouterLivre
    def ajouterLivre(self,Liv):
        self.ListeLivres.append(Liv)
    #21. Méthode ajouterAdherent
    def ajouterAdherent(self,Adh):
        self.ListeAdherents.append(Adh)
    #22. Méthode rechercherAdherent
    def rechercherAdherent(self,Ad):
        x=0
        for i in range(len(self.ListeAdherents)):
            if self.ListeAdherents[i].get_codeAdherent() == Ad:
                x+=1
            if x>0:
                return True
    #23. Méthode rechercherLivre
    def rechercherLivre(self,Livrr):
        z = False
        for i in range(len(self.ListeLivres)):
            if self.ListeLivres[i].get_codeLivre() == Livrr:
                z = True
        return z
    #24. Méthode ajouterEmprunte
    def ajouterEmprunt(self,codeA,codeL):
        if self.rechercherAdherent(codeA) != True:
            print("Cet Adherent n'existe pas")
        else:
            for i in self.ListeAdherents:
                if i.get_codeAdherent() == codeA:
                    Biblio.emprunt.set_emprunteur(i)
        if self.rechercherLivre(codeL) != True:
            print("Ce Livre n'existe pas")
        else:
            for i in self.ListeLivres:
                if i.get_codeLivre() == codeL:
                    Biblio.emprunt.set_livre(i)
        self.ListeEmprunts.append(Biblio.emprunt)
        Biblio.emprunt.set_dateEmprunt(date.today())
        Biblio.emprunt.set_dateRetourPrevue(date.today()+timedelta(days=3))
    #26. Méthode topEmprunts
    def topEmprunts(self):
        max = 0
        for i in self.ListeEmprunts:
            m=0
            for j in self.ListeLivres:
                if (i.get_livre()).get_codeLivre() == j.get_codeLivre():
                    m+=1
            if m>max:
                max = m
                b = i.get_livre()
        return b
    #27. Méthode emprunteurs
    def emprunteurs(self):
        liste=[]
        for i in self.ListeEmprunts:
            if i.etatEmprunt() == "non rendu" or i.etatEmprunt() == "en cours":
                liste.append((i.get_emprunteur()).get_nom())
        return liste
    #25. Méthode retourEmprunte
    def retourEmprunt(self,CODE_EMPRUNT):
        for x in self.ListeEmprunts:
            if CODE_EMPRUNT == x.get_codeEmprunt():
                x.set_dateRetourEffective(date.today())
    #28. Méthode datePossibiliteEmprunt
    def datePossibiliteEmprunt(self,codeL):
        for i in self.ListeEmprunts:
            if (i.get_livre()).get_codeLivre() == codeL:
                print("Ce livre sera disponible le : ", i.get_dateRetourPrevue())
            else:
                print("Ce livre n'exist pas")


#Instanciation
L1 = Livre(1521,"Livre n°1","Hamid Raiss",15,2)
A1 = Adherent("Hassouni","Anass",4562)
A2 = Adherent("Fathi","salah",1200)
B = Biblio([],[],[])

#Ajouter les objets
B.ajouterAdherent(A1)
B.ajouterAdherent(A2)
B.ajouterLivre(L1)
B.ajouterEmprunt(4562,1521)

#B.retourEmprunt(1235)

print("Le livre plus impruntée est : ",B.topEmprunts())
print("Les emprunteurs ayant des emprunts en cours ou non rendus sont : ",B.emprunteurs())
B.datePossibiliteEmprunt(1521)