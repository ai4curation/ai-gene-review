"""Compare zebrafish smad3a (Q8AY15) and smad3b (Q8AY16) with human SMAD3 and gar SMAD3.

Reproducible; nothing is hardcoded except accessions and database queries.

1. Reads the two zebrafish sequences from the cached UniProt records.
2. Fetches human SMAD3 (P84022) sequence and its annotated features from UniProt REST.
3. Fetches all spotted gar (Lepisosteus oculatus, taxon 7918) SMAD-family proteins from
   UniProt and picks the one most identical to human SMAD3 as the gar SMAD3 (the gar
   entries carry no gene names, so this choice is made by identity and reported).
4. Reports global identity for every pair, identity per region (MH1, linker, MH2 as
   annotated on P84022), and the residue at each annotated functional position of
   human SMAD3 (Zn-binding sites, Sites, Modified residues) in each fish protein.
5. Expression: queries the Bgee REST API (anatomical-entity expression calls) for both
   zebrafish genes and reports shared vs gene-specific expressed entities, and the
   ZFIN wild-type expression download rows for both genes.

Run: uv run python genes/DANRE/smad3a/smad3a-bioinformatics/compare_smad3.py > \
     genes/DANRE/smad3a/smad3a-bioinformatics/output.txt
"""
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
GENES = {
    "smad3a": ("Q8AY15", "ZDB-GENE-000509-3"),
    "smad3b": ("Q8AY16", "ZDB-GENE-030128-4"),
}
HUMAN = "P84022"
GAR_TAXON = 7918


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/1.0 (curl-compatible)"})
    for attempt in range(4):  # retry transient 5xx errors from public APIs
        try:
            return urllib.request.urlopen(req, timeout=180).read().decode()
        except urllib.error.HTTPError as exc:
            if exc.code < 500 or attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def parse_fasta(data: str) -> dict[str, str]:
    out, name = {}, None
    for line in data.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            out[name] = ""
        elif name:
            out[name] += line.strip()
    return out


def aligner():
    a = Align.PairwiseAligner(mode="global")
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


AL = aligner()


def align(s0, s1):
    return AL.align(s0, s1)[0]


def ident(aln):
    s0, s1 = aln[0], aln[1]
    same = sum(1 for x, y in zip(s0, s1) if x == y and x != "-")
    return 100.0 * same / len(s0), len(s0)


def pos_map(aln):
    """Map 1-based positions of seq0 to the aligned residue of seq1 ('-' for gap)."""
    m, i = {}, 0
    for c0, c1 in zip(aln[0], aln[1]):
        if c0 != "-":
            i += 1
            m[i] = c1
    return m


def region_identity(aln, start, end):
    """Identity over the columns where seq0 positions start..end are aligned."""
    i, same, cols = 0, 0, 0
    for c0, c1 in zip(aln[0], aln[1]):
        if c0 != "-":
            i += 1
            inside = start <= i <= end
        else:  # insertion in seq1: count it if it falls inside the span
            inside = start <= i < end
        if inside:
            cols += 1
            same += c0 == c1 and c0 != "-"
    return 100.0 * same / cols if cols else float("nan"), cols


def main():
    seqs = {g: uniprot_txt_seq(ROOT / f"genes/DANRE/{g}/{g}-uniprot.txt") for g in GENES}
    hjson = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{HUMAN}.json"))
    hseq = hjson["sequence"]["value"]
    seqs["human_SMAD3"] = hseq

    gar = parse_fasta(get(
        "https://rest.uniprot.org/uniprotkb/stream?format=fasta&query="
        f"organism_id:{GAR_TAXON}%20AND%20protein_name:decapentaplegic"))
    gar_scores = sorted(((ident(align(hseq, s))[0], k, len(s)) for k, s in gar.items()),
                        reverse=True)
    print("## Gar SMAD-family entries ranked by identity to human SMAD3")
    for sc, k, ln in gar_scores:
        print(f"  {k}\t{ln} aa\t{sc:.1f}%")
    best = gar_scores[0][1]
    seqs[f"gar_{best.split('|')[1]}"] = gar[best]
    print(f"Gar SMAD3 taken as: {best}\n")

    print("## Lengths")
    for k, v in seqs.items():
        print(f"  {k}: {len(v)} aa")

    print("\n## Pairwise global identity (BLOSUM62, gap -10/-0.5)")
    names = list(seqs)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            p, c = ident(align(seqs[a], seqs[b]))
            print(f"  {a} vs {b}: {p:.1f}% over {c} columns")

    feats = hjson["features"]
    regions = [(f["description"] or f["type"], f["location"]["start"]["value"],
                f["location"]["end"]["value"])
               for f in feats if f["type"] in ("Domain",) or
               (f["type"] == "Region" and f["description"] == "Linker")]
    print("\n## Identity per human SMAD3 region (columns aligned to that human span)")
    for g in list(GENES) + [k for k in seqs if k.startswith("gar_")]:
        aln = align(hseq, seqs[g])
        for name, s, e in regions:
            p, c = region_identity(aln, s, e)
            print(f"  {g}\t{name} {s}-{e}\t{p:.1f}% ({c} cols)")
    # paralog vs paralog per region, using smad3a numbering mapped through human
    print("\n## smad3a vs smad3b per region (human SMAD3 coordinates projected)")
    a_h = pos_map(align(hseq, seqs["smad3a"]))
    b_h = pos_map(align(hseq, seqs["smad3b"]))
    for name, s, e in regions:
        pairs = [(a_h[i], b_h[i]) for i in range(s, e + 1)]
        same = sum(1 for x, y in pairs if x == y and x != "-")
        print(f"  {name} {s}-{e}: {same}/{len(pairs)} human positions identical in both "
              f"({100*same/len(pairs):.1f}%)")
    diffs = [(i, hseq[i - 1], a_h[i], b_h[i]) for i in range(1, len(hseq) + 1)
             if a_h[i] != b_h[i]]
    print(f"\n## Human SMAD3 positions where smad3a and smad3b differ ({len(diffs)})")
    print("  " + ", ".join(f"{i}:{h}->{a}/{b}" for i, h, a, b in diffs))

    print("\n## Annotated functional positions of human SMAD3 (P84022 features)")
    garkey = [k for k in seqs if k.startswith("gar_")][0]
    maps = {g: pos_map(align(hseq, seqs[g])) for g in ["smad3a", "smad3b", garkey]}
    print("  pos\thuman\tsmad3a\tsmad3b\tgar\tfeature")
    for f in feats:
        if f["type"] not in ("Binding site", "Site", "Modified residue"):
            continue
        p = f["location"]["start"]["value"]
        if p != f["location"]["end"]["value"]:
            continue
        desc = f.get("description") or (f.get("ligand") or {}).get("name", "")
        print(f"  {p}\t{hseq[p-1]}\t{maps['smad3a'][p]}\t{maps['smad3b'][p]}\t"
              f"{maps[garkey][p]}\t{f['type']}: {desc}")
    print("  C-terminal 6 residues: human", hseq[-6:], "smad3a", seqs["smad3a"][-6:],
          "smad3b", seqs["smad3b"][-6:], "gar", seqs[garkey][-6:])

    # ---------------- expression -----------------
    print("\n## Bgee anatomical-entity expression calls (EXPRESSED, all data types)")
    ens = {}
    for g in GENES:
        x = json.loads(get(f"https://rest.ensembl.org/xrefs/symbol/danio_rerio/{g}"
                           "?content-type=application/json"))
        ens[g] = [r["id"] for r in x if r["type"] == "gene"]
        for gid in ens[g]:
            info = json.loads(get(f"https://rest.ensembl.org/lookup/id/{gid}"
                                  "?content-type=application/json"))
            print(f"  Ensembl {g} {gid}: seq_region {info.get('seq_region_name')}")
    calls = {}
    for g, ids in ens.items():
        calls[g] = {}
        for gid in ids:
            try:
                d = json.loads(get(
                    "https://www.bgee.org/api/?page=gene&action=expression&gene_id="
                    f"{gid}&species_id=7955&cond_param=anat_entity&data_type=all"
                    "&display_type=json"))
            except Exception as exc:  # gene not in Bgee
                print(f"  {g} {gid}: no Bgee data ({exc})")
                continue
            for c in d["data"]["calls"]:
                ae = c["condition"]["anatEntity"]
                score = float(c["expressionScore"]["expressionScore"])
                # a gene with two Ensembl ids: keep the higher score per entity
                calls[g][ae["name"]] = max(score, calls[g].get(ae["name"], score))
            print(f"  {g} {gid}: {len(d['data']['calls'])} expressed entities")
    a, b = set(calls["smad3a"]), set(calls["smad3b"])
    print(f"  shared: {len(a & b)}; smad3a only: {len(a - b)}; smad3b only: {len(b - a)}")
    print(f"  smad3a only: {sorted(a - b)}")
    print(f"  smad3b only: {sorted(b - a)}")
    print("  Top 15 entities by Bgee expression score:")
    for g in GENES:
        top = sorted(calls[g].items(), key=lambda kv: -kv[1])[:15]
        print(f"   {g}: " + "; ".join(f"{k} {v:.1f}" for k, v in top))
    shared = sorted(a & b, key=lambda k: -(calls['smad3a'][k] - calls['smad3b'][k]))
    print("  Largest score differences in shared entities (smad3a - smad3b):")
    for k in shared[:8] + shared[-8:]:
        print(f"   {k}: {calls['smad3a'][k]:.1f} vs {calls['smad3b'][k]:.1f}")

    print("\n## ZFIN wild-type expression download (curated rows)")
    zf = get("https://zfin.org/downloads/wildtype-expression_fish.txt").splitlines()
    for g, (_, zdb) in GENES.items():
        rows = [r.split("\t") for r in zf if r.startswith(zdb + "\t")]
        print(f"  {g} ({zdb}): {len(rows)} rows")
        for r in rows:
            print(f"   {r[4]} | {r[7]} | {r[9]} | {r[11]}")


if __name__ == "__main__":
    main()
