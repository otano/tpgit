import click
from controller.etudiant_controller import etudiant
from controller.professor_controller import professeur
from controller.cours_controller import cours
from controller.salle_controller import salle
from controller.planning_controller import planning


@click.group()
def cli():
    """Application de gestion d'établissement scolaire."""
    pass


cli.add_command(etudiant)
cli.add_command(professeur)
cli.add_command(cours)
cli.add_command(salle)
cli.add_command(planning)


if __name__ == "__main__":
    cli()
