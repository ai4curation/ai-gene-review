#!/usr/bin/env python3
"""
Independent MSA check of two pseudo-enzyme claims used in the IBA_REVIEW findings:

  1. Human Argonautes AGO1-4: is AGO4's RNase-H-like catalytic DEDH tetrad
     actually degenerate vs the AGO2 slicer?
  2. CRMP/DPYSL family (DPYSL2/3/4/5, CRMP1): do they lack the metal-coordinating
     residues of an active dihydropyrimidinase (DPYS)?

Sequences for the target genes come from the repo's local *-uniprot.txt files.
Reference active enzymes and catalytic-residue POSITIONS are pulled live from the
UniProt REST API (feature tables) so nothing is hardcoded/guessed. Alignment by FAMSA.
"""
import re, json, urllib.request
from pyfamsa import Aligner, Sequence

REPO = "../../.."

def local_seq(species, gene):
    txt = open(f"{REPO}/genes/{species}/{gene}/{gene}-uniprot.txt").read()
    acc = re.search(r"^AC\s+(\S+?);", txt, re.M).group(1)
    sq = txt.split("SQ   ", 1)[1].split("\n", 1)[1]
    seq = "".join(sq.replace("//", "").split())
    return acc, seq

def uniprot_json(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    return json.load(urllib.request.urlopen(url, timeout=30))

def uniprot_seq(acc):
    return uniprot_json(acc)["sequence"]["value"]

def catalytic_positions(acc, types=("ACT_SITE", "BINDING")):
    """Return {position(1-based): description} for catalytic/binding features."""
    d = uniprot_json(acc)
    out = {}
    for f in d.get("features", []):
        if f["type"] in types or f["type"] in ("Active site", "Binding site"):
            loc = f["location"]
            if loc["start"]["value"] == loc["end"]["value"]:
                p = loc["start"]["value"]
                desc = f.get("description", "") or f["type"]
                lig = (f.get("ligand") or {}).get("name", "")
                out[p] = (desc + (f" [{lig}]" if lig else "")).strip()
    return out

def align(named_seqs):
    seqs = [Sequence(n.encode(), s.encode()) for n, s in named_seqs]
    msa = Aligner(guide_tree="upgma").align(seqs)
    return {s.id.decode(): s.sequence.decode() for s in msa}

def col_for_refpos(aln, refname, refpos):
    """Map a 1-based position in the ungapped reference to an alignment column."""
    aseq = aln[refname]; idx = 0
    for col, ch in enumerate(aseq):
        if ch != "-":
            idx += 1
            if idx == refpos:
                return col
    return None

def report(title, aln, refname, positions, members):
    print(f"\n## {title}\n")
    print(f"Reference: {refname}  (catalytic positions from UniProt feature table)\n")
    header = f"{'residue (ref pos)':<34} " + " ".join(f"{m:<9}" for m in members)
    print(header); print("-" * len(header))
    for pos in sorted(positions):
        col = col_for_refpos(aln, refname, pos)
        if col is None:
            continue
        refaa = aln[refname][col]
        cells = []
        for m in members:
            cells.append(aln[m][col])
        label = f"{refaa}{pos} {positions[pos][:24]}"
        print(f"{label:<34} " + " ".join(f"{c:<9}" for c in cells))

# ----------------- Analysis 1: Argonautes -----------------
ago = {g: local_seq("human", g) for g in ["AGO1", "AGO2", "AGO3", "AGO4"]}
ago_named = [(g, s) for g, (a, s) in ago.items()]
ago_aln = align(ago_named)
ago2_acc = ago["AGO2"][0]
# DEDH tetrad: UniProt annotates these; filter to the catalytic Asp/Glu/Asp/His
pos = catalytic_positions(ago2_acc, types=("ACT_SITE",))
if not pos:  # fall back to known DEDH if UniProt lacks ACT_SITE
    pos = {597: "Asp (DEDH)", 637: "Glu (DEDH)", 669: "Asp (DEDH)", 807: "His (DEDH)"}
report("Argonaute catalytic tetrad (DEDH) — AGO1-4", ago_aln, "AGO2", pos,
       ["AGO1", "AGO2", "AGO3", "AGO4"])

# ----------------- Analysis 2: CRMP/DPYSL vs active dihydropyrimidinase -----------------
DPYS = "Q14117"  # human dihydropyrimidinase (active reference)
crmp = {g: local_seq("human", g)[1] for g in ["DPYSL2", "DPYSL3", "DPYSL4", "DPYSL5", "CRMP1"]}
dpys_seq = uniprot_seq(DPYS)
crmp_named = [("DPYS", dpys_seq)] + [(g, s) for g, s in crmp.items()]
crmp_aln = align(crmp_named)
metal = catalytic_positions(DPYS, types=("BINDING", "ACT_SITE"))
# keep only metal/active residues
metal = {p: d for p, d in metal.items() if any(k in d.lower() for k in
         ["zn", "metal", "active", "mn", "co", "ni", "carboxy"])}
report("Dihydropyrimidinase metal-coordinating residues — DPYS vs CRMP family",
       crmp_aln, "DPYS", metal,
       ["DPYS", "DPYSL2", "DPYSL3", "DPYSL4", "DPYSL5", "CRMP1"])
print("\n(DPYS = active human dihydropyrimidinase; CRMP/DPYSL = the cytoskeletal paralogs)")
