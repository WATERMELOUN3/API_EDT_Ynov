# API_EDT_Ynov
*Par Alexis GELIN--ANDRIEU*  
API faite en Python 3 avec Flask permettant l'accès à un système d'emploi du temps  
  
**Dépendances:** flask, flask-login, flask-sqlalchemy


## How to use:  
\* = necessary  
Datetime are in ISO format  
  
   * /  
      * -> Affiche HTML simple pour dire que c'est une API  
   * /cours  
        * GET -> Accède aux cours auquels l'élève est inscrit  
            * Form body: datedebut, datefin, matière  
        * PUT -> S'inscrit à un cours  
            * Form body: idCour\*  
        * POST -> Créé un cours (pour prof)  
            * Form body: idMatiere\*, idProf\*, heureDebut\*, heureFin\*  
        * DELETE -> Se désinscrit à un cours  
            * Form body: idCour\*, idStudent (en tant que prof pour desinscrire un eleve)  
   * /matiere  
        * GET -> Accède aux différentes matières  
            * Form body: idProf  
        * POST -> Créé une matière  
            * Form body: nom\*, idProf\*, ects\*  
        * PATCH -> Met à jour une matière  
            * Form body: id\*, nom, idProf, ects  
        * DELETE -> Supprime une matière  
            * Form body: id\*
   * /prof/user  
        * GET -> Affiche les info d'un utilisateur (sauf mdp)  
            * Form body: id\*  
        * POST -> Créé un utilisateur  
            * Form body: username\*, password\* (sha256 hash), prenom, nom, prof  
        * DELETE -> Supprime un utilisateur  
            * Form body: id\*  
        * PUT -> Met à jour un utilisateur  
            * Form body: id\*, username, password, prenom, nom, prof  
