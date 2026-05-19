import csv
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseManager(Generic[T]):
    _file: str

    @classmethod
    def all(cls) -> list[T]:
        return [cls._hydrate(r) for r in cls._load()]

    @classmethod
    def find(cls, id: int) -> T | None:
        id_field = cls._fieldnames()[0]
        for row in cls._load():
            if row[id_field] == str(id):
                return cls._hydrate(row)
        return None

    @classmethod
    def delete(cls, id: int) -> bool:
        rows = cls._load()
        id_field = cls._fieldnames()[0]
        filtered = [r for r in rows if r[id_field] != str(id)]
        if len(filtered) == len(rows):
            return False
        cls._save(filtered)
        return True

    @classmethod
    def _create_row(cls, data: dict) -> dict:
        rows = cls._load()
        id_field = cls._fieldnames()[0]
        next_id = max((int(r[id_field]) for r in rows), default=0) + 1
        new_row = {**data, id_field: str(next_id)}
        rows.append(new_row)
        cls._save(rows)
        return new_row

    @classmethod
    def _update_row(cls, id: int, data: dict) -> dict | None:
        rows = cls._load()
        id_field = cls._fieldnames()[0]
        for i, row in enumerate(rows):
            if row[id_field] == str(id):
                rows[i] = {**row, **data, id_field: str(id)}
                cls._save(rows)
                return rows[i]
        return None

    @classmethod
    def _fieldnames(cls) -> list[str]:
        with open(cls._file, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f).fieldnames or [])

    @classmethod
    def _load(cls) -> list[dict]:
        with open(cls._file, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    @classmethod
    def _save(cls, rows: list[dict]) -> None:
        fieldnames = cls._fieldnames() or (list(rows[0].keys()) if rows else [])
        with open(cls._file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @classmethod
    def _hydrate(cls, row: dict) -> T:
        raise NotImplementedError
