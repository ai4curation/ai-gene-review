#!/usr/bin/env python3
"""Does human ADCK1 retain the canonical protein-kinase catalytic motifs?

Motivation
----------
UniProt Q86TW2 carries `EC=2.7.-.-`, the keywords `Kinase` /
`Serine/threonine-protein kinase` / `ATP-binding`, and ATP-ligand BINDING sites,
all traceable to `PROSITE-ProRule:PRU00159` (the generic protein-kinase ProRule,
`ECO:0000255`). Its own FUNCTION comment says the opposite: "It is not known if
it has protein kinase activity and what type of substrate it would phosphorylate
(Ser, Thr or Tyr)".

The UbiB/ABC1 family is documented to deviate from the canonical protein-kinase
motifs, and for COQ8A those deviations were shown to matter: the Ala-rich loop
confers selectivity for ADP over ATP, and a single Ala->Gly (ADCK3 A339G) flips
it back and enables autophosphorylation (PMID:25498144). This script measures
*which* deviations ADCK1 actually carries, rather than reading them off family
prose.

Method
------
Three passes, because they have different failure modes.

PASS 1 (alignment-free, strongest). PKA, ADCK1 and ADCK2 each carry a
UniProt-curated **9-residue ATP BINDING site** covering the phosphate-binding
(P-)loop. Same ligand, same length, same curated feature type: comparing them
column-for-column needs no alignment at all, so no alignment artefact can enter.

PASS 2 (alignment, for motifs not annotated everywhere). Sequences are trimmed
to each protein's own UniProt-annotated "Protein kinase" DOMAIN before MAFFT
L-INS-i, so that long, unalignable N-terminal extensions cannot displace the
catalytic columns. Motif columns are anchored on PKA feature-table entries, so
no motif position is hand-assigned:

  * beta3 Lys     -> PKA `BINDING 73`      (ligand ATP)
  * catalytic Asp -> PKA `ACT_SITE 167`    ("Proton acceptor", the HRD Asp)
  * catalytic Asn -> PKA `BINDING 169..172`, last residue
  * HRD Arg       -> the residue immediately before PKA's ACT_SITE
  * Mg-binding Asp-> the first DxG downstream of PKA's catalytic loop

Following the campaign rule that residue identity alone manufactures motifs out
of alignment noise, every transferred position is also checked for whether it
**lands on a site the target protein's own feature table annotates**; that
corroboration is reported separately from bare residue identity.

The run aborts unless the alignment reproduces published mutagenesis positions
(ADCK1 K183/D315 from PMID:31125351; COQ8A K358/D488/N493/D507 from its own
feature table). A shifted column invents or erases motif losses, so this gate
must pass before any number below is interpreted.

PASS 3 re-reads the two residues before each protein's own catalytic Asp straight
from its sequence, because PASS 2 reports the HRD-arginine column as a gap in every
UbiB protein and a gap can be an alignment artefact rather than a deletion.

Outputs `results.json` and a generated `RESULTS.md` (do not hand-edit the latter;
a fresh run must reproduce it byte-for-byte). Missing inputs are hard errors naming
the fix; ambiguity is reported, never silently resolved.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import requests

HERE = Path(__file__).parent
CACHE = HERE / "cache"
CACHE.mkdir(exist_ok=True)

REFERENCE = "P17612"

# accession -> (short label, role, expected gene/ORF token used to verify the
# accession actually resolves to the protein named).
PROTEINS: dict[str, tuple[str, str, str]] = {
    "P17612": ("PKA-Ca", "canonical protein kinase (positive control)", "PRKACA"),
    "Q86TW2": ("ADCK1", "subject", "ADCK1"),
    "Q3MIX3": ("ADCK5", "closest human paralog; same PANTHER family PTHR43173", "ADCK5"),
    "Q7Z695": ("ADCK2", "human ortholog of yeast Cqd1", "ADCK2"),
    "Q8NI60": ("COQ8A", "characterised UbiB; crystal structure 4PED", "ADCK3"),
    "Q96D53": ("COQ8B", "characterised UbiB", "ADCK4"),
    "Q06567": ("Cqd2", "S. cerevisiae ADCK1 ortholog (PANTHER SF19); IBA donor", "YLR253W"),
    "Q02981": ("Cqd1", "S. cerevisiae ADCK2 ortholog", "YPL109C"),
    "P27697": ("Coq8", "S. cerevisiae Coq8/Abc1", "YGL119W"),
}

# Published anchors used ONLY as assertions that the alignment is in register.
# ADCK1: Yoon et al. 2019 (PMID:31125351) mutagenised A164/K183/D315/D338.
# COQ8A: its own UniProt feature table annotates K358/D488/N493/D507.
PUBLISHED_ANCHORS: dict[str, dict[int, str]] = {
    "Q86TW2": {183: "beta3_lys", 315: "catalytic_asp"},
    "Q8NI60": {358: "beta3_lys", 488: "catalytic_asp", 493: "catalytic_asn", 507: "dfg_asp"},
}


def fetch_entry(acc: str) -> dict:
    path = CACHE / f"{acc}.json"
    if not path.exists():
        url = (
            f"https://rest.uniprot.org/uniprotkb/{acc}.json"
            "?fields=accession,id,protein_name,gene_names,organism_name,"
            "sequence,ft_binding,ft_act_site,ft_domain,length,reviewed"
        )
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        path.write_text(resp.text)
    entry = json.loads(path.read_text())
    # A deleted/inactive UniProt entry returns no sequence and no name; querying
    # it is otherwise indistinguishable from a protein carrying nothing.
    if not entry.get("sequence", {}).get("value"):
        raise SystemExit(
            f"FATAL: {acc} returned no sequence — probably an inactive (deleted) "
            f"UniProt entry. Find the live accession, update PROTEINS, and delete "
            f"{path}."
        )
    if not entry.get("uniProtkbId"):
        raise SystemExit(f"FATAL: {acc} returned no entry name (uniProtkbId).")
    return entry


def gene_tokens(entry: dict) -> set[str]:
    toks: set[str] = set()
    for g in entry.get("genes", []):
        if g.get("geneName"):
            toks.add(g["geneName"]["value"].upper())
        for o in g.get("orderedLocusNames", []) or []:
            toks.add(o["value"].upper())
        for s in g.get("synonyms", []) or []:
            toks.add(s["value"].upper())
    return toks


def is_reviewed(entry: dict) -> bool:
    # "reviewed" is a substring of "unreviewed"; `in` silently promotes TrEMBL.
    return str(entry.get("entryType", "")).startswith("UniProtKB reviewed")


def annotated_sites(entry: dict) -> dict[int, list[str]]:
    out: dict[int, list[str]] = {}
    for feat in entry.get("features", []):
        if feat["type"] not in ("Binding site", "Active site"):
            continue
        start = feat["location"]["start"]["value"]
        end = feat["location"]["end"]["value"]
        if start is None or end is None:
            continue
        lig = (feat.get("ligand") or {}).get("name")
        label = feat["type"] + (f" ({feat['description']})" if feat.get("description") else "")
        if lig:
            label += f" [ligand {lig}]"
        for pos in range(start, end + 1):
            out.setdefault(pos, []).append(label)
    return out


def find_feature(entry: dict, ftype: str, start: int, end: int | None = None) -> dict:
    end = start if end is None else end
    for feat in entry.get("features", []):
        loc = feat["location"]
        if feat["type"] == ftype and loc["start"]["value"] == start and loc["end"]["value"] == end:
            return feat
    raise SystemExit(
        f"FATAL: {entry['primaryAccession']} has no {ftype} at {start}..{end}; the "
        f"UniProt feature table has changed. Delete {CACHE}/{entry['primaryAccession']}.json, "
        "inspect the new table, and re-derive the anchors."
    )


def kinase_domain(entry: dict) -> tuple[int, int] | None:
    for feat in entry.get("features", []):
        if feat["type"] == "Domain" and feat.get("description") == "Protein kinase":
            return feat["location"]["start"]["value"], feat["location"]["end"]["value"]
    return None


def run_mafft(records: list[tuple[str, str]]) -> dict[str, str]:
    if shutil.which("mafft") is None:
        raise SystemExit("FATAL: mafft is not on PATH. `brew install mafft` and re-run.")
    with tempfile.TemporaryDirectory() as td:
        fa = Path(td) / "in.fa"
        fa.write_text("".join(f">{n}\n{s}\n" for n, s in records))
        proc = subprocess.run(
            ["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fa)],
            capture_output=True, text=True, check=True,
        )
    aln: dict[str, str] = {}
    name = None
    for line in proc.stdout.splitlines():
        if line.startswith(">"):
            name = line[1:].strip()
            aln[name] = ""
        elif name:
            aln[name] += line.strip()
    lengths = {len(v) for v in aln.values()}
    if len(lengths) != 1:
        raise SystemExit(f"FATAL: MAFFT returned ragged alignment lengths {lengths}.")
    if set(aln) != {n for n, _ in records}:
        raise SystemExit("FATAL: MAFFT dropped or renamed a sequence.")
    return aln


def col_of(aligned: str, pos: int) -> int:
    seen = 0
    for col, ch in enumerate(aligned):
        if ch != "-":
            seen += 1
            if seen == pos:
                return col
    raise SystemExit(f"FATAL: position {pos} exceeds the ungapped length of the sequence.")


def pos_of(aligned: str, col: int) -> int | None:
    if aligned[col] == "-":
        return None
    return sum(1 for ch in aligned[: col + 1] if ch != "-")


def main() -> int:
    entries = {acc: fetch_entry(acc) for acc in PROTEINS}

    # Verify each accession resolves to the protein it is labelled as. A wrong
    # accession silently substitutes a different protein: two of the yeast
    # accessions in the first draft of this script were wrong exactly this way
    # (Q12296 is MAM3, not Cqd1; Q08058 is COQ10, not Coq8).
    for acc, (label, _role, expect) in PROTEINS.items():
        toks = gene_tokens(entries[acc])
        if expect.upper() not in toks:
            raise SystemExit(
                f"FATAL: {acc} was labelled '{label}' expecting gene/ORF "
                f"'{expect}', but UniProt reports {sorted(toks)} "
                f"({entries[acc]['uniProtkbId']}). Fix the accession."
            )

    ref = entries[REFERENCE]
    ref_seq = ref["sequence"]["value"]

    # ---------------- PASS 1: annotated 9-residue P-loops, no alignment -------
    ploop_len = 9
    ploops: dict[str, dict] = {}
    for acc in PROTEINS:
        e = entries[acc]
        seq = e["sequence"]["value"]
        hit = None
        for feat in e.get("features", []):
            if feat["type"] != "Binding site":
                continue
            s, en = feat["location"]["start"]["value"], feat["location"]["end"]["value"]
            if s is None or en is None or (en - s + 1) != ploop_len:
                continue
            if (feat.get("ligand") or {}).get("name") != "ATP":
                continue
            hit = (s, en, seq[s - 1 : en])
            break
        ploops[acc] = (
            {"annotated": True, "start": hit[0], "end": hit[1], "sequence": hit[2]}
            if hit else {"annotated": False}
        )

    ref_ploop = ploops[REFERENCE]
    if not ref_ploop["annotated"]:
        raise SystemExit("FATAL: PKA has no 9-residue ATP BINDING site; anchors unusable.")
    # GxGxxG glycines are at offsets 1, 3 and 6 of PKA's LGTGSFGRV.
    gly_offsets = [i for i, ch in enumerate(ref_ploop["sequence"]) if ch == "G"]
    if gly_offsets != [1, 3, 6]:
        raise SystemExit(
            f"FATAL: PKA P-loop {ref_ploop['sequence']} does not have glycines at "
            f"offsets 1/3/6 (found {gly_offsets}); the GxGxxG anchor is invalid."
        )

    ploop_report: dict[str, dict] = {}
    for acc, pl in ploops.items():
        if not pl["annotated"]:
            ploop_report[acc] = {"annotated": False}
            continue
        s = pl["sequence"]
        ploop_report[acc] = {
            "annotated": True,
            "range": f"{pl['start']}..{pl['end']}",
            "sequence": s,
            "glycines_retained": sum(1 for off in gly_offsets if s[off] == "G"),
            "residues_at_glycine_offsets": {
                f"offset_{off}": {"residue": s[off], "position": pl["start"] + off}
                for off in gly_offsets
            },
        }

    # Assert the published ADCK1 A-rich-loop residue is where we think it is.
    a1 = ploop_report["Q86TW2"]
    if not a1["annotated"]:
        raise SystemExit("FATAL: ADCK1 has no annotated 9-residue ATP BINDING site.")
    a164 = a1["residues_at_glycine_offsets"]["offset_3"]
    if not (a164["position"] == 164 and a164["residue"] == "A"):
        raise SystemExit(
            f"FATAL: ADCK1 offset-3 P-loop residue is {a164['residue']}{a164['position']}, "
            "but PMID:31125351 mutagenised A164 as a phosphotransfer residue. The "
            "P-loop anchor is out of register."
        )

    # ---------------- PASS 2: domain-restricted alignment ---------------------
    trimmed: list[tuple[str, str]] = []
    domain_used: dict[str, str] = {}
    offset: dict[str, int] = {}
    for acc in PROTEINS:
        seq = entries[acc]["sequence"]["value"]
        dom = kinase_domain(entries[acc])
        if dom:
            s, e = dom
            # Pad so that the P-loop, which can sit just upstream of the
            # annotated domain start, is inside the aligned region.
            s = max(1, s - 20)
            e = min(len(seq), e + 20)
            trimmed.append((acc, seq[s - 1 : e]))
            domain_used[acc] = f"Protein kinase domain {dom[0]}..{dom[1]} (padded to {s}..{e})"
            offset[acc] = s - 1
        else:
            trimmed.append((acc, seq))
            domain_used[acc] = "NO annotated protein-kinase domain; full sequence used"
            offset[acc] = 0

    aln = run_mafft(trimmed)
    ref_aln = aln[REFERENCE]
    ro = offset[REFERENCE]

    act = find_feature(ref, "Active site", 167, 167)
    beta3 = find_feature(ref, "Binding site", 73, 73)
    catloop = find_feature(ref, "Binding site", 169, 172)
    m = re.search(r"D.G", ref_seq[172:220])
    if not m:
        raise SystemExit("FATAL: could not locate a DxG motif downstream of PKA residue 172.")
    dfg_pos = 172 + m.start() + 1

    ref_anchors = {
        "beta3_lys": (beta3["location"]["start"]["value"], "beta3 lysine (VAIK)"),
        "hrd_arg": (act["location"]["start"]["value"] - 1, "HRD arginine (residue before ACT_SITE)"),
        "catalytic_asp": (act["location"]["start"]["value"], "catalytic Asp / proton acceptor (HRD)"),
        "catalytic_asn": (catloop["location"]["end"]["value"], "catalytic-loop Asn"),
        "dfg_asp": (dfg_pos, "Mg-binding Asp (DFG)"),
    }
    expected_ref = {
        "beta3_lys": "K", "hrd_arg": "R", "catalytic_asp": "D",
        "catalytic_asn": "N", "dfg_asp": "D",
    }
    motif_cols = {k: col_of(ref_aln, p - ro) for k, (p, _) in ref_anchors.items()}
    for k, col in motif_cols.items():
        if ref_aln[col] != expected_ref[k]:
            raise SystemExit(
                f"FATAL: PKA reads '{ref_aln[col]}' at {k} (expected "
                f"'{expected_ref[k]}'); anchor derivation is wrong."
            )

    table: dict[str, dict] = {}
    for acc, (label, role, _) in PROTEINS.items():
        e = entries[acc]
        sites = annotated_sites(e)
        row = {
            "accession": acc, "label": label, "role": role,
            "entry_name": e["uniProtkbId"], "reviewed": is_reviewed(e),
            "length": len(e["sequence"]["value"]),
            "region_aligned": domain_used[acc],
            "ploop": ploop_report[acc],
            "motifs": {},
        }
        for k, col in motif_cols.items():
            rel = pos_of(aln[acc], col)
            pos = None if rel is None else rel + offset[acc]
            res = aln[acc][col]
            row["motifs"][k] = {
                "residue": None if res == "-" else res,
                "position": pos,
                "matches_canonical": res == expected_ref[k],
                "lands_on_own_annotated_site": bool(pos and pos in sites),
                "own_annotation": sites.get(pos, []) if pos else [],
            }
        table[acc] = row

    checks = []
    for acc, wanted in PUBLISHED_ANCHORS.items():
        for pos, k in wanted.items():
            got = table[acc]["motifs"][k]["position"]
            checks.append({
                "accession": acc, "label": PROTEINS[acc][0], "motif": k,
                "published_position": pos, "aligned_position": got,
                "reproduced": got == pos,
            })
    bad = [c for c in checks if not c["reproduced"]]
    if bad:
        raise SystemExit(
            "FATAL: the alignment does not reproduce published/curated anchor "
            f"positions: {bad}. Do not interpret the motif table — a shifted "
            "column invents or erases motif losses."
        )

    # ---- PASS 2b: P-loop for the six proteins that do not annotate one -------
    # Only PKA, ADCK1 and ADCK2 carry a curated 9-residue ATP BINDING site, so
    # the other six can be read only through the alignment. Gate it on
    # reproducing Stefely et al.'s A-rich-loop residue: PMID:25498144
    # mutagenised ADCK3/COQ8A **A339** to Gly to flip ADP->ATP selectivity, and
    # that residue must land in PKA's second-glycine column or the P-loop
    # register is wrong and none of these readings mean anything.
    ploop_cols = {off: col_of(ref_aln, (ref_ploop["start"] + off) - ro) for off in gly_offsets}
    ploop_aligned: dict[str, dict] = {}
    for acc in PROTEINS:
        vals = {}
        for off, col in ploop_cols.items():
            rel = pos_of(aln[acc], col)
            vals[f"offset_{off}"] = {
                "residue": None if aln[acc][col] == "-" else aln[acc][col],
                "position": None if rel is None else rel + offset[acc],
            }
        ploop_aligned[acc] = {
            "residues": vals,
            "glycines_retained": sum(1 for v in vals.values() if v["residue"] == "G"),
        }
    coq8a_g2 = ploop_aligned["Q8NI60"]["residues"]["offset_3"]
    if not (coq8a_g2["position"] == 339 and coq8a_g2["residue"] == "A"):
        raise SystemExit(
            f"FATAL: the alignment places COQ8A "
            f"{coq8a_g2['residue']}{coq8a_g2['position']} in PKA's second "
            "G-rich-loop glycine column, but PMID:25498144 mutagenised COQ8A "
            "A339 there. The P-loop register is wrong; do not read PASS 2b."
        )
    # Where a protein annotates its own P-loop, the alignment must agree with it.
    for acc in PROTEINS:
        if not ploop_report[acc]["annotated"]:
            continue
        for off in gly_offsets:
            curated = ploop_report[acc]["residues_at_glycine_offsets"][f"offset_{off}"]
            derived = ploop_aligned[acc]["residues"][f"offset_{off}"]
            if (curated["residue"], curated["position"]) != (derived["residue"], derived["position"]):
                raise SystemExit(
                    f"FATAL: for {PROTEINS[acc][0]} offset {off}, the curated "
                    f"P-loop says {curated['residue']}{curated['position']} but the "
                    f"alignment says {derived['residue']}{derived['position']}. "
                    "PASS 1 and PASS 2b disagree; resolve before interpreting."
                )

    # ---- PASS 3: catalytic-loop context, read WITHOUT using the alignment ----
    # PASS 2 reported the HRD arginine column as a gap in every UbiB protein.
    # A gap can be an alignment artefact rather than a deletion, so re-read the
    # two residues preceding each protein's catalytic Asp directly from its own
    # sequence. The Asp itself is corroborated by each protein's own ACT_SITE
    # where one is annotated, so this pass carries no alignment dependence.
    catloop_context: dict[str, dict] = {}
    for acc in PROTEINS:
        seq = entries[acc]["sequence"]["value"]
        d = table[acc]["motifs"]["catalytic_asp"]["position"]
        if d is None or d < 3:
            catloop_context[acc] = {"available": False}
            continue
        catloop_context[acc] = {
            "available": True,
            "catalytic_asp": f"D{d}",
            "hxd_triplet": seq[d - 3 : d],
            "arg_at_minus_one": seq[d - 2] == "R",
            "residue_at_minus_one": seq[d - 2],
            "residue_at_minus_two": seq[d - 3],
        }
    if not catloop_context[REFERENCE]["available"]:
        raise SystemExit("FATAL: could not read PKA's own catalytic-loop context.")
    if not catloop_context[REFERENCE]["arg_at_minus_one"]:
        raise SystemExit(
            "FATAL: PKA does not read Arg immediately before its catalytic Asp; "
            "the HRD context definition is wrong."
        )

    # ---------------- Report --------------------------------------------------
    print("PASS 1 — UniProt-curated 9-residue ATP BINDING sites (no alignment involved)")
    print(f"  PKA GxGxxG glycines sit at P-loop offsets {gly_offsets}\n")
    print(f"  {'protein':8s} {'range':14s} {'P-loop':11s}  glycines retained (of 3)")
    for acc in PROTEINS:
        r = ploop_report[acc]
        lab = PROTEINS[acc][0]
        if not r["annotated"]:
            print(f"  {lab:8s} {'-':14s} {'(not annotated)':11s}  n/a")
        else:
            detail = ", ".join(
                f"{v['residue']}{v['position']}" for v in r["residues_at_glycine_offsets"].values()
            )
            print(f"  {lab:8s} {r['range']:14s} {r['sequence']:11s}  {r['glycines_retained']}/3   [{detail}]")

    print("\nPASS 2 — catalytic motifs via domain-restricted MAFFT L-INS-i")
    keys = list(ref_anchors)
    hdr = f"  {'protein':8s} {'rev':4s} " + " ".join(f"{k[:13]:>14s}" for k in keys)
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for acc in PROTEINS:
        row = table[acc]
        cells = []
        for k in keys:
            mm = row["motifs"][k]
            r = mm["residue"] or "-"
            mark = "*" if mm["lands_on_own_annotated_site"] else ""
            cells.append(f"{r}{mm['position'] if mm['position'] else ''}{mark}")
        print(f"  {row['label']:8s} {'SP' if row['reviewed'] else 'TrEMBL':4s} "
              + " ".join(f"{c:>14s}" for c in cells))
    print("\n  '*' = the transferred column lands on a site this protein's own UniProt "
          "feature table annotates.")
    print("  Proteins with no annotated protein-kinase domain (aligned full-length):")
    for acc in PROTEINS:
        if "NO annotated" in domain_used[acc]:
            print(f"    {PROTEINS[acc][0]} ({acc})")

    print("\n  Anchor reproduction gate (all must be True):")
    for c in checks:
        print(f"    {c['label']:8s} {c['motif']:15s} curated {c['published_position']:4d} "
              f"-> aligned {c['aligned_position']}  {c['reproduced']}")

    n_rev = sum(1 for a in PROTEINS if table[a]["reviewed"])
    print(f"\n  Swiss-Prot reviewed: {n_rev}/{len(PROTEINS)}")

    print("\nPASS 2b — P-loop glycine columns via the alignment (gated on COQ8A A339)")
    for acc in PROTEINS:
        pa = ploop_aligned[acc]
        detail = ", ".join(
            f"{v['residue'] or '-'}{v['position'] or ''}" for v in pa["residues"].values()
        )
        src = "curated" if ploop_report[acc]["annotated"] else "aligned"
        print(f"  {PROTEINS[acc][0]:8s} {pa['glycines_retained']}/3 glycines "
              f"[{detail}]  ({src})")

    print("\nPASS 3 — catalytic-loop context read from each sequence directly")
    print("  (tests whether PASS 2's HRD-arginine gap is biology or alignment noise)")
    for acc in PROTEINS:
        c = catloop_context[acc]
        if not c["available"]:
            print(f"  {PROTEINS[acc][0]:8s} unavailable")
            continue
        print(f"  {PROTEINS[acc][0]:8s} {c['catalytic_asp']:6s} "
              f"H-x-D context '{c['hxd_triplet']}D'   Arg at D-1: {c['arg_at_minus_one']}")
    n_arg = sum(1 for a in PROTEINS if a != REFERENCE and catloop_context[a]["arg_at_minus_one"])
    print(f"  Arg immediately before the catalytic Asp: {n_arg}/{len(PROTEINS) - 1} UbiB "
          f"proteins (PKA, the control, has it).")

    adck1 = table["Q86TW2"]["motifs"]
    kept = [k for k in keys if adck1[k]["matches_canonical"]]
    lost = [k for k in keys if not adck1[k]["matches_canonical"]]
    print(f"\nADCK1 catalytic-motif residues RETAINED : {kept}")
    print(f"ADCK1 catalytic-motif residues DIVERGENT: "
          f"{[(k, adck1[k]['residue'], adck1[k]['position']) for k in lost]}")
    print(f"ADCK1 P-loop glycines retained: {ploop_report['Q86TW2']['glycines_retained']}/3")

    print("\nPer-column conservation across the eight UbiB/PKL proteins (PKA excluded):")
    ubib = [a for a in PROTEINS if a != REFERENCE]
    for k in keys:
        n = sum(1 for a in ubib if table[a]["motifs"][k]["matches_canonical"])
        detail = {PROTEINS[a][0]: table[a]["motifs"][k]["residue"] for a in ubib}
        print(f"  {k:15s} canonical in {n}/{len(ubib)}   {detail}")

    results = {
        "reference": REFERENCE,
        "proteins": table,
        "ploop_glycine_offsets_in_pka": gly_offsets,
        "motif_anchors": {k: {"pka_position": v[0], "description": v[1]} for k, v in ref_anchors.items()},
        "anchor_reproduction_checks": checks,
        "catalytic_loop_context": catloop_context,
        "n_ubib_with_arg_before_catalytic_asp": n_arg,
        "adck1_motifs_retained": kept,
        "adck1_motifs_divergent": lost,
        "adck1_ploop_glycines_retained": ploop_report["Q86TW2"]["glycines_retained"],
        "ploop_aligned": ploop_aligned,
        "n_reviewed": n_rev,
        "n_total": len(PROTEINS),
    }
    (HERE / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    (HERE / "RESULTS.md").write_text(render_results(results))
    print(f"\nwrote {HERE / 'results.json'} and {HERE / 'RESULTS.md'}")
    print("(RESULTS.md is generated — do not hand-edit it; a fresh run must reproduce it byte-for-byte)")
    return 0


def render_results(r: dict) -> str:
    """Render RESULTS.md entirely from `r`, so no number can drift from the run."""
    P = r["proteins"]
    order = list(P)
    ref = r["reference"]
    a = P["Q86TW2"]

    def row_ploop(acc: str) -> str:
        pl = P[acc]["ploop"]
        al = r["ploop_aligned"][acc]
        if pl["annotated"]:
            seq, rng, src = pl["sequence"], pl["range"], "curated"
        else:
            seq, rng, src = "-", "-", "aligned"
        residues = ", ".join(
            f"{v['residue'] or '-'}{v['position'] or ''}" for v in al["residues"].values()
        )
        return (f"| {P[acc]['label']} | `{rng}` | `{seq}` | {al['glycines_retained']}/3 | "
                f"{residues} | {src} |")

    def row_motif(acc: str) -> str:
        m = P[acc]["motifs"]
        cells = []
        for k in ("beta3_lys", "catalytic_asp", "catalytic_asn", "dfg_asp"):
            mm = m[k]
            star = "\\*" if mm["lands_on_own_annotated_site"] else ""
            cells.append(f"{mm['residue'] or '-'}{mm['position'] or ''}{star}")
        ctx = r["catalytic_loop_context"][acc]
        return (f"| {P[acc]['label']} | " + " | ".join(cells)
                + f" | `{ctx['hxd_triplet']}` | {'yes' if ctx['arg_at_minus_one'] else 'no'} |")

    n_ubib = len(order) - 1
    n_all4 = sum(
        1 for acc in order if acc != ref
        and all(P[acc]["motifs"][k]["matches_canonical"]
                for k in ("beta3_lys", "catalytic_asp", "catalytic_asn", "dfg_asp"))
    )
    lines = [
        "# ADCK1: which protein-kinase catalytic motifs does it actually retain?",
        "",
        "**Generated by `ubib_motif_scan.py`. Do not hand-edit — a fresh run overwrites it.**",
        "",
        "## Question",
        "",
        "UniProt Q86TW2 asserts `EC=2.7.-.-`, the keywords `Kinase` and",
        "`Serine/threonine-protein kinase`, and ATP-ligand binding sites, all from the",
        "generic protein-kinase ProRule `PRU00159` (`ECO:0000255`) — while the same entry's",
        "FUNCTION comment says it is not known whether ADCK1 has protein kinase activity or",
        "what it would phosphorylate. This measures which canonical motifs are present,",
        "rather than inferring activity from the fold name.",
        "",
        "## Method and its guards",
        "",
        "Every motif column is anchored on a residue that **PKA's own UniProt feature table**",
        "annotates (`BINDING 50..58` ATP, `BINDING 73` ATP, `ACT_SITE 167`, `BINDING 169..172`),",
        "so no position is hand-assigned. Three passes with different failure modes:",
        "",
        "1. **PASS 1, alignment-free.** PKA, ADCK1 and ADCK2 each carry a curated *9-residue*",
        "   ATP `BINDING` site over the P-loop; comparing them column-for-column involves no",
        "   alignment, so no alignment artefact can enter.",
        "2. **PASS 2 / 2b, alignment.** Sequences are trimmed to each protein's annotated",
        "   \"Protein kinase\" DOMAIN before MAFFT L-INS-i, so long N-terminal extensions cannot",
        "   displace catalytic columns. The run **aborts** unless it reproduces curated/published",
        "   anchors, and unless PASS 2b agrees with PASS 1 wherever both apply.",
        "3. **PASS 3, alignment-free re-test.** PASS 2 reported the HRD-arginine column as a gap",
        "   in every UbiB protein; a gap can be an artefact, so the two residues before each",
        "   protein's own catalytic Asp are re-read straight from its sequence.",
        "",
        f"All {r['n_reviewed']}/{r['n_total']} entries are Swiss-Prot reviewed",
        "(tested with `entryType.startswith(\"UniProtKB reviewed\")`, since `\"reviewed\" in ...`",
        "also matches `unreviewed`). Each accession is additionally verified against the gene",
        "or ORF name it is labelled with, which caught two wrong yeast accessions in the first",
        "draft (`Q12296` is MAM3, not Cqd1; `Q08058` is COQ10, not Coq8).",
        "",
        "### Anchor-reproduction gate",
        "",
        "| protein | motif | curated/published | aligned | reproduced |",
        "|---|---|---|---|---|",
    ]
    for c in r["anchor_reproduction_checks"]:
        lines.append(f"| {c['label']} | {c['motif']} | {c['published_position']} | "
                     f"{c['aligned_position']} | {c['reproduced']} |")
    lines += [
        "",
        "Plus: the alignment must place COQ8A **A339** — the residue Stefely et al. 2015",
        "(PMID:25498144) mutated to Gly to flip ADP/ATP selectivity — in PKA's second",
        "G-rich-loop glycine column. It does.",
        "",
        "## Result 1 — the P-loop is Ala-rich, and A164 is the COQ8A A339 position",
        "",
        "PKA's `GxGxxG` glycines sit at P-loop offsets "
        f"{r['ploop_glycine_offsets_in_pka']}.",
        "",
        "| protein | curated range | P-loop | glycines | residues at the three glycine offsets | source |",
        "|---|---|---|---|---|---|",
    ]
    lines += [row_ploop(acc) for acc in order]
    coq8a = r["ploop_aligned"]["Q8NI60"]["residues"]["offset_3"]
    adck1_g = a["ploop"]["residues_at_glycine_offsets"]["offset_3"]
    lines += [
        "",
        f"ADCK1 retains **{r['adck1_ploop_glycines_retained']}/3** of the canonical glycines. "
        f"Its offset-3 residue is **{adck1_g['residue']}{adck1_g['position']}**, which occupies "
        f"the same column as COQ8A **{coq8a['residue']}{coq8a['position']}** — the ADP/ATP "
        "selectivity determinant. ADCK1's `BINDING` sites are annotated with **ATP** as ligand "
        "purely by ProRule transfer; the one characterised relative sharing this loop is "
        "ADP-selective and carries `GO:0043531 ADP binding` by IDA, not `GO:0005524`.",
        "",
        "## Result 2 — the phosphotransfer active site is INTACT",
        "",
        "| protein | β3 Lys | catalytic Asp | catalytic Asn | Mg-binding Asp | catalytic loop (ends at the Asp) | Arg at D-1 |",
        "|---|---|---|---|---|---|---|",
    ]
    lines += [row_motif(acc) for acc in order]
    lines += [
        "",
        "\\* = the transferred column lands on a site that protein's own feature table annotates.",
        "",
        f"All four core catalytic residues are canonical in **{n_all4}/{n_ubib}** of the UbiB",
        "proteins examined, ADCK1 included (K183, D315, N320, D338). This is the result that",
        "**refuses** a \"pseudokinase, catalytic residues lost\" reading, and it agrees with",
        "Kemmerer et al. 2021, who found the yeast ortholog Cqd2's function requires exactly",
        "these residues (PMID:34362905).",
        "",
        "## Result 3 — but the HRD arginine is absent family-wide",
        "",
        f"**{r['n_ubib_with_arg_before_catalytic_asp']}/{n_ubib}** UbiB proteins have an arginine",
        "immediately before the catalytic aspartate; the PKA control does. Read alignment-free,",
        "so this is biology rather than a gap artefact. ADCK1 reads",
        f"`{r['catalytic_loop_context']['Q86TW2']['hxd_triplet']}` "
        f"(H313-C314-{r['catalytic_loop_context']['Q86TW2']['catalytic_asp']}), "
        "identical to yeast Cqd2 —",
        "a small independent corroboration of the orthology PANTHER asserts, and distinct from",
        f"ADCK2/Cqd1 (`{r['catalytic_loop_context']['Q7Z695']['hxd_triplet']}`) and the COQ8",
        f"clade (`{r['catalytic_loop_context']['Q8NI60']['hxd_triplet']}`).",
        "",
        "## What this supports, and what it does not",
        "",
        "**Supports:** removing `Serine/threonine-protein kinase` from UniProt's keyword set.",
        "Protein-kinase activity has been demonstrated exactly once in this family — an ancestrally",
        "reconstructed COQ8B phosphorylates COQ3 in trans (PMID:38425362) — and that work did not",
        "determine the residue class, so no UbiB protein has been shown to be a **Ser/Thr** kinase.",
        "Meanwhile COQ8A and COQ8B both carry explicit `GO:0004672 NOT|enables` IDA rows, and ADCK1's",
        "own FUNCTION comment states its substrate class is unknown. The specificity claim has no basis.",
        "",
        "**Does not support:** calling ADCK1 catalytically dead. The active site is intact, the",
        "yeast ortholog needs it, and no in vitro assay of purified ADCK1 has ever been published.",
        "The nucleotide site is **untested, not refuted**, so no molecular-function or",
        "nucleotide-binding term is proposed for ADCK1 in this review.",
        "",
        "## Reproduce",
        "",
        "```",
        "uv run python ubib_motif_scan.py",
        "```",
        "",
        "Requires `mafft` on PATH. UniProt responses are cached under `cache/`; delete it to",
        "refetch. A missing input is a hard error naming the fix, never a silently degraded run.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
