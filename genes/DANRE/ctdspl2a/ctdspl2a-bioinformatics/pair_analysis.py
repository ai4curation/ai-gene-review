"""Paralog-pair analysis for zebrafish ctdspl2a / ctdspl2b (human CTDSPL2, SCP4).

Reproducible: reads the cached UniProt records for the two zebrafish proteins and
queries public services at run time (nothing is hardcoded apart from gene symbols,
Ensembl gene ids of the two zebrafish genes, and the human gene names to query):
  * UniProt REST  - reviewed human CTDSPL2 / CTDSP1 / CTDSP2 / CTDSPL sequences and CTDSPL2 features;
  * Ensembl REST  - Compara homologies (level of the zebrafish duplication, gar and medaka
                    orthologues), ortholog canonical proteins, gene coordinates, and
                    zebrafish within-species paralogues of neighbouring genes (synteny);
  * EBI Expression Atlas FTP - E-ERAD-475 (whole-embryo developmental time course) TPMs;
  * Bgee REST API - expressed calls per anatomical entity (zebrafish copies and gar);
  * ZFIN download - wildtype-expression_fish.txt (curated wild-type expression).

Run from the repo root:
    uv run python genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/pair_analysis.py \
        > genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/output.txt
"""

import csv
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
UA = {"User-Agent": "ai-gene-review-pair-analysis/1.0"}
ENSEMBL = "https://rest.ensembl.org"

CONFIG = {
    "genes": {
        "ctdspl2a": {"ens": "ENSDARG00000061587", "uniprot_txt": "genes/DANRE/ctdspl2a/ctdspl2a-uniprot.txt"},
        "ctdspl2b": {"ens": "ENSDARG00000060586", "uniprot_txt": "genes/DANRE/ctdspl2b/ctdspl2b-uniprot.txt"},
    },
    "human_genes": ["CTDSPL2", "CTDSP1", "CTDSP2", "CTDSPL"],
    "human_ref": "CTDSPL2",
    "feature_types": ("Domain", "Motif", "Region"),
    # HAD-family catalytic motif DxDx(T/V); in human SCP4/CTDSPL2 the two aspartates are D293 and D295
    # (PMID:35021089, D293A/D295A mutants), and D295N is phosphatase-dead (PMID:42315649).
    "motifs": {"DxDx(T/V)": r"D.D.[TV]"},
    "reference_sites": [293, 294, 295, 296, 297],
    "synteny_window_bp": 1_500_000,
    "gar_species": "lepisosteus_oculatus",
    "gar_taxon": 7918,
    "medaka_species": "oryzias_latipes",
}


def get(url: str, retries: int = 8) -> bytes:
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Content-Type": "application/json", **UA})
            return urllib.request.urlopen(req, timeout=180).read()
        except Exception:  # noqa: BLE001
            if i == retries - 1:
                raise
            time.sleep(3 + 4 * i)
    raise RuntimeError(url)


def ens_json(path: str):
    time.sleep(0.1)
    return json.loads(get(ENSEMBL + path + ("&" if "?" in path else "?") + "content-type=application/json"))


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def uniprot_human(gene: str) -> tuple[str, str]:
    q = urllib.parse.quote(f"gene_exact:{gene} AND organism_id:9606 AND reviewed:true")
    d = json.loads(get(f"https://rest.uniprot.org/uniprotkb/search?query={q}&format=json"))
    e = d["results"][0]
    return e["primaryAccession"], e["sequence"]["value"]


def ensembl_canonical_protein(gene_id: str) -> str:
    d = ens_json(f"/lookup/id/{gene_id}?expand=1")
    tr = [t for t in d["Transcript"] if t.get("is_canonical") and t.get("Translation")]
    tr = tr or [t for t in d["Transcript"] if t.get("Translation")]
    return ens_json(f"/sequence/id/{tr[0]['Translation']['id']}?type=protein")["seq"]


AL = Align.PairwiseAligner(mode="global")
AL.substitution_matrix = substitution_matrices.load("BLOSUM62")
AL.open_gap_score = -10
AL.extend_gap_score = -0.5


def aln(a: str, b: str):
    return AL.align(a, b)[0]


def identity(a: str, b: str) -> tuple[float, int]:
    x = aln(a, b)
    same = sum(1 for p, q in zip(x[0], x[1]) if p == q and p != "-")
    return 100.0 * same / len(x[0]), len(x[0])


def pos_map(a: str, b: str) -> dict[int, str | None]:
    """Map 1-based positions of a to the aligned residue of b (None for gap)."""
    x = aln(a, b)
    m, i = {}, 0
    for p, q in zip(x[0], x[1]):
        if p != "-":
            i += 1
            m[i] = None if q == "-" else q
    return m


def section(t: str):
    print(f"\n## {t}\n", flush=True)


def homologies(cfg):
    section("0. Ensembl Compara homologies")
    out = {}
    for g, v in cfg["genes"].items():
        d = ens_json(f"/homology/id/danio_rerio/{v['ens']}?sequence=none;format=condensed")
        hs = d["data"][0]["homologies"]
        out[g] = hs
        for h in hs:
            if h["species"] in ("danio_rerio", cfg["gar_species"], cfg["medaka_species"], "homo_sapiens"):
                print(f"{g}: {h['species']} {h['id']} {h['type']} (node {h.get('taxonomy_level')})")
    return out


def proteins(cfg, homs):
    zf = {g: uniprot_txt_seq(ROOT / v["uniprot_txt"]) for g, v in cfg["genes"].items()}
    hs, accs = {}, {}
    for gene in cfg["human_genes"]:
        acc, seq = uniprot_human(gene)
        hs[gene], accs[gene] = seq, acc
    orth = {}
    for g, hl in homs.items():
        for h in hl:
            if h["species"] == cfg["gar_species"] and h["type"].startswith("ortholog"):
                orth.setdefault(f"gar_{h['id']}", ensembl_canonical_protein(h["id"]))
            if h["species"] == cfg["medaka_species"] and h["type"].startswith("ortholog"):
                orth.setdefault(f"medaka_{h['id']}(orth of {g})", ensembl_canonical_protein(h["id"]))
    section("1. Sequence lengths and pairwise identities")
    for k, a in accs.items():
        print(f"human {k}: UniProt {a}")
    allseq = {**zf, **hs, **orth}
    for k, v in allseq.items():
        print(f"length {k}: {len(v)} aa")
    names = list(allseq)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            pid, cols = identity(allseq[a], allseq[b])
            print(f"identity {a} vs {b}: {pid:.1f}% over {cols} columns")
    return zf, hs, accs, orth


def regions(cfg, zf, hs, accs, orth):
    section("2. Regions of the human reference (UniProt features), motifs and key residues")
    ref = hs[cfg["human_ref"]]
    feats = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{accs[cfg['human_ref']]}.json"))["features"]
    regs = [(f["type"] + (": " + f["description"] if f.get("description") else ""),
             f["location"]["start"]["value"], f["location"]["end"]["value"])
            for f in feats if f["type"] in cfg["feature_types"]]
    gar = {k: v for k, v in orth.items() if k.startswith("gar_")}
    others = {**zf, **gar}
    maps = {k: pos_map(ref, v) for k, v in others.items()}
    for label, s, e in regs:
        n = e - s + 1
        for k, m in maps.items():
            aligned = sum(1 for p in range(s, e + 1) if m.get(p))
            same = sum(1 for p in range(s, e + 1) if m.get(p) == ref[p - 1])
            print(f"{label} [{s}-{e}] {k}: aligned {aligned}/{n}, identical {same}/{n} ({100*same/n:.1f}%)")
    for name, rx in cfg["motifs"].items():
        for k, s in {**others, cfg["human_ref"]: ref}.items():
            hits = [(m.start() + 1, m.group(0)) for m in re.finditer(rx, s)]
            print(f"motif {name} /{rx}/ in {k}: {hits or 'absent'}")
    for site in cfg["reference_sites"]:
        row = "; ".join(f"{k}: {m.get(site)}" for k, m in maps.items())
        print(f"human {cfg['human_ref']} residue {ref[site-1]}{site} aligned to -> {row}")


def relative_rate(zf, orth):
    section("3. Tajima-style relative-rate test (outgroup = gar)")
    gars = [v for k, v in orth.items() if k.startswith("gar_")]
    if not gars:
        print("no gar orthologue")
        return
    gar = gars[0]
    (na, a), (nb, b) = list(zf.items())
    ma, mb = pos_map(gar, a), pos_map(gar, b)
    m1 = m2 = shared = 0
    for p in range(1, len(gar) + 1):
        ra, rb, rg = ma.get(p), mb.get(p), gar[p - 1]
        if ra is None or rb is None:
            continue
        shared += 1
        if ra != rg and rb == rg:
            m1 += 1
        elif rb != rg and ra == rg:
            m2 += 1
    chi = (m1 - m2) ** 2 / (m1 + m2) if (m1 + m2) else 0.0
    print(f"gar positions aligned in both copies: {shared}")
    print(f"changes unique to {na} (m1): {m1}; unique to {nb} (m2): {m2}; chi2 (1 df) = {chi:.2f}"
          f" ({'P<0.05' if chi > 3.841 else 'not significant at 0.05'})")


def expression_timecourse(cfg):
    section("4. Whole-embryo time course, E-ERAD-475 (TPM, median of replicates)")
    base = "https://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/E-ERAD-475/"
    conf = get(base + "E-ERAD-475-configuration.xml").decode()
    labels = dict(re.findall(r'<assay_group id="([^"]+)" label="([^"]+)"', conf))
    order = re.findall(r'<assay_group id="([^"]+)"', conf)
    want = {v["ens"]: g for g, v in cfg["genes"].items()}
    rows = {}
    req = urllib.request.Request(base + "E-ERAD-475-tpms.tsv", headers=UA)
    with urllib.request.urlopen(req, timeout=600) as fh:
        header = fh.readline().decode().rstrip("\n").split("\t")
        for line in fh:
            f = line.decode().rstrip("\n").split("\t")
            if f[0] in want:
                rows[want[f[0]]] = dict(zip(header, f))
    genes = list(cfg["genes"])
    print("| stage | " + " | ".join(genes) + " |")
    print("|---|" + "---|" * len(genes))
    for gid in order:
        vals = []
        for g in genes:
            q = rows.get(g, {}).get(gid, "")
            parts = q.split(",") if q else []
            vals.append(parts[len(parts) // 2] if parts else "NA")
        print(f"| {labels[gid]} | " + " | ".join(vals) + " |")


def bgee_calls(gene_id: str, species: int):
    url = (f"https://www.bgee.org/api/?page=gene&action=expression&gene_id={gene_id}"
           f"&species_id={species}&cond_param=anat_entity&display_type=json")
    d = json.loads(get(url))
    return [(c["condition"]["anatEntity"]["name"], float(c["expressionScore"]["expressionScore"]),
             c["expressionQuality"], ",".join(c["dataTypesWithData"])) for c in d["data"]["calls"]]


def bgee(cfg, homs):
    section("5. Bgee expressed calls per anatomical entity (score 0-100; only 'expressed' calls are returned)")
    tables = {g: bgee_calls(v["ens"], 7955) for g, v in cfg["genes"].items()}
    gar_ids = sorted({h["id"] for hl in homs.values() for h in hl
                      if h["species"] == cfg["gar_species"] and h["type"].startswith("ortholog")})
    for gid in gar_ids:
        try:
            tables[f"gar {gid}"] = bgee_calls(gid, cfg["gar_taxon"])
        except Exception as e:  # noqa: BLE001
            print(f"gar {gid}: Bgee query failed ({e})")
    for k, calls in tables.items():
        print(f"### {k}: {len(calls)} calls")
        for name, score, qual, dt in calls:
            print(f"- {name}: {score:.1f} ({qual}; {dt})")
    zf = list(cfg["genes"])
    a = {n for n, _, _, dt in tables[zf[0]] if "RNA-Seq" in dt}
    b = {n for n, _, _, dt in tables[zf[1]] if "RNA-Seq" in dt}
    print(f"\nRNA-Seq-supported entities: {zf[0]} only: {sorted(a - b)}")
    print(f"RNA-Seq-supported entities: {zf[1]} only: {sorted(b - a)}")
    print(f"RNA-Seq-supported entities: both: {sorted(a & b)}")


def zfin(cfg):
    section("6. ZFIN curated wild-type expression (wildtype-expression_fish.txt)")
    text = get("https://zfin.org/downloads/wildtype-expression_fish.txt").decode("utf-8", errors="replace")
    recs = defaultdict(set)
    for row in csv.reader(io.StringIO(text), delimiter="\t"):
        if len(row) > 11 and row[1] in cfg["genes"]:
            anat = row[4] + (f" > {row[6]}" if row[6] else "")
            recs[row[1]].add((anat, row[7], row[9], row[11]))
    for g in cfg["genes"]:
        rs = sorted(recs.get(g, set()))
        print(f"### {g}: {len(rs)} records")
        for anat, stage, assay, pub in rs:
            print(f"- {anat} | {stage} | {assay} | {pub}")
    ga, gb = list(cfg["genes"])
    a = {r[0] for r in recs.get(ga, set())}
    b = {r[0] for r in recs.get(gb, set())}
    print(f"\nanatomy terms {ga} only: {sorted(a - b)}")
    print(f"anatomy terms {gb} only: {sorted(b - a)}")
    print(f"anatomy terms both: {sorted(a & b)}")


def genes_near(chrom: str, start: int, end: int):
    d = ens_json(f"/overlap/region/danio_rerio/{chrom}:{max(1, start)}-{end}?feature=gene;biotype=protein_coding")
    return [(x["id"], x.get("external_name"), x["start"]) for x in d]


def synteny(cfg, dup_level: str):
    section(f"7. Local synteny between the copies (neighbour paralogues with a {dup_level}-level node)")
    w = cfg["synteny_window_bp"]
    loc = {}
    for g, v in cfg["genes"].items():
        d = ens_json(f"/lookup/id/{v['ens']}?")
        loc[g] = (d["seq_region_name"], d["start"], d["end"])
        print(f"{g}: chr{d['seq_region_name']}:{d['start']}-{d['end']}")
    (ga, la), (gb, lb) = list(loc.items())
    for src, sloc, tgt, tloc in ((ga, la, gb, lb), (gb, lb, ga, la)):
        neigh = [n for n in genes_near(sloc[0], sloc[1] - w, sloc[2] + w) if n[0] != cfg["genes"][src]["ens"]]
        target_window = {gid: (name, start) for gid, name, start in genes_near(tloc[0], tloc[1] - w, tloc[2] + w)}
        chrom_len = ens_json(f"/info/assembly/danio_rerio/{tloc[0]}?")["length"]
        target_chrom = {}
        for cs in range(1, chrom_len + 1, 4_000_000):
            for gid, name, start in genes_near(tloc[0], cs, min(cs + 3_999_999, chrom_len)):
                target_chrom[gid] = (name, start)

        def teleost_paralogues(gid):
            try:
                h = ens_json(f"/homology/id/danio_rerio/{gid}?type=paralogues;sequence=none;format=condensed")
            except Exception:  # noqa: BLE001
                return None
            if not h.get("data"):
                return []
            return [x["id"] for x in h["data"][0]["homologies"]
                    if x.get("taxonomy_level") in ("Clupeocephala", "Osteoglossocephalai", "Teleostei")]

        with ThreadPoolExecutor(max_workers=3) as ex:
            results = list(ex.map(teleost_paralogues, [n[0] for n in neigh]))
        hits, chrom_hits, with_par, failed = [], [], 0, 0
        for (gid, name, _), pars in zip(neigh, results):
            if pars is None:
                failed += 1
                continue
            if pars:
                with_par += 1
            for pid in pars:
                if pid in target_window:
                    tname, tstart = target_window[pid]
                    hits.append(f"{name or gid} -> {tname or pid} (chr{tloc[0]}:{tstart})")
                if pid in target_chrom:
                    tname, tstart = target_chrom[pid]
                    chrom_hits.append(f"{name or gid} -> {tname or pid} (chr{tloc[0]}:{tstart})")
        print(f"\n{src} +/- {w/1e6:.1f} Mb: {len(neigh)} other protein-coding genes ({failed} homology queries "
              f"failed); {with_par} have a teleost-level (Teleostei/Osteoglossocephalai/Clupeocephala) zebrafish "
              f"paralogue; {len(hits)} such pairs have their partner within {w/1e6:.1f} Mb of {tgt}:")
        for h in hits:
            print(f"- {h}")
        print(f"{len(chrom_hits)} have their partner anywhere on chr{tloc[0]} ({len(target_chrom)} protein-coding genes):")
        for h in chrom_hits:
            print(f"- {h}")


def main():
    cfg = CONFIG
    print(f"# Pair analysis: {' / '.join(cfg['genes'])}  (run {time.strftime('%Y-%m-%d')})")
    homs = homologies(cfg)
    ga, gb = list(cfg["genes"])
    dup = [h.get("taxonomy_level") for h in homs[ga] if h["id"] == cfg["genes"][gb]["ens"]]
    print(f"\nCompara node of the {ga}/{gb} duplication: {dup}")
    zf, hs, accs, orth = proteins(cfg, homs)
    regions(cfg, zf, hs, accs, orth)
    relative_rate(zf, orth)
    expression_timecourse(cfg)
    bgee(cfg, homs)
    zfin(cfg)
    synteny(cfg, "teleost")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
