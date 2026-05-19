from dataclasses import dataclass, fields


@dataclass
class Etudiant:
    id: int
    nom: str
    prenom: str

    def __str__(self) -> str:
        parts = ", ".join(f"{f.name}={getattr(self, f.name)}" for f in fields(self))
        return f"Etudiant({parts})"
