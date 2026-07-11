"""Scan target cyanobacterial genomes for members of the septal-junction module.

Two independent, reproducible methods:

  Method A - Family membership (InterPro REST API): for each module component that
    has an InterPro family term, count member proteins in each target proteome's
    taxon. Answers "does genome X contain a member of family F?".

  Method B - Sequence homology (phmmer, via pyhmmer): search each Nostoc PCC 7120
    exemplar sequence against each target reference proteome and report the best
    hit (E-value, %identity, bitscore). This is the ONLY way to detect SepN (no
    family model) and pinpoints the specific ortholog for components whose
    InterPro family is too broad to be diagnostic.

Downloads (cached under ./data): exemplar FASTAs and target proteome FASTAs from
UniProt. Nothing is hard-coded; re-running reproduces the tables. Results are
written to results/*.tsv and printed. Inconclusive hits are reported as such.

Usage:
    uv run python scan.py            # run both methods
    uv run python scan.py --method A # family scan only (no downloads)
"""
from __future__ import annotations
import argparse, io, json, sys, time, urllib.request, urllib.error
from pathlib import Path
import pyhmmer
from config import COMPONENTS, TARGETS, EVALUE_CUTOFF

HERE = Path(__file__).parent
DATA = HERE / "data"; DATA.mkdir(exist_ok=True)
RES = HERE / "results"; RES.mkdir(exist_ok=True)
UA = {"User-Agent": "ai-gene-review-septal-junction-scan"}


def _get(url: str, accept: str = "application/json", timeout: int = 60):
    req = urllib.request.Request(url, headers={**UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        if getattr(r, "status", 200) == 204:
            return None
        return r.read()


def interpro_members(ipr: str, taxon: str) -> list[str]:
    """UniProt accessions in `taxon` that belong to InterPro entry `ipr` (empty if none)."""
    accs, url = [], (f"https://www.ebi.ac.uk/interpro/api/protein/UniProt/entry/"
                     f"InterPro/{ipr}/taxonomy/uniprot/{taxon}/?page_size=200")
    while url:
        try:
            raw = _get(url)
        except urllib.error.HTTPError as e:
            if e.code in (204, 404):
                break
            raise
        if not raw:
            break
        d = json.loads(raw)
        for item in d.get("results", []):
            meta = item.get("metadata", {})
            if meta.get("accession"):
                accs.append(meta["accession"])
        url = d.get("next")
        time.sleep(0.2)
    return accs


def download(url: str, dest: Path) -> Path:
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    dest.write_bytes(_get(url, accept="text/plain", timeout=180))
    return dest


def fetch_exemplar_fasta(acc: str) -> Path:
    return download(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", DATA / f"{acc}.fasta")


def fetch_proteome_fasta(upid: str) -> Path:
    url = (f"https://rest.uniprot.org/uniprotkb/stream?"
           f"query=(proteome:{upid})&format=fasta&includeIsoform=false")
    return download(url, DATA / f"{upid}.fasta")


def method_A() -> list[dict]:
    rows = []
    for gene, c in COMPONENTS.items():
        ipr = c["interpro"]
        for tax, (label, _upid, klass) in TARGETS.items():
            if ipr is None:
                rows.append(dict(gene=gene, interpro="(none)", family_specific=c["family_specific"],
                                 taxon=tax, target=label, klass=klass, n_members="NA",
                                 members="no family model - homology only"))
                continue
            accs = interpro_members(ipr, tax)
            rows.append(dict(gene=gene, interpro=ipr, family_specific=c["family_specific"],
                             taxon=tax, target=label, klass=klass, n_members=len(accs),
                             members=";".join(accs[:10])))
    return rows


def method_B() -> list[dict]:
    alph = pyhmmer.easel.Alphabet.amino()
    # load exemplar query sequences
    queries = {}
    for gene, c in COMPONENTS.items():
        fa = fetch_exemplar_fasta(c["exemplar"])
        with pyhmmer.easel.SequenceFile(str(fa), digital=True, alphabet=alph) as sf:
            seq = next(iter(sf))
        seq.name = gene.encode()
        queries[gene] = seq
    rows = []
    for tax, (label, upid, klass) in TARGETS.items():
        fa = fetch_proteome_fasta(upid)
        with pyhmmer.easel.SequenceFile(str(fa), digital=True, alphabet=alph) as sf:
            targets = sf.read_block()
        for gene, q in queries.items():
            hits = pyhmmer.plan7.Pipeline(alph).search_seq(q, targets)
            if len(hits) == 0:
                rows.append(dict(gene=gene, taxon=tax, target=label, klass=klass,
                                 best_hit="-", evalue="", bitscore="", pct_id="",
                                 detected=False))
                continue
            best = hits[0]
            best_name = best.name.decode() if isinstance(best.name, (bytes, bytearray)) else best.name
            # percent identity over the aligned region: identity_sequence is the
            # HMMER midline where alphabetic chars mark identical residues, '+'
            # marks conservative substitutions, spaces mark mismatches.
            pid = ""
            try:
                mid = best.best_domain.alignment.identity_sequence
                ident = sum(1 for ch in mid if ch.isalpha())
                pid = round(100 * ident / len(mid), 1) if mid else ""
            except Exception:
                pass
            rows.append(dict(gene=gene, taxon=tax, target=label, klass=klass,
                             best_hit=best_name, evalue=f"{best.evalue:.1e}",
                             bitscore=round(best.score, 1), pct_id=pid,
                             detected=best.evalue <= EVALUE_CUTOFF))
    return rows


def write_tsv(rows: list[dict], path: Path):
    if not rows:
        return
    cols = list(rows[0].keys())
    with path.open("w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]) for c in cols) + "\n")
    print(f"wrote {path.relative_to(HERE)} ({len(rows)} rows)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--method", choices=["A", "B", "both"], default="both")
    args = ap.parse_args()
    if args.method in ("A", "both"):
        a = method_A(); write_tsv(a, RES / "family_membership.tsv")
        print("\n== Method A: InterPro family membership (n members per genome) ==")
        genes = list(COMPONENTS)
        hdr = ["gene", "interpro", "spec"] + [TARGETS[t][2] + ":" + t for t in TARGETS]
        print("\t".join(hdr))
        for gene in genes:
            g = [r for r in a if r["gene"] == gene]
            spec = "SPECIFIC" if COMPONENTS[gene]["family_specific"] else "broad"
            line = [gene, g[0]["interpro"], spec] + [str(next(r["n_members"] for r in g if r["taxon"] == t)) for t in TARGETS]
            print("\t".join(line))
    if args.method in ("B", "both"):
        b = method_B(); write_tsv(b, RES / "homology_besthits.tsv")
        print(f"\n== Method B: phmmer best hit per exemplar (detected = E<= {EVALUE_CUTOFF:g}) ==")
        print("gene\t" + "\t".join(TARGETS[t][2] + ":" + TARGETS[t][0].split()[0] for t in TARGETS))
        for gene in COMPONENTS:
            cells = []
            for t in TARGETS:
                r = next(x for x in b if x["gene"] == gene and x["taxon"] == t)
                cells.append(f"{'Y' if r['detected'] else 'n'}({r['evalue']},{r['pct_id']}%)" if r["best_hit"] != "-" else "none")
            print(gene + "\t" + "\t".join(cells))


if __name__ == "__main__":
    main()
