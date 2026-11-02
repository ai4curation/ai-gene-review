"""Paralog-pair analysis for a zebrafish ohnolog pair (protein, targeting signals, expression, synteny).

Usage (from the repo root):
    uv run python genes/DANRE/agxta/agxta-bioinformatics/pair_analysis.py agxt \
        > genes/DANRE/agxta/agxta-bioinformatics/output.txt
    uv run python genes/DANRE/slc7a10a/slc7a10a-bioinformatics/pair_analysis.py slc7a10 \
        > genes/DANRE/slc7a10a/slc7a10a-bioinformatics/output.txt

Everything is fetched at run time (nothing is hardcoded apart from the query identifiers):
  * zebrafish proteins: the cached UniProt records in genes/DANRE/<gene>/<gene>-uniprot.txt;
  * UniProt REST: the human reference protein and its annotated sites;
  * Ensembl REST (Compara): orthologues of each zebrafish copy in a panel of species
    (their Compara member proteins), the paralogue call between the two copies,
    transcript structure / 5' flanking sequence (upstream in-frame ATG check), and local synteny;
  * EBI Expression Atlas FTP: E-ERAD-475 (White et al. 2017 developmental time course, TPM);
  * Bgee REST: expressed calls per anatomical entity (zebrafish copies and spotted gar ortholog);
  * ZFIN: wild-type expression download (curated anatomy terms).

Global alignments: Biopython PairwiseAligner, BLOSUM62, gap open -10 / extend -0.5;
identity = identical columns / alignment length.
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
from Bio.Seq import Seq

ROOT = Path(__file__).resolve().parents[4]

CONFIGS = {
    "agxt": {
        "genes": {
            "agxta": {"ens": "ENSDARG00000052099", "uniprot_txt": "genes/DANRE/agxta/agxta-uniprot.txt"},
            "agxtb": {"ens": "ENSDARG00000018478", "uniprot_txt": "genes/DANRE/agxtb/agxtb-uniprot.txt"},
        },
        "human": {"AGXT": "P21549"},
        "human_ref": "AGXT",
        # UniProt feature types of the human reference whose positions are checked for conservation
        "feature_types": ["Binding site", "Modified residue", "Active site"],
        "extra_sites": [],
        "targeting": True,  # N-terminal extension (MTS-like) and C-terminal PTS1 analysis
        "upstream_atg": True,
    },
    "slc7a10": {
        "genes": {
            "slc7a10a": {"ens": "ENSDARG00000008100", "uniprot_txt": "genes/DANRE/slc7a10a/slc7a10a-uniprot.txt"},
            "slc7a10b": {"ens": "ENSDARG00000051730", "uniprot_txt": "genes/DANRE/slc7a10b/slc7a10b-uniprot.txt"},
        },
        "human": {"SLC7A10": "Q9NS82", "SLC7A5": "Q01650", "SLC7A8": "Q9UHI5"},
        "human_ref": "SLC7A10",
        "feature_types": ["Binding site", "Modified residue", "Disulfide bond", "Glycosylation"],
        # residues of human Asc-1 tested by mutagenesis in the cryo-EM study (PMID:38589439),
        # plus Cys154 (disulfide to 4F2hc/SLC3A2)
        "extra_sites": [52, 131, 138, 154, 243, 250, 253, 257, 333, 339],
        "targeting": False,
        "upstream_atg": False,
    },
}

SPECIES = [
    "lepisosteus_oculatus", "amia_calva", "latimeria_chalumnae", "xenopus_tropicalis", "gallus_gallus",
    "homo_sapiens", "mus_musculus", "scleropages_formosus", "clupea_harengus", "astyanax_mexicanus",
    "esox_lucius", "salmo_salar", "gadus_morhua", "oryzias_latipes", "gasterosteus_aculeatus",
    "takifugu_rubripes", "oreochromis_niloticus",
]
TELEOSTS = {"scleropages_formosus", "clupea_harengus", "astyanax_mexicanus", "esox_lucius", "salmo_salar",
            "gadus_morhua", "oryzias_latipes", "gasterosteus_aculeatus", "takifugu_rubripes",
            "oreochromis_niloticus"}

ENSEMBL = "https://rest.ensembl.org"
UA = {"User-Agent": "ai-gene-review-pair-analysis/1.0"}


def get(url: str, retries: int = 10, json_headers: bool = False) -> bytes:
    for i in range(retries):
        try:
            h = dict(UA)
            if json_headers:
                h["Content-Type"] = "application/json"
            data = urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=180).read()
            if json_headers and data.lstrip()[:1] not in (b"{", b"["):
                raise ValueError("non-JSON response")
            return data
        except Exception:  # noqa: BLE001
            if i == retries - 1:
                raise
            time.sleep(5 + 6 * i)
    raise RuntimeError(url)


def ens_json(path: str):
    time.sleep(0.1)
    sep = "&" if "?" in path else "?"
    return json.loads(get(ENSEMBL + path + sep + "content-type=application/json", json_headers=True))


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


def uniprot_json(acc: str):
    return json.loads(get(f"https://rest.uniprot.org/uniprotkb/{acc}?format=json"))


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
    """map 1-based positions of a to the aligned residue of b (None = gap)."""
    x = aln(a, b)
    m, i = {}, 0
    for p, q in zip(x[0], x[1]):
        if p != "-":
            i += 1
            m[i] = None if q == "-" else q
    return m


AL_FREE_ENDS = Align.PairwiseAligner(mode="global")
AL_FREE_ENDS.substitution_matrix = substitution_matrices.load("BLOSUM62")
AL_FREE_ENDS.open_gap_score = -10
AL_FREE_ENDS.extend_gap_score = -0.5
AL_FREE_ENDS.end_open_gap_score = 0
AL_FREE_ENDS.end_extend_gap_score = 0


def n_extension(seq: str, ref: str) -> int:
    """residues of seq before the first residue aligned to ref residue 1 (end gaps free, so a
    leading extension is not forced into an alignment with the reference N-terminus)."""
    x = AL_FREE_ENDS.align(seq, ref)[0]
    lead = 0
    for p, q in zip(x[0], x[1]):
        if q != "-":
            break
        if p != "-":
            lead += 1
    return lead


EISENBERG = {"A": 0.62, "R": -2.53, "N": -0.78, "D": -0.90, "C": 0.29, "Q": -0.85, "E": -0.74, "G": 0.48,
             "H": -0.40, "I": 1.38, "L": 1.06, "K": -1.50, "M": 0.64, "F": 1.19, "P": 0.12, "S": -0.18,
             "T": -0.05, "W": 0.81, "Y": 0.26, "V": 1.08}


def max_hydrophobic_moment(seq: str, window: int = 18, angle: float = 100.0) -> float:
    import math
    best = 0.0
    for s in range(0, max(1, len(seq) - window + 1)):
        w = seq[s:s + window]
        x = sum(EISENBERG.get(a, 0) * math.cos(math.radians(angle * i)) for i, a in enumerate(w))
        y = sum(EISENBERG.get(a, 0) * math.sin(math.radians(angle * i)) for i, a in enumerate(w))
        best = max(best, math.hypot(x, y) / len(w))
    return best


def mts_features(seg: str) -> str:
    if not seg:
        return "none"
    pos = sum(seg.count(c) for c in "RK")
    neg = sum(seg.count(c) for c in "DE")
    return (f"{seg} (len {len(seg)}; R+K {pos}, D+E {neg}, net {pos - neg:+d}; "
            f"max 18-aa hydrophobic moment {max_hydrophobic_moment(seg):.2f})")


def section(t: str):
    print(f"\n## {t}\n")
    sys.stdout.flush()


def homologies(gene_id: str, kind: str):
    d = ens_json(f"/homology/id/danio_rerio/{gene_id}?type={kind};sequence=protein;aligned=0")
    return d["data"][0]["homologies"]


def collect(cfg):
    zf = {g: uniprot_txt_seq(ROOT / v["uniprot_txt"]) for g, v in cfg["genes"].items()}
    hs = {}
    hs_json = {}
    for name, acc in cfg["human"].items():
        j = uniprot_json(acc)
        hs[name] = j["sequence"]["value"]
        hs_json[name] = j
    orth = {}  # key -> dict
    for g, v in cfg["genes"].items():
        for h in homologies(v["ens"], "orthologues"):
            t = h["target"]
            if t["species"] not in SPECIES:
                continue
            key = t["protein_id"]
            rec = orth.setdefault(key, {"species": t["species"], "gene": t["id"], "protein": t["protein_id"],
                                        "seq": t["seq"].replace("-", ""), "of": {}})
            rec["of"][g] = h["type"]
    par = {}
    genes = list(cfg["genes"])
    for h in homologies(cfg["genes"][genes[0]]["ens"], "paralogues"):
        if h["target"]["id"] == cfg["genes"][genes[1]]["ens"]:
            par = {"type": h["type"], "taxonomy_level": h.get("taxonomy_level"),
                   "identity_a": h["source"].get("perc_id"), "identity_b": h["target"].get("perc_id")}
    return zf, hs, hs_json, orth, par


def report_orthologs(cfg, zf, hs, orth, par):
    section("1. Ensembl Compara: paralogue call and orthologues")
    genes = list(cfg["genes"])
    if par:
        print(f"{genes[0]} / {genes[1]}: Compara type {par['type']}, duplication node {par['taxonomy_level']}, "
              f"%id {par['identity_a']} / {par['identity_b']}")
    else:
        print(f"{genes[0]} / {genes[1]}: no paralogue relation returned by Compara")
    print("\n| species | Ensembl gene | protein | length | orthology to " + " | ".join(genes) + " |")
    print("|---|---|---|---|" + "---|" * len(genes))
    for k, r in sorted(orth.items(), key=lambda kv: SPECIES.index(kv[1]["species"])):
        print(f"| {r['species']} | {r['gene']} | {k} | {len(r['seq'])} | "
              + " | ".join(r["of"].get(g, "-") for g in genes) + " |")

    section("2. Pairwise identities")
    ref = hs[cfg["human_ref"]]
    for g, s in zf.items():
        print(f"length {g}: {len(s)} aa")
    for n, s in hs.items():
        print(f"length human {n}: {len(s)} aa")
    pid, cols = identity(zf[genes[0]], zf[genes[1]])
    print(f"identity {genes[0]} vs {genes[1]}: {pid:.1f}% over {cols} columns")
    for g, s in zf.items():
        for n, h in hs.items():
            pid, cols = identity(s, h)
            print(f"identity {g} vs human {n}: {pid:.1f}% over {cols} columns")
    gar = [r for r in orth.values() if r["species"] == "lepisosteus_oculatus"]
    for r in gar:
        for g, s in zf.items():
            pid, cols = identity(s, r["seq"])
            print(f"identity {g} vs gar {r['gene']} ({len(r['seq'])} aa): {pid:.1f}% over {cols} columns")
        pid, cols = identity(ref, r["seq"])
        print(f"identity human {cfg['human_ref']} vs gar {r['gene']}: {pid:.1f}% over {cols} columns")
    return gar


def sites(cfg, zf, hs, hs_json, orth):
    section("3. Conservation of annotated sites of the human reference")
    ref_name = cfg["human_ref"]
    ref = hs[ref_name]
    feats = []
    for f in hs_json[ref_name].get("features", []):
        if f["type"] in cfg["feature_types"]:
            s = f["location"]["start"]["value"]
            e = f["location"]["end"]["value"]
            desc = f.get("description") or (f.get("ligand", {}) or {}).get("name", "")
            for p in ([s, e] if f["type"] == "Disulfide bond" else range(s, e + 1)):
                feats.append((p, f"{f['type']}: {desc}"))
    for p in cfg["extra_sites"]:
        feats.append((p, "site tested in literature (see config)"))
    panel = dict(zf)
    for r in orth.values():
        if r["species"] in ("lepisosteus_oculatus", "oryzias_latipes", "latimeria_chalumnae"):
            panel[f"{r['species'].split('_')[0]}:{r['gene']}"] = r["seq"]
    maps = {k: pos_map(ref, v) for k, v in panel.items()}
    print("| human position | annotation | " + " | ".join(panel) + " |")
    print("|---|---|" + "---|" * len(panel))
    seen = set()
    for p, d in sorted(feats):
        if (p, d) in seen or p > len(ref):
            continue
        seen.add((p, d))
        print(f"| {ref[p-1]}{p} | {d} | " + " | ".join(str(maps[k].get(p) or "-") for k in panel) + " |")


def targeting(cfg, zf, hs, orth):
    section("4. Targeting signals: N-terminal extension before human Met1, and C-terminal tripeptide (PTS1)")
    ref = hs[cfg["human_ref"]]
    rows = [(g, "danio_rerio", s, "-") for g, s in zf.items()]
    for r in sorted(orth.values(), key=lambda r: SPECIES.index(r["species"])):
        rows.append((r["gene"], r["species"], r["seq"], ",".join(f"{k}:{v}" for k, v in r["of"].items())))
    rows.append((cfg["human_ref"] + " (UniProt)", "homo_sapiens", ref, "-"))
    print("PTS1 consensus for reference: C-terminal [SAC]-[KRH]-[LM]; human AGXT ends KKL.")
    print("| gene | species | length | N-ext before human Met1 | C-term 3 | orthology |")
    print("|---|---|---|---|---|---|")
    for name, sp, s, o in rows:
        ext = n_extension(s, ref)
        print(f"| {name} | {sp} | {len(s)} | {ext} | {s[-3:]} | {o} |")
    print("\nFirst 45 residues of each sequence:")
    for name, sp, s, o in rows:
        print(f"- {name} ({sp}): {s[:45]}")
    print("\nN-terminal extensions (composition; MTS are typically Arg-rich, acid-poor amphipathic helices):")
    for name, sp, s, o in rows:
        ext = n_extension(s, ref)
        if ext >= 10:
            print(f"- {name} ({sp}): {mts_features(s[:ext])}")


def upstream_atg(cfg):
    section("5. Upstream in-frame ATG check (5' of the annotated start codon)")
    print("For each zebrafish gene and for human AGXT: 5' UTR of the Ensembl canonical transcript and "
          "300 nt of genomic sequence 5' of the start codon, read in frame with the CDS back to the "
          "first in-frame stop. An in-frame ATG in this stretch could encode an N-terminal extension "
          "(as for the mammalian AGXT 'ATG1' that encodes the MTS).")
    targets = [(g, v["ens"], "danio_rerio") for g, v in cfg["genes"].items()]
    targets.append(("human AGXT", None, "homo_sapiens"))
    for name, gid, sp in targets:
        if gid is None:
            gid = ens_json("/lookup/symbol/homo_sapiens/AGXT?")["id"]
        d = ens_json(f"/lookup/id/{gid}?expand=1")
        trs = [t for t in d["Transcript"] if t.get("Translation")]
        canon = [t for t in trs if t.get("is_canonical")] or trs
        print(f"\n### {name} ({gid}); protein-coding transcripts: "
              + ", ".join(f"{t['id']} ({t['Translation']['length']} aa{', canonical' if t.get('is_canonical') else ''})"
                          for t in trs))
        t = canon[0]
        cdna = get(f"{ENSEMBL}/sequence/id/{t['id']}?type=cdna;content-type=text/plain").decode().strip()
        cds = get(f"{ENSEMBL}/sequence/id/{t['id']}?type=cds;content-type=text/plain").decode().strip()
        i = cdna.find(cds[:60])
        utr = cdna[:i] if i >= 0 else ""
        print(f"canonical {t['id']}: 5' UTR length {len(utr)} nt; CDS starts {cds[:3]}")
        for label, seq in (("5' UTR", utr), ("genomic 300 nt", None)):
            if seq is None:
                tr = t["Translation"]
                strand = t["strand"]
                if strand == 1:
                    s, e = tr["start"] - 300, tr["start"] - 1
                else:
                    s, e = tr["end"] + 1, tr["end"] + 300
                seq = get(f"{ENSEMBL}/sequence/region/{sp}/{t['seq_region_name']}:{s}..{e}:{strand}"
                          f"?content-type=text/plain").decode().strip()
            # read codons backwards from the start codon
            codons = []
            k = len(seq)
            while k >= 3:
                codons.append(seq[k - 3:k].upper())
                k -= 3
            upstream_atgs, stop_at = [], None
            for n, c in enumerate(codons, start=1):
                if c in ("TAA", "TAG", "TGA"):
                    stop_at = n
                    break
                if c == "ATG":
                    upstream_atgs.append(n)
            aa = str(Seq("".join(reversed(codons[:(stop_at - 1) if stop_at else len(codons)]))).translate())
            print(f"- {label}: first in-frame stop {stop_at if stop_at else 'not reached'} codons upstream; "
                  f"in-frame ATG(s) before it at codon(s) {upstream_atgs or 'none'} upstream; "
                  f"open upstream peptide (translated) '{aa}'")


def relative_rate(cfg, zf, gar):
    section("6. Tajima-style relative-rate test (outgroup = gar)")
    if not gar:
        print("no gar orthologue returned")
        return
    g = gar[0]["seq"]
    (na, a), (nb, b) = list(zf.items())
    ma, mb = pos_map(g, a), pos_map(g, b)
    m1 = m2 = shared = 0
    for p in range(1, len(g) + 1):
        ra, rb, rg = ma.get(p), mb.get(p), g[p - 1]
        if ra is None or rb is None:
            continue
        shared += 1
        if ra != rg and rb == rg:
            m1 += 1
        elif rb != rg and ra == rg:
            m2 += 1
    chi = (m1 - m2) ** 2 / (m1 + m2) if (m1 + m2) else 0.0
    print(f"gar {gar[0]['gene']} positions aligned in both copies: {shared}")
    print(f"changes unique to {na} (m1): {m1}; unique to {nb} (m2): {m2}; chi2 (1 df) = {chi:.2f}"
          f" ({'P<0.05' if chi > 3.841 else 'not significant at 0.05'})")


def expression_timecourse(cfg):
    section("7. Whole-embryo time course, E-ERAD-475 (TPM, median of replicates)")
    base = "https://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/experiments/E-ERAD-475/"
    conf = get(base + "E-ERAD-475-configuration.xml").decode()
    labels = dict(re.findall(r'<assay_group id="([^"]+)" label="([^"]+)"', conf))
    order = re.findall(r'<assay_group id="([^"]+)"', conf)
    want = {v["ens"]: g for g, v in cfg["genes"].items()}
    rows = {}
    with urllib.request.urlopen(urllib.request.Request(base + "E-ERAD-475-tpms.tsv", headers=UA), timeout=300) as fh:
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


def bgee(cfg, gar):
    section("8. Bgee expressed calls per anatomical entity (score 0-100; only 'expressed' calls are returned)")
    tables = {g: bgee_calls(v["ens"], 7955) for g, v in cfg["genes"].items()}
    for r in gar:
        try:
            tables[f"gar {r['gene']}"] = bgee_calls(r["gene"], 7918)
        except Exception as e:  # noqa: BLE001
            print(f"gar Bgee query failed: {e}")
    for k, calls in tables.items():
        print(f"### {k}: {len(calls)} calls")
        for name, score, qual, dt in sorted(calls, key=lambda c: -c[1]):
            print(f"- {name}: {score:.1f} ({qual}; {dt})")
    zf = list(cfg["genes"])
    a = {n: s for n, s, _, dt in tables[zf[0]] if "RNA-Seq" in dt}
    b = {n: s for n, s, _, dt in tables[zf[1]] if "RNA-Seq" in dt}
    print(f"\nRNA-Seq-supported entities, {zf[0]} only: {sorted(set(a) - set(b))}")
    print(f"RNA-Seq-supported entities, {zf[1]} only: {sorted(set(b) - set(a))}")
    both = sorted(set(a) & set(b))
    print(f"RNA-Seq-supported entities, both: {both}")
    print("\nScore comparison in shared RNA-Seq entities (score difference >= 10 flagged):")
    for n in both:
        flag = " <--" if abs(a[n] - b[n]) >= 10 else ""
        print(f"- {n}: {zf[0]} {a[n]:.1f} vs {zf[1]} {b[n]:.1f}{flag}")


def zfin(cfg):
    section("9. ZFIN curated wild-type expression")
    text = get("https://zfin.org/downloads/wildtype-expression_fish.txt").decode("utf-8", errors="replace")
    recs = {g: set() for g in cfg["genes"]}
    for row in csv.reader(io.StringIO(text), delimiter="\t"):
        if len(row) > 11 and row[1] in recs:
            anat = row[4] + (f" > {row[6]}" if row[6] else "")
            recs[row[1]].add((anat, row[7], row[9], row[11]))
    for g, rs in recs.items():
        print(f"### {g}: {len(rs)} records")
        for r in sorted(rs):
            print("- " + " | ".join(r))


def genes_near(chrom: str, start: int, end: int):
    d = ens_json(f"/overlap/region/danio_rerio/{chrom}:{max(1, start)}-{end}?feature=gene;biotype=protein_coding")
    return [(x["id"], x.get("external_name"), x["start"]) for x in d]


def synteny(cfg, window: int = 1_500_000):
    section("10. Local synteny between the two copies (Ensembl REST)")
    loc = {}
    for g, v in cfg["genes"].items():
        d = ens_json(f"/lookup/id/{v['ens']}?")
        loc[g] = (d["seq_region_name"], d["start"], d["end"])
        print(f"{g}: chr{d['seq_region_name']}:{d['start']}-{d['end']}")
    (ga, la), (gb, lb) = list(loc.items())

    def teleost_paralogues(gid):
        try:
            h = ens_json(f"/homology/id/danio_rerio/{gid}?type=paralogues;sequence=none;format=condensed")
        except Exception:  # noqa: BLE001
            return None
        return [x["id"] for x in h["data"][0]["homologies"]
                if x.get("taxonomy_level") in ("Clupeocephala", "Osteoglossocephalai", "Teleostei")]

    for src, sloc, tgt, tloc in ((ga, la, gb, lb), (gb, lb, ga, la)):
        neigh = [n for n in genes_near(sloc[0], sloc[1] - window, sloc[2] + window)
                 if n[0] != cfg["genes"][src]["ens"]]
        target_window = {gid: (name, start) for gid, name, start in genes_near(tloc[0], tloc[1] - window, tloc[2] + window)}
        with ThreadPoolExecutor(max_workers=3) as ex:
            results = list(ex.map(teleost_paralogues, [n[0] for n in neigh]))
        hits, failed, with_par = [], 0, 0
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
        print(f"\n{src} +/- {window/1e6:.1f} Mb: {len(neigh)} other protein-coding genes ({failed} homology "
              f"queries failed); {with_par} have a teleost-level (Teleostei/Osteoglossocephalai/Clupeocephala) "
              f"zebrafish paralogue; {len(hits)} of those paralogues lie within {window/1e6:.1f} Mb of {tgt}:")
        for h in hits:
            print(f"- {h}")


def main():
    cfg = CONFIGS[sys.argv[1]]
    print(f"# Pair analysis: {' / '.join(cfg['genes'])}  (run {time.strftime('%Y-%m-%d')})")
    zf, hs, hs_json, orth, par = collect(cfg)
    gar = report_orthologs(cfg, zf, hs, orth, par)
    sites(cfg, zf, hs, hs_json, orth)
    if cfg["targeting"]:
        targeting(cfg, zf, hs, orth)
    if cfg["upstream_atg"]:
        upstream_atg(cfg)
    relative_rate(cfg, zf, gar)
    expression_timecourse(cfg)
    bgee(cfg, gar)
    zfin(cfg)
    synteny(cfg)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
