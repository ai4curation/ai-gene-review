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

The ``review_action`` column is not hard-coded: it is read from
``treegrafter_review.tsv`` (regenerate that first with analyze_treegrafter.py).
``--refresh-actions`` updates just that column of the committed TSV offline.

Run:
  python3 projects/TREEGRAFTER/graft_check.py [--out-dir DIR]     # network
  python3 projects/TREEGRAFTER/graft_check.py --refresh-actions   # offline
Output: treegrafter_graft_check.tsv
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# (gene, organism, uniprot_acc, propagated_term, propagated_id, expected_function)
# The reviewer action is NOT stored here: it is looked up at run time from
# treegrafter_review.tsv (see review_actions()), so it cannot go stale.
EXEMPLARS = [
    ("aprA", "DESVH", "Q72DT2", "succinate dehydrogenase activity", "GO:0000104",
     "adenylylsulfate (APS) reductase alpha (EC 1.8.99.2)"),
    ("fcs", "PSEPK", "Q88HK0", "medium-chain fatty acid-CoA ligase activity",
     "GO:0031956", "feruloyl-CoA synthetase (EC 6.2.1.34)"),
    ("OCTS1", "OCTVU", "P27013", "glutathione transferase activity", "GO:0004364",
     "S-crystallin / lens structural protein (GST fold, ~no activity)"),
    ("eryAIII", "SACEN", "A4F7P1", "fatty acid synthase activity", "GO:0004312",
     "erythromycin polyketide synthase module (PKS)"),
    ("mcr-1", "ECOLX", "A0A0R6L508", "phosphotransferase activity, phosphate group as acceptor",
     "GO:0016776", "phosphoethanolamine transferase (lipid A modification)"),
    # --- second batch (distinct enzyme families) ---
    ("NaPMT3", "NICAT", "A0A314LG79", "spermidine synthase activity", "GO:0004766",
     "putrescine N-methyltransferase (PMT, neofunctionalized from spermidine synthase)"),
    ("ADAR2", "DOROP", "C1JAR3", "tRNA-specific adenosine deaminase activity", "GO:0008251",
     "double-stranded RNA / mRNA adenosine deaminase (ADAR, not tRNA-specific ADAT)"),
    ("NaUGT1_candidate_UGT85A2_0", "NICAT", "A0A2H4GSI3",
     "quercetin 3-O-glucosyltransferase activity", "GO:0080043",
     "UDP-glucuronosyltransferase / UGT family (specific flavonoid substrate unproven)"),
    ("aceK", "PSEPK", "Q88EA1", "phosphoprotein phosphatase activity", "GO:0004721",
     "isocitrate dehydrogenase kinase/phosphatase (bifunctional, atypical)"),
    ("ahpC", "PSEPK", "Q88K52", "thioredoxin peroxidase activity", "GO:0008379",
     "alkyl hydroperoxide reductase / 2-Cys peroxiredoxin (AhpC)"),
]

REVIEW_TSV = os.path.join(HERE, "treegrafter_review.tsv")
FIELDS = ["gene", "organism", "uniprot", "review_action", "propagated_term",
          "expected_function", "panther_family", "panther_subfamily", "pfam",
          "interpro_specific_entries", "interpro_all"]


def review_actions(path: str = REVIEW_TSV) -> dict:
    """{(organism, gene, term_id): action} from treegrafter_review.tsv.

    The review file path is ``genes/<ORG>/<gene-dir>/...``; exemplars are keyed
    on the directory name (UniProt accession for aprA, whose dir is Q72DT2)."""
    out = {}
    with open(path) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            parts = r["file"].split("/")
            if len(parts) >= 3:
                out[(parts[1], parts[2], r["term_id"])] = r["action"]
                out[(parts[1], r["gene"], r["term_id"])] = r["action"]
    return out


def action_for(actions: dict, gene: str, org: str, acc: str, term_id: str) -> str:
    return (actions.get((org, gene, term_id)) or actions.get((org, acc, term_id))
            or "NOT_IN_REVIEW_TSV")


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
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out-dir", default=HERE,
                    help="directory for treegrafter_graft_check.tsv (default: next to this script)")
    ap.add_argument("--refresh-actions", action="store_true",
                    help="offline: rewrite only the review_action column of the existing "
                         "treegrafter_graft_check.tsv from treegrafter_review.tsv (no network)")
    args = ap.parse_args()
    out = os.path.join(os.path.abspath(args.out_dir), "treegrafter_graft_check.tsv")
    actions = review_actions()
    by_acc = {acc: (gene, org, term_id) for gene, org, acc, _t, term_id, _e in EXEMPLARS}

    if args.refresh_actions:
        with open(os.path.join(HERE, "treegrafter_graft_check.tsv")) as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
        kept = []
        for r in rows:
            if r["uniprot"] not in by_acc:
                print(f"WARN: {r['uniprot']} is no longer in EXEMPLARS; dropping its row",
                      file=sys.stderr)
                continue
            gene, org, term_id = by_acc[r["uniprot"]]
            r["review_action"] = action_for(actions, gene, org, r["uniprot"], term_id)
            kept.append(r)
        rows = kept
    else:
        rows = []
        for gene, org, acc, term, term_id, expected in EXEMPLARS:
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
                "review_action": action_for(actions, gene, org, acc, term_id),
                "propagated_term": f"{term} ({term_id})",
                "expected_function": expected,
                "panther_family": fam,
                "panther_subfamily": sub,
                "pfam": ",".join(pfam),
                "interpro_specific_entries": interpro_is_more_specific(interpro, expected),
                "interpro_all": " | ".join(f"{i}:{n}" for i, n in interpro),
            })

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t")
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
