from dataclasses import dataclass, fields


@dataclass
class CoursHasEtudiant:
    id_cours: int
    id_etudiants: int

    def __str__(self) -> str:
        parts = ", ".join(f"{f.name}={getattr(self, f.name)}" for f in fields(self))
        return f"CoursHasEtudiant({parts})"
