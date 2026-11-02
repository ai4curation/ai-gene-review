"""Compare zebrafish eef1da and eef1db protein isoforms with human EEF1D and gar EEF1D.

Reproducible; nothing is hardcoded except accessions, gene symbols and database queries.

Background for the design: human EEF1D (P29692) is made as a 281-aa isoform (the EF-1
complex subunit with the C-terminal GEF domain) and a 647-aa isoform (eEF1BdeltaL,
isoform 2) that carries a 366-aa N-terminal extension. The two zebrafish accessions under
review (A0A8M6Z1P2, 463 aa; A0A8M2B7W1, 578 aa) are long RefSeq-model isoforms, so the
whole-protein identity mixes the conserved core with the extensions.

1. Fetches every UniProt entry for zebrafish eef1da and eef1db (gene_exact query).
2. Fetches human P29692 isoforms and spotted gar (taxon 7918) EEF1D entries.
3. Aligns every protein to human isoform 2 (647 aa) and reports identity over
   (a) the N-terminal extension (isoform-2 positions 1..len(iso2)-len(iso1)) and
   (b) the shared core, and over the core sub-regions annotated on P29692
   (Leucine-zipper, Catalytic (GEF) region), shifted to isoform-2 numbering.
4. Reports paralog-vs-paralog identity for the shortest and the longest isoform of each gene.
5. Expression: Bgee anatomical-entity calls and ZFIN wild-type expression rows.

Run: uv run python genes/DANRE/eef1da/eef1da-bioinformatics/compare_eef1d.py > \
     genes/DANRE/eef1da/eef1da-bioinformatics/output.txt
"""
import json
import random
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

GENES = {"eef1da": "ZDB-GENE-040426-2740", "eef1db": "ZDB-GENE-030131-6544"}
REVIEWED = {"eef1da": "A0A8M6Z1P2", "eef1db": "A0A8M2B7W1"}
HUMAN = "P29692"
GAR_TAXON = 7918


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/1.0"})
    return urllib.request.urlopen(req, timeout=180).read().decode()


def parse_fasta(data: str) -> dict[str, str]:
    out, name = {}, None
    for line in data.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0].split("|")[1]
            out[name] = ""
        elif name:
            out[name] += line.strip()
    return out


AL = Align.PairwiseAligner(mode="global")
AL.substitution_matrix = substitution_matrices.load("BLOSUM62")
AL.open_gap_score = -10
AL.extend_gap_score = -0.5


def align(a, b):
    return AL.align(a, b)[0]


def ident(aln):
    same = sum(1 for x, y in zip(aln[0], aln[1]) if x == y and x != "-")
    return 100.0 * same / len(aln[0]), len(aln[0])


def span_stats(aln, start, end):
    """Over seq0 positions start..end: aligned (non-gap) residues and identities."""
    i, aligned, same = 0, 0, 0
    for c0, c1 in zip(aln[0], aln[1]):
        if c0 == "-":
            continue
        i += 1
        if start <= i <= end and c1 != "-":
            aligned += 1
            same += c0 == c1
    n = end - start + 1
    return aligned, same, n


def main():
    zf = {}
    for g in GENES:
        fa = parse_fasta(get(
            "https://rest.uniprot.org/uniprotkb/stream?format=fasta&query="
            f"gene_exact:{g}%20AND%20organism_id:7955"))
        for acc, s in fa.items():
            zf[f"{g}|{acc}"] = s
    hum = parse_fasta(get(
        "https://rest.uniprot.org/uniprotkb/stream?format=fasta&includeIsoform=true"
        f"&query=accession:{HUMAN}"))
    gar = parse_fasta(get(
        "https://rest.uniprot.org/uniprotkb/stream?format=fasta&query="
        f"gene_exact:EEF1D%20AND%20organism_id:{GAR_TAXON}"))
    hjson = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{HUMAN}.json"))
    iso1 = hum[HUMAN]
    iso2 = hum[f"{HUMAN}-2"]
    ext = len(iso2) - len(iso1)
    assert iso2[ext:] == iso1[1:] or iso2.endswith(iso1[1:]), "iso2 is not iso1 + extension"
    print(f"Human {HUMAN} isoform 1: {len(iso1)} aa; isoform 2 (eEF1BdeltaL): {len(iso2)} aa;"
          f" N-terminal extension = isoform-2 positions 1..{ext}")
    regions = [("N-terminal extension (iso2 only)", 1, ext),
               ("shared core", ext + 1, len(iso2))]
    for f in hjson["features"]:
        if f["type"] == "Region" and f["description"] in ("Leucine-zipper", "Catalytic (GEF)"):
            s, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
            # isoform 2 = extension + isoform 1 lacking its initiator Met
            regions.append((f"{f['description']} (iso1 {s}-{e})", s + ext - 1, e + ext - 1))

    prots = {**zf, **{f"gar|{k}": v for k, v in gar.items()},
             f"human|{HUMAN}-1": iso1}
    print("\n## Proteins")
    for k, v in prots.items():
        print(f"  {k}\t{len(v)} aa")

    print("\n## Coverage and identity against human isoform 2, by region")
    print("  protein\tregion\taligned/len\tidentical/aligned")
    for k, v in prots.items():
        aln = align(iso2, v)
        for name, s, e in regions:
            a, same, n = span_stats(aln, s, e)
            pid = 100 * same / a if a else 0
            print(f"  {k}\t{name}\t{a}/{n}\t{same}/{a} ({pid:.1f}%)")

    print("\n## Shuffle control for the N-terminal extension similarity")
    print("  (zebrafish/gar residues preceding the core are shuffled 20x, seed 1, and "
          "re-aligned to human isoform 2; identity over the extension is recorded)")
    rng = random.Random(1)
    core_start = ext + 1
    for k in [f"eef1da|{REVIEWED['eef1da']}", f"eef1db|{REVIEWED['eef1db']}"] + \
            [f"gar|{g}" for g in gar]:
        v = prots[k]
        aln = align(iso2, v)
        # number of residues of v aligned before human core position core_start
        i = j = 0
        for c0, c1 in zip(aln[0], aln[1]):
            if c0 != "-":
                i += 1
            if i >= core_start:
                break
            if c1 != "-":
                j += 1
        nterm, rest = v[:j], v[j:]
        a0, s0, _ = span_stats(aln, 1, ext)
        obs = 100 * s0 / a0 if a0 else 0
        vals = []
        for _ in range(20):
            sh = list(nterm)
            rng.shuffle(sh)
            a1, s1, _ = span_stats(align(iso2, "".join(sh) + rest), 1, ext)
            vals.append(100 * s1 / a1 if a1 else 0)
        print(f"  {k}: N-terminal segment {len(nterm)} aa; observed {obs:.1f}% over {a0} "
              f"aligned; shuffled mean {sum(vals)/len(vals):.1f}%, max {max(vals):.1f}%")

    print("\n## Paralog comparisons (global identity)")
    for label, pick in (("shortest", min), ("longest", max)):
        a = pick((kv for kv in zf.items() if kv[0].startswith("eef1da")),
                 key=lambda kv: len(kv[1]))
        b = pick((kv for kv in zf.items() if kv[0].startswith("eef1db")),
                 key=lambda kv: len(kv[1]))
        p, c = ident(align(a[1], b[1]))
        print(f"  {label}: {a[0]} ({len(a[1])} aa) vs {b[0]} ({len(b[1])} aa): "
              f"{p:.1f}% over {c} columns")
    ra = zf[f"eef1da|{REVIEWED['eef1da']}"]
    rb = zf[f"eef1db|{REVIEWED['eef1db']}"]
    p, c = ident(align(ra, rb))
    print(f"  reviewed accessions {REVIEWED['eef1da']} vs {REVIEWED['eef1db']}: "
          f"{p:.1f}% over {c} columns")
    # core-only paralog identity: C-terminal region matching human isoform 1
    ca = align(iso2, ra)
    cb = align(iso2, rb)

    def proj(aln):
        m, i = {}, 0
        for c0, c1 in zip(aln[0], aln[1]):
            if c0 != "-":
                i += 1
                m[i] = c1
        return m
    ma, mb = proj(ca), proj(cb)
    for name, s, e in regions:
        both = [(ma[i], mb[i]) for i in range(s, e + 1) if ma[i] != "-" and mb[i] != "-"]
        same = sum(1 for x, y in both if x == y)
        print(f"  reviewed pair, {name}: {same}/{len(both)} positions aligned in both are "
              f"identical ({100*same/len(both) if both else 0:.1f}%)")

    print("\n## Bgee anatomical-entity expression calls")
    calls = {}
    for g in GENES:
        x = json.loads(get(f"https://rest.ensembl.org/xrefs/symbol/danio_rerio/{g}"
                           "?content-type=application/json"))
        calls[g] = {}
        for gid in [r["id"] for r in x if r["type"] == "gene"]:
            try:
                d = json.loads(get(
                    "https://www.bgee.org/api/?page=gene&action=expression&gene_id="
                    f"{gid}&species_id=7955&cond_param=anat_entity&data_type=all"
                    "&display_type=json"))
            except Exception as exc:
                print(f"  {g} {gid}: no Bgee data ({exc})")
                continue
            for c in d["data"]["calls"]:
                n = c["condition"]["anatEntity"]["name"]
                sc = float(c["expressionScore"]["expressionScore"])
                calls[g][n] = max(sc, calls[g].get(n, sc))
            print(f"  {g} {gid}: {len(d['data']['calls'])} expressed entities")
    a, b = set(calls["eef1da"]), set(calls["eef1db"])
    print(f"  shared: {len(a & b)}; eef1da only: {len(a - b)}; eef1db only: {len(b - a)}")
    print(f"  eef1da only: {sorted(a - b)}")
    print(f"  eef1db only: {sorted(b - a)}")
    for g in GENES:
        top = sorted(calls[g].items(), key=lambda kv: -kv[1])[:15]
        print(f"  top {g}: " + "; ".join(f"{k} {v:.1f}" for k, v in top))
    shared = sorted(a & b, key=lambda k: -(calls['eef1da'][k] - calls['eef1db'][k]))
    diffs = [calls['eef1da'][k] - calls['eef1db'][k] for k in shared]
    if diffs:
        print(f"  shared entities: median score difference (eef1da - eef1db) = "
              f"{sorted(diffs)[len(diffs)//2]:.1f}; eef1da higher in "
              f"{sum(d > 0 for d in diffs)}/{len(diffs)}")
        for k in shared[:6] + shared[-6:]:
            print(f"   {k}: {calls['eef1da'][k]:.1f} vs {calls['eef1db'][k]:.1f}")

    print("\n## ZFIN wild-type expression download")
    zfin = get("https://zfin.org/downloads/wildtype-expression_fish.txt").splitlines()
    for g, zdb in GENES.items():
        rows = [r.split("\t") for r in zfin if r.startswith(zdb + "\t")]
        print(f"  {g} ({zdb}): {len(rows)} rows")
        for r in rows:
            print(f"   {r[4]} | {r[7]}-{r[8]} | {r[9]} | {r[11]}")


if __name__ == "__main__":
    main()
