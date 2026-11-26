"""Protein identity and conserved-synteny check for a zebrafish paralog pair.

Usage (from repo root):
    uv run python genes/DANRE/lhfpl5a/lhfpl5a-bioinformatics/pair_analysis.py lhfpl5a lhfpl5b LHFPL5

What it does (all data fetched live from the Ensembl REST API; nothing is hardcoded):
  1. Looks up both zebrafish genes (chromosome, coordinates).
  2. Reports the Ensembl Compara paralogy node that joins them, and their
     orthologues in spotted gar (Lepisosteus oculatus), medaka (Oryzias latipes)
     and human.
  3. Fetches canonical protein sequences for the two zebrafish copies, the gar
     orthologue and the human orthologue and computes global pairwise identity
     (Biopython PairwiseAligner, BLOSUM62, gap -10/-0.5). Identity of each copy to
     the gar sequence is a crude relative-rate check: the copy with lower identity
     to the unduplicated outgroup has diverged more since the duplication.
  4. Conserved synteny: for WINDOW protein-coding genes either side of each
     zebrafish copy, finds gar orthologues and records their gar chromosome and
     distance from the gar orthologue of the pair. Neighbours of BOTH copies that
     map near the single gar gene are the double-conserved-synteny signature of a
     whole-genome duplication; the same is reported for human.

Results can be inconclusive (e.g. unplaced gar scaffolds); the script only prints
what the API returns.
"""

import json
import sys
import time
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

SERVER = "https://rest.ensembl.org"
WINDOW = 15  # protein-coding genes on each side
NEAR_BP = 5_000_000  # "near" threshold in the outgroup genome
TARGETS = ["lepisosteus_oculatus", "homo_sapiens", "oryzias_latipes"]


def get(path: str):
    url = SERVER + path + ("&" if "?" in path else "?") + "content-type=application/json"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 - retry on any transient API error
            if attempt == 4:
                raise
            time.sleep(2 + attempt * 2)
    return None


def lookup_symbol(symbol: str, species: str = "danio_rerio"):
    return get(f"/lookup/symbol/{species}/{symbol}?expand=0")


def lookup_id(eid: str, expand: bool = False):
    return get(f"/lookup/id/{eid}?expand={1 if expand else 0}")


def orthologues(gene_id: str, species: str = "danio_rerio"):
    q = ";".join(f"target_species={t}" for t in TARGETS)
    d = get(f"/homology/id/{species}/{gene_id}?type=orthologues;{q};sequence=none")
    out = []
    for h in d["data"][0]["homologies"] if d and d.get("data") else []:
        out.append((h["target"]["species"], h["target"]["id"], h["type"], h["target"].get("perc_id"), h["source"].get("perc_id")))
    return out


def paralogy_node(a_id: str, b_id: str):
    d = get(f"/homology/id/danio_rerio/{a_id}?type=paralogues;target_species=danio_rerio;sequence=none")
    for h in d["data"][0]["homologies"]:
        if h["target"]["id"] == b_id:
            return h.get("taxonomy_level"), h["source"].get("perc_id"), h["target"].get("perc_id")
    return None, None, None


def canonical_protein(gene_id: str) -> str:
    g = lookup_id(gene_id, expand=True)
    canon = g.get("canonical_transcript", "").split(".")[0]
    tx = next((t for t in g.get("Transcript", []) if t["id"] == canon), None)
    if tx is None or not tx.get("Translation"):
        tx = max((t for t in g.get("Transcript", []) if t.get("Translation")), key=lambda t: t["Translation"]["length"])
    seq = get(f"/sequence/id/{tx['Translation']['id']}?type=protein")
    return seq["seq"]


def identity(a: str, b: str):
    aligner = Align.PairwiseAligner(mode="global")
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(a, b)[0]
    ident = sim = cols = 0
    m = aligner.substitution_matrix
    for x, y in zip(*aln):
        cols += 1
        if x == "-" or y == "-":
            continue
        if x == y:
            ident += 1
        if m[x][y] > 0:
            sim += 1
    return 100 * ident / cols, 100 * sim / cols, cols


def neighbours(g, n=WINDOW):
    """Protein-coding genes within a region around g, n on each side (by order)."""
    span = 2_000_000  # overlap endpoint limit is 5 Mb
    region = f"{g['seq_region_name']}:{max(1, g['start'] - span)}-{g['end'] + span}"
    genes = get(f"/overlap/region/danio_rerio/{region}?feature=gene;biotype=protein_coding")
    genes = sorted(genes, key=lambda x: x["start"])
    idx = next(i for i, x in enumerate(genes) if x["id"] == g["id"])
    return genes[max(0, idx - n): idx] + genes[idx + 1: idx + 1 + n]


def main():
    a_sym, b_sym, human_sym = sys.argv[1], sys.argv[2], sys.argv[3]
    a, b = lookup_symbol(a_sym), lookup_symbol(b_sym)
    print(f"# {a_sym} / {b_sym} pair analysis (Ensembl REST, {time.strftime('%Y-%m-%d')})\n")
    for s, g in ((a_sym, a), (b_sym, b)):
        print(f"- {s}: {g['id']} chr{g['seq_region_name']}:{g['start']}-{g['end']} ({g['strand']:+d})")
    if a["seq_region_name"] == b["seq_region_name"]:
        print(f"- Same chromosome; distance between copies: {abs(a['start'] - b['start']):,} bp")
    node, pa, pb = paralogy_node(a["id"], b["id"])
    print(f"- Ensembl Compara paralogy node: {node} (identity {pa}% / {pb}%)\n")

    print("## Orthologues (Ensembl Compara)\n")
    orth = {}
    for s, g in ((a_sym, a), (b_sym, b)):
        for sp, tid, typ, tpid, spid in orthologues(g["id"]):
            orth.setdefault(sp, set()).add(tid)
            print(f"- {s} -> {sp} {tid} {typ} (target %id {tpid}, source %id {spid})")
    print()

    gar_ids = sorted(orth.get("lepisosteus_oculatus", []))
    human_ids = sorted(orth.get("homo_sapiens", []))
    human = lookup_symbol(human_sym, "homo_sapiens")
    print("## Protein identity (canonical translations)\n")
    seqs = {a_sym: canonical_protein(a["id"]), b_sym: canonical_protein(b["id"]), f"human {human_sym}": canonical_protein(human["id"])}
    for gid in gar_ids:
        seqs[f"gar {gid}"] = canonical_protein(gid)
    names = list(seqs)
    print("| Pair | Len 1 | Len 2 | Identity | Similarity | Columns |")
    print("|---|---|---|---|---|---|")
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            idt, sim, cols = identity(seqs[names[i]], seqs[names[j]])
            print(f"| {names[i]} vs {names[j]} | {len(seqs[names[i]])} | {len(seqs[names[j]])} | {idt:.1f}% | {sim:.1f}% | {cols} |")
    print()

    print("## Conserved synteny\n")
    gar_anchor = [lookup_id(x) for x in gar_ids]
    human_anchor = lookup_id(human["id"])
    for x in gar_anchor:
        print(f"- gar orthologue {x['id']} on {x['seq_region_name']}:{x['start']}")
    print(f"- human {human_sym} on chr{human_anchor['seq_region_name']}:{human_anchor['start']}\n")
    summary = {}
    gar_chroms = {}
    for s, g in ((a_sym, a), (b_sym, b)):
        nb = neighbours(g)
        near_gar = near_human = with_gar = with_human = 0
        rows = []
        for n in nb:
            o = orthologues(n["id"])
            time.sleep(0.07)
            garhits, humhits = [], []
            for sp, tid, typ, *_ in o:
                if sp not in ("lepisosteus_oculatus", "homo_sapiens"):
                    continue
                loc = lookup_id(tid)
                if sp == "lepisosteus_oculatus":
                    garhits.append(loc)
                else:
                    humhits.append(loc)
            gnear = any(
                x["seq_region_name"] == ga["seq_region_name"] and abs(x["start"] - ga["start"]) <= NEAR_BP
                for x in garhits for ga in gar_anchor
            )
            hnear = any(
                x["seq_region_name"] == human_anchor["seq_region_name"] and abs(x["start"] - human_anchor["start"]) <= NEAR_BP
                for x in humhits
            )
            with_gar += bool(garhits)
            with_human += bool(humhits)
            near_gar += gnear
            near_human += hnear
            rows.append((n.get("external_name") or n["id"], n["start"],
                         ", ".join(sorted({f"{x['seq_region_name']}:{x['start']/1e6:.1f}Mb" for x in garhits})) or "-",
                         ", ".join(sorted({f"{x['seq_region_name']}:{x['start']/1e6:.1f}Mb" for x in humhits})) or "-",
                         "yes" if gnear else "", "yes" if hnear else ""))
            for x in garhits:
                gar_chroms.setdefault(s, {}).setdefault(x["seq_region_name"], 0)
                gar_chroms[s][x["seq_region_name"]] += 1
        summary[s] = (len(nb), with_gar, near_gar, with_human, near_human)
        print(f"### Neighbours of {s} (chr{g['seq_region_name']})\n")
        print(f"| Zebrafish gene | Start | Gar orthologue location | Human orthologue location | Near gar anchor (<= {NEAR_BP/1e6:.0f} Mb) | Near human {human_sym} (<= {NEAR_BP/1e6:.0f} Mb) |")
        print("|---|---|---|---|---|---|")
        for r in rows:
            print("| " + " | ".join(str(x) for x in r) + " |")
        print()
    print("## Summary\n")
    print("| Copy | Neighbours | with gar orthologue | near gar anchor | with human orthologue | near human anchor |")
    print("|---|---|---|---|---|---|")
    for s, v in summary.items():
        print(f"| {s} | " + " | ".join(str(x) for x in v) + " |")
    print()
    print("Gar chromosomes/scaffolds hit by neighbours (count of neighbour genes):\n")
    for s, d in gar_chroms.items():
        print(f"- {s}: " + ", ".join(f"{k} ({v})" for k, v in sorted(d.items(), key=lambda kv: -kv[1])))
    print()
    print("## Medaka co-orthologue locations\n")
    for mid in sorted(orth.get("oryzias_latipes", [])):
        m = lookup_id(mid)
        print(f"- {mid} ({m.get('display_name', '')}) on chr{m['seq_region_name']}:{m['start']}")


if __name__ == "__main__":
    main()
