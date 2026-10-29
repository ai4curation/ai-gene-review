"""Double-conserved synteny test for a zebrafish paralog pair against spotted gar.

A pair of zebrafish genes that arose in the teleost genome duplication (TGD)
should sit in two zebrafish regions that are both orthologous to the single
region around the gar (unduplicated outgroup) gene. This script:

  1. lists protein-coding genes within +/- WINDOW of each zebrafish copy and of
     the gar gene (Ensembl REST /overlap; GRCz11 and LepOcu1);
  2. takes zebrafish-gar orthology from PANTHER v19 (AllOrthologs, the same
     release used for projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv), mapping
     PANTHER's zebrafish identifiers (Ensembl=, ZFIN=, Gene=) to Ensembl genes
     through ZFIN's ensembl_1_to_1 file, the ZFIN accession in the Ensembl gene
     description, ZFIN gene.txt (NCBI LOC placeholders), or the gene symbol;
  3. reports, for each zebrafish window, which neighbours have a gar ortholog
     inside the gar window, and which gar-window genes have orthologs in BOTH
     zebrafish windows (double-conserved synteny: each such gene is itself a
     retained ohnolog pair from the same duplicated block).

It also asks Ensembl Compara (REST /homology) how it classifies the focal
pair, as an independent gene-tree view; if Ensembl is unavailable that line
says so.

The first run streams PANTHER AllOrthologs.tar.gz (~1 GB compressed) once and
caches the zebrafish-gar pairs as danre_lepoc_orthologs.tsv next to it.

Usage (from the repository root):
    uv run python <this script> ZF_GENE_A ZF_GENE_B GAR_GENE [--window 1500000] \
        [--panther-dir projects/DANRE_DUPLICATION/.cache]
The same script is kept in two gene folders. Runs used in this repository:
  si:dkey-283b1.7 / vwc2 (gar vwc2):
    ... synteny.py ENSDARG00000053460 ENSDARG00000076495 ENSLOCG00000005007
  magi3b (LOC564220) / wu:fi36a10 (gar magi3):
    ... synteny.py ENSDARG00000025974 ENSDARG00000101869 ENSLOCG00000010996
"""

import argparse
import csv
import io
import json
import re
import tarfile
import time
import urllib.error
import urllib.request
from pathlib import Path

SERVER = "https://rest.ensembl.org"
PANTHER_URL = "https://data.pantherdb.org/ftp/ortholog/current_release/AllOrthologs.tar.gz"
ZFIN_ENSEMBL = "https://zfin.org/downloads/ensembl_1_to_1.txt"
ZFIN_GENES = "https://zfin.org/downloads/gene.txt"


def get(path: str, tries: int = 4) -> dict | list:
    url = SERVER + path + ("&" if "?" in path else "?") + "content-type=application/json"
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return json.loads(r.read())
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            if attempt < tries - 1:
                time.sleep(3 * (attempt + 1))
                continue
            raise
    raise RuntimeError(url)


def window_genes(species: str, chrom: str, start: int, end: int) -> list[dict]:
    genes = get(f"/overlap/region/{species}/{chrom}:{max(1, start)}-{end}?feature=gene")
    return [g for g in genes if g.get("biotype") == "protein_coding"]


def danre_lepoc_pairs(panther_dir: Path) -> list[tuple[str, str]]:
    cache = panther_dir / "danre_lepoc_orthologs.tsv"
    if not cache.exists():
        tar_path = panther_dir / "AllOrthologs.tar.gz"
        if not tar_path.exists():
            panther_dir.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(PANTHER_URL, tar_path)
        rows = []
        with tarfile.open(tar_path, "r:gz") as tf:
            for member in tf:
                fh = tf.extractfile(member)
                if fh is None:
                    continue
                for raw in fh:
                    if b"DANRE|" not in raw or b"LEPOC|" not in raw:
                        continue
                    a, b = raw.decode().split("\t")[:2]
                    if a.startswith("DANRE|") and b.startswith("LEPOC|"):
                        rows.append((a, b))
                    elif b.startswith("DANRE|") and a.startswith("LEPOC|"):
                        rows.append((b, a))
        cache.write_text("".join(f"{a}\t{b}\n" for a, b in rows))
    return [tuple(line.split("\t")) for line in cache.read_text().splitlines() if line]


def field(ident: str, key: str) -> str | None:
    for part in ident.split("|"):
        if part.startswith(key + "="):
            return part.split("=", 1)[1].split(".")[0]
    return None


def zfin_to_ensembl() -> dict[str, str]:
    raw = urllib.request.urlopen(ZFIN_ENSEMBL, timeout=300).read().decode()
    return {r[0]: r[3] for r in csv.reader(io.StringIO(raw), delimiter="\t") if len(r) > 3}


def zfin_genes() -> tuple[dict[str, str], dict[str, str]]:
    """ZFIN gene.txt: ZDB id -> symbol, and NCBI GeneID -> ZDB id."""
    raw = urllib.request.urlopen(ZFIN_GENES, timeout=300).read().decode()
    sym, ncbi = {}, {}
    for r in csv.reader(io.StringIO(raw), delimiter="\t"):
        if len(r) > 3:
            sym[r[0]] = r[2]
            ncbi[r[3]] = r[0]
    return sym, ncbi


def compara_line(a: str, b: str) -> str:
    try:
        d = get(f"/homology/id/danio_rerio/{a}?type=paralogues;format=condensed", tries=2)
    except Exception as e:  # network or server error: report, do not guess
        return f"unavailable ({type(e).__name__})"
    for h in d["data"][0]["homologies"] if d.get("data") else []:
        if h["id"] == b:
            return f"{h['type']} at {h['taxonomy_level']}"
    return "not reported as paralogs"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("gene_a")
    ap.add_argument("gene_b")
    ap.add_argument("gar_gene")
    ap.add_argument("--window", type=int, default=1_500_000)
    ap.add_argument("--panther-dir", type=Path, default=Path("projects/DANRE_DUPLICATION/.cache"))
    args = ap.parse_args()
    w = args.window

    focal = {k: get(f"/lookup/id/{k}") for k in (args.gene_a, args.gene_b)}
    gar = get(f"/lookup/id/{args.gar_gene}")
    print("## Focal genes\n")
    for k, g in list(focal.items()) + [(args.gar_gene, gar)]:
        print(f"- {k} ({g.get('display_name')}): {g['species']} chr {g['seq_region_name']}:"
              f"{g['start']}-{g['end']} ({g.get('assembly_name')})")
    print(f"\nEnsembl Compara relation of the zebrafish pair: {compara_line(args.gene_a, args.gene_b)}\n")

    z2e = zfin_to_ensembl()
    zsym, ncbi2z = zfin_genes()
    zf_to_gar: dict[str, set[str]] = {}
    sym_to_gar: dict[str, set[str]] = {}
    zdb_to_gar: dict[str, set[str]] = {}
    for dan, lep in danre_lepoc_pairs(args.panther_dir):
        gid = field(lep, "Ensembl")
        if not gid:
            continue
        zdb = field(dan, "ZFIN")
        sym = field(dan, "Gene")
        if not zdb and sym and sym.startswith("LOC") and sym[3:].isdigit():
            zdb = ncbi2z.get(sym[3:])  # NCBI placeholder symbol -> ZFIN gene
        if zdb:
            zdb_to_gar.setdefault(zdb, set()).add(gid)
        ens = field(dan, "Ensembl") or z2e.get(zdb or "")
        if ens:
            zf_to_gar.setdefault(ens, set()).add(gid)
        for s in {sym, zsym.get(zdb or "")} - {None, ""}:
            sym_to_gar.setdefault(s.lower(), set()).add(gid)

    def gar_orthologs(g: dict) -> set[str]:
        # Ensembl gene descriptions end with "[Source:ZFIN;Acc:ZDB-GENE-...]" for ZFIN-named genes
        m = re.search(r"Acc:(ZDB-GENE-[0-9-]+)", g.get("description") or "")
        by_zdb = zdb_to_gar.get(m.group(1), set()) if m else set()
        return (zf_to_gar.get(g["id"], set()) | by_zdb
                | sym_to_gar.get((g.get("external_name") or "").lower(), set()))

    for k, g in focal.items():
        print(f"- PANTHER gar orthologs of {g.get('display_name')} ({k}): "
              f"{', '.join(sorted(gar_orthologs(g))) or 'none'}")

    gar_win = window_genes("lepisosteus_oculatus", gar["seq_region_name"], gar["start"] - w, gar["end"] + w)
    gar_ids = {g["id"]: (g.get("external_name") or g["id"]) for g in gar_win}
    print(f"\n## Windows (+/- {w:,} bp)\n")
    print(f"Gar window around {args.gar_gene}: {len(gar_win)} protein-coding genes.\n")

    hits: dict[str, dict[str, list[str]]] = {}
    for k, g in focal.items():
        genes = window_genes("danio_rerio", g["seq_region_name"], g["start"] - w, g["end"] + w)
        with_any = 0
        matched = []
        for n in genes:
            if n["id"] == k:
                continue
            orth = gar_orthologs(n)
            if orth:
                with_any += 1
            for gid in orth & set(gar_ids):
                if gid == args.gar_gene:
                    continue
                label = n.get("external_name") or n["id"]
                matched.append((label, gid))
                hits.setdefault(gid, {}).setdefault(k, []).append(label)
        print(f"### {g.get('display_name')} ({k}) window: {len(genes)} protein-coding genes; "
              f"{with_any} have any PANTHER gar ortholog; {len(matched)} gene-ortholog links fall in the gar window\n")
        for zn, gid in matched:
            print(f"- {zn} -> gar {gar_ids[gid]} ({gid})")
        print()

    both = {gid: d for gid, d in hits.items() if len(d) == 2}
    print("## Double-conserved synteny\n")
    print(f"Gar-window genes (other than the focal gar gene) with orthologs in BOTH zebrafish windows: {len(both)}\n")
    for gid, d in both.items():
        parts = "; ".join(f"{focal[k].get('display_name')} window: {', '.join(v)}" for k, v in d.items())
        print(f"- gar {gar_ids[gid]} ({gid}): {parts}")
    print("\nGar-window genes with an ortholog in only one zebrafish window:")
    for k in focal:
        n = sum(1 for d in hits.values() if len(d) == 1 and k in d)
        print(f"- only near {focal[k].get('display_name')}: {n}")


if __name__ == "__main__":
    main()
