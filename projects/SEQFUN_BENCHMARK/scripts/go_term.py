"""Offline GO term lookup for agent-review sandboxes (no network).

python3 tools/go_term.py search "protein kinase activity"
python3 tools/go_term.py info GO:0004672
"""

import sqlite3
import sys
from pathlib import Path

DB = Path.home() / ".data" / "oaklib" / "go.db"


def main() -> None:
    cmd, arg = sys.argv[1], " ".join(sys.argv[2:])
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    if cmd == "search":
        rows = con.execute(
            "SELECT DISTINCT s.subject, l.value FROM statements s "
            "JOIN statements l ON l.subject = s.subject AND l.predicate = 'rdfs:label' "
            "WHERE s.subject LIKE 'GO:%' AND s.predicate IN "
            "('rdfs:label', 'oio:hasExactSynonym', 'oio:hasRelatedSynonym', 'oio:hasNarrowSynonym') "
            "AND s.value LIKE ? AND l.value NOT LIKE 'obsolete %' LIMIT 40",
            (f"%{arg}%",),
        ).fetchall()
        for sid, label in rows:
            print(f"{sid}\t{label}")
    elif cmd == "info":
        for pred, name in (("rdfs:label", "label"), ("IAO:0000115", "definition")):
            for (v,) in con.execute(
                "SELECT value FROM statements WHERE subject=? AND predicate=?",
                (arg, pred),
            ):
                print(f"{name}: {v}")
        for (parent,) in con.execute(
            "SELECT object FROM statements WHERE subject=? AND predicate='rdfs:subClassOf' "
            "AND object LIKE 'GO:%'",
            (arg,),
        ):
            (label,) = con.execute(
                "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'",
                (parent,),
            ).fetchone() or ("?",)
            print(f"is_a: {parent} {label}")
    else:
        sys.exit("usage: go_term.py search TEXT | info GO:NNNNNNN")


if __name__ == "__main__":
    main()
