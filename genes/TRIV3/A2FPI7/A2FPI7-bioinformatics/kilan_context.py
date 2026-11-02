"""Family context for A2FPI7 (T. vaginalis KilA-N protein).

Queries the InterPro REST API (live) for:
  1. number of Pfam PF04383 (KilA-N) proteins in the T. vaginalis G3 proteome
  2. number of PANTHER PTHR48135 members in that proteome and overall
  3. superkingdom composition of PTHR48135
  4. length distribution of T. vaginalis KilA-N proteins
  5. A2FPI7's own Pfam / PANTHER match coordinates and scores
Then does global/local pairwise alignment (BLOSUM62) of A2FPI7 against the
KilA-N / APSES N-terminal region of S. cerevisiae Mbp1 (P39678, residues 1-124,
an experimentally characterised DNA-binding APSES domain) and phage P1 KilA
(P19653). Nothing is hardcoded; results are printed as JSON.
"""
import json
import statistics
import time
import urllib.error
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

IP = "https://www.ebi.ac.uk/interpro/api"
PROTEOME = "UP000001542"


def get(url, attempts=6):
    # InterPro answers 408 while a slow query is still being computed; its API
    # documentation says to wait and repeat the request.
    for i in range(attempts):
        try:
            return _get(url)
        except urllib.error.HTTPError as e:
            if e.code != 408 or i == attempts - 1:
                raise
            time.sleep(20)


def _get(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        if r.status == 204:  # InterPro returns 204 No Content for an empty intersection
            return None
        return json.load(r)


def count(url):
    d = get(url + "?page_size=1")
    return 0 if d is None else d["count"]


def seq(acc):
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60) as r:
        return "".join(r.read().decode().splitlines()[1:])


res = {}
res["tvag_pf04383_proteins"] = count(f"{IP}/protein/uniprot/entry/pfam/PF04383/proteome/uniprot/{PROTEOME}/")
res["tvag_pthr48135_proteins"] = count(f"{IP}/protein/uniprot/entry/panther/PTHR48135/proteome/uniprot/{PROTEOME}/")
res["pthr48135_total_proteins"] = count(f"{IP}/protein/uniprot/entry/panther/PTHR48135/")
comp = {}
for sk, taxid in [("Bacteria", 2), ("Eukaryota", 2759), ("Viruses", 10239), ("Archaea", 2157)]:
    comp[sk] = count(f"{IP}/protein/uniprot/entry/panther/PTHR48135/taxonomy/uniprot/{taxid}/")
res["pthr48135_by_superkingdom"] = comp

# Paging the InterPro protein list times out (persistent 408), so lengths come
# from the UniProt stream endpoint for the same proteome x Pfam intersection.
with urllib.request.urlopen(
    "https://rest.uniprot.org/uniprotkb/stream?format=tsv&fields=accession,length"
    f"&query=proteome:{PROTEOME}%20AND%20xref:pfam-PF04383", timeout=300) as r:
    rows = r.read().decode().splitlines()[1:]
lengths = [int(x.split("\t")[1]) for x in rows]
res["tvag_kilan_length_stats"] = {
    "n": len(lengths), "min": min(lengths), "median": statistics.median(lengths), "max": max(lengths),
    "n_le_150": sum(1 for x in lengths if x <= 150),
}

matches = {}
for db in ["pfam", "panther", "profile", "smart"]:
    d = get(f"{IP}/entry/{db}/protein/uniprot/A2FPI7/")
    for r in d["results"]:
        for p in r["proteins"]:
            for loc in p["entry_protein_locations"]:
                matches[r["metadata"]["accession"]] = {
                    "fragments": [(f["start"], f["end"]) for f in loc["fragments"]],
                    "score": loc.get("score"), "model": loc.get("model"),
                }
res["a2fpi7_matches"] = matches

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -11
aligner.extend_gap_score = -1
aligner.mode = "local"
q = seq("A2FPI7")
targets = {"MBP1_YEAST_1-124": seq("P39678")[:124], "KILA_BPP1": seq("P19653")}
aln_out = {}
for name, t in targets.items():
    a = aligner.align(q, t)[0]
    qa, ta = a[0], a[1]
    pairs = [(x, y) for x, y in zip(qa, ta) if x != "-" and y != "-"]
    idn = sum(1 for x, y in pairs if x == y)
    aln_out[name] = {
        "local_score": a.score,
        "aligned_pairs": len(pairs),
        "identity_pct": round(100 * idn / len(pairs), 1) if pairs else 0,
        "query_span": (int(a.aligned[0][0][0]) + 1, int(a.aligned[0][-1][1])),
        "alignment": str(a),
    }
    # shuffled-sequence background for the score
    import random
    rnd = random.Random(1)
    bg = []
    for _ in range(200):
        s = list(t)
        rnd.shuffle(s)
        bg.append(aligner.score(q, "".join(s)))
    aln_out[name]["shuffled_mean"] = round(statistics.mean(bg), 1)
    aln_out[name]["shuffled_sd"] = round(statistics.pstdev(bg), 1)
    aln_out[name]["z"] = round((a.score - statistics.mean(bg)) / statistics.pstdev(bg), 2)
res["pairwise"] = aln_out
print(json.dumps(res, indent=2))
