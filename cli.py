import click

# Colones de chaque fichier (nécessaires pour écrire l'en-tête du CSV)
ETUDIANT_FIELDS = ["id", "nom", "prenom"]
PROFESSEUR_FIELDS = ["id", "nom", "prenom"]
COURS_FIELDS = ["id", "cours_name", "id_profs"]
SALLE_FIELDS = ["id", "nom", "capacite"]


# --- Point d'entrée principal ---
@click.group()
def cli():
    """Application de gestion d'établissement scolaire."""

    pass


# ==========================================
# === COMMANDES POUR LES ÉTUDIANTS ===
# ==========================================
@click.group()
def etudiant():
    """Gestion des étudiants."""

    pass


@etudiant.command()
@click.option("--nom", prompt="Nom", help="Nom de l'étudiant")
@click.option("--prenom", prompt="Prénom", help="Prénom de l'étudiant")
def add(nom, prenom):
    """Ajouter un nouvel étudiant."""


@etudiant.command()
def list():
    """Lister tous les étudiants."""


@etudiant.command()
@click.argument("id", type=int)
@click.option("--nom", default=None, help="Nouveau nom")
@click.option("--prenom", default=None, help="Nouveau prénom")
def update(id, nom, prenom):
    """Mettre à jour un étudiant."""


@etudiant.command()
@click.argument("id", type=int)
def delete(id):
    """Supprimer un étudiant."""


# ==========================================
# === COMMANDES POUR LES PROFESSEURS ===
# ==========================================
@click.group()
def professeur():
    """Gestion des professeurs."""
    pass


@professeur.command()
@click.option("--nom", prompt="Nom")
@click.option("--prenom", prompt="Prénom")
def add(nom, prenom):
    """Ajouter un professeur."""


@professeur.command()
def list():
    """Lister les professeurs."""


@professeur.command()
@click.argument("id", type=int)
@click.option("--nom", default=None)
@click.option("--prenom", default=None)
def update(id, nom, prenom):
    """Mettre à jour un professeur."""


@professeur.command()
@click.argument("id", type=int)
def delete(id):
    """Supprimer un professeur."""


# ==========================================
# === COMMANDES POUR LES COURS ===
# ==========================================
@click.group()
def cours():
    """Gestion des cours."""
    pass


@cours.command()
@click.option("--nom", prompt="Nom du cours")
@click.option("--id-prof", prompt="ID du professeur", type=int)
def add(nom, id_prof):
    """Ajouter un cours."""


@cours.command()
def list():
    """Lister les cours."""
    pass


@cours.command()
@click.argument("id", type=int)
@click.option("--nom", default=None)
@click.option("--id-prof", type=int, default=None)
def update(id, nom, id_prof):
    pass


@cours.command()
@click.argument("id", type=int)
def delete(id):
    pass


# ==========================================
# === COMMANDES POUR LES SALLES ===
# ==========================================
@click.group()
def salle():
    """Gestion des salles."""
    pass


@salle.command()
@click.option("--nom", prompt="Nom de la salle")
@click.option("--capacite", prompt="Capacité", type=int)
def add(nom, capacite):
    """Ajouter une salle."""


@salle.command()
def list():
    """Lister les salles."""
    pass


@salle.command()
@click.argument("id", type=int)
@click.option("--nom", default=None)
@click.option("--capacite", type=int, default=None)
def update(id, nom, capacite):
    """Mettre à jour une salle."""


@salle.command()
@click.argument("id", type=int)
def delete(id):
    """Supprimer une salle."""


# --- Ajout des sous-groupes au groupe principal ---
cli.add_command(etudiant)
cli.add_command(professeur)
cli.add_command(cours)
cli.add_command(salle)

if __name__ == "__main__":
    cli()
