"""Paralog-pair analysis for zebrafish guca1c / guca1d (GCAP3 / GCAP4; human GUCA1C).

Reproducible: reads the cached UniProt records for the two zebrafish proteins and
queries public services at run time (nothing is hardcoded except identifiers):
  * ZFIN aliases download - maps the historical protein names (GCAP1-7) used in
                    the literature to current ZFIN gene symbols;
  * UniProt REST  - human GUCA1A/GUCA1B/GUCA1C sequences and the Ca2+-binding
                    residues / myristoylation site annotated on human GUCA1C;
  * Ensembl REST  - spotted gar and medaka ortholog proteins (canonical transcripts),
                    gene coordinates, and zebrafish within-species paralogues of
                    neighbouring genes;
  * EBI Expression Atlas FTP - E-ERAD-475 (whole-embryo developmental time course);
  * Bgee REST API  - expressed calls per anatomical entity for the two zebrafish
                    genes and the gar ortholog.

Sections:
  0. ZFIN symbol <-> GCAP name mapping;
  1. pairwise global identities (Biopython PairwiseAligner, BLOSUM62, gap open -10 /
     extend -0.5; identity = identical columns / alignment length);
  2. residues aligned to the human GUCA1C Ca2+-binding positions (EF-hand loops),
     the N-myristoylation glycine, and EF1 loop; identity per EF-hand domain;
  3. Tajima-style relative-rate test (outgroup = gar);
  4. whole-embryo time course (E-ERAD-475 medians);
  5. Bgee calls (zebrafish copies + gar);
  6. local synteny between the copies.

Run from the repo root:
    uv run python genes/DANRE/guca1c/guca1c-bioinformatics/pair_analysis.py \
        > genes/DANRE/guca1c/guca1c-bioinformatics/output.txt
"""

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
        "guca1c": {"ens": "ENSDARG00000030758", "uniprot_txt": "genes/DANRE/guca1c/guca1c-uniprot.txt"},
        "guca1d": {"ens": "ENSDARG00000044629", "uniprot_txt": "genes/DANRE/guca1d/guca1d-uniprot.txt"},
    },
    "human": {"GUCA1C": "O95843", "GUCA1A": "P43080", "GUCA1B": "Q9UMX6"},
    "human_ref": "GUCA1C",
    "ensembl_orthologs": {  # from Ensembl homology of the zebrafish genes
        "gar_GUCA1C": "ENSLOCG00000009269",
        "medaka_ortholog_of_guca1c": "ENSORLG00000002874",
        "medaka_ortholog_of_guca1d": "ENSORLG00000013800",
    },
    "gar_key": "gar_GUCA1C",
    "gar_species_id": 7918,
    "zfin_alias_pattern": r"^(guca1|gcap)",
    "teleost_levels": ("Osteoglossocephalai", "Clupeocephala"),
    "synteny_window_bp": 1_500_000,
}

ENSEMBL = "https://rest.ensembl.org"


def get(url: str, retries: int = 8) -> bytes:
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Content-Type": "application/json", **UA})
            return urllib.request.urlopen(req, timeout=120).read()
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


def parse_fasta(text: str) -> dict[str, str]:
    out, name = {}, None
    for line in text.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0].split("|")[1]
            out[name] = ""
        elif name:
            out[name] += line.strip()
    return out


def uniprot_fasta(acc: str, isoforms: bool = False) -> dict[str, str]:
    url = f"https://rest.uniprot.org/uniprotkb/stream?query=accession:{acc}&format=fasta"
    if isoforms:
        url += "&includeIsoform=true"
    return parse_fasta(get(url).decode())


def ensembl_canonical_protein(gene_id: str) -> str:
    d = ens_json(f"/lookup/id/{gene_id}?expand=1")
    tr = [t for t in d["Transcript"] if t.get("is_canonical") and t.get("Translation")]
    tr = tr or [t for t in d["Transcript"] if t.get("Translation")]
    return ens_json(f"/sequence/id/{tr[0]['Translation']['id']}?type=protein")["seq"]


def aligner():
    a = Align.PairwiseAligner(mode="global")
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


AL = aligner()


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


def proteins(cfg):
    zf = {g: uniprot_txt_seq(ROOT / v["uniprot_txt"]) for g, v in cfg["genes"].items()}
    hs = {name: uniprot_fasta(acc)[acc] for name, acc in cfg["human"].items()}
    orth = {k: ensembl_canonical_protein(v) for k, v in cfg["ensembl_orthologs"].items()}
    allseq = {**zf, **hs, **orth}
    section("1. Sequence lengths and pairwise identities")
    for k, v in allseq.items():
        print(f"length {k}: {len(v)} aa")
    names = list(allseq)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            pid, cols = identity(allseq[a], allseq[b])
            print(f"identity {a} vs {b}: {pid:.1f}% over {cols} columns")
    section("1b. Zebrafish copies vs each isoform of the human reference")
    iso = uniprot_fasta(cfg["human"][cfg["human_ref"]], isoforms=True)
    for iname, iseq in iso.items():
        for g, s in zf.items():
            pid, cols = identity(iseq, s)
            print(f"identity {g} vs {iname} ({len(iseq)} aa): {pid:.1f}% over {cols} columns; "
                  f"N-terminal 60 aa: {identity(iseq[:60], s[:60])[0]:.1f}%")
    return zf, hs, orth


def relative_rate(cfg, zf, orth):
    section("3. Tajima-style relative-rate test (outgroup = gar)")
    gar = orth[cfg["gar_key"]]
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


def bgee(cfg):
    section("5. Bgee expressed calls per anatomical entity (expression score 0-100; only 'expressed' calls are returned)")
    tables = {g: bgee_calls(v["ens"], 7955) for g, v in cfg["genes"].items()}
    gar_id = cfg["ensembl_orthologs"][cfg["gar_key"]]
    tables[cfg["gar_key"] + " (spotted gar)"] = bgee_calls(gar_id, cfg["gar_species_id"])
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


def genes_near(chrom: str, start: int, end: int):
    d = ens_json(f"/overlap/region/danio_rerio/{chrom}:{max(1, start)}-{end}?feature=gene;biotype=protein_coding")
    return [(x["id"], x.get("external_name"), x["start"]) for x in d]


def synteny(cfg):
    section("6. Local synteny between the two copies (Ensembl REST)")
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
            return [x["id"] for x in h["data"][0]["homologies"] if x.get("taxonomy_level") in cfg["teleost_levels"]]

        with ThreadPoolExecutor(max_workers=4) as ex:
            results = list(ex.map(teleost_paralogues, [n[0] for n in neigh]))
        hits, chrom_hits, with_teleost_par, failed = [], [], 0, 0
        for (gid, name, _), pars in zip(neigh, results):
            if pars is None:
                failed += 1
                continue
            if pars:
                with_teleost_par += 1
            for pid in pars:
                if pid in target_window:
                    tname, tstart = target_window[pid]
                    hits.append(f"{name or gid} -> {tname or pid} (chr{tloc[0]}:{tstart})")
                if pid in target_chrom:
                    tname, tstart = target_chrom[pid]
                    chrom_hits.append(f"{name or gid} -> {tname or pid} (chr{tloc[0]}:{tstart})")
        print(f"\n{src} +/- {w/1e6:.1f} Mb: {len(neigh)} other protein-coding genes "
              f"({failed} homology queries failed); "
              f"{with_teleost_par} have a teleost-level ({'/'.join(cfg['teleost_levels'])}) zebrafish paralogue; "
              f"{len(hits)} such paralogue pairs have their partner within {w/1e6:.1f} Mb of {tgt}:")
        for h in hits:
            print(f"- {h}")
        print(f"Of the teleost-level paralogue pairs, {len(chrom_hits)} have their partner anywhere on "
              f"chr{tloc[0]} (the chromosome of {tgt}, {len(target_chrom)} protein-coding genes):")
        for h in chrom_hits:
            print(f"- {h}")



def zfin_names(cfg):
    section("0. ZFIN gene symbols and aliases for the GCAP family (ZFIN aliases.txt)")
    txt = get("https://zfin.org/downloads/aliases.txt").decode("utf-8", errors="replace")
    pat = re.compile(cfg["zfin_alias_pattern"], re.I)
    rows = {}
    for line in txt.splitlines():
        f = line.split("\t")
        if len(f) >= 4 and f[0].startswith("ZDB-GENE") and (pat.search(f[2]) or pat.search(f[3])):
            rows.setdefault((f[0], f[2], f[1]), []).append(f[3])
    for (zid, sym, name), aliases in sorted(rows.items(), key=lambda x: x[0][1]):
        print(f"- {sym} ({zid}; {name}): aliases {', '.join(aliases)}")


def regions(cfg, zf, hs, orth):
    section("2. Human GUCA1C landmarks aligned in each protein")
    ref = hs[cfg["human_ref"]]
    acc = cfg["human"][cfg["human_ref"]]
    feats = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))["features"]
    ca = [f["location"]["start"]["value"] for f in feats
          if f["type"] == "Binding site" and "Ca" in f.get("ligand", {}).get("name", "")]
    efs = [(f["description"], f["location"]["start"]["value"], f["location"]["end"]["value"])
           for f in feats if f["type"] == "Domain" and f.get("description", "").startswith("EF-hand")]
    myr = [f["location"]["start"]["value"] for f in feats if f["type"] == "Lipidation"]
    others = {**zf, cfg["gar_key"]: orth[cfg["gar_key"]],
              "medaka_ortholog_of_guca1c": orth["medaka_ortholog_of_guca1c"],
              "medaka_ortholog_of_guca1d": orth["medaka_ortholog_of_guca1d"]}
    maps = {k: pos_map(ref, v) for k, v in others.items()}
    print(f"human {cfg['human_ref']} ({acc}) Ca2+-binding positions: {ca}; lipidation: {myr}")
    print("| position (human) | human | " + " | ".join(others) + " |")
    print("|---|---|" + "---|" * len(others))
    for p in myr + ca:
        print(f"| {p} | {ref[p-1]} | " + " | ".join(str(maps[k].get(p)) for k in others) + " |")
    print()
    for label, s, e in efs:
        n = e - s + 1
        seg = {k: "".join(maps[k].get(p) or "-" for p in range(s, e + 1)) for k in others}
        print(f"{label} [{s}-{e}] human: {ref[s-1:e]}")
        for k in others:
            same = sum(1 for p in range(s, e + 1) if maps[k].get(p) == ref[p - 1])
            print(f"  {k}: {seg[k]}  identical {same}/{n}")
    for k, s in {**others, cfg["human_ref"]: ref}.items():
        print(f"N-terminal myristoylation motif (M-G at 1-2) in {k}: {s[:2] == 'MG'} ({s[:8]}...)")
    # EF-hand loop pairwise comparison between the two zebrafish copies
    (na, a), (nb, b) = list(zf.items())
    x = aln(a, b)
    diffs = [(i + 1, p, q) for i, (p, q) in enumerate(zip(x[0], x[1])) if p != q]
    print(f"\n{na} vs {nb}: {len(diffs)} differing alignment columns out of {len(x[0])}")


def main():
    cfg = CONFIG
    print(f"# Pair analysis: {' / '.join(cfg['genes'])}  (run {time.strftime('%Y-%m-%d')})")
    zfin_names(cfg)
    zf, hs, orth = proteins(cfg)
    regions(cfg, zf, hs, orth)
    relative_rate(cfg, zf, orth)
    expression_timecourse(cfg)
    bgee(cfg)
    synteny(cfg)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
