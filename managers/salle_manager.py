from managers.base_manager import BaseManager
from models.salle import Salle


class SalleManager(BaseManager[Salle]):
    _file = "data/salles.csv"

    @classmethod
    def _hydrate(cls, row: dict) -> Salle:
        return Salle(id=int(row["id"]), nom=row["nom"], etage=int(row["etage"]))

    @classmethod
    def create(cls, nom: str, etage: int) -> Salle:
        created = cls._create_row({"nom": nom, "etage": str(etage)})
        return cls._hydrate(created)

    @classmethod
    def update(
        cls, id: int, nom: str | None = None, etage: int | None = None
    ) -> Salle | None:
        data: dict = {}
        if nom is not None:
            data["nom"] = nom
        if etage is not None:
            data["etage"] = str(etage)
        row = cls._update_row(id, data)
        return cls._hydrate(row) if row else None
