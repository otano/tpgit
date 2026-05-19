# AGENTS.md — epsi-tpgit

## What this is lol

A starter repo for a Git collaboration workshop (EPSI school, TP Git). No commits have been made yet — the repo is a blank canvas for teaching branching, merging, and team workflows.

## Project structure

| Path                               | Purpose                                                       |
| ---------------------------------- | ------------------------------------------------------------- |
| `main.py`                          | CLI entrypoint (CRUD sur les CSV data/)                       |
| `data/etudiants.csv`               | Student roster (DUPUIS, DUPONT, PICHET)                       |
| `data/professeur.csv`              | Professor roster (MENARD)                                     |
| `data/salles.csv`                  | Room list (101, 201)                                          |
| `Collaboration dans un projet.pdf` | Workshop instructions (French)                                |
| `pyproject.toml`                   | Minimal — no dependencies, Python >=3.13                      |

## Key facts

- **Python 3.13** (see `.python-version`)
- **No dependencies** — `pyproject.toml` has an empty `dependencies = []`
- **No test framework**, no linter, no formatter, no type checker configured
- **No commits yet** — `git status` shows all files as untracked
- The workshop PDF (`Collaboration dans un projet.pdf`) contains the exercise instructions (in French)

## Run

```sh
python main.py
```

## CLI — CRUD sur les CSV

```sh
python main.py list <table>                  # consulter
python main.py add   <table> [field=val ...]  # ajouter (omettre = interactif)
python main.py delete <table> <field>=<val>   # supprimer
python main.py update <table> <field>=<val> <field2>=<new> ...   # modifier
```

Tables : `etudiants`, `professeur`, `salles`. Pas de dépendances — stdlib uniquement.

## Git workflow notes

- First committer should make an initial commit to establish `main`
- CSV files in `data/` are the primary manipulation targets for the workshop exercises
- No CI, no pre-commit hooks, no branch protection rules exist
