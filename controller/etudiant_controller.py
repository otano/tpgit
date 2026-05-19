import click
from managers.etudiant_manager import EtudiantManager


@click.group()
def etudiant():
    """Gestion des étudiants."""
    pass


@etudiant.command("add")
@click.option("--nom", prompt="Nom", help="Nom de l'étudiant")
@click.option("--prenom", prompt="Prénom", help="Prénom de l'étudiant")
def add(nom, prenom):
    """Ajouter un nouvel étudiant."""
    e = EtudiantManager.create(nom=nom, prenom=prenom)
    click.echo(f"Étudiant créé : {e}")


@etudiant.command("list")
def list_all():
    """Lister tous les étudiants."""
    etudiants = EtudiantManager.all()
    if not etudiants:
        click.echo("Aucun étudiant.")
        return
    for e in etudiants:
        click.echo(e)


@etudiant.command("update")
@click.argument("id", type=int)
@click.option("--nom", default=None, help="Nouveau nom")
@click.option("--prenom", default=None, help="Nouveau prénom")
def update(id, nom, prenom):
    """Mettre à jour un étudiant."""
    e = EtudiantManager.update(id=id, nom=nom, prenom=prenom)
    if e is None:
        click.echo(f"Étudiant {id} introuvable.")
    else:
        click.echo(f"Étudiant mis à jour : {e}")


@etudiant.command("delete")
@click.argument("id", type=int)
def delete(id):
    """Supprimer un étudiant."""
    ok = EtudiantManager.delete(id)
    if ok:
        click.echo(f"Étudiant {id} supprimé.")
    else:
        click.echo(f"Étudiant {id} introuvable.")
