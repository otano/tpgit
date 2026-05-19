mimport argparse
import csv
import os
import sys

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

TABLES = {
    "etudiants": {"file": "etudiants.csv", "headers": ["nom", "prenom"]},
    "professeur": {"file": "professeur.csv", "headers": ["nom", "prenom"]},
    "salles": {"file": "salles.csv", "headers": ["nom", "etage"]},
}


def _table_path(table):
    return os.path.join(DATA_DIR, TABLES[table]["file"])


def _read(table):
    path = _table_path(table)
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def _write(table, headers, rows):
    path = _table_path(table)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        w.writerows(rows)


def cmd_list(args):
    headers = TABLES[args.table]["headers"]
    rows = _read(args.table)
    if not rows:
        print(f"Aucune entrée dans {args.table}.")
        return
    header_row = "  ".join(f"{h:>12}" for h in headers)
    sep = "-" * len(header_row)
    print(f"{'#':>3}  {header_row}")
    print(f"{'---':>3}  {sep}")
    for i, row in enumerate(rows, 1):
        vals = "  ".join(f"{row.get(h, ''):>12}" for h in headers)
        print(f"{i:>3}  {vals}")


def cmd_add(args):
    headers = TABLES[args.table]["headers"]
    rows = _read(args.table)
    if args.values:
        new = {}
        for kv in args.values:
            if "=" not in kv:
                print(f"ERREUR: format {kv} — attendu field=value")
                sys.exit(1)
            k, v = kv.split("=", 1)
            new[k] = v
        missing = [h for h in headers if h not in new]
        if missing:
            print(f"ERREUR: champs manquants — {', '.join(missing)}")
            sys.exit(1)
    else:
        new = {}
        print(f"Ajout dans {args.table} :")
        for h in headers:
            new[h] = input(f"  {h} : ").strip()
    rows.append(new)
    _write(args.table, headers, rows)
    print("Entrée ajoutée.")


def cmd_delete(args):
    headers = TABLES[args.table]["headers"]
    rows = _read(args.table)
    if "=" not in args.filter:
        print(f"ERREUR: format {args.filter} — attendu field=value")
        sys.exit(1)
    k, v = args.filter.split("=", 1)
    before = len(rows)
    rows = [r for r in rows if r.get(k) != v]
    removed = before - len(rows)
    if removed == 0:
        print(f"Aucune entrée avec {k}={v}.")
        return
    _write(args.table, headers, rows)
    print(f"{removed} entrée(s) supprimée(s).")


def cmd_update(args):
    headers = TABLES[args.table]["headers"]
    rows = _read(args.table)
    filter_key = filter_val = None
    updates = {}
    for kv in args.values:
        if "=" not in kv:
            print(f"ERREUR: format {kv} — attendu field=value")
            sys.exit(1)
        k, v = kv.split("=", 1)
        if filter_key is None:
            filter_key, filter_val = k, v
        else:
            updates[k] = v
    if filter_key is None or not updates:
        print("ERREUR: fournissez field=valeur (filtre) field2=nouveau ...")
        sys.exit(1)
    updated = 0
    for row in rows:
        if row.get(filter_key) == filter_val:
            row.update(updates)
            updated += 1
    if updated == 0:
        print(f"Aucune entrée avec {filter_key}={filter_val}.")
        return
    _write(args.table, headers, rows)
    print(f"{updated} entrée(s) mise(s) à jour.")


def main():
    parser = argparse.ArgumentParser(description="CRUD sur les CSV du TP Git")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("list", help="Lister les entrées")
    p.add_argument("table", choices=list(TABLES))
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("add", help="Ajouter une entrée")
    p.add_argument("table", choices=list(TABLES))
    p.add_argument("values", nargs="*", help="field=value … (omettre pour mode interactif)")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("delete", help="Supprimer des entrées")
    p.add_argument("table", choices=list(TABLES))
    p.add_argument("filter", help="field=value")
    p.set_defaults(func=cmd_delete)

    p = sub.add_parser("update", help="Modifier des entrées")
    p.add_argument("table", choices=list(TABLES))
    p.add_argument("values", nargs="+", help="field=valeur (filtre) field2=nouveau …")
    p.set_defaults(func=cmd_update)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
