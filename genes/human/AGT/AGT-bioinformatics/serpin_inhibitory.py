"""Is angiotensinogen an inhibitory serpin?

GOA gives human AGT `GO:0004867 serine-type endopeptidase inhibitor activity`
three times: by IBA from PANTHER node PTN008970140, by IEA from InterPro
IPR000215 (Serpin_fam), and by TAS from a 1988 mouse gene-cloning paper. The GO
definition of that term is "Binds to and stops, prevents or reduces the activity
of a serine-type endopeptidase", so the claim is testable against the two
sequence features that make a serpin inhibitory:

1. A **reactive bond** (P1-P1') in the reactive centre loop, which UniProt
   annotates as a `SITE` of description "Reactive bond".
2. A conserved **hinge** at P17-P9. Loop insertion into beta-sheet A - the
   conformational change that traps the protease - requires small residues at
   P12-P9. Non-inhibitory serpins have a degenerate hinge.

Independently, MEROPS classifies every serpin, and reserves identifiers in the
`.9xx` range of family I04 for *non-inhibitor homologues*. That classification
is fetched from UniProt cross-references, not assumed.

The panel is built from the data, not hand-picked:
  - the target (AGT / P01019);
  - every seed protein of the PAINT IBD node that AGT inherits GO:0004867 from,
    read out of the committed PAINT slice;
  - every reviewed human SERPINA protein, which is the clade AGT sits in;
  - three reviewed non-inhibitory serpins from other clades as positive controls
    for the "non-inhibitory" end of each measure.

Run: uv run python serpin_inhibitory.py
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

from Bio import Align

from uniprot import resolve_mod_id, summarise, uniprot_entry, uniprot_search

HERE = Path(__file__).parent
PAINT = HERE.parent.parent.parent.parent / "interpro" / "panther" / "PTHR11461" / "PTHR11461-paint.tsv"

TARGET = "P01019"
ANCHOR = "P01009"  # SERPINA1, the archetypal inhibitory serpin
NODE = "PTN008970140"  # the IBD node AGT's GO:0004867 IBA descends from
TERM = "GO:0004867"

# Non-inhibitory serpins from outside the SERPINA clade, as controls.
CONTROLS = ["P36955", "P50454", "P01012"]  # SERPINF1/PEDF, SERPINH1/HSP47, ovalbumin

SMALL = set("AGST")  # residues compatible with hinge insertion into sheet A


def node_seeds() -> list[str]:
    """Seed identifiers of the IBD node AGT inherits GO:0004867 from."""
    with PAINT.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["node"] == NODE and row["go_id"] == TERM:
                return [t for t in row["seeds"].split("|") if t]
    raise SystemExit(f"no {TERM} IBD row for node {NODE} in {PAINT}")


def to_accession(token: str) -> str:
    if token.startswith("UniProtKB:"):
        return token.split(":", 1)[1]
    hits = resolve_mod_id(token)
    if not hits:
        raise SystemExit(f"could not resolve seed {token}")
    reviewed = [h for h in hits if h.get("entryType", "").startswith("UniProtKB reviewed")]
    return (reviewed or hits)[0]["primaryAccession"]


def reactive_bond(acc: str) -> int | None:
    """1-based position of P1 from UniProt's 'Reactive bond' SITE, if annotated."""
    entry = uniprot_entry(acc)
    for f in entry.get("features", []):
        if f["type"] == "Site" and "reactive bond" in f.get("description", "").lower():
            return f["location"]["start"]["value"]
    return None


def hinge_via_alignment(seq: str, anchor_seq: str, anchor_p1: int) -> tuple[str, int, str]:
    """Return the residues aligned to the anchor's P17-P9 hinge, how many of the
    four P12-P9 positions are small enough for sheet-A insertion, and the
    1-based positions those residues occupy **in the query's own UniProt
    sequence** (so any claim can be anchored on a real residue number rather
    than an alignment column)."""
    aligner = Align.PairwiseAligner(scoring="blastp", mode="global",
                                    open_gap_score=-11, extend_gap_score=-1)
    aln = aligner.align(anchor_seq, seq)[0]
    # Map anchor position -> (query residue, 1-based query position).
    mapping: dict[int, tuple[str, int]] = {}
    for (a_start, a_end), (q_start, q_end) in zip(*aln.aligned):
        for off in range(a_end - a_start):
            mapping[a_start + off] = (seq[q_start + off], q_start + off + 1)
    cols = [mapping.get(anchor_p1 - 1 - i) for i in range(16, 7, -1)]  # P17..P9
    hinge = "".join(c[0] if c else "-" for c in cols)
    positions = [c[1] for c in cols if c]
    span = f"{positions[0]}-{positions[-1]}" if positions else ""
    p12_p9 = hinge[-4:]
    return hinge, sum(1 for r in p12_p9 if r in SMALL), span


def main() -> None:
    anchor = summarise(uniprot_entry(ANCHOR))
    anchor_p1 = reactive_bond(ANCHOR)
    if anchor_p1 is None:
        raise SystemExit(f"anchor {ANCHOR} has no annotated reactive bond; cannot proceed")
    print(f"anchor {ANCHOR} ({anchor['gene']}) length {anchor['length']}, "
          f"reactive bond P1 = {anchor_p1} ({anchor['sequence'][anchor_p1 - 1]})")

    seeds = node_seeds()
    print(f"IBD node {NODE} {TERM} seeds: {len(seeds)}")
    seed_accs = [to_accession(t) for t in seeds]

    serpina = [
        h["primaryAccession"]
        for h in uniprot_search(
            "(gene:SERPINA*) AND (organism_id:9606) AND (reviewed:true)", size=60
        )
    ]
    print(f"reviewed human SERPINA entries: {len(serpina)}")

    panel: list[str] = []
    role: dict[str, list[str]] = {}
    for acc, tag in (
        [(TARGET, "target")]
        + [(a, "IBD-seed") for a in seed_accs]
        + [(a, "human-SERPINA") for a in serpina]
        + [(a, "non-inhibitory-control") for a in CONTROLS]
    ):
        base = acc.split("-")[0]
        if base not in panel:
            panel.append(base)
        role.setdefault(base, []).append(tag)

    rows = []
    for acc in panel:
        s = summarise(uniprot_entry(acc))
        if "Serpin" not in " ".join(s["keywords"]) and not any(
            m.startswith("I04.") for m in s["merops"]
        ):
            # Keep the panel to serpins; report anything dropped.
            print(f"  (dropped {acc} {s['gene']}: no serpin MEROPS id or keyword)")
            continue
        p1 = reactive_bond(acc)
        hinge, n_small, span = hinge_via_alignment(s["sequence"], anchor["sequence"], anchor_p1)
        merops = ";".join(s["merops"])
        m = re.match(r"I04\.(\d+)", merops)
        merops_class = ""
        if m:
            merops_class = "non-inhibitor homologue" if int(m.group(1)) >= 900 else "inhibitor"
        rows.append(
            {
                "accession": acc,
                "gene": s["gene"],
                "organism": s["organism"],
                "role": "/".join(sorted(set(role[acc]))),
                "merops": merops,
                "merops_class": merops_class,
                "reactive_bond_P1": str(p1) if p1 else "",
                "hinge_P17_P9": hinge,
                "hinge_positions": span,
                "small_at_P12_P9": str(n_small),
            }
        )

    out = HERE / "serpin_inhibitory.tsv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    print(f"\npanel: {len(rows)} serpins -> {out.name}\n")
    hdr = f"{'acc':10} {'gene':12} {'role':28} {'MEROPS':10} {'class':22} {'RB':5} {'hinge P17-P9':14} small"
    print(hdr)
    print("-" * len(hdr))
    for r in sorted(rows, key=lambda r: (r["merops_class"] != "non-inhibitor homologue", r["gene"])):
        print(f"{r['accession']:10} {r['gene']:12} {r['role']:28} {r['merops']:10} "
              f"{r['merops_class']:22} {r['reactive_bond_P1'] or '-':5} {r['hinge_P17_P9']:14} "
              f"{r['small_at_P12_P9']}")

    # Summary statistics, computed - not asserted.
    noninh = [r for r in rows if r["merops_class"] == "non-inhibitor homologue"]
    inh = [r for r in rows if r["merops_class"] == "inhibitor"]
    print(f"\nMEROPS non-inhibitor homologues (I04.9xx): {len(noninh)} "
          f"{[r['gene'] for r in noninh]}")
    print(f"MEROPS inhibitors: {len(inh)}")
    for label, group in (("non-inhibitor homologue", noninh), ("inhibitor", inh)):
        if not group:
            continue
        rb = sum(1 for r in group if r["reactive_bond_P1"])
        mean_small = sum(int(r["small_at_P12_P9"]) for r in group) / len(group)
        print(f"  {label:24} UniProt 'Reactive bond' annotated: {rb}/{len(group)}; "
              f"mean small residues at P12-P9: {mean_small:.2f}/4")
    tgt = next(r for r in rows if r["accession"] == TARGET)
    print(f"\nTARGET {TARGET} AGT: MEROPS {tgt['merops']} ({tgt['merops_class']}), "
          f"reactive bond {tgt['reactive_bond_P1'] or 'NOT ANNOTATED'}, "
          f"hinge {tgt['hinge_P17_P9']} at P01019 residues {tgt['hinge_positions']}, "
          f"{tgt['small_at_P12_P9']}/4 small at P12-P9")
    anc = next(r for r in rows if r["accession"] == ANCHOR)
    print(f"ANCHOR {ANCHOR} SERPINA1: hinge {anc['hinge_P17_P9']} at P01009 residues "
          f"{anc['hinge_positions']}, {anc['small_at_P12_P9']}/4 small at P12-P9")
    seed_rows = [r for r in rows if "IBD-seed" in r["role"]]
    print(f"IBD seeds classed as MEROPS inhibitors: "
          f"{sum(1 for r in seed_rows if r['merops_class'] == 'inhibitor')}/{len(seed_rows)}")


if __name__ == "__main__":
    main()
