from managers.base_manager import BaseManager
from models.cours import Cours


class CoursManager(BaseManager[Cours]):
    _file = "data/cours.csv"

    @classmethod
    def _hydrate(cls, row: dict) -> Cours:
        return Cours(
            id=int(row["id"]),
            cours_name=row["cours_name"],
            id_profs=int(row["id_profs"]),
        )

    @classmethod
    def create(cls, cours_name: str, id_profs: int) -> Cours:
        created = cls._create_row({"cours_name": cours_name, "id_profs": str(id_profs)})
        return cls._hydrate(created)

    @classmethod
    def update(
        cls, id: int, cours_name: str | None = None, id_profs: int | None = None
    ) -> Cours | None:
        data: dict = {}
        if cours_name is not None:
            data["cours_name"] = cours_name
        if id_profs is not None:
            data["id_profs"] = str(id_profs)
        row = cls._update_row(id, data)
        return cls._hydrate(row) if row else None
