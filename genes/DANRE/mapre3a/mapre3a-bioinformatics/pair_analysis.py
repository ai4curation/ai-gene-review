"""Paralog-pair analysis for zebrafish mapre3a / mapre3b (human MAPRE3, EB3).

Reproducible: reads the cached UniProt records for the two zebrafish proteins and
queries public services at run time (nothing is hardcoded):
  * UniProt REST  - human paralog sequences and features of the human reference
                    protein, plus the alternative zebrafish UniProt entries listed
                    in CONFIG["extra_zebrafish"] (other RefSeq isoforms);
  * Ensembl REST  - Compara homologies (paralogue level, gar / medaka orthologues),
                    canonical proteins of the gar and medaka orthologues, gene
                    coordinates and zebrafish paralogues of neighbouring genes;
  * EBI Expression Atlas FTP - E-ERAD-475 whole-embryo developmental time course
                    (TPM, median of replicates);
  * Bgee REST API - expressed calls per anatomical entity (zebrafish + gar);
  * ZFIN download - curated wild-type expression (wildtype-expression_fish.txt).

Sections: 0 Compara homologies; 1 identities; 2 per-region identity against the
human reference features and C-terminal tails; 3 Tajima-style relative-rate test
with the gar orthologue as outgroup; 4 E-ERAD-475; 5 Bgee; 6 ZFIN; 7 local synteny.

Run from the repo root:
    uv run python genes/DANRE/mapre3a/mapre3a-bioinformatics/pair_analysis.py \
        > genes/DANRE/mapre3a/mapre3a-bioinformatics/output.txt
"""

import csv
import io
import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
UA = {"User-Agent": "ai-gene-review-pair-analysis/1.0"}

CONFIG = {
    "genes": {
        "mapre3a": {"ens": "ENSDARG00000020231", "uniprot_txt": "genes/DANRE/mapre3a/mapre3a-uniprot.txt"},
        "mapre3b": {"ens": "ENSDARG00000102878", "uniprot_txt": "genes/DANRE/mapre3b/mapre3b-uniprot.txt"},
    },
    # other UniProt entries for the same genes (RefSeq NP isoforms)
    "extra_zebrafish": {"mapre3a_NP_Q4V903": "Q4V903", "mapre3b_NP_Q6GMJ3": "Q6GMJ3"},
    "human": {"MAPRE3": "Q9UPY8", "MAPRE1": "Q15691", "MAPRE2": "Q15555"},
    "human_ref": "MAPRE3",
    "feature_types": ("Domain", "Region", "Coiled coil", "Motif"),
    "tail_length": 12,
    "teleost_levels": ("Teleostei", "Osteoglossocephalai", "Clupeocephala"),
    "synteny_window_bp": 1_500_000,
}

ENSEMBL = "https://rest.ensembl.org"
ZFIN_URL = "https://zfin.org/downloads/wildtype-expression_fish.txt"
ATLAS = "https://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/E-ERAD-475/"


def get(url: str, retries: int = 8) -> bytes:
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Content-Type": "application/json", **UA})
            return urllib.request.urlopen(req, timeout=300).read()
        except Exception:  # noqa: BLE001
            if i == retries - 1:
                raise
            time.sleep(3 + 4 * i)
    raise RuntimeError(url)


def ens_json(path: str):
    time.sleep(0.08)
    return json.loads(get(ENSEMBL + path + ("&" if "?" in path else "?") + "content-type=application/json"))


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def uniprot_seq(acc: str) -> str:
    txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").decode()
    return "".join(txt.splitlines()[1:])


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
    x = aln(a, b)
    m, i = {}, 0
    for p, q in zip(x[0], x[1]):
        if p != "-":
            i += 1
            m[i] = None if q == "-" else q
    return m


def section(t: str):
    print(f"\n## {t}\n")


def homologies(cfg):
    section("0. Ensembl Compara homologies of the two zebrafish genes")
    orth = {}
    for g, v in cfg["genes"].items():
        h = ens_json(f"/homology/id/danio_rerio/{v['ens']}?sequence=none;format=condensed")["data"][0]["homologies"]
        for x in h:
            if x["species"] == "danio_rerio" and x["id"] in {w["ens"] for w in cfg["genes"].values()}:
                print(f"{g}: within-species paralogue {x['id']} ({x['type']}), duplication node {x['taxonomy_level']}")
            if x["species"] in ("lepisosteus_oculatus", "oryzias_latipes", "homo_sapiens"):
                print(f"{g}: {x['type']} {x['species']} {x['id']} (node {x['taxonomy_level']})")
                orth.setdefault((x["species"], x["id"]), set()).add(g)
    gar = sorted({i for (s, i) in orth if s == "lepisosteus_oculatus"})
    med = {g: [i for (s, i), gs in orth.items() if s == "oryzias_latipes" and g in gs] for g in cfg["genes"]}
    print(f"gar orthologue gene(s): {gar}")
    return gar, med


def proteins(cfg, gar_ids, med_ids):
    zf = {g: uniprot_txt_seq(ROOT / v["uniprot_txt"]) for g, v in cfg["genes"].items()}
    extra = {k: uniprot_seq(a) for k, a in cfg["extra_zebrafish"].items()}
    hs = {name: uniprot_seq(acc) for name, acc in cfg["human"].items()}
    orth = {f"gar_{gid}": ensembl_canonical_protein(gid) for gid in gar_ids}
    for g, ids in med_ids.items():
        for gid in ids:
            orth[f"medaka_{gid}_orth_of_{g}"] = ensembl_canonical_protein(gid)
    allseq = {**zf, **extra, **hs, **orth}
    section("1. Sequence lengths and pairwise identities (global, BLOSUM62, -10/-0.5)")
    for k, v in allseq.items():
        print(f"length {k}: {len(v)} aa")
    names = list(allseq)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            pid, cols = identity(allseq[a], allseq[b])
            print(f"identity {a} vs {b}: {pid:.1f}% over {cols} columns")
    return zf, extra, hs, orth


def regions(cfg, zf, extra, hs, orth):
    section("2. Regions of the human reference (UniProt features) and C-terminal tails")
    ref = hs[cfg["human_ref"]]
    acc = cfg["human"][cfg["human_ref"]]
    feats = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))["features"]
    regs = [(f["type"] + (": " + f["description"] if f.get("description") else ""),
             f["location"]["start"]["value"], f["location"]["end"]["value"])
            for f in feats if f["type"] in cfg["feature_types"]]
    gar = {k: v for k, v in orth.items() if k.startswith("gar_")}
    others = {**zf, **extra, **gar}
    maps = {k: pos_map(ref, v) for k, v in others.items()}
    for label, s, e in regs:
        n = e - s + 1
        for k, m in maps.items():
            aligned = sum(1 for p in range(s, e + 1) if m.get(p))
            same = sum(1 for p in range(s, e + 1) if m.get(p) == ref[p - 1])
            print(f"{label} [{s}-{e}] {k}: aligned {aligned}/{n}, identical {same}/{n} ({100*same/n:.1f}%)")
    t = cfg["tail_length"]
    for k, s in {cfg["human_ref"]: ref, **{h: v for h, v in hs.items() if h != cfg["human_ref"]}, **others,
                 **{k: v for k, v in orth.items() if k.startswith("medaka_")}}.items():
        print(f"C-terminal {t} aa of {k}: {s[-t:]}")
    # direct alignment of the two zebrafish copies: where do the differences lie?
    (na, a), (nb, b) = list(zf.items())
    x = aln(a, b)
    print(f"\nAlignment {na} (top) vs {nb} (bottom):")
    for i in range(0, len(x[0]), 70):
        print(x[0][i:i + 70])
        print("".join("|" if p == q and p != "-" else ("." if "-" not in (p, q) else " ")
                      for p, q in zip(x[0][i:i + 70], x[1][i:i + 70])))
        print(x[1][i:i + 70])
        print()


def relative_rate(zf, orth):
    section("3. Tajima-style relative-rate test (outgroup = gar orthologue)")
    for gk, gar in ((k, v) for k, v in orth.items() if k.startswith("gar_")):
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
        print(f"{gk}: positions aligned in both copies: {shared}")
        print(f"changes unique to {na} (m1): {m1}; unique to {nb} (m2): {m2}; chi2 (1 df) = {chi:.2f}"
              f" ({'P<0.05' if chi > 3.841 else 'not significant at 0.05'})")


def expression_timecourse(cfg):
    section("4. Whole-embryo time course, E-ERAD-475 (TPM, median of replicates)")
    conf = get(ATLAS + "E-ERAD-475-configuration.xml").decode()
    labels = dict(re.findall(r'<assay_group id="([^"]+)" label="([^"]+)"', conf))
    order = re.findall(r'<assay_group id="([^"]+)"', conf)
    want = {v["ens"]: g for g, v in cfg["genes"].items()}
    rows = {}
    req = urllib.request.Request(ATLAS + "E-ERAD-475-tpms.tsv", headers=UA)
    with urllib.request.urlopen(req, timeout=300) as fh:
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


def bgee(cfg, gar_ids):
    section("5. Bgee expressed calls per anatomical entity (score 0-100; only 'expressed' calls are returned)")
    tables = {g: bgee_calls(v["ens"], 7955) for g, v in cfg["genes"].items()}
    for gid in gar_ids:
        try:
            tables[f"gar {gid}"] = bgee_calls(gid, 7918)
        except Exception as e:  # noqa: BLE001
            print(f"Bgee query failed for gar {gid}: {e}")
    for k, calls in tables.items():
        print(f"### {k}: {len(calls)} calls")
        for name, score, qual, dt in sorted(calls, key=lambda c: -c[1]):
            print(f"- {name}: {score:.1f} ({qual}; {dt})")
    zf = list(cfg["genes"])
    a = {n for n, _, _, _ in tables[zf[0]]}
    b = {n for n, _, _, _ in tables[zf[1]]}
    print(f"\nentities called for {zf[0]} only: {sorted(a - b)}")
    print(f"entities called for {zf[1]} only: {sorted(b - a)}")
    print(f"entities called for both: {sorted(a & b)}")


def zfin(cfg):
    section("6. ZFIN curated wild-type expression (wildtype-expression_fish.txt)")
    text = get(ZFIN_URL).decode("utf-8", errors="replace")
    recs = {g: [] for g in cfg["genes"]}
    for row in csv.reader(io.StringIO(text), delimiter="\t"):
        if len(row) > 11 and row[1] in recs:
            recs[row[1]].append(f"{row[4]}{' > ' + row[6] if row[6] else ''} | {row[7]} - {row[8]} | {row[9]} | {row[11]}")
    for g, rows in recs.items():
        print(f"### {g}: {len(rows)} records")
        for r in rows:
            print(f"- {r}")


def genes_near(chrom: str, start: int, end: int):
    d = ens_json(f"/overlap/region/danio_rerio/{chrom}:{max(1, start)}-{end}?feature=gene;biotype=protein_coding")
    return [(x["id"], x.get("external_name"), x["start"]) for x in d]


def synteny(cfg):
    section("7. Local synteny between the two copies (Ensembl REST)")
    w = cfg["synteny_window_bp"]
    loc = {}
    for g, v in cfg["genes"].items():
        d = ens_json(f"/lookup/id/{v['ens']}?")
        loc[g] = (d["seq_region_name"], d["start"], d["end"])
        print(f"{g}: chr{d['seq_region_name']}:{d['start']}-{d['end']}")
    levels = set(cfg["teleost_levels"])
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
            return [x["id"] for x in h["data"][0]["homologies"] if x.get("taxonomy_level") in levels]

        with ThreadPoolExecutor(max_workers=4) as ex:
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
        print(f"\n{src} +/- {w/1e6:.1f} Mb: {len(neigh)} other protein-coding genes "
              f"({failed} homology queries failed); {with_par} have a teleost-level "
              f"({'/'.join(sorted(levels))}) zebrafish paralogue; "
              f"{len(hits)} such pairs have their partner within {w/1e6:.1f} Mb of {tgt}:")
        for h in hits:
            print(f"- {h}")
        print(f"Of the teleost-level paralogue pairs, {len(chrom_hits)} have their partner anywhere on "
              f"chr{tloc[0]} (the chromosome of {tgt}, {len(target_chrom)} protein-coding genes):")
        for h in chrom_hits:
            print(f"- {h}")


def main():
    cfg = CONFIG
    print(f"# Pair analysis: {' / '.join(cfg['genes'])}  (run {time.strftime('%Y-%m-%d')})")
    gar_ids, med_ids = homologies(cfg)
    zf, extra, hs, orth = proteins(cfg, gar_ids, med_ids)
    regions(cfg, zf, extra, hs, orth)
    relative_rate(zf, orth)
    expression_timecourse(cfg)
    bgee(cfg, gar_ids)
    zfin(cfg)
    synteny(cfg)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
