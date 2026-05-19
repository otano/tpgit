from managers.base_manager import BaseManager
from models.professeur import Professeur


class ProfesseurManager(BaseManager[Professeur]):
    _file = "data/professeur.csv"

    @classmethod
    def _hydrate(cls, row: dict) -> Professeur:
        return Professeur(id=int(row["id"]), nom=row["nom"], prenom=row["prenom"])

    @classmethod
    def create(cls, nom: str, prenom: str) -> Professeur:
        created = cls._create_row({"nom": nom, "prenom": prenom})
        return cls._hydrate(created)

    @classmethod
    def update(
        cls, id: int, nom: str | None = None, prenom: str | None = None
    ) -> Professeur | None:
        data: dict = {}
        if nom is not None:
            data["nom"] = nom
        if prenom is not None:
            data["prenom"] = prenom
        row = cls._update_row(id, data)
        return cls._hydrate(row) if row else None
