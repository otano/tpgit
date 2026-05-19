import click
from managers.cours_manager import CoursManager
from managers.cours_has_etudiants_manager import CoursHasEtudiantsManager
from managers.etudiant_manager import EtudiantManager
from managers.professeur_manager import ProfesseurManager


@click.group()
def planning():
    """Affichage du planning."""
    pass


@planning.command("show")
def show():
    """Afficher tous les cours avec leur professeur et leurs étudiants."""
    cours_list = CoursManager.all()
    if not cours_list:
        click.echo("Aucun cours.")
        return
    for c in cours_list:
        prof = ProfesseurManager.find(c.id_profs)
        prof_label = f"{prof.nom} {prof.prenom}" if prof else f"id={c.id_profs}"
        click.echo(f"\n[Cours {c.id}] {c.cours_name} — {prof_label}")
        links = CoursHasEtudiantsManager.find_by_cours(c.id)
        if not links:
            click.echo("  Aucun étudiant inscrit.")
        else:
            for link in links:
                e = EtudiantManager.find(link.id_etudiants)
                if e:
                    click.echo(f"  - {e.nom} {e.prenom}")


@planning.command("by-etudiant")
@click.argument("id_etudiant", type=int)
def by_etudiant(id_etudiant):
    """Afficher les cours d'un étudiant."""
    e = EtudiantManager.find(id_etudiant)
    if e is None:
        click.echo(f"Étudiant {id_etudiant} introuvable.")
        return
    links = CoursHasEtudiantsManager.find_by_etudiant(id_etudiant)
    if not links:
        click.echo(f"{e.nom} {e.prenom} n'est inscrit à aucun cours.")
        return
    click.echo(f"Cours de {e.nom} {e.prenom}:")
    for link in links:
        c = CoursManager.find(link.id_cours)
        if c:
            prof = ProfesseurManager.find(c.id_profs)
            prof_label = f"{prof.nom} {prof.prenom}" if prof else f"id={c.id_profs}"
            click.echo(f"  - [{c.id}] {c.cours_name} ({prof_label})")
