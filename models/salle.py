from dataclasses import dataclass, fields


@dataclass
class Salle:
    id: int
    nom: str
    etage: int

    def __str__(self) -> str:
        parts = ", ".join(f"{f.name}={getattr(self, f.name)}" for f in fields(self))
        return f"Salle({parts})"
