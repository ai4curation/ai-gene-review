#!/usr/bin/env python3
"""Lightweight TreeGrafter graft check for the down-graded exemplars.

This is the "did it land on the right part of the tree?" check the project's
[failure-modes](failure-modes.md) page calls for, done *without* a full local
InterProScan/TreeGrafter install. For each exemplar protein we fetch the live
UniProt record and read two independent classifications:

  * PANTHER family + subfamily  — the TreeGrafter graft point (what propagated
    the GO term).
  * InterPro entries            — signature-based identification (InterPro2GO's
    basis), an independent opinion on what the protein actually is.

We then ask: does InterPro identify the protein *more specifically/correctly*
than the PANTHER subfamily TreeGrafter used? When it does (e.g. aprA), the
TreeGrafter error is a PANTHER **subfamily-resolution / coverage gap**, and an
InterPro-based call would have been better. When neither has a function-specific
entry (e.g. fcs), the protein sits in the correct fold superfamily but no
database resolves its specific substrate.

Network: UniProt REST (https://rest.uniprot.org). Honors HTTPS_PROXY.

Run:
  uv run --with requests projects/TREEGRAFTER/graft_check.py
Output: treegrafter_graft_check.tsv
"""
from __future__ import annotations

import csv
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# (gene, organism, uniprot_acc, propagated_term, propagated_id, review_action,
#  expected_function)
EXEMPLARS = [
    ("aprA", "DESVH", "Q72DT2", "succinate dehydrogenase activity", "GO:0000104",
     "REMOVE", "adenylylsulfate (APS) reductase alpha (EC 1.8.99.2)"),
    ("fcs", "PSEPK", "Q88HK0", "medium-chain fatty acid-CoA ligase activity",
     "GO:0031956", "MODIFY", "feruloyl-CoA synthetase (EC 6.2.1.34)"),
    ("OCTS1", "OCTVU", "P27013", "glutathione transferase activity", "GO:0004364",
     "MARK_AS_OVER_ANNOTATED", "S-crystallin / lens structural protein (GST fold, ~no activity)"),
    ("eryAIII", "SACEN", "A4F7P1", "fatty acid synthase activity", "GO:0004312",
     "MODIFY", "erythromycin polyketide synthase module (PKS)"),
    ("mcr-1", "ECOLX", "A0A0R6L508", "phosphotransferase activity, phosphate group as acceptor",
     "GO:0016776", "MODIFY", "phosphoethanolamine transferase (lipid A modification)"),
]


def fetch_uniprot(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.txt"
    req = urllib.request.Request(url, headers={"User-Agent": "aigr-treegrafter-check"})
    with urllib.request.urlopen(req, timeout=40) as fh:  # noqa: S310 - fixed host
        return fh.read().decode("utf-8", "replace")


def parse_xrefs(text: str):
    """Return (panther_family, panther_subfamily, interpro:[(id,name)], pfam:[..])."""
    fam = sub = ""
    interpro = []
    pfam = []
    for line in text.splitlines():
        if not line.startswith("DR   "):
            continue
        body = line[5:].strip().rstrip(".")
        parts = [p.strip() for p in body.split(";")]
        db = parts[0]
        if db == "PANTHER":
            pid = parts[1] if len(parts) > 1 else ""
            name = parts[2] if len(parts) > 2 else ""
            if ":SF" in pid:
                sub = f"{pid} {name}"
            else:
                fam = f"{pid} {name}"
        elif db == "InterPro":
            interpro.append((parts[1], parts[2] if len(parts) > 2 else ""))
        elif db == "Pfam":
            pfam.append(parts[1])
    return fam, sub, interpro, pfam


def interpro_is_more_specific(interpro, expected: str) -> str:
    """Heuristic: does any InterPro entry name a specific function/family that
    the PANTHER subfamily missed? Returns a short verdict string."""
    names = " | ".join(n for _, n in interpro).lower()
    # Look for a specific (non-superfamily, non-domain) InterPro family name.
    specific = [f"{i} {n}" for i, n in interpro
                if n and not any(t in n.lower() for t in
                                 ("domain", "superfamily", "_sf", "-like", "fold"))]
    return "; ".join(specific) if specific else "(only generic domain/superfamily entries)"


def main() -> None:
    rows = []
    for gene, org, acc, term, term_id, action, expected in EXEMPLARS:
        try:
            text = fetch_uniprot(acc)
        except Exception as exc:  # noqa: BLE001
            print(f"WARN: fetch failed for {gene} ({acc}): {exc}", file=sys.stderr)
            continue
        fam, sub, interpro, pfam = parse_xrefs(text)
        rows.append({
            "gene": gene,
            "organism": org,
            "uniprot": acc,
            "review_action": action,
            "propagated_term": f"{term} ({term_id})",
            "expected_function": expected,
            "panther_family": fam,
            "panther_subfamily": sub,
            "pfam": ",".join(pfam),
            "interpro_specific_entries": interpro_is_more_specific(interpro, expected),
            "interpro_all": " | ".join(f"{i}:{n}" for i, n in interpro),
        })

    out = os.path.join(HERE, "treegrafter_graft_check.tsv")
    fields = ["gene", "organism", "uniprot", "review_action", "propagated_term",
              "expected_function", "panther_family", "panther_subfamily", "pfam",
              "interpro_specific_entries", "interpro_all"]
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    for r in rows:
        print(f"\n### {r['gene']} ({r['uniprot']}) — review: {r['review_action']}")
        print(f"  propagated term : {r['propagated_term']}")
        print(f"  expected        : {r['expected_function']}")
        print(f"  PANTHER family  : {r['panther_family']}")
        print(f"  PANTHER subfam  : {r['panther_subfamily']}  <- graft point")
        print(f"  InterPro specific: {r['interpro_specific_entries']}")
    print(f"\nWrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
