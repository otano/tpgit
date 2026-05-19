from dataclasses import dataclass, fields


@dataclass
class Cours:
    id: int
    cours_name: str
    id_profs: int

    def __str__(self) -> str:
        parts = ", ".join(f"{f.name}={getattr(self, f.name)}" for f in fields(self))
        return f"Cours({parts})"
