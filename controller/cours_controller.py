import click
from managers.cours_manager import CoursManager
from managers.cours_has_etudiants_manager import CoursHasEtudiantsManager
from managers.etudiant_manager import EtudiantManager
from managers.professeur_manager import ProfesseurManager


@click.group()
def cours():
    """Gestion des cours."""
    pass


@cours.command("add")
@click.option("--nom", prompt="Nom du cours", help="Nom du cours")
@click.option("--id-prof", prompt="ID du professeur", type=int, help="ID du professeur")
def add(nom, id_prof):
    """Ajouter un nouveau cours."""
    c = CoursManager.create(cours_name=nom, id_profs=id_prof)
    click.echo(f"Cours créé : {c}")


@cours.command("list")
def list_all():
    """Lister tous les cours."""
    cours_list = CoursManager.all()
    if not cours_list:
        click.echo("Aucun cours.")
        return
    for c in cours_list:
        prof = ProfesseurManager.find(c.id_profs)
        prof_label = f"{prof.nom} {prof.prenom}" if prof else f"id={c.id_profs}"
        click.echo(f"[{c.id}] {c.cours_name} — Professeur: {prof_label}")


@cours.command("update")
@click.argument("id", type=int)
@click.option("--nom", default=None, help="Nouveau nom")
@click.option("--id-prof", default=None, type=int, help="Nouvel ID de professeur")
def update(id, nom, id_prof):
    """Mettre à jour un cours."""
    c = CoursManager.update(id=id, cours_name=nom, id_profs=id_prof)
    if c is None:
        click.echo(f"Cours {id} introuvable.")
    else:
        click.echo(f"Cours mis à jour : {c}")


@cours.command("delete")
@click.argument("id", type=int)
def delete(id):
    """Supprimer un cours."""
    ok = CoursManager.delete(id)
    if ok:
        click.echo(f"Cours {id} supprimé.")
    else:
        click.echo(f"Cours {id} introuvable.")


@cours.command("enroll")
@click.argument("id_cours", type=int)
@click.argument("id_etudiant", type=int)
def enroll(id_cours, id_etudiant):
    """Inscrire un étudiant à un cours."""
    CoursHasEtudiantsManager.create(id_cours=id_cours, id_etudiants=id_etudiant)
    click.echo(f"Étudiant {id_etudiant} inscrit au cours {id_cours}.")


@cours.command("unenroll")
@click.argument("id_cours", type=int)
@click.argument("id_etudiant", type=int)
def unenroll(id_cours, id_etudiant):
    """Désinscrire un étudiant d'un cours."""
    ok = CoursHasEtudiantsManager.delete(id_cours=id_cours, id_etudiants=id_etudiant)
    if ok:
        click.echo(f"Étudiant {id_etudiant} désinscrit du cours {id_cours}.")
    else:
        click.echo(f"Inscription introuvable.")


@cours.command("students")
@click.argument("id_cours", type=int)
def students(id_cours):
    """Lister les étudiants inscrits à un cours."""
    c = CoursManager.find(id_cours)
    if c is None:
        click.echo(f"Cours {id_cours} introuvable.")
        return
    links = CoursHasEtudiantsManager.find_by_cours(id_cours)
    if not links:
        click.echo(f"Aucun étudiant inscrit au cours '{c.cours_name}'.")
        return
    click.echo(f"Étudiants du cours '{c.cours_name}':")
    for link in links:
        e = EtudiantManager.find(link.id_etudiants)
        if e:
            click.echo(f"  - [{e.id}] {e.nom} {e.prenom}")
