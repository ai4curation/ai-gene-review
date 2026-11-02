"""Paralog-pair analysis for zebrafish tusc2a / tusc2b (human TUSC2, FUS1).

Reproducible: reads the cached UniProt records for the two zebrafish proteins and
queries public services at run time (nothing is hardcoded):
  * UniProt REST  - human TUSC2 (all isoforms) and its annotated features;
  * Ensembl REST  - spotted gar and medaka orthologue proteins (canonical
                    transcripts), gene coordinates and within-species paralogues of
                    neighbouring genes (for synteny);
  * EBI Expression Atlas FTP - E-ERAD-475 whole-embryo developmental time course;
  * Bgee REST API  - expressed calls per anatomical entity (zebrafish copies + gar);
  * ZFIN download  - curated wild-type expression (wildtype-expression_fish.txt).

Sections:
  1. pairwise global identities (Biopython PairwiseAligner, BLOSUM62, gap -10/-0.5;
     identity = identical columns / alignment length);
  1b. each zebrafish copy vs every human isoform (full-length vs short forms);
  2. identity per annotated region of the human protein (UniProt features) and per
     domain/repeat annotated on the zebrafish 'a' copy, mapped to the 'b' copy;
     conservation of listed motif residues;
  3. Tajima-style relative-rate test (outgroup = gar);
  4. whole-embryo time course (E-ERAD-475 medians);
  5. Bgee calls;
  6. ZFIN curated wild-type expression;
  7. local synteny between the copies (teleost-level paralogues of neighbours).

Run from the repo root:
    uv run python genes/DANRE/tusc2a/tusc2a-bioinformatics/pair_analysis.py \
        > genes/DANRE/tusc2a/tusc2a-bioinformatics/output.txt
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
        "tusc2a": {"ens": "ENSDARG00000099817", "zfin": "ZDB-GENE-061013-612",
                   "uniprot_txt": "genes/DANRE/tusc2a/tusc2a-uniprot.txt"},
        "tusc2b": {"ens": "ENSDARG00000025340", "zfin": "ZDB-GENE-040718-99",
                   "uniprot_txt": "genes/DANRE/tusc2b/tusc2b-uniprot.txt"},
    },
    "human": {"TUSC2": "O75896"},
    "human_ref": "TUSC2",
    "ensembl_orthologs": {  # Ensembl Compara orthologues of the zebrafish genes
        "gar_TUSC2": "ENSLOCG00000014230",
        "medaka_ortholog_of_tusc2a": "ENSORLG00000027802",
        "medaka_ortholog_of_tusc2b": "ENSORLG00000027402",
    },
    "gar_key": "gar_TUSC2",
    "gar_species_id": 7918,
    "feature_types": ("Chain", "Modified residue", "Lipidation"),
    "zf_feature_keys": ("DOMAIN", "REPEAT", "COILED"),
    # calcium-binding motif of TUSC2 as quoted in PMID:42314984 (exact and D-x-D-x-D variants)
    "motifs": {"CBM_exact": "DEDGDLAHEFYEE", "DxDxD": "D.D.D"},
    "teleost_levels": {"Teleostei", "Osteoglossocephalai", "Clupeocephala"},
    "synteny_window_bp": 1_500_000,
}

ENSEMBL = "https://rest.ensembl.org"


def get(url: str, retries: int = 10) -> bytes:
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
    time.sleep(0.1)
    return json.loads(get(ENSEMBL + path + ("&" if "?" in path else "?") + "content-type=application/json"))


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def uniprot_txt_features(path: Path, keys) -> list[tuple[str, int, int]]:
    out = []
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^FT   (\w+)\s+(\d+)\.\.(\d+)", line)
        if m and m.group(1) in keys:
            note = ""
            for nxt in lines[i + 1:i + 4]:
                if re.match(r"^FT   \w", nxt):
                    break  # next feature starts; this one has no note
                n = re.search(r'/note="([^"]*)', nxt)
                if n:
                    note = n.group(1)
                    break
            out.append((f"{m.group(1)} {note}".strip(), int(m.group(2)), int(m.group(3))))
    return out


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
    section("1b. Zebrafish copies vs each human isoform")
    iso = uniprot_fasta(cfg["human"][cfg["human_ref"]], isoforms=True)
    for iname, iseq in iso.items():
        for g, s in zf.items():
            pid, cols = identity(iseq, s)
            print(f"identity {g} vs {iname} ({len(iseq)} aa): {pid:.1f}% over {cols} columns")
    return zf, hs, orth


def regions(cfg, zf, hs, orth):
    section("2. Regions of the human protein (UniProt features) and of the zebrafish 'a' copy")
    ref = hs[cfg["human_ref"]]
    acc = cfg["human"][cfg["human_ref"]]
    feats = json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}.json"))["features"]
    regs = [(f["type"] + (": " + f["description"] if f.get("description") else ""),
             f["location"]["start"]["value"], f["location"]["end"]["value"])
            for f in feats if f["type"] in cfg["feature_types"]]
    others = {**zf, cfg["gar_key"]: orth[cfg["gar_key"]]}
    maps = {k: pos_map(ref, v) for k, v in others.items()}
    print(f"### human {cfg['human_ref']} ({acc}) features")
    for label, s, e in regs:
        n = e - s + 1
        for k, m in maps.items():
            aligned = sum(1 for p in range(s, e + 1) if m.get(p))
            same = sum(1 for p in range(s, e + 1) if m.get(p) == ref[p - 1])
            extra = ""
            if n <= 3:
                extra = " residues: " + ", ".join(f"{ref[p-1]}{p}->{m.get(p)}" for p in range(s, e + 1))
            print(f"{label} [{s}-{e}] {k}: aligned {aligned}/{n}, identical {same}/{n} ({100*same/n:.1f}%){extra}")
    (ga, sa), (gb, sb) = list(zf.items())
    fa = uniprot_txt_features(ROOT / cfg["genes"][ga]["uniprot_txt"], cfg["zf_feature_keys"])
    mab = pos_map(sa, sb)
    print(f"\n### zebrafish {ga} features (cached UniProt record) mapped to {gb}")
    for label, s, e in fa:
        n = e - s + 1
        aligned = sum(1 for p in range(s, e + 1) if mab.get(p))
        same = sum(1 for p in range(s, e + 1) if mab.get(p) == sa[p - 1])
        print(f"{label} [{s}-{e}] {ga} vs {gb}: aligned {aligned}/{n}, identical {same}/{n} ({100*same/n:.1f}%)")
    if cfg["motifs"]:
        print("\n### literal motif search")
        for mname, motif in cfg["motifs"].items():
            for k, s in {**zf, **hs, **orth}.items():
                hits = [m.start() + 1 for m in re.finditer(motif, s)]
                print(f"motif {mname} ({motif}) in {k}: {hits or 'not found'}")
    for k, s in {**zf, **hs, cfg["gar_key"]: orth[cfg["gar_key"]]}.items():
        print(f"N-terminus of {k}: {s[:12]} (Gly at position 2: {s[1:2] == 'G'})")


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
    with urllib.request.urlopen(req, timeout=600) as fh:
        header = fh.readline().decode().rstrip("\n").split("\t")
        for line in fh:
            f = line.decode().rstrip("\n").split("\t")
            if f[0] in want:
                rows[want[f[0]]] = dict(zip(header, f))
    genes = list(cfg["genes"])
    for g in genes:
        if g not in rows:
            print(f"{g}: no row in E-ERAD-475 for {cfg['genes'][g]['ens']}")
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
    sa = {n: s for n, s, _, _ in tables[zf[0]]}
    sb = {n: s for n, s, _, _ in tables[zf[1]]}
    shared = sorted(set(sa) & set(sb))
    if shared:
        diffs = [sa[k] - sb[k] for k in shared]
        print(f"entities called for both: {len(shared)}; {zf[0]} score higher in "
              f"{sum(d > 0 for d in diffs)}, median difference ({zf[0]} - {zf[1]}) "
              f"= {sorted(diffs)[len(diffs)//2]:.1f}")


def zfin(cfg):
    section("6. ZFIN curated wild-type expression (wildtype-expression_fish.txt)")
    rows = get("https://zfin.org/downloads/wildtype-expression_fish.txt").decode(errors="replace").splitlines()
    for g, v in cfg["genes"].items():
        mine = [r.split("\t") for r in rows if r.startswith(v["zfin"] + "\t")]
        print(f"### {g} ({v['zfin']}): {len(mine)} rows")
        seen = set()
        for r in mine:
            key = (r[4], r[7], r[8], r[9], r[11] if len(r) > 11 else "")
            if key in seen:
                continue
            seen.add(key)
            print(f"- {r[4]} | {r[7]} to {r[8]} | assay {r[9]} | {r[11] if len(r) > 11 else ''}")


def genes_near(chrom: str, start: int, end: int):
    d = ens_json(f"/overlap/region/danio_rerio/{chrom}:{max(1, start)}-{end}?feature=gene;biotype=protein_coding")
    return [(x["id"], x.get("external_name"), x["start"]) for x in d]


def synteny(cfg):
    section("7. Local synteny between the two copies (Ensembl REST)")
    w = cfg["synteny_window_bp"]
    levels = cfg["teleost_levels"]
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
            return [x["id"] for x in h["data"][0]["homologies"] if x.get("taxonomy_level") in levels]

        with ThreadPoolExecutor(max_workers=3) as ex:
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
              f"{with_teleost_par} have a teleost-level ({', '.join(sorted(levels))}) zebrafish paralogue; "
              f"{len(hits)} such paralogue pairs have their partner within {w/1e6:.1f} Mb of {tgt}:")
        for h in hits:
            print(f"- {h}")
        print(f"Of the teleost-level paralogue pairs, {len(chrom_hits)} have their partner anywhere on "
              f"chr{tloc[0]} (the chromosome of {tgt}, {len(target_chrom)} protein-coding genes):")
        for h in chrom_hits:
            print(f"- {h}")


def main():
    cfg = CONFIG
    print(f"# Pair analysis: {' / '.join(cfg['genes'])}  (run {time.strftime('%Y-%m-%d')})")
    zf, hs, orth = proteins(cfg)
    regions(cfg, zf, hs, orth)
    relative_rate(cfg, zf, orth)
    sys.stdout.flush()
    for step in (expression_timecourse, bgee, zfin, synteny):
        try:
            step(cfg)
        except Exception as e:  # noqa: BLE001  - report, do not invent
            print(f"\n[{step.__name__} failed: {type(e).__name__}: {e}]")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
