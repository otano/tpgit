from managers.base_manager import BaseManager
from models.cours_has_etudiant import CoursHasEtudiant


class CoursHasEtudiantsManager(BaseManager[CoursHasEtudiant]):
    _file = "data/cours-has-etudiants.csv"

    @classmethod
    def _hydrate(cls, row: dict) -> CoursHasEtudiant:
        return CoursHasEtudiant(
            id_cours=int(row["id_cours"]), id_etudiants=int(row["id_etudiants"])
        )

    @classmethod
    def find_by_cours(cls, id_cours: int) -> list[CoursHasEtudiant]:
        result = []
        for r in cls._load():
            if r["id_cours"] == str(id_cours):
                result.append(cls._hydrate(r))
        return result

    @classmethod
    def find_by_etudiant(cls, id_etudiants: int) -> list[CoursHasEtudiant]:
        result = []
        for r in cls._load():
            if r["id_etudiants"] == str(id_etudiants):
                result.append(cls._hydrate(r))
        return result

    @classmethod
    def create(cls, id_cours: int, id_etudiants: int) -> CoursHasEtudiant:
        rows = cls._load()
        new_row = {"id_cours": str(id_cours), "id_etudiants": str(id_etudiants)}
        rows.append(new_row)
        cls._save(rows)
        return cls._hydrate(new_row)

    @classmethod
    def delete(cls, id_cours: int, id_etudiants: int) -> bool:  # type: ignore[override]
        rows = cls._load()
        filtered = [
            r
            for r in rows
            if not (
                r["id_cours"] == str(id_cours)
                and r["id_etudiants"] == str(id_etudiants)
            )
        ]
        if len(filtered) == len(rows):
            return False
        cls._save(filtered)
        return True
