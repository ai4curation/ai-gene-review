#!/usr/bin/env python3
"""
Align JmjC domains of Epe1, active JmjC demethylases and UniProt JmjC homologs,
then report the residue each protein carries at the alignment columns of
Epe1's UniProt-annotated sites (Fe(II) ligands, other binding sites, the CC
CAUTION position and the MUTAGEN site).

Domain boundaries come from UniProt FT DOMAIN "JmjC" features for every
protein; proteins without such a feature are skipped and listed. The
alignment is computed with MAFFT (must be on PATH). No verdict about catalytic
activity is written: the output is the residue table and per-column
conservation, which the reader interprets.
"""

import shutil
import subprocess
from collections import Counter
from pathlib import Path

import requests
from Bio import AlignIO, SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from uniprot_features import parse_uniprot_json, parse_uniprot_txt

EPE1_TXT = Path(__file__).parent.parent / "Epe1-uniprot.txt"
SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"
QUERIES = [
    'gene:epe1 AND taxonomy_name:fungi',            # Epe1 orthologs
    'jmjc AND taxonomy_name:"Schizosaccharomyces"',  # fission-yeast JmjC proteins
]


def search_homologs(limit=12) -> list:
    """Accessions of fungal Epe1 orthologs and Schizosaccharomyces JmjC proteins."""
    accessions = []
    for query in QUERIES:
        r = requests.get(SEARCH_URL, params={"query": query, "format": "json", "size": 25})
        r.raise_for_status()
        for entry in r.json().get("results", []):
            acc = entry["primaryAccession"]
            if acc != "O94603" and acc not in accessions:
                accessions.append(acc)
    return accessions[:limit]


def fetch_json_record(accession: str, data_dir: Path) -> dict:
    path = data_dir / f"homolog_{accession}.json"
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{accession}.json")
    r.raise_for_status()
    path.write_text(r.text, encoding="utf-8")
    return parse_uniprot_json(path)


def column_of(aligned: str, residue_pos: int, domain_start: int):
    """Alignment column (0-based) holding residue `residue_pos` of a domain that
    starts at `domain_start`, or None if the position is outside the domain."""
    target = residue_pos - domain_start  # 0-based index within the domain
    if target < 0:
        return None
    seen = -1
    for col, ch in enumerate(aligned):
        if ch != "-":
            seen += 1
            if seen == target:
                return col
    return None


def main():
    print("=" * 60)
    print("JmjC Domain Alignment and Site Comparison")
    print("=" * 60)
    if shutil.which("mafft") is None:
        raise SystemExit("mafft not found on PATH; install it to run this step")

    data_dir, results_dir = Path("data"), Path("results")
    results_dir.mkdir(exist_ok=True)

    records = {"Epe1": parse_uniprot_txt(EPE1_TXT)}
    for path in sorted(data_dir.glob("kdm*.json")):
        rec = parse_uniprot_json(path)
        records[rec["entry_name"]] = rec
    for acc in search_homologs():
        rec = fetch_json_record(acc, data_dir)
        records.setdefault(rec["entry_name"] or acc, rec)

    skipped = [name for name, rec in records.items() if rec["jmjc"] is None]
    domains = {n: r for n, r in records.items() if r["jmjc"] is not None}
    domain_records = [
        SeqRecord(Seq(r["sequence"][r["jmjc"][0] - 1:r["jmjc"][1]]), id=n,
                  description=f"{r['accession']} JmjC {r['jmjc'][0]}-{r['jmjc'][1]}")
        for n, r in domains.items()
    ]
    raw = results_dir / "jmjc_domains.fasta"
    SeqIO.write(domain_records, raw, "fasta")
    aligned_path = results_dir / "jmjc_domains_aligned.fasta"
    out = subprocess.run(["mafft", "--quiet", "--auto", str(raw)],
                         capture_output=True, text=True, check=True)
    aligned_path.write_text(out.stdout, encoding="utf-8")
    alignment = {rec.id: str(rec.seq) for rec in AlignIO.read(aligned_path, "fasta")}

    epe1 = records["Epe1"]
    sites = [(p, "Fe ligand") for p in epe1["fe_ligands"]]
    sites += [(p, f"binding ({lig})") for p, lig in epe1["binding"] if p not in epe1["fe_ligands"]]
    sites += [(p, f"CAUTION ({exp}->{fnd})") for p, exp, fnd in epe1["caution_positions"]]
    sites += [(p, "MUTAGEN") for p, _ in epe1["mutagen"]]
    sites.sort()

    names = list(alignment)
    lines = ["JmjC Domain Alignment and Site Comparison", "=" * 60, "",
             f"Proteins aligned ({len(names)}): " + ", ".join(names),
             "Skipped (no UniProt JmjC domain feature): " + (", ".join(skipped) or "none"),
             f"Alignment: {aligned_path} (MAFFT --auto)", "",
             "Residue at the alignment column of each annotated Epe1 site.",
             "An asterisk marks a residue that its own UniProt entry annotates as an Fe ligand.", ""]
    header = f"{'Epe1 site':<26}" + "".join(f"{n[:12]:>13}" for n in names) + "   most-common fraction"
    lines += [header, "-" * len(header)]
    for pos, label in sites:
        col = column_of(alignment["Epe1"], pos, epe1["jmjc"][0])
        if col is None:
            lines.append(f"{epe1['sequence'][pos - 1]}{pos} {label:<20} (outside the JmjC domain)")
            continue
        cells, residues = [], []
        for n in names:
            ch = alignment[n][col]
            residues.append(ch)
            rec = domains[n]
            mark = ""
            if ch != "-":
                res_pos = rec["jmjc"][0] + len(alignment[n][:col + 1].replace("-", "")) - 1
                mark = "*" if res_pos in rec["fe_ligands"] else ""
                ch = f"{ch}{res_pos}{mark}"
            cells.append(f"{ch:>13}")
        common, count = Counter(r for r in residues if r != "-").most_common(1)[0]
        frac = count / len(residues)
        lines.append(f"{epe1['sequence'][pos - 1]}{pos} {label:<20}" + "".join(cells)
                     + f"   {common} {frac:.2f}")

    text = "\n".join(lines) + "\n"
    print(text)
    (results_dir / "conservation_analysis.txt").write_text(text, encoding="utf-8")
    print(f"✓ Results saved to {results_dir / 'conservation_analysis.txt'}")


if __name__ == "__main__":
    main()
