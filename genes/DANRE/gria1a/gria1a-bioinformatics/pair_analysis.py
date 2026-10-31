"""Paralog-pair analysis for zebrafish gria1a / gria1b (human GRIA1, GluA1).

Reproducible: reads the cached UniProt records for the two zebrafish proteins and
queries public services at run time (nothing is hardcoded):
  * UniProt REST  - human reference proteins and the features of the human ortholog;
  * Ensembl REST  - Compara orthologs/paralogues (gar, medaka, human), canonical
                    proteins of the gar ortholog, gene coordinates, neighbouring genes
                    and their zebrafish paralogues (synteny);
  * EBI Expression Atlas FTP - E-ERAD-475 whole-embryo developmental time course (TPM);
  * Bgee REST API - expressed calls per anatomical entity (zebrafish copies and gar);
  * ZFIN download - curated wild-type expression (anatomy terms, stages, publications).

Sections:
  0. Ensembl Compara homologies of each copy (orthologs, within-species paralogue level);
  1. pairwise global identities (Biopython PairwiseAligner, BLOSUM62, gap open -10 /
     extend -0.5; identity = identical columns / alignment length);
  2. identity per UniProt feature region of the human ortholog and conservation of
     point features (binding sites, modified residues, lipidation, motifs) in the
     zebrafish copies, gar and medaka orthologs;
  2b. the same point features across every Ensembl translation of each zebrafish copy;
  3. Tajima-style relative-rate test (outgroup = gar);
  4. whole-embryo time course (E-ERAD-475 medians);
  5. Bgee calls (zebrafish copies + gar);
  6. ZFIN curated wild-type expression;
  7. local synteny between the copies.

Run from the repo root:
    uv run python genes/DANRE/gria1a/gria1a-bioinformatics/pair_analysis.py \
        > genes/DANRE/gria1a/gria1a-bioinformatics/output.txt
"""

import csv
import io
import json
import re
import sys
import time
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
UA = {"User-Agent": "ai-gene-review-pair-analysis/1.0"}

CONFIG = {
    "genes": {
        "gria1a": {"uniprot_txt": "genes/DANRE/gria1a/gria1a-uniprot.txt"},
        "gria1b": {"uniprot_txt": "genes/DANRE/gria1b/gria1b-uniprot.txt"},
    },
    # human proteins to compare against (ortholog first)
    "human": {"GRIA1": "P42261", "GRIA2": "P42262"},
    "human_ref": "GRIA1",
    "feature_types_region": ("Region", "Domain", "Topological domain", "Transmembrane", "Intramembrane"),
    "feature_types_point": ("Binding site", "Modified residue", "Lipidation", "Motif", "Active site", "Site"),
    "window_regions": [],
    "segments": [("pore loop and M2-M3 (Q/R site region)", 585, 612), ("C-terminal tail", 827, 906)],
    "teleost_levels": ("Clupeocephala", "Osteoglossocephalai", "Teleostei"),
    "synteny_window_bp": 1_500_000,
    "gar_species": "lepisosteus_oculatus",
    "gar_species_id": 7918,
}

ENSEMBL = "https://rest.ensembl.org"


def get(url: str, retries: int = 10, headers: dict | None = None) -> bytes:
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={**UA, **(headers or {})})
            return urllib.request.urlopen(req, timeout=300).read()
        except Exception:  # noqa: BLE001
            if i == retries - 1:
                raise
            time.sleep(3 + 4 * i)
    raise RuntimeError(url)


def ens_json(path: str):
    time.sleep(0.1)
    return json.loads(get(ENSEMBL + path + ("&" if "?" in path else "?") + "content-type=application/json",
                          headers={"Content-Type": "application/json"}))


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def parse_fasta(text: str) -> dict[str, str]:
    out, name = {}, None
    for line in text.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0].split("|")[1]
            out[name] = ""
        elif name:
            out[name] += line.strip()
    return out


def uniprot_fasta(acc: str) -> str:
    return parse_fasta(get(f"https://rest.uniprot.org/uniprotkb/stream?query=accession:{acc}&format=fasta").decode())[acc]


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
    sys.stdout.flush()


def homologies(cfg):
    section("0. Ensembl Compara homologies")
    for g, v in cfg["genes"].items():
        d = ens_json(f"/lookup/symbol/danio_rerio/{g}?")
        v["ens"] = d["id"]
        v["loc"] = (d["seq_region_name"], d["start"], d["end"])
        print(f"{g}: {d['id']} chr{d['seq_region_name']}:{d['start']}-{d['end']}")
        h = ens_json(f"/homology/id/danio_rerio/{d['id']}?format=condensed")
        for x in h["data"][0]["homologies"]:
            if x["species"] in ("lepisosteus_oculatus", "oryzias_latipes", "homo_sapiens") or (
                x["species"] == "danio_rerio" and x["type"] == "within_species_paralog"
                    and x.get("taxonomy_level") in cfg["teleost_levels"] + ("Neopterygii",)):
                print(f"  {x['species']} {x['type']} {x['id']} node={x.get('taxonomy_level')}")
            if x["species"] == cfg["gar_species"] and x["type"].startswith("ortholog"):
                cfg.setdefault("gar_ids", set()).add(x["id"])
            if x["species"] == "oryzias_latipes" and x["type"].startswith("ortholog"):
                v.setdefault("medaka", []).append(x["id"])
    print(f"gar orthologs (union): {sorted(cfg.get('gar_ids', []))}")


def proteins(cfg):
    zf = {g: uniprot_txt_seq(ROOT / v["uniprot_txt"]) for g, v in cfg["genes"].items()}
    hs = {name: uniprot_fasta(acc) for name, acc in cfg["human"].items()}
    orth = {}
    for gid in sorted(cfg.get("gar_ids", [])):
        orth[f"gar_{gid}"] = ensembl_canonical_protein(gid)
    for g, v in cfg["genes"].items():
        for mid in v.get("medaka", []):
            orth[f"medaka_{mid}(orth of {g})"] = ensembl_canonical_protein(mid)
    allseq = {**zf, **hs, **orth}
    section("1. Sequence lengths and pairwise identities")
    for k, v in allseq.items():
        print(f"length {k}: {len(v)} aa")
    names = list(allseq)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            pid, cols = identity(allseq[a], allseq[b])
            print(f"identity {a} vs {b}: {pid:.1f}% over {cols} columns")
    return zf, hs, orth


def regions(cfg, zf, hs, orth):
    section("2. Regions and point features of the human ortholog")
    ref = hs[cfg["human_ref"]]
    acc = cfg["human"][cfg["human_ref"]]
    feats = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))["features"]
    regs = [(f["type"] + (": " + f["description"] if f.get("description") else ""),
             f["location"]["start"]["value"], f["location"]["end"]["value"])
            for f in feats if f["type"] in cfg["feature_types_region"]]
    regs += cfg["window_regions"]
    gar = {k: v for k, v in orth.items() if k.startswith("gar_")}
    others = {**zf, **orth}
    maps = {k: pos_map(ref, v) for k, v in others.items()}
    for label, s, e in regs:
        n = e - s + 1
        row = []
        for k, m in maps.items():
            same = sum(1 for p in range(s, e + 1) if m.get(p) == ref[p - 1])
            aligned = sum(1 for p in range(s, e + 1) if m.get(p))
            row.append(f"{k} {same}/{n} identical ({100*same/n:.1f}%; aligned {aligned})")
        print(f"{label} [{s}-{e}]: " + "; ".join(row))
    print()
    for f in feats:
        if f["type"] not in cfg["feature_types_point"]:
            continue
        s, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
        desc = f.get("description") or f.get("ligand", {}).get("name", "")
        human = ref[s - 1:e]
        row = []
        for k, m in maps.items():
            got = "".join(m.get(p) or "-" for p in range(s, e + 1))
            row.append(f"{k}={got}{'' if got == human else ' (DIFFERENT)'}")
        print(f"{f['type']} {s}-{e} ({desc}) human={human}: " + "; ".join(row))
    print()
    for label, s, e in cfg.get("segments", []):
        print(f"aligned segment {label} [{s}-{e}] human={ref[s-1:e]}: "
              + "; ".join(f"{k}=" + "".join(m.get(p) or "-" for p in range(s, e + 1)) for k, m in maps.items()))
    for k, s in {**zf, cfg["human_ref"]: ref, **gar}.items():
        print(f"C-terminal 10 residues {k}: {s[-10:]}")


def isoform_check(cfg, hs):
    """Map point features of the human ortholog onto every Ensembl translation of each zebrafish copy,
    to check that differences seen in the UniProt entry are not an isoform artefact."""
    section("2b. Point features across all Ensembl translations of each zebrafish copy")
    ref = hs[cfg["human_ref"]]
    acc = cfg["human"][cfg["human_ref"]]
    feats = [f for f in json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))["features"]
             if f["type"] in cfg["feature_types_point"]]
    for g, v in cfg["genes"].items():
        d = ens_json(f"/lookup/id/{v['ens']}?expand=1")
        for t in d["Transcript"]:
            if not t.get("Translation"):
                continue
            pid = t["Translation"]["id"]
            seq = ens_json(f"/sequence/id/{pid}?type=protein")["seq"]
            m = pos_map(ref, seq)
            row = []
            for f in feats:
                s, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
                got = "".join(m.get(p) or "-" for p in range(s, e + 1))
                if got != ref[s - 1:e]:
                    row.append(f"{f['type']} {s} {ref[s-1:e]}->{got}")
            print(f"{g} {t['id']} ({len(seq)} aa{', canonical' if t.get('is_canonical') else ''}): "
                  f"C-term {seq[-6:]}; differing point features: {row or 'none'}")


def relative_rate(cfg, zf, orth):
    section("3. Tajima-style relative-rate test (outgroup = gar)")
    gars = [v for k, v in orth.items() if k.startswith("gar_")]
    if not gars:
        print("no gar ortholog")
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
    print(f"gar protein length {len(gar)}; positions aligned in both copies: {shared}")
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
    text = get(base + "E-ERAD-475-tpms.tsv").decode()
    lines = text.splitlines()
    header = lines[0].split("\t")
    for line in lines[1:]:
        f = line.split("\t")
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


def bgee(cfg):
    section("5. Bgee expressed calls per anatomical entity (expression score 0-100; only 'expressed' calls)")
    tables = {g: bgee_calls(v["ens"], 7955) for g, v in cfg["genes"].items()}
    for gid in sorted(cfg.get("gar_ids", [])):
        try:
            tables[f"gar {gid}"] = bgee_calls(gid, cfg["gar_species_id"])
        except Exception as exc:  # noqa: BLE001
            print(f"gar {gid}: Bgee query failed ({exc})")
    for k, calls in tables.items():
        print(f"### {k}: {len(calls)} calls")
        for name, score, qual, dt in sorted(calls, key=lambda c: -c[1]):
            print(f"- {name}: {score:.1f} ({qual}; {dt})")
    zf = list(cfg["genes"])
    a = {n: s for n, s, _, _ in tables[zf[0]]}
    b = {n: s for n, s, _, _ in tables[zf[1]]}
    print(f"\nentities called for {zf[0]} only: {sorted(set(a) - set(b))}")
    print(f"entities called for {zf[1]} only: {sorted(set(b) - set(a))}")
    both = sorted(set(a) & set(b))
    print(f"entities called for both ({len(both)}); score {zf[0]} - {zf[1]}:")
    for n in both:
        print(f"- {n}: {a[n]:.1f} vs {b[n]:.1f} (diff {a[n]-b[n]:+.1f})")


def zfin(cfg):
    section("6. ZFIN curated wild-type expression (wildtype-expression_fish.txt)")
    text = get("https://zfin.org/downloads/wildtype-expression_fish.txt").decode("utf-8", errors="replace")
    recs = defaultdict(list)
    for row in csv.reader(io.StringIO(text), delimiter="\t"):
        if len(row) > 11 and row[1] in cfg["genes"]:
            anat = row[4] + (f" > {row[6]}" if len(row) > 6 and row[6] else "")
            recs[row[1]].append((anat, row[7], row[9], row[11]))
    terms = {}
    for g in cfg["genes"]:
        rs = recs.get(g, [])
        pubs = sorted({r[3] for r in rs})
        terms[g] = {r[0] for r in rs}
        print(f"### {g}: {len(rs)} records, {len(terms[g])} anatomy terms, publications: {pubs}")
        by_pub = defaultdict(set)
        for anat, st, assay, pub in rs:
            by_pub[pub].add(anat)
        for pub, ts in sorted(by_pub.items()):
            print(f"- {pub}: {'; '.join(sorted(ts))}")
    ga, gb = list(cfg["genes"])
    print(f"\nterms for {ga} only: {sorted(terms[ga] - terms[gb])}")
    print(f"terms for {gb} only: {sorted(terms[gb] - terms[ga])}")
    print(f"terms for both: {sorted(terms[ga] & terms[gb])}")


def genes_near(chrom: str, start: int, end: int):
    d = ens_json(f"/overlap/region/danio_rerio/{chrom}:{max(1, start)}-{end}?feature=gene;biotype=protein_coding")
    return [(x["id"], x.get("external_name"), x["start"]) for x in d]


def synteny(cfg):
    section("7. Local synteny between the two copies (Ensembl REST)")
    w = cfg["synteny_window_bp"]
    loc = {g: v["loc"] for g, v in cfg["genes"].items()}
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
            return [x["id"] for x in h["data"][0]["homologies"] if x.get("taxonomy_level") in cfg["teleost_levels"]]

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
        print(f"\n{src} chr{sloc[0]}:{sloc[1]} +/- {w/1e6:.1f} Mb: {len(neigh)} other protein-coding genes "
              f"({failed} homology queries failed); {with_par} have a teleost-level "
              f"({'/'.join(cfg['teleost_levels'])}) zebrafish paralogue; "
              f"{len(hits)} such pairs have their partner within {w/1e6:.1f} Mb of {tgt}:")
        for h in hits:
            print(f"- {h}")
        print(f"{len(chrom_hits)} have their partner anywhere on chr{tloc[0]} (chromosome of {tgt}, "
              f"{len(target_chrom)} protein-coding genes):")
        for h in chrom_hits:
            print(f"- {h}")


def main():
    cfg = CONFIG
    print(f"# Pair analysis: {' / '.join(cfg['genes'])}  (run {time.strftime('%Y-%m-%d')})")
    homologies(cfg)
    zf, hs, orth = proteins(cfg)
    regions(cfg, zf, hs, orth)
    try:
        isoform_check(cfg, hs)
    except Exception as exc:  # noqa: BLE001
        print(f"\n[isoform_check failed: {exc}]")
    relative_rate(cfg, zf, orth)
    for step in (expression_timecourse, bgee, zfin, synteny):
        try:
            step(cfg)
        except Exception as exc:  # noqa: BLE001
            print(f"\n[{step.__name__} failed: {exc}]")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
