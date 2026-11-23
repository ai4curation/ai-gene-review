# /// script
# requires-python = ">=3.11"
# dependencies = ["requests"]
# ///
"""Compare exon structures of the donkey SNAP23 Ensembl transcripts.

Fetches the Ensembl gene (with transcripts, exons and translations) for the
donkey SNAP23 gene and reports, for each protein-coding transcript, its exon
coordinates and protein length, and which exons of the benchmark transcript
are shared with the transcript encoding the UniProt gene-centric canonical
product (A0A8C4M333 = ENSEAST00005020803).

Usage:
    uv run --script compare_transcripts_rereview.py ENSEASG00005013173 ENSEAST00005020804 ENSEAST00005020803
"""

import sys

import requests

SERVER = "https://rest.ensembl.org"


def fetch_gene(gene_id: str) -> dict:
    r = requests.get(
        f"{SERVER}/lookup/id/{gene_id}",
        params={"expand": 1},
        headers={"Content-Type": "application/json"},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def exon_set(transcript: dict) -> list[tuple[int, int]]:
    return sorted(((e["start"], e["end"]) for e in transcript["Exon"]), reverse=True)


def main() -> None:
    gene_id, target_id, canonical_id = sys.argv[1:4]
    gene = fetch_gene(gene_id)
    print(
        f"Gene {gene['id']} {gene.get('display_name')} chr{gene['seq_region_name']}:"
        f"{gene['start']}-{gene['end']} strand {gene['strand']}"
    )
    transcripts = {t["id"]: t for t in gene["Transcript"]}
    for tid, t in sorted(transcripts.items()):
        tr = t.get("Translation") or {}
        print(
            f"{tid}\tbiotype={t['biotype']}\tensembl_canonical={t.get('is_canonical')}"
            f"\texons={len(t['Exon'])}\tprotein={tr.get('id')}\tlength={tr.get('length')}"
        )
    target = exon_set(transcripts[target_id])
    canonical = exon_set(transcripts[canonical_id])
    print(f"\nExons of {target_id} (5'->3' on gene strand):")
    for ex in target:
        status = "shared with canonical" if ex in canonical else "NOT in canonical"
        print(f"  {ex[0]}-{ex[1]}\t{status}")
    print(f"\nExons of {canonical_id} (5'->3' on gene strand):")
    for ex in canonical:
        status = "shared with target" if ex in target else "NOT in target"
        print(f"  {ex[0]}-{ex[1]}\t{status}")


if __name__ == "__main__":
    main()
