import click
from managers.salle_manager import SalleManager


@click.group()
def salle():
    """Gestion des salles."""
    pass


@salle.command("add")
@click.option("--nom", prompt="Nom", help="Nom de la salle")
@click.option("--etage", prompt="Étage", type=int, help="Numéro d'étage")
def add(nom, etage):
    """Ajouter une nouvelle salle."""
    s = SalleManager.create(nom=nom, etage=etage)
    click.echo(f"Salle créée : {s}")


@salle.command("list")
def list_all():
    """Lister toutes les salles."""
    salles = SalleManager.all()
    if not salles:
        click.echo("Aucune salle.")
        return
    for s in salles:
        click.echo(s)


@salle.command("update")
@click.argument("id", type=int)
@click.option("--nom", default=None, help="Nouveau nom")
@click.option("--etage", default=None, type=int, help="Nouvel étage")
def update(id, nom, etage):
    """Mettre à jour une salle."""
    s = SalleManager.update(id=id, nom=nom, etage=etage)
    if s is None:
        click.echo(f"Salle {id} introuvable.")
    else:
        click.echo(f"Salle mise à jour : {s}")


@salle.command("delete")
@click.argument("id", type=int)
def delete(id):
    """Supprimer une salle."""
    ok = SalleManager.delete(id)
    if ok:
        click.echo(f"Salle {id} supprimée.")
    else:
        click.echo(f"Salle {id} introuvable.")
