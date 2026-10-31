"""Family placement and genomic context of the L. lactis plasmid UPF0014 protein (dashboard NZ_CP016699.1_28).

1. Download the Pfam UPF0014 HMM (PF03649) and the NCBIfam FetB equivalog HMM (TIGR00245) from the
   InterPro API, cache them, and hmmsearch (pyhmmer) the query and reference UPF0014 proteins.
   Each hit is reported with its bit score and the model's own gathering (GA) and trusted (TC)
   cutoffs. A protein scoring at or above TIGR00245 TC is inside the FetB equivalog.
2. Global alignment (Biopython PairwiseAligner, BLOSUM62, gap -11/-1) of the query to each
   reference: identity = identical pairs / aligned pairs, coverage = aligned pairs / query length.
3. Genomic context: download the GenBank record of the plasmid carrying the query (NCBI efetch),
   find every CDS whose translation equals the query, and list the flanking CDSs. Each adjacent
   CDS annotated as an ABC ATP-binding protein is aligned to the partner reference (E. coli FetA).
"""
from __future__ import annotations

import argparse
import gzip
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

import pyhmmer
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

INTERPRO_HMM = "https://www.ebi.ac.uk/interpro/api/entry/{db}/{acc}?annotation=hmm"
UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={acc}&rettype=gbwithparts&retmode=text"


def fetch(url: str, path: Path) -> Path:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        for attempt in range(5):
            try:
                with urllib.request.urlopen(url, timeout=180) as r:
                    data = r.read()
                break
            except urllib.error.HTTPError:
                if attempt == 4:
                    raise
                time.sleep(5 * (attempt + 1))
        path.write_bytes(gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data)
    return path


def read_fasta(path: Path) -> list[tuple[str, str]]:
    recs, name, buf = [], None, []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if name:
                recs.append((name, "".join(buf)))
            name = line[1:].split()[0]
            name = name.split("|")[1] if "|" in name else name
            buf = []
        elif line.strip():
            buf.append(line.strip())
    if name:
        recs.append((name, "".join(buf)))
    return recs


def _s(v) -> str:
    return v.decode() if isinstance(v, bytes) else str(v)


def hmm_search(hmm_path: Path, seqs: list[tuple[str, str]]) -> dict:
    alphabet = pyhmmer.easel.Alphabet.amino()
    with pyhmmer.plan7.HMMFile(hmm_path) as fh:
        hmm = fh.read()
    digital = [pyhmmer.easel.TextSequence(name=n.encode(), sequence=s).digitize(alphabet) for n, s in seqs]
    scores = {n: None for n, _ in seqs}
    for hits in pyhmmer.hmmsearch([hmm], digital, E=10.0):
        for hit in hits:
            dom = hit.best_domain
            scores[_s(hit.name)] = {
                "bit_score": round(hit.score, 1),
                "evalue": float(f"{hit.evalue:.2e}"),
                "env": [dom.env_from, dom.env_to],
            }
    cutoffs = {
        "GA": hmm.cutoffs.gathering[0] if hmm.cutoffs.gathering_available() else None,
        "TC": hmm.cutoffs.trusted[0] if hmm.cutoffs.trusted_available() else None,
    }
    for n, sc in scores.items():
        if sc is not None:
            sc["above_GA"] = cutoffs["GA"] is not None and sc["bit_score"] >= cutoffs["GA"]
            sc["above_TC"] = cutoffs["TC"] is not None and sc["bit_score"] >= cutoffs["TC"]
    return {"model": _s(hmm.accession), "name": _s(hmm.name), "description": _s(hmm.description),
            "cutoffs": cutoffs, "scores": scores}


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score, a.extend_gap_score = -11, -1
    a.mode = "global"
    a.end_gap_score = 0
    return a


def identity(q: str, r: str) -> dict:
    aln = aligner().align(q, r)[0]
    pairs = ident = 0
    for (qs, qe), (rs, re_) in zip(*aln.aligned):
        for i, j in zip(range(qs, qe), range(rs, re_)):
            pairs += 1
            ident += q[i] == r[j]
    return {"identity": round(100 * ident / pairs, 1), "aligned_pairs": pairs,
            "query_coverage": round(100 * pairs / len(q), 1), "ref_length": len(r)}


def neighborhood(gb_path: Path, query: str, flank: int) -> dict:
    rec = SeqIO.read(gb_path, "genbank")
    cds = [f for f in rec.features if f.type == "CDS"]
    rows = []
    for f in cds:
        q = f.qualifiers
        rows.append({
            "locus_tag": q.get("locus_tag", [""])[0],
            "old_locus_tag": q.get("old_locus_tag", [""])[0],
            "protein_id": q.get("protein_id", [""])[0],
            "product": q.get("product", [""])[0],
            "start": int(f.location.start) + 1, "end": int(f.location.end),
            "strand": "+" if f.location.strand == 1 else "-",
            "translation": q.get("translation", [""])[0],
        })
    hits = [i for i, r in enumerate(rows) if r["translation"] == query]
    out = []
    for i in hits:
        block = []
        for j in range(max(0, i - flank), min(len(rows), i + flank + 1)):
            r = {k: v for k, v in rows[j].items() if k != "translation"}
            r["offset"] = j - i
            r["cds_index"] = j + 1
            block.append(r)
        out.append(block)
    return {"record": rec.id, "description": rec.description, "length": len(rec.seq),
            "n_cds": len(rows), "query_copies": len(hits), "blocks": out}


def neighborhood_rows(gb_path: Path) -> list[dict]:
    rec = SeqIO.read(gb_path, "genbank")
    return [{"cds_index": i + 1, "locus_tag": f.qualifiers.get("locus_tag", [""])[0],
             "translation": f.qualifiers.get("translation", [""])[0]}
            for i, f in enumerate(f for f in rec.features if f.type == "CDS")]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", type=Path, required=True)
    ap.add_argument("--references", nargs="+", required=True, help="UniProt accessions")
    ap.add_argument("--hmm", nargs="+", required=True, help="db:acc, e.g. pfam:PF03649 ncbifam:TIGR00245")
    ap.add_argument("--plasmid", required=True, help="nucleotide accession carrying the query")
    ap.add_argument("--flank", type=int, default=4)
    ap.add_argument("--partner-ref", default="P77279", help="UniProt accession of the ATPase partner reference")
    ap.add_argument("--cache", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    query = read_fasta(args.query)
    qname, qseq = query[0]
    refs = []
    for acc in args.references:
        refs += read_fasta(fetch(UNIPROT_FASTA.format(acc=acc), args.cache / "uniprot" / f"{acc}.fasta"))
    seqs = query + refs

    results = {"query": qname, "query_length": len(qseq), "hmm": [], "identity": {}}
    for spec in args.hmm:
        db, acc = spec.split(":")
        path = fetch(INTERPRO_HMM.format(db=db, acc=acc), args.cache / "hmms" / f"{acc}.hmm")
        results["hmm"].append(hmm_search(path, seqs))
    for n, s in refs:
        results["identity"][n] = identity(qseq, s)
    gb = fetch(EFETCH.format(acc=args.plasmid), args.cache / "genbank" / f"{args.plasmid}.gb")
    results["neighborhood"] = neighborhood(gb, qseq, args.flank)
    pname, pseq = read_fasta(fetch(UNIPROT_FASTA.format(acc=args.partner_ref),
                                   args.cache / "uniprot" / f"{args.partner_ref}.fasta"))[0]
    rows = {r["cds_index"]: r for r in neighborhood_rows(gb)}
    partners = []
    for block in results["neighborhood"]["blocks"]:
        for r in block:
            if abs(r["offset"]) == 1 and "ATP-binding" in r["product"]:
                tr = rows[r["cds_index"]]["translation"]
                partners.append({"locus_tag": r["locus_tag"], "length": len(tr), "partner_ref": pname,
                                 **identity(tr, pseq)})
    if len(partners) == 2:
        a, b = (rows[i]["translation"] for i in rows if rows[i]["locus_tag"] in {p["locus_tag"] for p in partners})
        results["partner_copies_identical"] = a == b
    results["partners"] = partners

    args.output.write_text(json.dumps(results, indent=2) + "\n")

    for h in results["hmm"]:
        print(f"\n{h['model']} ({h['description']}) GA={h['cutoffs']['GA']} TC={h['cutoffs']['TC']}")
        for n, sc in h["scores"].items():
            ident = results["identity"].get(n, {}).get("identity", "query")
            print(f"  {n:14s} id={ident!s:6s} " + ("no hit" if sc is None else
                  f"bits={sc['bit_score']:7.1f} E={sc['evalue']:.1e} >=TC={sc['above_TC']}"))
    nb = results["neighborhood"]
    print(f"\n{nb['record']} {nb['description']} ({nb['n_cds']} CDS); query copies: {nb['query_copies']}")
    for block in nb["blocks"]:
        print("  --")
        for r in block:
            print(f"  {r['offset']:+d} #{r['cds_index']:3d} {r['locus_tag']:16s} {r['old_locus_tag']:14s} "
                  f"{r['strand']} {r['start']}-{r['end']} {r['product']}")

    for pr in results["partners"]:
        print(f"  partner {pr['locus_tag']} ({pr['length']} aa) vs {pr['partner_ref']}: "
              f"{pr['identity']}% identity over {pr['query_coverage']}% of the partner")
    if "partner_copies_identical" in results:
        print(f"  partner copies identical: {results['partner_copies_identical']}")


if __name__ == "__main__":
    main()
