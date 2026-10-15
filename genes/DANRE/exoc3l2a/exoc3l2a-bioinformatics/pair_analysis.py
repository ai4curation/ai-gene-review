"""Paralog-pair analysis for zebrafish exoc3l2a / exoc3l2b (EXOC3/Sec6 family).

Question addressed first: which human gene are these two zebrafish genes orthologous
to?  ZFIN/Ensembl name them after EXOC3L2, whereas the PANTHER TGD pair table lists
EXOC3L4 as the human ortholog and PANTHER's HMM places them in TNFAIP2-named
subfamilies.  The script therefore compares the zebrafish proteins with every human
EXOC3-family member, and checks conserved synteny with human and gar.

Reproducible: reads the cached UniProt records for the two zebrafish proteins and
queries public services at run time (nothing is hardcoded apart from the two
zebrafish Ensembl gene ids and the human gene symbols to fetch):
  * UniProt REST  - human EXOC3 family proteins (reviewed entries) and their PANTHER
                    subfamily cross-references;
  * InterPro REST - Pfam Sec6 (PF06046) domain boundaries on human EXOC3L2;
  * Ensembl REST  - Compara homologies (paralogues, orthologues and duplication node),
                    canonical proteins of gar, medaka and zebrafish family members,
                    gene coordinates and neighbouring genes;
  * EBI Expression Atlas FTP - E-ERAD-475 (whole-embryo developmental time course);
  * Bgee REST     - expressed calls per anatomical entity (zebrafish copies and gar);
  * ZFIN download - wildtype-expression_fish.txt (curated expression rows).

Sections:
  0. Ensembl Compara homologies of the two zebrafish genes;
  1. pairwise global identities (Biopython PairwiseAligner, BLOSUM62, gap open -10 /
     extend -0.5; identity = identical columns / alignment length);
  2. identity inside and outside the Pfam Sec6 domain of human EXOC3L2, and the
     residues aligned to human EXOC3L2 Leu41 and Arg72 (sites of reported patient
     variants, PMID:30327448);
  3. Tajima-style relative-rate test (outgroup = gar);
  4. whole-embryo time course (E-ERAD-475 medians);
  5. Bgee calls (zebrafish copies + gar);
  6. ZFIN curated wild-type expression;
  7. synteny: teleost-level paralogues shared by the two neighbourhoods, and where the
     human and gar orthologues of the neighbours lie.

Run from the repo root:
    uv run python genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/pair_analysis.py \
        > genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/output.txt
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
ENSEMBL = "https://rest.ensembl.org"

CONFIG = {
    "genes": {
        "exoc3l2a": {"ens": "ENSDARG00000008414", "zfin": "ZDB-GENE-060526-343",
                     "uniprot_txt": "genes/DANRE/exoc3l2a/exoc3l2a-uniprot.txt"},
        "exoc3l2b": {"ens": "ENSDARG00000030782", "zfin": "ZDB-GENE-100728-5",
                     "uniprot_txt": "genes/DANRE/exoc3l2b/exoc3l2b-uniprot.txt"},
    },
    "human_symbols": ["EXOC3L2", "EXOC3L4", "TNFAIP2", "EXOC3L1", "EXOC3"],
    "human_ref": "EXOC3L2",
    "human_variant_sites": [41, 72],
    "pfam": "PF06046",
    "outgroup_species": {"lepisosteus_oculatus": "gar", "oryzias_latipes": "medaka",
                         "homo_sapiens": "human", "mus_musculus": "mouse"},
    "gar_species_id": 7918,
    "teleost_levels": ("Osteoglossocephalai", "Clupeocephala", "Teleostei"),
    "synteny_window_bp": 1_500_000,
    "human_window_bp": 5_000_000,
    "gar_window_bp": 5_000_000,
}


def get(url: str, retries: int = 10, data: bytes | None = None) -> bytes:
    for i in range(retries):
        try:
            req = urllib.request.Request(url, data=data, headers={
                "Content-Type": "application/json", "Accept": "application/json", **UA})
            return urllib.request.urlopen(req, timeout=180).read()
        except Exception:  # noqa: BLE001
            if i == retries - 1:
                raise
            time.sleep(3 + 4 * i)
    raise RuntimeError(url)


def ens_json(path: str):
    time.sleep(0.1)
    for i in range(6):
        raw = get(ENSEMBL + path + ("&" if "?" in path else "?") + "content-type=application/json")
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            time.sleep(5 + 5 * i)
    raise RuntimeError(path)


def ens_lookup_many(ids: list[str]) -> dict:
    out = {}
    for i in range(0, len(ids), 200):
        chunk = ids[i:i + 200]
        for k in range(6):
            raw = get(ENSEMBL + "/lookup/id", data=json.dumps({"ids": chunk}).encode())
            try:
                out.update(json.loads(raw))
                break
            except json.JSONDecodeError:
                time.sleep(5 + 5 * k)
    return out


def uniprot_txt_seq(path: Path) -> str:
    txt = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", txt, re.S | re.M)
    return re.sub(r"[\s\d]", "", m.group(1))


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
    print(f"\n## {t}\n", flush=True)


def homologies(gene_id: str):
    d = ens_json(f"/homology/id/danio_rerio/{gene_id}?sequence=none;format=condensed")
    return d["data"][0]["homologies"]


def compara(cfg):
    section("0. Ensembl Compara homologies of the two zebrafish genes")
    fam = {}
    orth = {}
    for g, v in cfg["genes"].items():
        hs = homologies(v["ens"])
        ids = [h["id"] for h in hs if h["species"] in ("danio_rerio", *cfg["outgroup_species"])]
        info = ens_lookup_many(ids)
        print(f"### {g} ({v['ens']})")
        for h in hs:
            sp = h["species"]
            if sp == "danio_rerio" or sp in cfg["outgroup_species"]:
                d = info.get(h["id"]) or {}
                name = d.get("display_name") or ""
                print(f"- {h['type']} {sp} {h['id']} {name} chr{d.get('seq_region_name')}:"
                      f"{d.get('start')} level={h.get('taxonomy_level')}")
                if sp == "danio_rerio" and h["id"] not in [x["ens"] for x in cfg["genes"].values()]:
                    fam[h["id"]] = name or h["id"]
                if sp in ("lepisosteus_oculatus", "oryzias_latipes"):
                    orth.setdefault(f"{cfg['outgroup_species'][sp]}_{h['id']}", (h["id"], g))
    return fam, orth


def proteins(cfg, fam, orth):
    zf = {g: uniprot_txt_seq(ROOT / v["uniprot_txt"]) for g, v in cfg["genes"].items()}
    q = " OR ".join(f"gene_exact:{s}" for s in cfg["human_symbols"])
    url = ("https://rest.uniprot.org/uniprotkb/search?query=" + urllib.request.quote(
        f"({q}) AND organism_id:9606 AND reviewed:true") + "&fields=accession,gene_primary,sequence,xref_panther&format=json")
    res = json.loads(get(url))["results"]
    hs, hs_acc = {}, {}
    section("1. Human EXOC3-family proteins (UniProt) and their PANTHER subfamilies")
    for r in res:
        sym = r["genes"][0]["geneName"]["value"]
        hs[sym] = r["sequence"]["value"]
        hs_acc[sym] = r["primaryAccession"]
        pan = [x["id"] for x in r.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"]
        print(f"- {sym} {r['primaryAccession']} {len(hs[sym])} aa; PANTHER {', '.join(pan)}")
    others = {}
    for k, (gid, _) in orth.items():
        others[k] = ensembl_canonical_protein(gid)
    for gid, name in fam.items():
        others[f"zf_{name}"] = ensembl_canonical_protein(gid)
    section("1b. Pairwise identities")
    for k, v in {**zf, **hs, **others}.items():
        print(f"length {k}: {len(v)} aa")
    pid, cols = identity(zf["exoc3l2a"], zf["exoc3l2b"])
    print(f"\nidentity exoc3l2a vs exoc3l2b: {pid:.1f}% over {cols} columns\n")
    print("| protein | exoc3l2a | exoc3l2b |")
    print("|---|---|---|")
    for k, v in {**hs, **others}.items():
        row = []
        for g in zf:
            p, c = identity(zf[g], v)
            row.append(f"{p:.1f}% ({c})")
        print(f"| {k} | " + " | ".join(row) + " |")
    print("\nOutgroup proteins vs human family members (identity %):")
    print("| outgroup | " + " | ".join(hs) + " |")
    print("|---|" + "---|" * len(hs))
    for k, v in others.items():
        print(f"| {k} | " + " | ".join(f"{identity(v, s)[0]:.1f}" for s in hs.values()) + " |")
    return zf, hs, hs_acc, others


def regions(cfg, zf, hs, hs_acc, others, gar_key):
    section("2. Identity inside/outside the Pfam Sec6 domain of human EXOC3L2; patient-variant sites")
    ref = hs[cfg["human_ref"]]
    acc = hs_acc[cfg["human_ref"]]
    d = json.loads(get(f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{cfg['pfam']}/protein/uniprot/{acc}"))
    frags = d["proteins"][0]["entry_protein_locations"][0]["fragments"]
    s, e = frags[0]["start"], frags[-1]["end"]
    print(f"Pfam {cfg['pfam']} on human {cfg['human_ref']} ({acc}): {s}-{e}")
    seqs = {**zf}
    if gar_key:
        seqs[gar_key] = others[gar_key]
    for k, v in seqs.items():
        m = pos_map(ref, v)
        for label, a, b in (("N-terminal (before Sec6)", 1, s - 1), ("Sec6 domain", s, e),
                            ("C-terminal (after Sec6)", e + 1, len(ref))):
            n = b - a + 1
            if n <= 0:
                continue
            aligned = sum(1 for p in range(a, b + 1) if m.get(p))
            same = sum(1 for p in range(a, b + 1) if m.get(p) == ref[p - 1])
            print(f"{label} [{a}-{b}] {k}: aligned {aligned}/{n}, identical {same}/{n} ({100*same/n:.1f}%)")
        sites = ", ".join(f"{ref[p-1]}{p}->{m.get(p)}" for p in cfg["human_variant_sites"])
        print(f"human {cfg['human_ref']} residues {sites} in {k}")


def relative_rate(zf, gar):
    section("3. Tajima-style relative-rate test (outgroup = gar)")
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


def bgee(cfg, gar_id):
    section("5. Bgee expressed calls per anatomical entity (expression score 0-100; only 'expressed' calls are returned)")
    tables = {g: bgee_calls(v["ens"], 7955) for g, v in cfg["genes"].items()}
    if gar_id:
        try:
            tables[f"gar {gar_id}"] = bgee_calls(gar_id, cfg["gar_species_id"])
        except Exception as ex:  # noqa: BLE001
            print(f"gar Bgee query failed: {ex}")
    for k, calls in tables.items():
        print(f"### {k}: {len(calls)} calls")
        for name, score, qual, dt in calls:
            print(f"- {name}: {score:.1f} ({qual}; {dt})")
    zf = list(cfg["genes"])
    a = {n for n, *_ in tables[zf[0]]}
    b = {n for n, *_ in tables[zf[1]]}
    print(f"\nentities with a call for {zf[0]} only: {sorted(a - b)}")
    print(f"entities with a call for {zf[1]} only: {sorted(b - a)}")
    print(f"entities with a call for both: {sorted(a & b)}")


def zfin(cfg):
    section("6. ZFIN curated wild-type expression (wildtype-expression_fish.txt)")
    txt = get("https://zfin.org/downloads/wildtype-expression_fish.txt").decode(errors="replace")
    for g, v in cfg["genes"].items():
        rows = [ln.split("\t") for ln in txt.splitlines() if ln.startswith(v["zfin"] + "\t")]
        print(f"### {g} ({v['zfin']}): {len(rows)} rows")
        for f in rows:
            sub = f" ({f[6]})" if len(f) > 6 and f[6] else ""
            print(f"- {f[4]}{sub}; {f[7]} to {f[8]}; {f[9]}; {f[11]}")


def genes_near(species: str, chrom: str, start: int, end: int):
    d = ens_json(f"/overlap/region/{species}/{chrom}:{max(1, start)}-{end}?feature=gene;biotype=protein_coding")
    return [(x["id"], x.get("external_name"), x["start"]) for x in d]


def synteny(cfg, gar_id):
    section("7. Synteny (Ensembl REST)")
    w = cfg["synteny_window_bp"]
    info = ens_lookup_many([v["ens"] for v in cfg["genes"].values()])
    loc = {}
    for g, v in cfg["genes"].items():
        d = info[v["ens"]]
        loc[g] = (d["seq_region_name"], d["start"], d["end"])
        print(f"{g}: chr{d['seq_region_name']}:{d['start']}-{d['end']}")
    hs_ids = {}
    for sym in ("EXOC3L2", "EXOC3L4", "TNFAIP2"):
        x = ens_json(f"/xrefs/symbol/homo_sapiens/{sym}?")
        gid = [y["id"] for y in x if y["type"] == "gene" and y["id"].startswith("ENSG")][0]
        hs_ids[sym] = gid
    hinfo = ens_lookup_many(list(hs_ids.values()) + ([gar_id] if gar_id else []))
    hloc = {s: (hinfo[i]["seq_region_name"], hinfo[i]["start"]) for s, i in hs_ids.items()}
    for s, (c, p) in hloc.items():
        print(f"human {s}: chr{c}:{p}")
    gloc = (hinfo[gar_id]["seq_region_name"], hinfo[gar_id]["start"]) if gar_id else None
    if gloc:
        print(f"gar ortholog {gar_id}: {gloc[0]}:{gloc[1]}")

    neigh = {}
    for g, (c, s, e) in loc.items():
        neigh[g] = [n for n in genes_near("danio_rerio", c, s - w, e + w) if n[0] != cfg["genes"][g]["ens"]]

    def hom(gid):
        try:
            return homologies(gid)
        except Exception:  # noqa: BLE001
            return None

    allids = sorted({n[0] for v in neigh.values() for n in v})
    with ThreadPoolExecutor(max_workers=4) as ex:
        homs = dict(zip(allids, ex.map(hom, allids)))
    partner_ids = set()
    for hs_ in homs.values():
        for h in hs_ or []:
            if h["species"] in ("homo_sapiens", "lepisosteus_oculatus"):
                partner_ids.add(h["id"])
    pinfo = ens_lookup_many(sorted(partner_ids))
    names = {n[0]: n[1] for v in neigh.values() for n in v}
    ga, gb = list(cfg["genes"])
    for src, tgt in ((ga, gb), (gb, ga)):
        tc = loc[tgt][0]
        failed = sum(1 for n in neigh[src] if homs.get(n[0]) is None)
        print(f"\n### Neighbours of {src} (+/- {w/1e6:.1f} Mb): {len(neigh[src])} protein-coding genes "
              f"({failed} homology queries failed)")
        par_hits, near_hs, near_gar = [], {s: [] for s in hloc}, []
        for gid, name, _ in neigh[src]:
            for h in homs.get(gid) or []:
                if h["species"] == "danio_rerio" and h.get("taxonomy_level") in cfg["teleost_levels"]:
                    tg = h["id"]
                    d = ens_lookup_many([tg]).get(tg) or {}
                    if d.get("seq_region_name") == tc:
                        dist = min(abs(d["start"] - loc[tgt][1]), abs(d["start"] - loc[tgt][2]))
                        par_hits.append(f"{name or gid} -> {d.get('display_name') or tg} "
                                        f"(chr{tc}:{d['start']}, {dist/1e6:.2f} Mb from {tgt}; level {h['taxonomy_level']})")
                if h["species"] == "homo_sapiens":
                    d = pinfo.get(h["id"]) or {}
                    for s, (c, p) in hloc.items():
                        if d.get("seq_region_name") == c and abs(d["start"] - p) <= cfg["human_window_bp"]:
                            near_hs[s].append(f"{name or gid} -> {d.get('display_name')} ({(d['start']-p)/1e6:+.2f} Mb)")
                if h["species"] == "lepisosteus_oculatus" and gloc:
                    d = pinfo.get(h["id"]) or {}
                    if d.get("seq_region_name") == gloc[0] and abs(d["start"] - gloc[1]) <= cfg["gar_window_bp"]:
                        near_gar.append(f"{name or gid} -> {d.get('display_name') or h['id']} ({(d['start']-gloc[1])/1e6:+.2f} Mb)")
        print(f"Teleost-level zebrafish paralogues of these neighbours that lie on chr{tc} (chromosome of {tgt}):")
        for x in par_hits or ["(none)"]:
            print(f"- {x}")
        for s in hloc:
            print(f"Neighbours whose human orthologue lies within {cfg['human_window_bp']/1e6:.0f} Mb of human {s}: "
                  f"{len(set(near_hs[s]))}")
            for x in sorted(set(near_hs[s])):
                print(f"- {x}")
        print(f"Neighbours whose gar orthologue lies within {cfg['gar_window_bp']/1e6:.0f} Mb of gar {gar_id}: "
              f"{len(set(near_gar))}")
        for x in sorted(set(near_gar)):
            print(f"- {x}")


def main():
    cfg = CONFIG
    print(f"# Pair analysis: {' / '.join(cfg['genes'])}  (run {time.strftime('%Y-%m-%d')})")
    fam, orth = compara(cfg)
    zf, hs, hs_acc, others = proteins(cfg, fam, orth)
    gar_keys = [k for k in orth if k.startswith("gar_")]
    gar_key = gar_keys[0] if len(gar_keys) == 1 else None
    gar_id = orth[gar_key][0] if gar_key else None
    regions(cfg, zf, hs, hs_acc, others, gar_key)
    if gar_key:
        relative_rate(zf, others[gar_key])
    expression_timecourse(cfg)
    bgee(cfg, gar_id)
    zfin(cfg)
    synteny(cfg, gar_id)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
