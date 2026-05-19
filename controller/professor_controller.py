import click
from managers.professeur_manager import ProfesseurManager


@click.group()
def professeur():
    """Gestion des professeurs."""
    pass


@professeur.command("add")
@click.option("--nom", prompt="Nom", help="Nom du professeur")
@click.option("--prenom", prompt="Prénom", help="Prénom du professeur")
def add(nom, prenom):
    """Ajouter un nouveau professeur."""
    p = ProfesseurManager.create(nom=nom, prenom=prenom)
    click.echo(f"Professeur créé : {p}")


@professeur.command("list")
def list_all():
    """Lister tous les professeurs."""
    profs = ProfesseurManager.all()
    if not profs:
        click.echo("Aucun professeur.")
        return
    for p in profs:
        click.echo(p)


@professeur.command("update")
@click.argument("id", type=int)
@click.option("--nom", default=None, help="Nouveau nom")
@click.option("--prenom", default=None, help="Nouveau prénom")
def update(id, nom, prenom):
    """Mettre à jour un professeur."""
    p = ProfesseurManager.update(id=id, nom=nom, prenom=prenom)
    if p is None:
        click.echo(f"Professeur {id} introuvable.")
    else:
        click.echo(f"Professeur mis à jour : {p}")


@professeur.command("delete")
@click.argument("id", type=int)
def delete(id):
    """Supprimer un professeur."""
    ok = ProfesseurManager.delete(id)
    if ok:
        click.echo(f"Professeur {id} supprimé.")
    else:
        click.echo(f"Professeur {id} introuvable.")
