Contexte

• Création d'un logiciel de gestion d'une école d'ingénieurs
• On donne les CSV suivants :
• Table des étudiants
• Table des professeurs
• Table des salles
• On veut un programme capable de :
• Consulter, saisir et supprimer des entrées dans chaque csv
• Mettre à jour un fichier "cours" (format au choix) avec pour chaque entrée le
nom du cours, un professeur et plusieurs étudiants

• Créer un fichier "emploi du temps" (format au choix) avec pour chaque entrée :
une date de début, plusieurs étudiants, un professeur, une salle et une date de
fin
• Le tout utilisable en CLI

# petit orm :

## features :

- read a l'id :i
- read tout
- write a l'id :i
- create a l'id :i
- updatde a l'id :i
- delete a l'id :i

# managers :

## Cours manager

- creer un cours (nom du cours, un professeur et tableau d'etudiens )
- - crud classic

## Autres managers

- crud classic

## Service emploi du temps

- une fonction createEntityPlanning

# Main

- Une commande par operation crud par exemple sauf update pour les csv de base

  ```sh
  py main.py create -e {entity_type} {champs....}
  ```

- Une commande qui creer le fichier emploi du temps dans output
